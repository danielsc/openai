

There are a few important concepts to notice in this YAML/Python parameter:

#### Readiness route vs. liveness route

An HTTP server defines paths for both _liveness_ and _readiness_. A liveness route is used to check whether the server is running. A readiness route is used to check whether the server is ready to do work. In machine learning inference, a server could respond 200 OK to a liveness request before loading a model. The server could respond 200 OK to a readiness request only after the model has been loaded into memory.

Review the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) for more information about liveness and readiness probes.

Notice that this deployment uses the same path for both liveness and readiness, since TF Serving only defines a liveness route.

#### Locating the mounted model

When you deploy a model as an online endpoint, Azure Machine Learning _mounts_ your model to your endpoint. Model mounting enables you to deploy new versions of the model without having to create a new Docker image. By default, a model registered with the name *foo* and version *1* would be located at the following path inside of your deployed container: `/var/azureml-app/azureml-models/foo/1`

For example, if you have a directory structure of `/azureml-examples/cli/endpoints/online/custom-container` on your local machine, where the model is named `half_plus_two`:

:::image type="content" source="./media/how-to-deploy-custom-container/local-directory-structure.png" alt-text="Diagram showing a tree view of the local directory structure.":::

# [Azure CLI](#tab/cli)

and `tfserving-deployment.yml` contains:

```yaml
model:
    name: tfserving-mounted
    version: 1
    path: ./half_plus_two
```

# [Python SDK](#tab/python)

and `Model` class contains:

```python
model = Model(name="tfserving-mounted", version="1", path="half_plus_two")
```


then your model will be located under `/var/azureml-app/azureml-models/tfserving-deployment/1` in your deployment:

:::image type="content" source="./media/how-to-deploy-custom-container/deployment-location.png" alt-text="Diagram showing a tree view of the deployment directory structure.":::

You can optionally configure your `model_mount_path`. It enables you to change the path where the model is mounted. 

> [!IMPORTANT]
> The `model_mount_path` must be a valid absolute path in Linux (the OS of the container image).

# [Azure CLI](#tab/cli)

For example, you can have `model_mount_path` parameter in your _tfserving-deployment.yml_:

```YAML
name: tfserving-deployment
endpoint_name: tfserving-endpoint
model:
  name: tfserving-mounted
  version: 1
  path: ./half_plus_two
model_mount_path: /var/tfserving-model-mount
.....
```

# [Python SDK](#tab/python)

For example, you can have `model_mount_path` parameter in your `ManagedOnlineDeployment` class:

```python
blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=online_endpoint_name,
    model=model,
    environment=env,
    model_mount_path="/var/tfserving-model-mount",
    ...
)
```


then your model will be located at `/var/tfserving-model-mount/tfserving-deployment/1` in your deployment. Note that it's no longer under `azureml-app/azureml-models`, but under the mount path you specified:

:::image type="content" source="./media/how-to-deploy-custom-container/mount-path-deployment-location.png" alt-text="Diagram showing a tree view of the deployment directory structure when using mount_model_path.":::

### Create your endpoint and deployment

# [Azure CLI](#tab/cli)

Now that you've understood how the YAML was constructed, create your endpoint.

```azurecli
az ml online-endpoint create --name tfserving-endpoint -f endpoints/online/custom-container/tfserving-endpoint.yml
```

Creating a deployment may take few minutes.

```azurecli
az ml online-deployment create --name tfserving-deployment -f endpoints/online/custom-container/tfserving-deployment.yml --all-traffic
```
