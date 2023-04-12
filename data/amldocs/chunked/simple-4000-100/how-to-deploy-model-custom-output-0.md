
# Customize outputs in batch deployments

[!INCLUDE [ml v2](../../includes/machine-learning-dev-v2.md)]

Sometimes you need to execute inference having a higher control of what is being written as output of the batch job. Those cases include:

> [!div class="checklist"]
> * You need to control how the predictions are being written in the output. For instance, you want to append the prediction to the original data (if data is tabular).
> * You need to write your predictions in a different file format from the one supported out-of-the-box by batch deployments.
> * Your model is a generative model that can't write the output in a tabular format. For instance, models that produce images as outputs.
> * Your model produces multiple tabular files instead of a single one. This is the case for instance of models that perform forecasting considering multiple scenarios.

In any of those cases, Batch Deployments allow you to take control of the output of the jobs by allowing you to write directly to the output of the batch deployment job. In this tutorial, we'll see how to deploy a model to perform batch inference and writes the outputs in `parquet` format by appending the predictions to the original input data.

## About this sample

This example shows how you can deploy a model to perform batch inference and customize how your predictions are written in the output. This example uses an MLflow model based on the [UCI Heart Disease Data Set](https://archive.ics.uci.edu/ml/datasets/Heart+Disease). The database contains 76 attributes, but we are using a subset of 14 of them. The model tries to predict the presence of heart disease in a patient. It is integer valued from 0 (no presence) to 1 (presence).

The model has been trained using an `XGBBoost` classifier and all the required preprocessing has been packaged as a `scikit-learn` pipeline, making this model an end-to-end pipeline that goes from raw data to predictions.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste YAML and other files, clone the repo and then change directories to the `cli/endpoints/batch` if you are using the Azure CLI or `sdk/endpoints/batch` if you are using our SDK for Python.

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/cli/endpoints/batch
```

### Follow along in Jupyter Notebooks

You can follow along this sample in a Jupyter Notebook. In the cloned repository, open the notebook: [custom-output-batch.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/batch/custom-output-batch.ipynb).

## Prerequisites

[!INCLUDE [basic cli prereqs](../../includes/machine-learning-cli-prereqs.md)]

* A model registered in the workspace. In this tutorial, we'll use an MLflow model. Particularly, we are using the *heart condition classifier* created in the tutorial [Using MLflow models in batch deployments](how-to-mlflow-batch.md).
* You must have an endpoint already created. If you don't, follow the instructions at [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md). This example assumes the endpoint is named `heart-classifier-batch`.
* You must have a compute created where to deploy the deployment. If you don't, follow the instructions at [Create compute](how-to-use-batch-endpoint.md#create-compute). This example assumes the name of the compute is `cpu-cluster`.

## Creating a batch deployment with a custom output

In this example, we are going to create a deployment that can write directly to the output folder of the batch deployment job. The deployment will use this feature to write custom parquet files.

### Registering the model

Batch Endpoint can only deploy registered models. In this case, we already have a local copy of the model in the repository, so we only need to publish the model to the registry in the workspace. You can skip this step if the model you are trying to deploy is already registered.
