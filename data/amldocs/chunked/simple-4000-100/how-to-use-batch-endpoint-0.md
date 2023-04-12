
# Use batch endpoints for batch scoring

[!INCLUDE [cli v2](../../includes/machine-learning-dev-v2.md)]

Batch endpoints provide a convenient way to run inference over large volumes of data. They simplify the process of hosting your models for batch scoring, so you can focus on machine learning, not infrastructure. For more information, see [What are Azure Machine Learning endpoints?](./concept-endpoints.md).

Use batch endpoints when:

> [!div class="checklist"]
> * You have expensive models that requires a longer time to run inference.
> * You need to perform inference over large amounts of data, distributed in multiple files.
> * You don't have low latency requirements.
> * You can take advantage of parallelization.

In this article, you'll learn how to use batch endpoints to do batch scoring.

> [!TIP]
> We suggest you to read the Scenarios sections (see the navigation bar at the left) to find more about how to use Batch Endpoints in specific scenarios including NLP, computer vision, or how to integrate them with other Azure services.

## About this example

In this example, we're going to deploy a model to solve the classic MNIST ("Modified National Institute of Standards and Technology") digit recognition problem to perform batch inferencing over large amounts of data (image files). In the first section of this tutorial, we're going to create a batch deployment with a model created using Torch. Such deployment will become our default one in the endpoint. In the second half, [we're going to see how we can create a second deployment](#adding-deployments-to-an-endpoint) using a model created with TensorFlow (Keras), test it out, and then switch the endpoint to start using the new deployment as default.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste YAML and other files, first clone the repo. Then, change directories to either `cli/endpoints/batch` if you're using the Azure CLI or `sdk/endpoints/batch` if you're using the Python SDK.

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/cli/endpoints/batch
```

### Follow along in Jupyter Notebooks

You can follow along this sample in the following notebooks. In the cloned repository, open the notebook: [mnist-batch.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/batch/mnist-batch.ipynb).

## Prerequisites

[!INCLUDE [basic cli prereqs](../../includes/machine-learning-cli-prereqs.md)]

### Connect to your workspace

First, let's connect to Azure Machine Learning workspace where we're going to work on.

# [Azure CLI](#tab/azure-cli)

```azurecli
az account set --subscription <subscription>
az configure --defaults workspace=<workspace> group=<resource-group> location=<location>
```

# [Python](#tab/python)

The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. In this section, we'll connect to the workspace in which you'll perform deployment tasks.

1. Import the required libraries:

```python
from azure.ai.ml import MLClient, Input
from azure.ai.ml.entities import BatchEndpoint, BatchDeployment, Model, AmlCompute, Data, BatchRetrySettings
from azure.ai.ml.constants import AssetTypes, BatchDeploymentOutputAction
from azure.identity import DefaultAzureCredential
```

2. Configure workspace details and get a handle to the workspace:

```python
subscription_id = "<subscription>"
resource_group = "<resource-group>"
workspace = "<workspace>"

ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)
```

# [Studio](#tab/azure-studio)

Open the [Azure ML studio portal](https://ml.azure.com) and sign in using your credentials.


### Create compute

Batch endpoints run on compute clusters. They support both [Azure Machine Learning Compute clusters (AmlCompute)](./how-to-create-attach-compute-cluster.md) or [Kubernetes clusters](./how-to-attach-kubernetes-anywhere.md). Clusters are a shared resource so one cluster can host one or many batch deployments (along with other workloads if desired).
