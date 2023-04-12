
# Image processing with batch deployments

[!INCLUDE [ml v2](../../includes/machine-learning-dev-v2.md)]

Batch Endpoints can be used for processing tabular data, but also any other file type like images. Those deployments are supported in both MLflow and custom models. In this tutorial, we will learn how to deploy a model that classifies images according to the ImageNet taxonomy.

## About this sample

The model we are going to work with was built using TensorFlow along with the RestNet architecture ([Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027)). A sample of this model can be downloaded from `https://azuremlexampledata.blob.core.windows.net/data/imagenet/model.zip`. The model has the following constrains that are important to keep in mind for deployment:

* It works with images of size 244x244 (tensors of `(224, 224, 3)`).
* It requires inputs to be scaled to the range `[0,1]`.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste YAML and other files, clone the repo, and then change directories to the `cli/endpoints/batch` if you are using the Azure CLI or `sdk/endpoints/batch` if you are using our SDK for Python.

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/cli/endpoints/batch
```

### Follow along in Jupyter Notebooks

You can follow along this sample in a Jupyter Notebook. In the cloned repository, open the notebook: [imagenet-classifier-batch.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/batch/imagenet-classifier-batch.ipynb).

## Prerequisites

[!INCLUDE [basic cli prereqs](../../includes/machine-learning-cli-prereqs.md)]

* You must have a batch endpoint already created. This example assumes the endpoint is named `imagenet-classifier-batch`. If you don't have one, follow the instructions at [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md).
* You must have a compute created where to deploy the deployment. This example assumes the name of the compute is `cpu-cluster`. If you don't, follow the instructions at [Create compute](how-to-use-batch-endpoint.md#create-compute).

## Image classification with batch deployments

In this example, we are going to learn how to deploy a deep learning model that can classify a given image according to the [taxonomy of ImageNet](https://image-net.org/). 

### Registering the model

Batch Endpoint can only deploy registered models so we need to register it. You can skip this step if the model you are trying to deploy is already registered.

1. Downloading a copy of the model:

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    wget https://azuremlexampledata.blob.core.windows.net/data/imagenet/model.zip
    mkdir -p imagenet-classifier
    unzip model.zip -d imagenet-classifier
    ```
    
    # [Python](#tab/sdk)

    ```python
    import os
    import urllib.request
    from zipfile import ZipFile
    
    response = urllib.request.urlretrieve('https://azuremlexampledata.blob.core.windows.net/data/imagenet/model.zip', 'model.zip')
    
    os.mkdirs("imagenet-classifier", exits_ok=True)
    with ZipFile(response[0], 'r') as zip:
      model_path = zip.extractall(path="imagenet-classifier")
    ```
    
2. Register the model:
   
    # [Azure CLI](#tab/cli)

    ```azurecli
    MODEL_NAME='imagenet-classifier'
    az ml model create --name $MODEL_NAME --type "custom_model" --path "imagenet-classifier/model"
    ```

    # [Python](#tab/sdk)

    ```python
    model_name = 'imagenet-classifier'
    model = ml_client.models.create_or_update(
        Model(name=model_name, path=model_path, type=AssetTypes.CUSTOM_MODEL)
    )
    ```

### Creating a scoring script

We need to create a scoring script that can read the images provided by the batch deployment and return the scores of the model. The following script:
