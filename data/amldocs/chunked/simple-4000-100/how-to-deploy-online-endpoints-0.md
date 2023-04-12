
# Deploy and score a machine learning model by using an online endpoint

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Learn how to use an online endpoint to deploy your model, so you don't have to create and manage the underlying infrastructure. You'll begin by deploying a model on your local machine to debug any errors, and then you'll deploy and test it in Azure.

You'll also learn how to view the logs and monitor the service-level agreement (SLA). You start with a model and end up with a scalable HTTPS/REST endpoint that you can use for online and real-time scoring. 

Online endpoints are endpoints that are used for online (real-time) inferencing. There are two types of online endpoints: **managed online endpoints** and **Kubernetes online endpoints**. For more information on endpoints, and differences between managed online endpoints and Kubernetes online endpoints, see [What are Azure Machine Learning endpoints?](concept-endpoints.md#managed-online-endpoints-vs-kubernetes-online-endpoints).

Managed online endpoints help to deploy your ML models in a turnkey manner. Managed online endpoints work with powerful CPU and GPU machines in Azure in a scalable, fully managed way. Managed online endpoints take care of serving, scaling, securing, and monitoring your models, freeing you from the overhead of setting up and managing the underlying infrastructure. 

The main example in this doc uses managed online endpoints for deployment. To use Kubernetes instead, see the notes in this document inline with the managed online endpoint discussion. 

> [!TIP]
> To create managed online endpoints in the Azure Machine Learning studio, see [Use managed online endpoints in the studio](how-to-use-managed-online-endpoint-studio.md).

## Prerequisites

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [basic prereqs cli](../../includes/machine-learning-cli-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

   ```azurecli
   az account set --subscription <subscription ID>
   az configure --defaults workspace=<Azure Machine Learning workspace name> group=<resource group>
   ```

* (Optional) To deploy locally, you must [install Docker Engine](https://docs.docker.com/engine/install/) on your local computer. We *highly recommend* this option, so it's easier to debug issues.

> [!IMPORTANT]
> The examples in this document assume that you are using the Bash shell. For example, from a Linux system or [Windows Subsystem for Linux](/windows/wsl/about). 

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!INCLUDE [basic prereqs sdk](../../includes/machine-learning-sdk-v2-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* (Optional) To deploy locally, you must [install Docker Engine](https://docs.docker.com/engine/install/) on your local computer. We *highly recommend* this option, so it's easier to debug issues.

# [ARM template](#tab/arm)

> [!NOTE]
> While the Azure CLI and CLI extension for machine learning are used in these steps, they're not the main focus. they're used more as utilities, passing templates to Azure and checking the status of template deployments.
