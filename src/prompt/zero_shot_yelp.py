import pandas as pd
import numpy as np
import openai
import argparse
import mlflow
import os
import evaluate
import yaml
from langchain.prompts import PromptTemplate
from openai_llm import AzureOpenAI

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
      prompts.append(f"Classify the following yelp review into 1 of the following categories: [1, 2, 3, 4, 5]\n\nyelp review: {text} \n\nClassified category:")

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

def classify_yelp_batch(llm, 
                        texts,
                        prompt, 
                        batch_size=20):
    results = []
    input_prompt = PromptTemplate(input_variables=["text"], template=prompt)

    for i in tqdm(range(0, len(texts), batch_size)):
        prompts = [ input_prompt.format(text=text) for text in texts[i:i+batch_size]]
        batch_results = llm(prompts)
        batch_results = [item.strip()[0] for item in batch_results]
        results.extend(batch_results)
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
    parser.add_argument("--prompts", default="./data/1prompts/prompts.csv")
    parser.add_argument("--prompt_number", default=1, type=int)
    parser.add_argument("--test_output", default="./data/1zero_shot/metrics.yaml")
    parser.add_argument("--prompt_column", default="text")
    parser.add_argument("--completion_column", default="stars")
    parser.add_argument("--aoai_endpoint", default="https://aoai.openai.azure.com/")
    parser.add_argument("--api_version", default="2022-06-01-preview")
    parser.add_argument("--deployment", default="text-davinci-002")
    # add temperture, max_tokens, top_p, frequency_penalty, presence_penalty
    parser.add_argument("--temperature", default=0.5, type=float)
    parser.add_argument("--max_tokens", default=2, type=int)
    parser.add_argument("--top_p", default=1, type=float)
    parser.add_argument("--frequency_penalty", default=0, type=float)
    parser.add_argument("--presence_penalty", default=0, type=float)    
    args = parser.parse_args()

    mlflow.log_params({
        "data": args.data,
        "test_output": args.test_output,
        "prompt_column": args.prompt_column,
        "completion_column": args.completion_column,
        "aoai_endpoint": args.aoai_endpoint,
        "api_version": args.api_version,
        "deployment": args.deployment,
        "prompt_number": args.prompt_number,
        "prompts": args.prompts,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "top_p": args.top_p,
        "frequency_penalty": args.frequency_penalty,
        "presence_penalty": args.presence_penalty
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
    
    # get prompt
    prompts = pd.read_csv(args.prompts)
    prompt = prompts.iloc[args.prompt_number]['prompt']
    print(f"prompt: {prompt}")
    mlflow.log_param("prompt", prompt)

    llm = AzureOpenAI(deployment=args.deployment,
                      api_base=args.aoai_endpoint,
                      temperature=args.temperature,
                      max_tokens=args.max_tokens,
                      top_p=args.top_p,
                      frequency_penalty=args.frequency_penalty,
                      presence_penalty=args.presence_penalty)

    results = classify_yelp_batch(llm=llm,
                                  texts=df[args.prompt_column].values, 
                                  prompt=prompt)

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
        "prompt": prompt,
        "completion_column": args.completion_column,
        "aoai_endpoint": args.aoai_endpoint,
        "api_version": args.api_version,
        "completion_deployment": args.deployment,
        "metrics": metrics
    }, args.test_output)





