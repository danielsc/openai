from time import sleep
import requests
import os, argparse
import openai, yaml
import mlflow, time
import pandas as pd

def load_yaml(filename):
   with open(filename, encoding='utf-8') as fh:
      file_dict = yaml.load(fh, Loader=yaml.FullLoader)
   return file_dict

def save_yaml(content, filename):
   with open(filename, encoding='utf-8', mode='w') as fh:
      yaml.dump(content, fh)

def load_api_key(keyname = "openai-key"):
  from azureml.core.run import _OfflineRun
  from azureml.core import Run
  run = Run.get_context()
  if run.__class__ == _OfflineRun:
    print(f"loading key {keyname} from environment variables")
    secret_value = os.getenv("OPENAI_API_KEY")
  else:
    print(f"loading key {keyname} from keyvault")
    secret_value = run.get_secret(name=keyname)

  if not secret_value is None and secret_value.startswith("sk"):
    return secret_value
  else:
    raise Exception("secret does not start with the letters 'sk'")


def submit_fine_tune(url, api_key, training_file, validation_file, args):
  payload = {
    "training_file": training_file,
    "validation_file": validation_file,
    "model": args.model,
    "n_epochs": args.n_epochs,
    "batch_size": args.batch_size,
    "learning_rate_multiplier": args.learning_rate_multiplier,
    "use_packing": args.use_packing,
  }
  if not args.classification_n_classes is None:
    payload["classification_n_classes"] = args.classification_n_classes
    payload["compute_classification_metrics"] = True

  print("Submitting fine tune")
  print(payload)

  r = requests.post(url,
    headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "OpenAI-Organization": "msft-finetuning-2"
    },
    json = payload
  )
  data = r.json()
  print("response:")
  print(data)
  save_yaml(data, args.fine_tune_metadata + "/MLArtifact.yaml")
  return data['id']

def get_fine_tune(url, api_key, fine_tune_id, args):
  #print("getting status")
  r = requests.get(url + "/" + fine_tune_id,
    headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "OpenAI-Organization": "msft-finetuning-2"
    }
  )
  data = r.json()
  #print(data)
  save_yaml(data, args.fine_tune_metadata + "/MLArtifact.yaml")
  return data

def stream_fine_tune_status(url, api_key, fine_tune_id):
  r = requests.get(url + "/" + fine_tune_id + "/events",
    headers={
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json",
      "OpenAI-Organization": "msft-finetuning-2"
    },
    params={
      "stream": True
    },
    stream=True
  )
  for data in r.iter_lines():
    print(data)

  return 

def log_result_file(url, api_key, fine_tune):
  if 'fine_tuned_model' in fine_tune:
    mlflow.log_param("fine_tuned_model", fine_tune['fine_tuned_model'])

  if not 'result_files' in fine_tune:
    raise Exception("no result_files in fine_tune: " + fine_tune)

  result_files = fine_tune['result_files']
  fine_tune_results = next((file for file in result_files if file['purpose']=='fine-tune-results'), None)
  
  if fine_tune_results is None:
    raise Exception("no result_files with purpose fine-tune-results in fine_tune: " + fine_tune)

  print("getting fine_tune_results")
  r = requests.get(url + "/" + fine_tune_results['id'] + "/content",
    headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "OpenAI-Organization": "msft-finetuning-2"
    }
  )
  with open(fine_tune_results['filename'], 'wb') as file:
    file.write(r.content)

  mlflow.log_artifact(fine_tune_results['filename'])

  df = pd.read_csv(fine_tune_results['filename'])

  for col in ['training_loss','classification/accuracy','classification/weighted_f1_score']: 
    values = df[['step',col]].dropna() 
    for i, row in values.iterrows(): 
      mlflow.log_metric(col, row[col], int(row.step)) 


parser = argparse.ArgumentParser()
parser.add_argument("--training_data", default="./data/3train_uploaded")
parser.add_argument("--validation_data", default="./data/3validation_uploaded")
parser.add_argument("--model", default="ada")
parser.add_argument("--n_epochs", default=1, type=int)
parser.add_argument("--batch_size", default=4, type=int)
parser.add_argument("--learning_rate_multiplier", default=0.1, type=float)
parser.add_argument("--use_packing", default=True, type=bool)
parser.add_argument("--classification_n_classes", default=5, type=int)
parser.add_argument("--fine_tune_metadata", default="./data/4fine_tune")
args = parser.parse_args()

mlflow.log_params({
  "model": args.model,
  "n_epochs": args.n_epochs,
  "batch_size": args.batch_size,
  "learning_rate_multiplier": args.learning_rate_multiplier,
  "use_packing": args.use_packing,
  "classification_n_classes": args.classification_n_classes
})

#openai.organization = "org-hTGGKhbVgQIQFEXlrcWgLHk9"
api_key = load_api_key()
training_file_metadata = load_yaml(f"{args.training_data}/MLArtifact.yaml")
validation_file_metadata = load_yaml(f"{args.validation_data}/MLArtifact.yaml")
url = "https://api.openai.com/v1/fine-tunes"

# kick off the fine tune job
fine_tune_id = submit_fine_tune(url, api_key, training_file_metadata['id'], validation_file_metadata['id'], args)
mlflow.log_param("fine_tune_id", fine_tune_id)

# stream the events while the job is running
stream_fine_tune_status(url, api_key, fine_tune_id)

# write final data of the fine_tune job to the output 
fine_tune = get_fine_tune(url, api_key, fine_tune_id, args)
print("fine_tune ended with status:", fine_tune['status'])

# end with error of the job failed
if fine_tune['status'] in ['failed', 'cancelled']:
  print(fine_tune)
  exit(1)

# log the metrics to mlflow
log_result_file("https://api.openai.com/v1/files", api_key, fine_tune)


print("done...")

