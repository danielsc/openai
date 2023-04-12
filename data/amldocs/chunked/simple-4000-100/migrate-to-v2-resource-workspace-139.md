
## Load/connect to workspace using config file

* SDK v1

    ```python
    from azureml.core import Workspace
    
    ws = Workspace.from_config()
    ws.get_details()
    ```

* SDK v2

    ```python
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Workspace
    from azure.identity import DefaultAzureCredential
    
    ws = MLClient.from_config(
        DefaultAzureCredential()
    )
    ```

## Mapping of key functionality in SDK v1 and SDK v2

|Functionality in SDK v1|Rough mapping in SDK v2|
|-|-|
|[Method/API in SDK v1 (use links to ref docs)](/python/api/azureml-core/azureml.core.workspace.workspace)|[Method/API in SDK v2 (use links to ref docs)](/python/api/azure-ai-ml/azure.ai.ml.entities.workspace)|

## Related documents

For more information, see:

* [What is a workspace?](concept-workspace.md)
