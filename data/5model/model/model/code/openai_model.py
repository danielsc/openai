import requests, os
import mlflow, yaml
import pandas as pd

def load_yaml(filename):
  with open(filename, encoding='utf-8') as fh:
    file_dict = yaml.load(fh, Loader=yaml.FullLoader)
  return file_dict

class OpenAIModel(mlflow.pyfunc.PythonModel):
  def load_context(self, context):
    fine_tune = load_yaml(context.artifacts['fine_tune'])
    self.BATCH_SIZE = 20
    self.model = fine_tune['fine_tuned_model']
    self.api_key = os.getenv("OPENAI_API_KEY")
    self.url = f"https://api.openai.com/v1/engines/{self.model.split(':')[0]}-shared-msft/completions"
    print("moodel", self.model)
    print("url", self.url)
    if self.api_key is None or not self.api_key.startswith("sk"):
      raise Exception("Please set env var OPENAI_API_KEY")

  def call_oai_endpoint(self, context, model_input: pd.DataFrame):
    print(model_input)
    payload = {
      "prompt": list(model_input.prompt.values),
      "model": self.model
    }

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
    ## need to batch to 20 -- that is the max that the service accepts
    list_df = [model_input[i:i+self.BATCH_SIZE] for i in range(0,model_input.shape[0],self.BATCH_SIZE)]
    scores = []
    for df in list_df:
      scores = scores + self.call_oai_endpoint(context, df)
    return scores