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
    self.model = fine_tune['fine_tuned_model']
    self.api_key = os.getenv("OPENAI_API_KEY")
    self.url = f"https://api.openai.com/v1/engines/{self.model.split(':')[0]}-shared-msft/completions"

  def predict(self, context, model_input: pd.DataFrame):
    
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
    return [row['text'] for row in data['choices']]
