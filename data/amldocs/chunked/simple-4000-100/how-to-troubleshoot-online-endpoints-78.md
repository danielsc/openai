1. If there are errors locally, try resolving the conda environment and creating a functional one before redeploying. 

1. If the container crashes even if it resolves locally, the SKU size used for deployment may be too small. 
    1. Conda package installation occurs at runtime, so if the SKU size is too small to accommodate all of the packages detailed in the `conda.yaml` environment file, then the container may crash. 
    1. A Standard_F4s_v2 VM is a good starting SKU size, but larger ones may be needed depending on which dependencies are specified in the conda file.
    1. For Kubernetes online endpoint, the Kubernetes cluster must have minimum of 4 vCPU cores and 8-GB memory.

## Get container logs

You can't get direct access to the VM where the model is deployed. However, you can get logs from some of the containers that are running on the VM. The amount of information you get depends on the provisioning status of the deployment. If the specified container is up and running, you'll see its console output; otherwise, you'll get a message to try again later.

There are two types of containers that you can get the logs from:
- Inference server: Logs include the console log (from [the inference server](how-to-inference-server-http.md)) which contains the output of print/logging functions from your scoring script (`score.py` code). 
- Storage initializer: Logs contain information on whether code and model data were successfully downloaded to the container. The container will run before the inference server container starts to run.

# [Azure CLI](#tab/cli)

To see log output from a container, use the following CLI command:

```azurecli
az ml online-deployment get-logs -e <endpoint-name> -n <deployment-name> -l 100
```

or

```azurecli
az ml online-deployment get-logs --endpoint-name <endpoint-name> --name <deployment-name> --lines 100
```

Add `--resource-group` and `--workspace-name` to the commands above if you have not already set these parameters via `az configure`.

To see information about how to set these parameters, and if current values are already set, run:

```azurecli
az ml online-deployment get-logs -h
```

By default the logs are pulled from the inference server. 

> [!NOTE]
> If you use Python logging, ensure you use the correct logging level order for the messages to be published to logs. For example, INFO.

You can also get logs from the storage initializer container by passing `–-container storage-initializer`. 

Add `--help` and/or `--debug` to commands to see more information. 

# [Python SDK](#tab/python)

To see log output from container, use the `get_logs` method as follows:

```python
ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100
)
```

To see information about how to set these parameters, see
[reference for get-logs](/python/api/azure-ai-ml/azure.ai.ml.operations.onlinedeploymentoperations#azure-ai-ml-operations-onlinedeploymentoperations-get-logs)

By default the logs are pulled from the inference server.

> [!NOTE]
> If you use Python logging, ensure you use the correct logging level order for the messages to be published to logs. For example, INFO.

You can also get logs from the storage initializer container by adding `container_type="storage-initializer"` option. 

```python
ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100, container_type="storage-initializer"
)
```

# [Studio](#tab/studio)

To see log output from a container, use the **Endpoints** in the studio:

1. In the left navigation bar, select Endpoints.
1. (Optional) Create a filter on compute type to show only managed compute types.
1. Select an endpoint's name to view the endpoint's details page.
1. Select the **Deployment logs** tab in the endpoint's details page.
1. Use the dropdown to select the deployment whose log you want to see.

:::image type="content" source="media/how-to-troubleshoot-online-endpoints/deployment-logs.png" lightbox="media/how-to-troubleshoot-online-endpoints/deployment-logs.png" alt-text="A screenshot of observing deployment logs in the studio.":::
