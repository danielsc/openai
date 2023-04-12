
1. Create a YAML configuration file for your endpoint. The following example configures the name and authentication mode of the endpoint. The one used in the following commands is located at `/cli/endpoints/online/triton/single-model/create-managed-endpoint.yml` in the azureml-examples repo you cloned earlier:

    __create-managed-endpoint.yaml__

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-endpoint
auth_mode: aml_token
```

1. Create a YAML configuration file for the deployment. The following example configures a deployment named __blue__ to the endpoint defined in the previous step. The one used in the following commands is located at `/cli/endpoints/online/triton/single-model/create-managed-deployment.yml` in the azureml-examples repo you cloned earlier:

    > [!IMPORTANT]
    > For Triton no-code-deployment (NCD) to work, setting **`type`** to **`triton_model​`** is required, `type: triton_model​`. For more information, see [CLI (v2) model YAML schema](reference-yaml-model.md).
    >
    > This deployment uses a Standard_NC6s_v3 VM. You may need to request a quota increase for your subscription before you can use this VM. For more information, see [NCv3-series](../virtual-machines/ncv3-series.md).

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
endpoint_name: my-endpoint
model:
  name: sample-densenet-onnx-model
  version: 1
  path: ./models
  type: triton_model
instance_count: 1
instance_type: Standard_NC6s_v3
```

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

This section shows how you can define a Triton deployment to deploy to a managed online endpoint using the Azure Machine Learning Python SDK (v2).

> [!IMPORTANT]
> For Triton no-code-deployment, **[testing via local endpoints](how-to-deploy-online-endpoints.md#deploy-and-debug-locally-by-using-local-endpoints)** is currently not supported.


1. To connect to a workspace, we need identifier parameters - a subscription, resource group and workspace name. 

    ```python 
    subscription_id = "<SUBSCRIPTION_ID>"
    resource_group = "<RESOURCE_GROUP>"
    workspace_name = "<AML_WORKSPACE_NAME>"
    ```

1. Use the following command to set the name of the endpoint that will be created. In this example, a random name is created for the endpoint:

    ```python
    import random

    endpoint_name = f"endpoint-{random.randint(0, 10000)}"
    ```

1. We use these details above in the `MLClient` from `azure.ai.ml` to get a handle to the required Azure Machine Learning workspace. Check the [configuration notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/configuration.ipynb) for more details on how to configure credentials and connect to a workspace.

    ```python 
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential

    ml_client = MLClient(
        DefaultAzureCredential(),
        subscription_id,
        resource_group,
        workspace_name,
    )
    ```

1. Create a `ManagedOnlineEndpoint` object to configure the endpoint. The following example configures the name and authentication mode of the endpoint. 

    ```python 
    from azure.ai.ml.entities import ManagedOnlineEndpoint

    endpoint = ManagedOnlineEndpoint(name=endpoint_name, auth_mode="key")
    ```

1. Create a `ManagedOnlineDeployment` object to configure the deployment. The following example configures a deployment named __blue__ to the endpoint defined in the previous step and defines a local model inline.

    ```python
    from azure.ai.ml.entities import ManagedOnlineDeployment, Model
    
    model_name = "densenet-onnx-model"
    model_version = 1
    
    deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=endpoint_name,
        model=Model(
            name=model_name, 
            version=model_version,
            path="./models",
            type="triton_model"
        ),
        instance_type="Standard_NC6s_v3",
        instance_count=1,
    )
    ``` 
