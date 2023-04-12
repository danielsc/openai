   1. Permission in the workspace to read batch deployments and perform actions over them.
   1. Permissions to read/write in data stores. 

## Enabling data access

We will be using cloud URIs provided by Event Grid to indicate the input data to send to the deployment job. Batch deployments use the identity of the compute to mount the data. The identity of the job is used to read the data once mounted for external storage accounts. You will need to assign a user-assigned managed identity to the compute cluster in order to ensure it does have access to mount the underlying data. Follow these steps to ensure data access:

1. Create a [managed identity resource](../active-directory/managed-identities-azure-resources/overview.md):

   # [Azure ML CLI](#tab/cli)

   ```azurecli
   IDENTITY=$(az identity create  -n azureml-cpu-cluster-idn  --query id -o tsv)
   ```

   # [Azure ML SDK for Python](#tab/sdk)

   ```python
   # Use the Azure CLI to create the managed identity. Then copy the value of the variable IDENTITY into a Python variable
   identity="/subscriptions/<subscription>/resourcegroups/<resource-group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/azureml-cpu-cluster-idn"
   ```

1. Update the compute cluster to use the managed identity we created:

   > [!NOTE]
   > This examples assumes you have a compute cluster created named `cpu-cluster` and it is used for the default deployment in the endpoint.

   # [Azure ML CLI](#tab/cli)

   ```azurecli
   az ml compute update --name cpu-cluster --identity-type user_assigned --user-assigned-identities $IDENTITY
   ```

   # [Azure ML SDK for Python](#tab/sdk)

   ```python
   from azure.ai.ml import MLClient
   from azure.ai.ml.entities import AmlCompute, ManagedIdentityConfiguration
   from azure.ai.ml.constants import ManagedServiceIdentityType
   
   compute_name = "cpu-cluster"
   compute_cluster = ml_client.compute.get(name=compute_name)
   
   compute_cluster.identity.type = ManagedServiceIdentityType.USER_ASSIGNED
   compute_cluster.identity.user_assigned_identities = [
       ManagedIdentityConfiguration(resource_id=identity)
   ]
   
   ml_client.compute.begin_create_or_update(compute_cluster)
   ```

1. Go to the [Azure portal](https://portal.azure.com) and ensure the managed identity has the right permissions to read the data. To access storage services, you must have at least [Storage Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader) access to the storage account. Only storage account owners can [change your access level via the Azure portal](../storage/blobs/assign-azure-role-data-access.md).

## Create a Logic App

1. In the [Azure portal](https://portal.azure.com), sign in with your Azure account.

1. On the Azure home page, select **Create a resource**.

1. On the Azure Marketplace menu, select **Integration** > **Logic App**.

   ![Screenshot that shows Azure Marketplace menu with "Integration" and "Logic App" selected.](../logic-apps/media/tutorial-build-scheduled-recurring-logic-app-workflow/create-new-logic-app-resource.png)

1. On the **Create Logic App** pane, on the **Basics** tab, provide the following information about your logic app resource.

   ![Screenshot showing Azure portal, logic app creation pane, and info for new logic app resource.](../logic-apps/media/tutorial-build-scheduled-recurring-logic-app-workflow/create-logic-app-settings.png)

   | Property | Required | Value | Description |
   |----------|----------|-------|-------------|
   | **Subscription** | Yes | <*Azure-subscription-name*> | Your Azure subscription name. This example uses **Pay-As-You-Go**. |
   | **Resource Group** | Yes | **LA-TravelTime-RG** | The [Azure resource group](../azure-resource-manager/management/overview.md) where you create your logic app resource and related resources. This name must be unique across regions and can contain only letters, numbers, hyphens (`-`), underscores (`_`), parentheses (`(`, `)`), and periods (`.`). |
