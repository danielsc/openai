import requests, os
import mlflow
import pandas as pd


api_key = os.getenv("OPENAI_API_KEY")

# url = "https://api.openai.com/v1/engines/curie-shared-msft/completions"
# "model": "curie:ft-msft-finetuning-2-2021-10-10-01-38-13"

# {'error': {'code': None, 'message': 'That model is still being loaded. Please try again shortly.', 'param': None, 'type': 'server_error'}}
url = "https://api.openai.com/v1/engines/ada-shared-msft/completions"

payload = {
  "prompt": ["Mediocre dining experience -- would not recommend.\n\n###\n\n", "Awesome \n\n###\n\n"],
  "model": "ada:ft-msft-finetuning-2-2021-10-23-15-06-15"
}

r = requests.post(url,
  headers={
  "Authorization": f"Bearer {api_key}",
  "Content-Type": "application/json",
  "OpenAI-Organization": "msft-finetuning-2"
  },
  json = payload
)
data = r.json()
print(data)
