from os import listdir, rename
import argparse
import pandas as pd
import json

parser = argparse.ArgumentParser()
parser.add_argument("--raw_data", default="./data/1raw/yelp_small.csv")
parser.add_argument("--train_output", default="./data/2train/yelp_train.jsonl")
parser.add_argument("--validation_output", default="./data/2validation/yelp_validation.jsonl")
parser.add_argument("--prompt_column", default="text")
parser.add_argument("--completion_column", default="stars")
parser.add_argument("--train_test_split", default=0.8, type=float)
parser.add_argument("--seed", default=42, type=int)
args = parser.parse_args()

def split_dataframe(df, ratio):
  part_train = df.sample(frac = ratio)
  part_validation = df.drop(part_train.index)
  return part_train, part_validation

file = args.raw_data
print(f"processing {file}")
df = pd.read_csv(file)
## pick columns
df = df[[args.prompt_column, args.completion_column]]
## rename columns
df = df.rename(columns={args.prompt_column:'prompt', args.completion_column:'completion'})
## add leading space to completion
df.completion = ' ' + df.completion.astype(str)
## remove \n from prompts
#df.prompt = df.prompt.replace(r'\n',' ', regex=True) 
## add trailing token to prompt
df.prompt = df.prompt + "\n\n###\n\n"

## split into train and validation
train, validation = split_dataframe(df, args.train_test_split)
train.to_json(f"{args.train_output}", orient='records', lines=True)
print(f"wrote train {args.train_output}")
validation.to_json(f"{args.validation_output}", orient='records', lines=True)
print(f"wrote validation {args.validation_output}")
