
# Quickstart: Create workspace resources you need to get started with Azure Machine Learning

In this quickstart, you'll create a workspace and then add compute resources to the workspace. You'll then have everything you need to get started with Azure Machine Learning.  

The workspace is the top-level resource for your machine learning activities, providing a centralized place to view and manage the artifacts you create when you use Azure Machine Learning. The compute resources provide a pre-configured cloud-based environment you can use to train, deploy, automate, manage, and track machine learning models.


## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).

## Create the workspace

If you  already have a workspace, skip this section and continue to [Create a compute instance](#create-compute-instance).

If you don't yet have a workspace, create one now: 
1. Sign in to [Azure Machine Learning studio](https://ml.azure.com)
1. Select **Create workspace**
1. Provide the following information to configure your new workspace:

   Field|Description 
   ---|---
   Workspace name |Enter a unique name that identifies your workspace. Names must be unique across the resource group. Use a name that's easy to recall and to differentiate from workspaces created by others. The workspace name is case-insensitive.
   Subscription |Select the Azure subscription that you want to use.
   Resource group | Use an existing resource group in your subscription or enter a name to create a new resource group. A resource group holds related resources for an Azure solution. You need *contributor* or *owner* role to use an existing resource group.  For more information about access, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).
   Region | Select the Azure region closest to your users and the data resources to create your workspace.
1. Select **Create** to create the workspace

> [!NOTE]
> This creates a workspace along with all required resources. If you would like to reuse resources, such as Storage Account, Azure Container Registry, Azure KeyVault, or Application Insights, use the [Azure portal](https://ms.portal.azure.com/#create/Microsoft.MachineLearningServices) instead.

## Create compute instance

You could install Azure Machine Learning on your own computer.  But in this quickstart, you'll create an online compute resource that has a development environment already installed and ready to go.  You'll use this online machine, a *compute instance*, for your development environment to write and run code in Python scripts and Jupyter notebooks.

Create a *compute instance* to use this development environment for the rest of the tutorials and quickstarts.

1. If you didn't just create a workspace in the previous section, sign in to [Azure Machine Learning studio](https://ml.azure.com) now, and select your workspace.
1. On the left side, select **Compute**.

    :::image type="content" source="media/quickstart-create-resources/compute-section.png" alt-text="Screenshot: shows Compute section on left hand side of screen." lightbox="media/quickstart-create-resources/compute-section.png":::

1. Select **+New** to create a new compute instance.
1. Supply a name, Keep all the defaults on the first page.
1. Select **Create**.
 
In about two minutes, you'll see the **State** of the compute instance change from *Creating* to *Running*.  It's now ready to go.  

## Create compute clusters

Next you'll create a compute cluster.  You'll submit code to this cluster to distribute your training or batch inference processes across a cluster of CPU or GPU compute nodes in the cloud.  

Create a compute cluster that will autoscale between zero and four nodes:

1. Still in the **Compute** section, in the top tab, select **Compute clusters**.
1. Select **+New** to create a new compute cluster.
1. Keep all the defaults on the first page, select **Next**. If you don't see any available compute, you'll need to request a quota increase. Learn more about [managing and increasing quotas](how-to-manage-quotas.md).
