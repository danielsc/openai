import requests, os
import mlflow, yaml
import pandas as pd
import time
from dataclasses import dataclass
from typing import List
import numpy as np

def load_api_key(keyname = "openai-key"):
  secret_value = os.getenv("OPENAI_API_KEY")
  if secret_value is None:
    try:
      from azureml.core.run import _OfflineRun
      from azureml.core import Run
      run = Run.get_context()
      secret_value = run.get_secret(name=keyname)
    except Exception as e:
      Exception("No OPENAI_API_KEY found in environment variables or keyvault", e)

  return secret_value

@dataclass
class AzureOpenAI(mlflow.pyfunc.PythonModel):
  deployment :str
  max_tokens :int = 100
  temperature :float = 0.5
  top_p :float = 0.5
  frequency_penalty :float = 0.5
  api_version :str = "2022-06-01-preview"
  BATCH_SIZE :int = 20
  api_key :str = None
  api_base :str = None

  def __post_init__(self):
    if self.api_key is None:
      self.api_key = load_api_key()
      if self.api_key is None:
        raise Exception("Please set env var OPENAI_API_KEY")

    if self.api_base is None:
      self.api_base = os.environ.get("OPENAI_API_BASE", None)
      if self.api_base is None:
        raise Exception("Please set env var OPENAI_API_BASE")

    self.url = self.api_base + "openai/deployments/" + self.deployment + "/completions?api-version=" + self.api_version
    print(f"url: {self.url}")

  def call_oai_endpoint(self, context, model_input: np.array, debug=False):
    headers={
      "api-key": self.api_key,
      "Content-Type": "application/json"
    }
    payload = {
      "prompt": list(model_input),
      "max_tokens": self.max_tokens,
      "temperature": self.temperature,
      "top_p": self.top_p,
      "frequency_penalty": self.frequency_penalty,
    }    
    while True:
      print(f"sending {len(model_input)} items to url {self.url}")
      if debug:
        print("url:", self.url)
        print("headers: ", {k:v for (k,v) in headers.items() if k!='api-key'})
        print("payload:", payload)

      r = requests.post(self.url,
        headers=headers,
        json = payload
      )
      data = r.json()

      if "error" in data:
        print(data)
        if (data['error']['code'] == 'DeploymentNotReady'):
          print("Deployment not ready, waiting 10 seconds")
          time.sleep(10)
        elif (data['error']['code'] == '429'):
          print("Too many requests, waiting 2 seconds")
          time.sleep(2)
        else:
          raise Exception(data['error']['message'])
      else:
        break
    
    if debug:
      print("data:", data)
    
    return [row['text'] for row in data['choices']]

  def __call__(self, model_input: np.ndarray, debug=False) -> np.ndarray:
    ## need to batch to 20 -- that is the max that the service accepts
    list_df = [model_input[i:i+self.BATCH_SIZE] for i in range(0,model_input.shape[0],self.BATCH_SIZE)]
    scores = []
    for df in list_df:
      scores = scores + self.call_oai_endpoint(context, df, debug)
    # parse the stars from the completion and return an int array
    return scores

  def predict(self, context, model_input: pd.DataFrame):
    return self.__call__(model_input)
  
  def source_paths(self):
    return [__file__]

  def conda_path(self):
    return os.path.join(os.path.dirname(__file__), "conda.yaml")

if __name__=="__main__":
  # just for testing
  import pathlib
  this_dir = pathlib.Path(os.path.realpath(__file__)).parent.resolve()
  #context = mlflow.pyfunc.PythonModelContext({'deployment':f'{this_dir}/../artifacts/MLArtifact.yaml'})
  context = None
  model = AzureOpenAI(deployment="text-davinci-002")
  #model.load_context(context)
  prompts = np.array(["This is a great movie", "This is a terrible movie"])
  print(model(prompts, debug=True))
