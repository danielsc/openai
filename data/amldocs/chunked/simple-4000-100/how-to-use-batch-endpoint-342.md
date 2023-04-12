
# [Python](#tab/python)

```python
compute_name = "batch-cluster"
compute_cluster = AmlCompute(name=compute_name, description="amlcompute", min_instances=0, max_instances=5)
ml_client.begin_create_or_update(compute_cluster)
```

# [Studio](#tab/azure-studio)

*Create a compute cluster as explained in the following tutorial [Create an Azure Machine Learning compute cluster](./how-to-create-attach-compute-cluster.md?tabs=azure-studio).*


> [!NOTE]
> You are not charged for compute at this point as the cluster will remain at 0 nodes until a batch endpoint is invoked and a batch scoring job is submitted. Learn more about [manage and optimize cost for AmlCompute](./how-to-manage-optimize-cost.md#use-azure-machine-learning-compute-cluster-amlcompute).


### Registering the model

Batch Deployments can only deploy models registered in the workspace. You can skip this step if the model you're trying to deploy is already registered. In this case, we're registering a Torch model for the popular digit recognition problem (MNIST).

> [!TIP]
> Models are associated with the deployment rather than with the endpoint. This means that a single endpoint can serve different models or different model versions under the same endpoint as long as they are deployed in different deployments.

   
# [Azure CLI](#tab/azure-cli)

```azurecli
MODEL_NAME='mnist'
az ml model create --name $MODEL_NAME --type "custom_model" --path "./mnist/model/"
```

# [Python](#tab/python)

```python
model_name = 'mnist'
model = ml_client.models.create_or_update(
    Model(name=model_name, path='./mnist/model/', type=AssetTypes.CUSTOM_MODEL)
)
```

# [Studio](#tab/azure-studio)

1. Navigate to the __Models__ tab on the side menu.
1. Select __Register__ > __From local files__.
1. In the wizard, leave the option *Model type* as __Unspecified type__.
1. Select __Browse__ > __Browse folder__ > Select the folder `./mnist/model/` > __Next__.
1. Configure the name of the model: `mnist`. You can leave the rest of the fields as they are.
1. Select __Register__.


## Create a batch endpoint

A batch endpoint is an HTTPS endpoint that clients can call to trigger a batch scoring job. A batch scoring job is a job that scores multiple inputs (for more, see [What are batch endpoints?](./concept-endpoints.md#what-are-batch-endpoints)). A batch deployment is a set of compute resources hosting the model that does the actual batch scoring. One batch endpoint can have multiple batch deployments.

> [!TIP]
> One of the batch deployments will serve as the default deployment for the endpoint. The default deployment will be used to do the actual batch scoring when the endpoint is invoked. Learn more about [batch endpoints and batch deployment](./concept-endpoints.md#what-are-batch-endpoints).

### Steps

1. Decide on the name of the endpoint. The name of the endpoint will end-up in the URI associated with your endpoint. Because of that, __batch endpoint names need to be unique within an Azure region__. For example, there can be only one batch endpoint with the name `mybatchendpoint` in `westus2`.

    # [Azure CLI](#tab/azure-cli)
    
    In this case, let's place the name of the endpoint in a variable so we can easily reference it later.
    
    ```azurecli
    ENDPOINT_NAME="mnist-batch"
    ```
    
    # [Python](#tab/python)
    
    In this case, let's place the name of the endpoint in a variable so we can easily reference it later.

    ```python
    endpoint_name="mnist-batch"
    ```
    
    # [Studio](#tab/azure-studio)
    
    *You'll configure the name of the endpoint later in the creation wizard.*
    

1. Configure your batch endpoint

    # [Azure CLI](#tab/azure-cli)

    The following YAML file defines a batch endpoint, which you can include in the CLI command for [batch endpoint creation](#create-a-batch-endpoint). In the repository, this file is located at `/cli/endpoints/batch/batch-endpoint.yml`.
    
    __mnist-endpoint.yml__

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/batchEndpoint.schema.json
name: mnist-batch
description: A batch endpoint for scoring images from the MNIST dataset.
auth_mode: aad_token
```
