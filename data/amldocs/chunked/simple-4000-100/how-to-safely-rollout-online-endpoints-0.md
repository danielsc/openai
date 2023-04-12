
# Safe rollout for online endpoints

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

In this article, you'll learn how to deploy a new version of a machine learning model in production without causing any disruption. You'll use blue-green deployment, also known as a safe rollout strategy, to introduce a new version of a web service to production. This strategy will allow you to roll out your new version of the web service to a small subset of users or requests before rolling it out completely.

This article assumes you're using online endpoints, that is, endpoints that are used for online (real-time) inferencing. There are two types of online endpoints: **managed online endpoints** and **Kubernetes online endpoints**. For more information on endpoints and the differences between managed online endpoints and Kubernetes online endpoints, see [What are Azure Machine Learning endpoints?](concept-endpoints.md#managed-online-endpoints-vs-kubernetes-online-endpoints).

> [!Note]
> The main example in this article uses managed online endpoints for deployment. To use Kubernetes endpoints instead, see the notes in this document inline with the managed online endpoints discussion.

In this article, you'll learn to:

> [!div class="checklist"]
> * Define an online endpoint and a deployment called "blue" to serve version 1 of a model
> * Scale the blue deployment so that it can handle more requests
> * Deploy version 2 of the model (called the "green" deployment) to the endpoint, but send the deployment no live traffic
> * Test the green deployment in isolation
> * Mirror a percentage of live traffic to the green deployment to validate it (preview)
> * Send a small percentage of live traffic to the green deployment
> * Send over all live traffic to the green deployment
> * Delete the now-unused v1 blue deployment

## Prerequisites

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [basic prereqs cli](../../includes/machine-learning-cli-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

   ```azurecli
   az account set --subscription <subscription id>
   az configure --defaults workspace=<azureml workspace name> group=<resource group>
   ```

* (Optional) To deploy locally, you must [install Docker Engine](https://docs.docker.com/engine/install/) on your local computer. We *highly recommend* this option, so it's easier to debug issues.

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!INCLUDE [basic prereqs sdk](../../includes/machine-learning-sdk-v2-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* (Optional) To deploy locally, you must [install Docker Engine](https://docs.docker.com/engine/install/) on your local computer. We *highly recommend* this option, so it's easier to debug issues.


## Prepare your system

# [Azure CLI](#tab/azure-cli)

### Clone the examples repository

To follow along with this article, first clone the [examples repository (azureml-examples)](https://github.com/azure/azureml-examples). Then, go to the repository's `cli/` directory:
