 ![Link Azure DB and Azure Machine Learning workspaces](./media/how-to-use-mlflow-azure-databricks/link-workspaces.png)
 
After you link your Azure Databricks workspace with your Azure Machine Learning workspace, MLflow Tracking is automatically set to be tracked in all of the following places:

* The linked Azure Machine Learning workspace.
* Your original ADB workspace. 

You can use then MLflow in Azure Databricks in the same way as you're used to. The following example sets the experiment name as it is usually done in Azure Databricks and start logging some parameters:

```python
import mlflow 

experimentName = "/Users/{user_name}/{experiment_folder}/{experiment_name}" 
mlflow.set_experiment(experimentName) 

with mlflow.start_run():
   mlflow.log_param('epochs', 20)
   pass
```

> [!NOTE] 
> As opposite to tracking, model registries don't support registering models at the same time on both Azure Machine Learning and Azure Databricks. Either one or the other has to be used. Please read the section [Registering models in the registry with MLflow](#registering-models-in-the-registry-with-mlflow) for more details.

### Tracking exclusively on Azure Machine Learning workspace

If you prefer to manage your tracked experiments in a centralized location, you can set MLflow tracking  to **only** track in your Azure Machine Learning workspace. This configuration has the advantage of enabling easier path to deployment using Azure Machine Learning deployment options.

> [!WARNING]
> For [private link enabled Azure Machine Learning workspace](how-to-configure-private-link.md), you have to [deploy Azure Databricks in your own network (VNet injection)](/azure/databricks/administration-guide/cloud-configurations/azure/vnet-inject) to ensure proper connectivity.

You have to configure the MLflow tracking URI to point exclusively to Azure Machine Learning, as it is demonstrated in the following example:

**Configure tracking URI**

1. Get the tracking URI for your workspace:

    # [Azure CLI](#tab/cli)
    
    [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
    
    1. Login and configure your workspace:
    
        ```bash
        az account set --subscription <subscription>
        az configure --defaults workspace=<workspace> group=<resource-group> location=<location> 
        ```
    
    1. You can get the tracking URI using the `az ml workspace` command:
    
        ```bash
        az ml workspace show --query mlflow_tracking_uri
        ```
        
    # [Python](#tab/python)
    
    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
    
    You can get the Azure ML MLflow tracking URI using the [Azure Machine Learning SDK v2 for Python](concept-v2.md). Ensure you have the library `azure-ai-ml` installed in the compute you are using. The following sample gets the unique MLFLow tracking URI associated with your workspace.
    
    1. Login into your workspace using the `MLClient`. The easier way to do that is by using the workspace config file:
    
        ```python
        from azure.ai.ml import MLClient
        from azure.identity import DefaultAzureCredential
    
        ml_client = MLClient.from_config(credential=DefaultAzureCredential())
        ```
    
        > [!TIP]
        > You can download the workspace configuration file by:
        > 1. Navigate to [Azure ML studio](https://ml.azure.com)
        > 2. Click on the upper-right corner of the page -> Download config file.
        > 3. Save the file `config.json` in the same directory where you are working on.
    
    1. Alternatively, you can use the subscription ID, resource group name and workspace name to get it:
    
        ```python
        from azure.ai.ml import MLClient
        from azure.identity import DefaultAzureCredential
    
        #Enter details of your AzureML workspace
        subscription_id = '<SUBSCRIPTION_ID>'
        resource_group = '<RESOURCE_GROUP>'
        workspace_name = '<WORKSPACE_NAME>'
    
        ml_client = MLClient(credential=DefaultAzureCredential(),
                                subscription_id=subscription_id, 
                                resource_group_name=resource_group)
        ```
