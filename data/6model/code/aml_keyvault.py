from azureml.core.run import _OfflineRun
from azureml.core import Run
from typing import List
import os 

def load_secrets(secrets: List[str]):
    run = Run.get_context()
    if not run.__class__ == _OfflineRun:
        for secret in secrets:
            print("loading secret", secret)
            # keyvault secrets can't have underscores
            secret_name = secret.replace("_", "-")
            secret_value = run.get_secret(name=secret_name)
            os.environ[secret] = secret_value
    else:
        from dotenv import load_dotenv, find_dotenv
        dotenv_file = find_dotenv()
        print("running offline, loading secrets from .env file: ", dotenv_file)
        _ = load_dotenv(dotenv_file)
        for secret in secrets:
            if not secret in os.environ:
                raise Exception(f"Secret {secret} not found in environment variables")

