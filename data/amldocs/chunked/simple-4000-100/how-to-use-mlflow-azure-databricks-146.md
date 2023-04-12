    
        > [!IMPORTANT]
        > `DefaultAzureCredential` will try to pull the credentials from the available context. If you want to specify credentials in a different way, for instance using the web browser in an interactive way, you can use `InteractiveBrowserCredential` or any other method available in [`azure.identity`](https://pypi.org/project/azure-identity/) package.
    
    1. Get the Azure Machine Learning Tracking URI:
    
        ```python
        mlflow_tracking_uri = ml_client.workspaces.get(ml_client.workspace_name).mlflow_tracking_uri
        ```
    
    # [Studio](#tab/studio)
    
    Use the Azure Machine Learning portal to get the tracking URI:
    
    1. Open the [Azure Machine Learning studio portal](https://ml.azure.com) and log in using your credentials.
    1. In the upper right corner, click on the name of your workspace to show the __Directory + Subscription + Workspace__ blade.
    1. Click on __View all properties in Azure Portal__.
    1. On the __Essentials__ section, you will find the property __MLflow tracking URI__.
    
    
    # [Manually](#tab/manual)
    
    The Azure Machine Learning Tracking URI can be constructed using the subscription ID, region of where the resource is deployed, resource group name and workspace name. The following code sample shows how:
    
    > [!WARNING]
    > If you are working in a private link-enabled workspace, the MLflow endpoint will also use a private link to communicate with Azure Machine Learning. As a consequence, the tracking URI will look different as proposed here. You need to get the tracking URI using the Azure ML SDK or CLI v2 on those cases.
    
    ```python
    region = "<LOCATION>"
    subscription_id = '<SUBSCRIPTION_ID>'
    resource_group = '<RESOURCE_GROUP>'
    workspace_name = '<AML_WORKSPACE_NAME>'
    
    mlflow_tracking_uri = f"azureml://{region}.api.azureml.ms/mlflow/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}"
    ```

1. Configuring the tracking URI:

    # [Using MLflow SDK](#tab/mlflow)
    
    Then the method [`set_tracking_uri()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_tracking_uri) points the MLflow tracking URI to that URI.
    
    ```python
    import mlflow
    
    mlflow.set_tracking_uri(mlflow_tracking_uri)
    ```
    
    # [Using environment variables](#tab/environ)
    
    You can set the MLflow environment variables [MLFLOW_TRACKING_URI](https://mlflow.org/docs/latest/tracking.html#logging-to-a-tracking-server) in your compute to make any interaction with MLflow in that compute to point by default to Azure Machine Learning.
    
    ```bash
    MLFLOW_TRACKING_URI=$(az ml workspace show --query mlflow_tracking_uri | sed 's/"//g') 
    ```
    

    > [!TIP]
    > When working on shared environments, like an Azure Databricks cluster, Azure Synapse Analytics cluster, or similar, it is useful to set the environment variable `MLFLOW_TRACKING_URI` at the cluster level to automatically configure the MLflow tracking URI to point to Azure Machine Learning for all the sessions running in the cluster rather than to do it on a per-session basis.
    >
    > ![Configure the environment variables in an Azure Databricks cluster](./media/how-to-use-mlflow-azure-databricks/env.png)
    >
    > Once the environment variable is configured, any experiment running in such cluster will be tracked in Azure Machine Learning.


**Configure authentication**

Once the tracking is configured, you'll also need to configure how the authentication needs to happen to the associated workspace. By default, the Azure Machine Learning plugin for MLflow will perform interactive authentication by opening the default browser to prompt for credentials. Refer to [Configure MLflow for Azure Machine Learning: Configure authentication](how-to-use-mlflow-configure-tracking.md#configure-authentication) to additional ways to configure authentication for MLflow in Azure Machine Learning workspaces.
