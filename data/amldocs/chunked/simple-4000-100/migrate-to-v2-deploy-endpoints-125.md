
For more information on concepts for endpoints and deployments, see [What are online endpoints?](concept-endpoints.md#what-are-online-endpoints)


## Submit a request

* SDK v1

    ```python
    import json
    data = {
        "query": "What color is the fox",
        "context": "The quick brown fox jumped over the lazy dog.",
    }
    data = json.dumps(data)
    predictions = service.run(input_data=data)
    print(predictions)
    ```

* SDK v2

    ```python
    # test the endpoint (the request will route to blue deployment as set above)
    ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        request_file="../model-1/sample-request.json",
    )
    
    # test the specific (blue) deployment
    ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="blue",
        request_file="../model-1/sample-request.json",
    )
    ```

## Delete resources

* SDK v1

    ```python
    service.delete()
    ```

* SDK v2

    ```python
    ml_client.online_endpoints.begin_delete(name=online_endpoint_name)
    ```

## Mapping of key functionality in SDK v1 and SDK v2

|Functionality in SDK v1|Rough mapping in SDK v2|
|-|-|
|[azureml.core.model.Model class](/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py&preserve-view=true)|[azure.ai.ml.entities.Model class](/python/api/azure-ai-ml/azure.ai.ml.entities.model)|
|[azureml.core.Environment class](/python/api/azureml-core/azureml.core.environment%28class%29?view=azure-ml-py&preserve-view=true)|[azure.ai.ml.entities.Environment class](/python/api/azure-ai-ml/azure.ai.ml.entities.environment)|
|[azureml.core.model.InferenceConfig class](/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py&preserve-view=true)|[azure.ai.ml.entities.CodeConfiguration class](/python/api/azure-ai-ml/azure.ai.ml.entities.codeconfiguration)|
|[azureml.core.webservice.AciWebservice class](/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py&preserve-view=true#azureml-core-webservice-aciwebservice-deploy-configuration)|[azure.ai.ml.entities.OnlineDeployment class](/python/api/azure-ai-ml/azure.ai.ml.entities.onlinedeployment?view=azure-python-&preserve-view=true) (and [azure.ai.ml.entities.ManagedOnlineEndpoint class](/en-us/python/api/azure-ai-ml/azure.ai.ml.entities.managedonlineendpoint))|
|[Model.deploy](/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py&preserve-view=true#azureml-core-model-deploy) or [Webservice.deploy](/python/api/azureml-core/azureml.core.webservice%28class%29?view=azure-ml-py&preserve-view=true#azureml-core-webservice-deploy) |[ml_client.begin_create_or_update(online_deployment)](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-begin-create-or-update)|
[Webservice.run](/python/api/azureml-core/azureml.core.webservice%28class%29?view=azure-ml-py&preserve-view=true#azureml-core-webservice-run)|[ml_client.online_endpoints.invoke](/python/api/azure-ai-ml/azure.ai.ml.operations.onlineendpointoperations#azure-ai-ml-operations-onlineendpointoperations-invoke)|
[Webservice.delete](/python/api/azureml-core/azureml.core.webservice%28class%29?view=azure-ml-py&preserve-view=true#azureml-core-webservice-delete)|[ml_client.online_endpoints.delete](/python/api/azure-ai-ml/azure.ai.ml.operations.onlineendpointoperations#azure-ai-ml-operations-onlineendpointoperations-begin-delete)|

## Related documents

For more information, see

v2 docs:
* [What are endpoints?](concept-endpoints.md)
* [Deploy machine learning models to managed online endpoint using Python SDK v2](how-to-deploy-managed-online-endpoint-sdk-v2.md)

v1 docs:
* [MLOps: ML model management v1](v1/concept-model-management-and-deployment.md)
* [Deploy machine learning models](v1/how-to-deploy-and-where.md?tabs=python.md)
