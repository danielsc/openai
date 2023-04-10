import functools
import mlflow
import tempfile, json, os
from langchain.docstore.document import Document
import json
import os

def serialize(obj):
    # Handle simple types
    if isinstance(obj, (int, float, str, bool)):
        return obj

    # Handle dicts
    elif isinstance(obj, dict):
        serialized_dict = {}
        for key, value in obj.items():
            serialized_dict[key] = serialize(value)
        return serialized_dict

    # Handle lists and tuples
    elif isinstance(obj, (list, tuple)):
        serialized_list = []
        for item in obj:
            serialized_list.append(serialize(item))
        if isinstance(obj, tuple):
            return tuple(serialized_list)
        else:
            return serialized_list

    # Handle LangChain Document
    elif isinstance(obj, Document):
        serialized_doc = { 'page_content': obj.page_content, 'metadata': obj.metadata  } 
        return serialized_doc
    
    # handle pydantic models (openai uses pydantic)
    elif hasattr(obj, "dict") and callable(getattr(obj, "dict")):
        return {str(obj.__class__): serialize(obj.dict())}
    
    # Handle other types
    else:
        return str(obj)

def log_json_artifact(json_data, artifact_name):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file in the temporary directory
        with open(os.path.join(temp_dir, artifact_name), "w") as f:
            json.dump(serialize(json_data), f)

        # Log the file as an artifact
        mlflow.log_artifact(os.path.join(temp_dir, artifact_name))

counter = [0]
def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global counter
        counter[-1] = counter[-1] + 1
        json_call = {}
        json_call['module'] = func.__module__
        json_call['name'] = func.__name__
        json_call['args'] = args
        json_call['kwargs'] = kwargs
        
        print("json_call:", json_call)
        log_json_artifact(json_call, f"{'_'.join([str(i) for i in counter])}_{func.__module__}_{func.__name__}_call.json")
        counter.append(0)
        result = func(*args, **kwargs)
        counter.pop()
        json_result = result
        print("json_result:", json_result)
        log_json_artifact(json_result, f"{'_'.join([str(i) for i in counter])}_{func.__module__}_{func.__name__}_result.json")
        return result
    return wrapper

from langchain.llms import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI
from langchain import SerpAPIWrapper
from langchain.python import PythonREPL
from langchain import LLMMathChain

def patch_langchain():
    AzureOpenAI._generate = log_function_call(AzureOpenAI._generate)
    AzureChatOpenAI._generate = log_function_call(AzureChatOpenAI._generate)
    SerpAPIWrapper.run = log_function_call(SerpAPIWrapper.run)
    PythonREPL.run = log_function_call(PythonREPL.run)
    LLMMathChain.run = log_function_call(LLMMathChain.run)