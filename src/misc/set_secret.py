import argparse
from azureml.core import Workspace
from azureml.core import Keyvault
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="foo")
parser.add_argument("--secret", default="geheim")
args = parser.parse_args()

ws = Workspace.from_config()
keyvault = ws.get_default_keyvault()
keyvault.set_secret(name=args.name, value = args.secret)