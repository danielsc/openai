import requests, os
import mlflow, yaml
import pandas as pd

def load_yaml(filename):
  with open(filename, encoding='utf-8') as fh:
    file_dict = yaml.load(fh, Loader=yaml.FullLoader)
  return file_dict

def parse_stars(completion: str) -> int:
  try:
    return int(completion[1])
  except:
    return 0

class OpenAIModel(mlflow.pyfunc.PythonModel):
  def load_context(self, context):
    fine_tune = load_yaml(context.artifacts['fine_tune'])
    self.BATCH_SIZE = 20
    self.model = fine_tune['fine_tuned_model']
    #self.api_key = os.getenv("OPENAI_API_KEY")
    self.api_key = "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"
    self.url = f"https://api.openai.com/v1/engines/{self.model.split(':')[0]}-shared-msft/completions"
    print("moodel", self.model)
    print("url", self.url)
    if self.api_key is None or not self.api_key.startswith("sk"):
      print("key is ", self.api_key)
      raise Exception("Please set env var OPENAI_API_KEY")

  def call_oai_endpoint(self, context, model_input: pd.DataFrame):
    payload = {
      "prompt": list(model_input.prompt.values),
      "model": self.model
    }

    print(payload)
    
    r = requests.post(self.url,
      headers={
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json",
        "OpenAI-Organization": "msft-finetuning-2"
      },
      json = payload
    )
    data = r.json()
    print("DEBUG: ", data)
    print("\n\n\n")
    return [row['text'] for row in data['choices']]

  def predict(self, context, model_input: pd.DataFrame):
    ## apply to prompt modifications, in this case add "\n\n###\n\n'    
    df = model_input
    ## pick column
    df = df[["text"]]
    ## rename columns
    df = df.rename(columns={'text':'prompt'})
    ## add trailing token to prompt
    df.prompt = df.prompt + "\n\n###\n\n"    
    ## need to batch to 20 -- that is the max that the service accepts
    list_df = [df[i:i+self.BATCH_SIZE] for i in range(0,df.shape[0],self.BATCH_SIZE)]
    scores = []
    for df in list_df:
      scores = scores + self.call_oai_endpoint(context, df)
    # parse the stars from the completion and return an int array
    return [parse_stars(completion) for completion in scores]