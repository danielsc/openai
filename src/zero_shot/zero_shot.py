import pandas as pd
import numpy as np
import openai
import argparse
import mlflow
import os
import evaluate
import yaml

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


import openai
from tqdm import tqdm
def classify_yelp(texts, deployment):
    prompts = []
    for text in texts:
      prompts.append(f"Classify the following yelp review into 1 of the following categories: categories: [1, 2, 3, 4, 5]\n\nyelp review: {text} \n\nClassified category:")

    response = openai.Completion.create(
      engine=deployment,
      prompt=prompts,
      temperature=0,
      max_tokens=60,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
    )
    results = [choice['text'].strip()[0] for choice in response['choices']]
    return results

def classify_yelp_batch(texts, deployment, batch_size=20):
    results = []
    for i in tqdm(range(0, len(texts), batch_size)):
        results.extend(classify_yelp(texts[i:i+batch_size], deployment))
    return results

def calculate_metrics(references, predictions):
    f1 = evaluate.load("f1").compute(references=references, predictions=predictions, average='weighted')
    accuracy = evaluate.load("accuracy").compute(references=references, predictions=predictions)
    precision = evaluate.load("precision").compute(references=references, predictions=predictions, average='weighted')
    recall = evaluate.load("recall").compute(references=references, predictions=predictions, average='weighted')
    # merge the dicts
    metrics = {**f1, **accuracy, **precision, **recall}
    return metrics

def save_yaml(content, filename):
   with open(filename, encoding='utf-8', mode='w') as fh:
      yaml.dump(content, fh)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="./data/1raw/yelp_mini.csv")
    parser.add_argument("--test_output", default="./data/1zero_shot/metrics.yaml")
    parser.add_argument("--prompt_column", default="text")
    parser.add_argument("--completion_column", default="stars")
    parser.add_argument("--aoai_endpoint", default="https://aoai.openai.azure.com/")
    parser.add_argument("--api_version", default="2022-06-01-preview")
    parser.add_argument("--completion_deployment", default="text-davinci-002")
    args = parser.parse_args()

    mlflow.log_params({
        "data": args.data,
        "test_output": args.test_output,
        "prompt_column": args.prompt_column,
        "completion_column": args.completion_column,
        "aoai_endpoint": args.aoai_endpoint,
        "api_version": args.api_version,
        "completion_deployment": args.completion_deployment
    })

    api_key = load_api_key()
    openai.api_version = args.api_version
    openai.api_key = api_key
    openai.api_base = args.aoai_endpoint
    openai.api_type = "azure"


    file = args.data
    print(f"processing {file}")
    df = pd.read_csv(file)

    df[args.completion_column] = df[args.completion_column].astype(str)

    results = classify_yelp_batch(df[args.prompt_column].values, args.completion_deployment)
    # convert results to int, set values that don't convert to 3
    results = [x if x.isdigit() else '3' for x in results]

    df['prediction'] = results
    print(df[['prediction','stars']])
    metrics = calculate_metrics(df[args.completion_column].values, results)

    mlflow.log_metrics(metrics)
    print(metrics)

    save_yaml({
        "data": args.data,
        "test_output": args.test_output,
        "prompt_column": args.prompt_column,
        "completion_column": args.completion_column,
        "aoai_endpoint": args.aoai_endpoint,
        "api_version": args.api_version,
        "completion_deployment": args.completion_deployment,
        "metrics": metrics
    }, args.test_output)





