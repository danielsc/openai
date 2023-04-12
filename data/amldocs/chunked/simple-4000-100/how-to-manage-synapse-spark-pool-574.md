We might want to detach an attached Synapse Spark pool, to clean up a workspace.


# [Studio UI](#tab/studio-ui)

The Azure Machine Learning studio UI also provides a way to detach an attached Synapse Spark pool. Follow these steps to do this:

1. Open the **Details** page for the Synapse Spark pool, in the Azure Machine Learning studio.

1. Select **Detach**, to detach the attached Synapse Spark pool.

# [CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

An attached Synapse Spark pool can be detached by executing the `az ml compute detach` command with name of the pool passed using `--name` parameter as shown here:

```azurecli
az ml compute detach --name <ATTACHED_SPARK_POOL_NAME> --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME>
```

This sample shows the expected output of the above command:

```azurecli 
Are you sure you want to perform this operation? (y/n): y
```

# [Python SDK](#tab/sdk)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

 We will use an `MLClient.compute.begin_delete()` function call. Pass the `name` of the attached Synapse Spark pool, along with the action `Detach`, to the function. This code snippet detaches a Synapse Spark pool from an Azure Machine Learning workspace:

```python
# import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import SynapseSparkCompute
from azure.identity import DefaultAzureCredential

subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
)

synapse_name = "<ATTACHED_SPARK_POOL_NAME>"
ml_client.compute.begin_delete(name=synapse_name, action="Detach")
```

## Managed Synapse Spark Pool in Azure Machine Learning

Some user scenarios may require access to a Synapse Spark Pool, during an Azure Machine Learning job submission, without a need to attach a Spark pool. The Azure Synapse Analytics integration with Azure Machine Learning (preview) also provides a Managed (Automatic) Spark compute experience that allows access to a Spark pool in a job, without a need to attach the compute to a workspace first. [Learn more about the Managed (Automatic) Spark compute experience](interactive-data-wrangling-with-apache-spark-azure-ml.md).

## Next steps

- [Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)](./interactive-data-wrangling-with-apache-spark-azure-ml.md)

- [Submit Spark jobs in Azure Machine Learning (preview)](./how-to-submit-spark-jobs.md)
