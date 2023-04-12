
# Set up AutoML training with the Azure ML Python SDK v2

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)] 
> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning Python you are using:"]
> * [v1](./v1/how-to-configure-auto-train-v1.md)
> * [v2 (current version)](how-to-configure-auto-train.md)

In this guide, learn how to set up an automated machine learning, AutoML, training job with the [Azure Machine Learning Python SDK v2](/python/api/overview/azure/ml/intro). Automated ML picks an algorithm and hyperparameters for you and generates a model ready for deployment. This guide provides details of the various options that you can use to configure automated ML experiments.

If you prefer a no-code experience, you can also [Set up no-code AutoML training in the Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md).

If you prefer to submit training jobs with the Azure Machine learning CLI v2 extension, see [Train models](how-to-train-model.md).

## Prerequisites

For this article you need: 
* An Azure Machine Learning workspace. To create the workspace, see [Create workspace resources](quickstart-create-resources.md).

* The Azure Machine Learning Python SDK v2 installed.
    To install the SDK you can either, 
    * Create a compute instance, which already has installed the latest AzureML Python SDK and is pre-configured for ML workflows. See [Create and manage an Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md) for more information. 

    * Use the followings commands to install Azure ML Python SDK v2:
       * Uninstall previous preview version:
       ```Python
       pip uninstall azure-ai-ml
       ```
       * Install the Azure ML Python SDK v2:
       ```Python
       pip install azure-ai-ml
       ```

    [!INCLUDE [automl-sdk-version](../../includes/machine-learning-automl-sdk-version.md)]

## Set up your workspace 

To connect to a workspace, you need to provide a subscription, resource group and workspace name. These details are used in the `MLClient` from `azure.ai.ml` to get a handle to the required Azure Machine Learning workspace. 

In the following example, the default Azure authentication is used along with the default workspace configuration or from any `config.json` file you might have copied into the folders structure. If no `config.json` is found, then you need to manually introduce the subscription_id, resource_group and workspace when creating `MLClient`.

```Python
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

credential = DefaultAzureCredential()
ml_client = None
try:
    ml_client = MLClient.from_config(credential)
except Exception as ex:
    print(ex)
    # Enter details of your AzureML workspace
    subscription_id = "<SUBSCRIPTION_ID>"
    resource_group = "<RESOURCE_GROUP>"
    workspace = "<AZUREML_WORKSPACE_NAME>"
    ml_client = MLClient(credential, subscription_id, resource_group, workspace)

```

## Data source and format

In order to provide training data to AutoML in SDK v2 you need to upload it into the cloud through an **MLTable**.

Requirements for loading data into an MLTable:
- Data must be in tabular form.
- The value to predict, target column, must be in the data.

Training data must be accessible from the remote compute. Automated ML v2 (Python SDK and CLI/YAML) accepts MLTable data assets (v2), although for backwards compatibility it also supports v1 Tabular Datasets from v1 (a registered Tabular Dataset) through the same input dataset properties. However the recommendation is to use MLTable available in v2.

The following YAML code is the definition of a MLTable that could be placed in a local folder or a remote folder in the cloud, along with the data file (.CSV or Parquet file).

```
# MLTable definition file

paths:
  - file: ./bank_marketing_train_data.csv
transformations:
  - read_delimited:
        delimiter: ','
        encoding: 'ascii'
