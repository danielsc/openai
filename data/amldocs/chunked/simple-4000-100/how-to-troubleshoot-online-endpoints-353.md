Make sure the model is registered to the same workspace as the deployment. To show details for a model in a workspace: 
  
#### [Azure CLI](#tab/cli)

```azurecli
az ml model show --name <model-name> --version <version>
```

#### [Python SDK](#tab/python)

```python
ml_client.models.get(name="<model-name>", version=<version>)
```

#### [Studio](#tab/studio)

See the **Models** page in the studio:

1. In the left navigation bar, select Models.
1. Select a model's name to view the model's details page.


> [!WARNING]
> You must specify either version or label to get the model's information.

You can also check if the blobs are present in the workspace storage account.

- For example, if the blob is `https://foobar.blob.core.windows.net/210212154504-1517266419/WebUpload/210212154504-1517266419/GaussianNB.pkl`, you can use this command to check if it exists:
   
  ```azurecli
  az storage blob exists --account-name foobar --container-name 210212154504-1517266419 --name WebUpload/210212154504-1517266419/GaussianNB.pkl --subscription <sub-name>`
  ```
  
- If the blob is present, you can use this command to obtain the logs from the storage initializer:

  #### [Azure CLI](#tab/cli)

  ```azurecli
  az ml online-deployment get-logs --endpoint-name <endpoint-name> --name <deployment-name> –-container storage-initializer`
  ```

  #### [Python SDK](#tab/python)

  ```python
  ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100, container_type="storage-initializer"
  )
  ```

  #### [Studio](#tab/studio)

  You can't see logs from the storage initializer in the studio. Use the Azure CLI or Python SDK (see each tab for details). 


#### Resource requests greater than limits

Requests for resources must be less than or equal to limits. If you don't set limits, we set default values when you attach your compute to an Azure Machine Learning workspace. You can check limits in the Azure portal or by using the `az ml compute show` command.

#### azureml-fe not ready
The front-end component (azureml-fe) that routes incoming inference requests to deployed services automatically scales as needed. It's installed during your k8s-extension installation.

This component should be healthy on cluster, at least one healthy replica. You will get this error message if it's not available when you trigger kubernetes online endpoint and deployment creation/update request.

Please check the pod status and logs to fix this issue, you can also try to update the k8s-extension installed on the cluster.


### ERROR: ResourceNotReady

To run the `score.py` provided as part of the deployment, Azure creates a container that includes all the resources that the `score.py` needs, and runs the scoring script on that container. The error in this scenario is that this container is crashing when running, which means scoring can't happen. This error happens when:

- There's an error in `score.py`. Use `get-logs` to help diagnose common problems:
    - A package that was imported but isn't in the conda environment.
    - A syntax error.
    - A failure in the `init()` method.
- If `get-logs` isn't producing any logs, it usually means that the container has failed to start. To debug this issue, try [deploying locally](#deploy-locally) instead.
- Readiness or liveness probes aren't set up correctly.
- There's an error in the environment set up of the container, such as a missing dependency.
- When you face `TypeError: register() takes 3 positional arguments but 4 were given` error, the error may be caused by the dependency between flask v2 and `azureml-inference-server-http`. See [FAQs for inference HTTP server](how-to-inference-server-http.md#1-i-encountered-the-following-error-during-server-startup) for more details.

### ERROR: ResourceNotFound

Below is a list of reasons you might run into this error only when using either managed online endpoint or Kubernetes online endpoint:

* [Azure Resource Manager cannot find a required resource](#resource-manager-cannot-find-a-resource)
