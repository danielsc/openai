
# Set up MLOps with Azure DevOps

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Azure Machine Learning allows you to integrate with [Azure DevOps pipeline](/azure/devops/pipelines/) to automate the machine learning lifecycle. Some of the operations you can automate are:

* Deployment of AzureML infrastructure
* Data preparation (extract, transform, load operations)
* Training machine learning models with on-demand scale-out and scale-up
* Deployment of machine learning models as public or private web services
* Monitoring deployed machine learning models (such as for performance analysis)

In this article, you learn about using Azure Machine Learning to set up an end-to-end MLOps pipeline that runs a linear regression to predict taxi fares in NYC. The pipeline is made up of components, each serving  different functions, which can be registered with the workspace, versioned, and reused with various inputs and outputs. you're going to be using the [recommended Azure architecture for MLOps](/azure/architecture/data-guide/technology-choices/machine-learning-operations-v2) and [Azure MLOps (v2) solution accelerator](https://github.com/Azure/mlops-v2) to quickly setup an MLOps project in AzureML.

> [!TIP]
> We recommend you understand some of the [recommended Azure architectures](/azure/architecture/data-guide/technology-choices/machine-learning-operations-v2) for MLOps before implementing any solution. You'll need to pick the best architecture for your given Machine learning project.

## Prerequisites

- An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
- An Azure Machine Learning workspace.
- Git running on your local machine.
- An [organization](/azure/devops/organizations/accounts/create-organization) in Azure DevOps.
- [Azure DevOps project](how-to-devops-machine-learning.md) that will host the source repositories and pipelines.
- The [Terraform extension for Azure DevOps](https://marketplace.visualstudio.com/items?itemName=ms-devlabs.custom-terraform-tasks) if you're using Azure DevOps + Terraform to spin up infrastructure

> [!NOTE]
>
>Git version 2.27 or newer is required. For more information on installing the Git command, see https://git-scm.com/downloads and select your operating system

> [!IMPORTANT]
>The CLI commands in this article were tested using Bash. If you use a different shell, you may encounter errors.

## Set up authentication with Azure and DevOps

Before you can set up an MLOps project with AzureML, you need to set up authentication for Azure DevOps.

### Create service principal
   For the use of the demo, the creation of one or two service principles is required, depending on how many environments, you want to work on (Dev or Prod or Both). These principles can be created using one of the following methods:

# [Create from Azure Cloud Shell](#tab/azure-shell)

1. Launch the [Azure Cloud Shell](https://shell.azure.com).

    > [!TIP]
    > The first time you've launched the Cloud Shell, you'll be prompted to create a storage account for the Cloud Shell.

1. If prompted, choose **Bash** as the environment used in the Cloud Shell. You can also change environments in the drop-down on the top navigation bar

    ![Screenshot of the cloud shell environment dropdown.](./media/how-to-setup-mlops-azureml/PS_CLI1_1.png)

1. Copy the following bash commands to your computer and update the **projectName**, **subscriptionId**, and **environment** variables with the values for your project. If you're creating both a Dev and Prod environment, you'll need to run this script once for each environment, creating a service principal for each. This command will also grant the **Contributor** role to the service principal in the subscription provided. This is required for Azure DevOps to properly use resources in that subscription. 

    ``` bash
    projectName="<your project name>"
    roleName="Contributor"
    subscriptionId="<subscription Id>"
    environment="<Dev|Prod>" #First letter should be capitalized
    servicePrincipalName="Azure-ARM-${environment}-${projectName}"
    # Verify the ID of the active subscription
    echo "Using subscription ID $subscriptionID"
    echo "Creating SP for RBAC with name $servicePrincipalName, with role $roleName and in scopes     /subscriptions/$subscriptionId"
    az ad sp create-for-rbac --name $servicePrincipalName --role $roleName --scopes /subscriptions/$subscriptionId
    echo "Please ensure that the information created here is properly save for future use."
    ```
