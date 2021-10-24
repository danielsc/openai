import mlflow
import pandas as pd
import yaml 

def load_yaml(filename):
   with open(filename, encoding='utf-8') as fh:
      file_dict = yaml.load(fh, Loader=yaml.FullLoader)
   return file_dict


def foo():
  df = pd.read_csv('logs/ft-msft-finetuning-2-2021-10-10-08-31-43.results.csv')

  for col in ['training_loss','classification/accuracy','classification/weighted_f1_score']: 
    values = df[['step',col]].dropna() 
    for i, row in values.iterrows(): 
      mlflow.log_metric(col, row[col], int(row.step)) 

fine_tune = load_yaml("MLArtifact.yaml")

if 'fine_tuned_model' in fine_tune:
  mlflow.log_param("fine_tuned_model", fine_tune['fine_tuned_model'])

