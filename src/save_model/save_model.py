from openai_model import OpenAIModel
import shutil, mlflow
import argparse
import pandas as pd
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--fine_tune", default="../../data/4fine_tune")
parser.add_argument("--model", default="../../data/5model/model")
parser.add_argument("--test_data", default=None)
args = parser.parse_args()

def load_yaml(filename):
   with open(filename, encoding='utf-8') as fh:
      file_dict = yaml.load(fh, Loader=yaml.FullLoader)
   return file_dict

def save_yaml(content, filename):
   with open(filename, encoding='utf-8', mode='w') as fh:
      yaml.dump(content, fh)

def save_pyfunc_model(fine_tune, path):
  artifacts = {
    'fine_tune': fine_tune
  }
  try:
    shutil.rmtree(path)
  except:
    pass
  model = OpenAIModel()
  mlflow.pyfunc.save_model(path, python_model=model, artifacts=artifacts,
    code_path=['openai_model.py'], conda_env='conda.yml')

#fine_tune = load_yaml(args.fine_tune + "/MLArtifact.yaml")

save_pyfunc_model(args.fine_tune + "/MLArtifact.yaml", args.model + "/model")

if not args.test_data is None:
  model = mlflow.pyfunc.load_model(args.model)
  import pandas as pd
  df = pd.read_csv(args.test_data)
  print(model.predict(df[:27]))