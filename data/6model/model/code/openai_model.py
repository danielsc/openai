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
    deployment = load_yaml(context.artifacts['deployment'])
    self.BATCH_SIZE = 20
    self.api_version="2022-06-01-preview" # hardcode for now
    self.deployment = deployment['id']
    self.endpoint = deployment['endpoint']
    self.api_key = os.getenv("OPENAI_API_KEY")

    if self.api_key is None:
      print("key is ", self.api_key)
      raise Exception("Please set env var OPENAI_API_KEY")

    print("api_key", self.api_key)
    self.url = self.endpoint + "openai/deployments/" + self.deployment + "/completions?api-version=" + self.api_version
    print("url", self.url)

  def call_oai_endpoint(self, context, model_input: pd.DataFrame):
    payload = {
      "prompt": list(model_input.prompt.values)
    }

    print(payload)
    
    r = requests.post(self.url,
      headers={
        "api-key": self.api_key,
        "Content-Type": "application/json"
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
  
if __name__=="__main__":
  import pathlib
  this_dir = pathlib.Path(os.path.realpath(__file__)).parent.resolve()
  context = mlflow.pyfunc.PythonModelContext({'deployment':f'{this_dir}/../artifacts/MLArtifact.yaml'})
  model = OpenAIModel()
  model.load_context(context)
  df = pd.DataFrame({"text": ["This is a great movie", "This is a terrible movie"]})
  print(model.predict(context, df))
