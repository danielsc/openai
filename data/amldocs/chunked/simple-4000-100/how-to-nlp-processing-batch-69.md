We need to create a scoring script that can read the CSV files provided by the batch deployment and return the scores of the model with the summary. The following script does the following:

> [!div class="checklist"]
> * Indicates an `init` function that load the model using `transformers`. Notice that the tokenizer of the model is loaded separately to account for the limitation in the sequence lenghs of the model we are currently using.
> * Indicates a `run` function that is executed for each mini-batch the batch deployment provides.
> * The `run` function read the entire batch using the `datasets` library. The text we need to summarize is on the column `text`.
> * The `run` method iterates over each of the rows of the text and run the prediction. Since this is a very expensive model, running the prediction over entire files will result in an out-of-memory exception. Notice that the model is not execute with the `pipeline` object from `transformers`. This is done to account for long sequences of text and the limitation of 1024 tokens in the underlying model we are using.
> * It returns the summary of the provided text.

__transformer_scorer.py__

```python
import os
import numpy as np
from transformers import pipeline, AutoTokenizer, TFBartForConditionalGeneration
from datasets import load_dataset

def init():
    global model
    global tokenizer

    # AZUREML_MODEL_DIR is an environment variable created during deployment
    # Change "model" to the name of the folder used by you model, or model file name.
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model")

    # load the model
    tokenizer = AutoTokenizer.from_pretrained(model_path, truncation=True, max_length=1024)
    model = TFBartForConditionalGeneration.from_pretrained(model_path)

def run(mini_batch):
    resultList = []

    ds = load_dataset('csv', data_files={ 'score': mini_batch})
    for text in ds['score']['text']:
        # perform inference
        input_ids = tokenizer.batch_encode_plus([text], truncation=True, padding=True, max_length=1024)['input_ids']
        summary_ids = model.generate(input_ids, max_length=130, min_length=30, do_sample=False)
        summaries = [tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=False) for s in summary_ids]

        # Get results:
        resultList.append(summaries[0])

    return resultList
```

> [!TIP]
> Although files are provided in mini-batches by the deployment, this scoring script processes one row at a time. This is a common pattern when dealing with expensive models (like transformers) as trying to load the entire batch and send it to the model at once may result in high-memory pressure on the batch executor (OOM exeptions).


### Creating the deployment

One the scoring script is created, it's time to create a batch deployment for it. Follow the following steps to create it:

1. We need to indicate over which environment we are going to run the deployment. In our case, our model runs on `TensorFlow`. Azure Machine Learning already has an environment with the required software installed, so we can reutilize this environment. We are just going to add a couple of dependencies in a `conda.yml` file including the libraries `transformers` and `datasets`.

   # [Azure CLI](#tab/cli)
   
   No extra step is required for the Azure ML CLI. The environment definition will be included in the deployment file.
   
   # [Python](#tab/sdk)
   
   Let's get a reference to the environment:
   
   ```python
   environment = Environment(
       conda_file="./bart-text-summarization/environment/conda.yml",
       image="mcr.microsoft.com/azureml/tensorflow-2.4-ubuntu18.04-py37-cpu-inference:latest",
   )
   ```

2. Now, let create the deployment.

   > [!NOTE]
   > This example assumes you have an endpoint created with the name `text-summarization-batch` and a compute cluster with name `cpu-cluster`. If you don't, please follow the steps in the doc [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md).
