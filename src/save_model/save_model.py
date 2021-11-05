from pandas.core.frame import DataFrame
from openai_model import OpenAIModel
import shutil, mlflow
import mlflow.models 
import argparse
import pandas as pd
import yaml
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--fine_tune", default="../../data/4fine_tune")
parser.add_argument("--model", default="../../data/5model/")
parser.add_argument("--test_data", default=None)
args = parser.parse_args()

def load_yaml(filename):
   with open(filename, encoding='utf-8') as fh:
      file_dict = yaml.load(fh, Loader=yaml.FullLoader)
   return file_dict

def save_yaml(content, filename):
   with open(filename, encoding='utf-8', mode='w') as fh:
      yaml.dump(content, fh)

def save_pyfunc_model(fine_tune: str, path: str):
  artifacts = {
    'fine_tune': fine_tune
  }
  try:
    shutil.rmtree(path)
  except:
    pass
  model = OpenAIModel()

  df = DataFrame({"text": ["foo", "bar", "baz"]})
  signature = mlflow.models.infer_signature(model_input=df, model_output=np.array([3,4,5]))

  mlflow.pyfunc.save_model(path, python_model=model, artifacts=artifacts,
    code_path=['openai_model.py'], conda_env='conda.yml', signature=signature)

save_pyfunc_model(args.fine_tune + "/MLArtifact.yaml", args.model + "/model")

if not args.test_data is None:
  df = pd.read_csv(args.test_data)
  model = mlflow.pyfunc.load_model(args.model + "/model")
  print(model.predict(df[:27]))