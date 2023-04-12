
# Text processing with batch deployments

[!INCLUDE [cli v2](../../includes/machine-learning-dev-v2.md)]

Batch Endpoints can be used for processing tabular data, but also any other file type like text. Those deployments are supported in both MLflow and custom models. In this tutorial we will learn how to deploy a model that can perform text summarization of long sequences of text using a model from HuggingFace.

## About this sample

The model we are going to work with was built using the popular library transformers from HuggingFace along with [a pre-trained model from Facebook with the BART architecture](https://huggingface.co/facebook/bart-large-cnn). It was introduced in the paper [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation](https://arxiv.org/abs/1910.13461). This model has the following constrains that are important to keep in mind for deployment:

* It can work with sequences up to 1024 tokens.
* It is trained for summarization of text in English.
* We are going to use TensorFlow as a backend.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste YAML and other files, clone the repo and then change directories to the `cli/endpoints/batch` if you are using the Azure CLI or `sdk/endpoints/batch` if you are using our SDK for Python.

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/cli/endpoints/batch
```

### Follow along in Jupyter Notebooks

You can follow along this sample in a Jupyter Notebook. In the cloned repository, open the notebook: [text-summarization-batch.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/batch/text-summarization-batch.ipynb).

## Prerequisites

[!INCLUDE [basic cli prereqs](../../includes/machine-learning-cli-prereqs.md)]

* You must have an endpoint already created. If you don't please follow the instructions at [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md). This example assumes the endpoint is named `text-summarization-batch`.
* You must have a compute created where to deploy the deployment. If you don't please follow the instructions at [Create compute](how-to-use-batch-endpoint.md#create-compute). This example assumes the name of the compute is `cpu-cluster`.
* Due to the size of the model, it hasn't been included in this repository. Instead, you can generate a local copy with the following code. A local copy of the model will be placed at `bart-text-summarization/model`. We will use it during the course of this tutorial.

   ```python
   from transformers import pipeline

   model = pipeline("summarization", model="facebook/bart-large-cnn")
   model_local_path = 'bart-text-summarization/model'
   summarizer.save_pretrained(model_local_path)
   ```

## NLP tasks with batch deployments

In this example, we are going to learn how to deploy a deep learning model based on the BART architecture that can perform text summarization over text in English. The text will be placed in CSV files for convenience. 

### Registering the model

Batch Endpoint can only deploy registered models. In this case, we need to publish the model we have just downloaded from HuggingFace. You can skip this step if the model you are trying to deploy is already registered.
   
# [Azure CLI](#tab/cli)

```azurecli
MODEL_NAME='bart-text-summarization'
az ml model create --name $MODEL_NAME --type "custom_model" --path "bart-text-summarization/model"
```

# [Python](#tab/sdk)

```python
model_name = 'bart-text-summarization'
model = ml_client.models.create_or_update(
    Model(name=model_name, path='bart-text-summarization/model', type=AssetTypes.CUSTOM_MODEL)
)
```

### Creating a scoring script

We need to create a scoring script that can read the CSV files provided by the batch deployment and return the scores of the model with the summary. The following script does the following:
