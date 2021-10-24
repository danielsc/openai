
import os, argparse, uuid, yaml
import openai
from azureml.core import Run

parser = argparse.ArgumentParser()
parser.add_argument("--folder_to_upload", default="./data/2train")
parser.add_argument("--upload_metadata", default="./data/3train_uploaded")
args = parser.parse_args()

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

def uploade_jsonl_file_from_folder(folder):
  filepaths = [f for f in os.listdir(folder) if f.endswith('.jsonl')]
  if len(filepaths) == 0:
    raise Exception(f"No jsonl file found in {folder}")
  elif len(filepaths) > 1:
    print(f"WARNING: more than 1 jsonl file found in {folder} -- will proceed with the first one: {filepaths[0]}")

  upload_result = openai.File.create(
    file=open(folder + '/' + filepaths[0]),
    purpose='fine-tune'
  )
  print(upload_result)
  return upload_result

openai.organization = "org-hTGGKhbVgQIQFEXlrcWgLHk9"
openai.api_key = load_api_key()

## upload the files
print("Uploading data")
metadata = uploade_jsonl_file_from_folder(args.folder_to_upload)
print("success")
print(metadata)

print("writing metadata to output")
save_yaml(metadata.to_dict(), args.upload_metadata + "/MLArtifact.yaml")

