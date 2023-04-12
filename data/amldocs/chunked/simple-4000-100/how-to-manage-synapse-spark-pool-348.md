
> [!NOTE] 
> The `azure.ai.ml.MLClient.begin_create_or_update()` function attaches a new Synapse Spark pool, if a pool with the specified name does not already exist in the workspace. However, if a Synapse Spark pool with that specified name is already attached to the workspace, a call to the `azure.ai.ml.MLClient.begin_create_or_update()` function will update the existing attached pool with the new identity or identities.


## Add role assignments in Azure Synapse Analytics

To ensure that the attached Synapse Spark Pool works properly, assign the [Administrator Role](../synapse-analytics/security/synapse-workspace-synapse-rbac.md#roles) to it, from the Azure Synapse Analytics studio UI. The following steps show how to do it:

1. Open your **Synapse Workspace** in Azure portal.

1. In the left pane, select **Overview**.

    :::image type="content" source="media/how-to-manage-synapse-spark-pool/synapse-workspace-open-synapse-studio.png" alt-text="Screenshot showing Open Synapse Studio.":::
1. Select **Open Synapse Studio**.

1. In the Azure Synapse Analytics studio, select **Manage** in the left pane.

1. Select **Access Control** in the **Security** section of the left pane, second from the left.

1. Select **Add**.

1. The **Add role assignment** panel will open on the right side of the screen. In this panel:

    1. Select **Workspace item** for **Scope**.

    1. In the **Item type** dropdown menu, select **Apache Spark pool**.

    1. In the **Item** dropdown menu, select your Apache Spark pool.

    1. In **Role** dropdown menu, select **Synapse Administrator**.

    1. In the **Select user** search box, start typing the name of your Azure Machine Learning Workspace. It will show you a list of attached Synapse Spark pools. Select your desired Synapse Spark pool from the list.

    1. Select **Apply**.

        :::image type="content" source="media/how-to-manage-synapse-spark-pool/workspace-add-role-assignment.png" alt-text="Screenshot showing Add Role Assignment.":::

## Update the Synapse Spark Pool

# [Studio UI](#tab/studio-ui)

You can manage the attached Synapse Spark pool from the Azure Machine Learning studio UI. Spark pool management functionality includes associated managed identity updates for an attached Synapse Spark pool. You can assign a system-assigned or a user-assigned identity while updating a Synapse Spark pool. You should [create a user-assigned managed identity](../active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities.md#create-a-user-assigned-managed-identity) in Azure portal, before assigning it to a Synapse Spark pool.

To update managed identity for the attached Synapse Spark pool:

:::image type="content" source="media/how-to-manage-synapse-spark-pool/synapse_compute_update_managed_identity.png" alt-text="Screenshot showing Synapse Spark Pool managed identity update.":::

1. Open the **Details** page for the Synapse Spark pool in the Azure Machine Learning studio.

1. Find the edit icon, located on the right side of the **Managed identity** section.

1. To assign a managed identity for the first time, toggle **Assign a managed identity** to enable it.

1. To assign a system-assigned managed identity:
   1.  Select **System-assigned** as the **Identity type**.
   1.  Select **Update**.

1. To assign a user-assigned managed identity:
   1. Select **User-assigned** as the **Identity type**.
   1. Select an Azure **Subscription** from the dropdown menu.
   1. Type the first few letters of the name of user-assigned managed identity in the box showing text **Search by name**. A list with matching user-assigned managed identity names will appear. Select the user-assigned managed identity you want from the list. You can select multiple user-assigned managed identities, and assign them to the attached Synapse Spark pool.
   1. Select **Update**.

# [CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
Execute the `az ml compute update` command, with appropriate parameters, to update the identity associated with an attached Synapse Spark pool. To assign a system-assigned identity, set the `--identity` parameter in the command to `SystemAssigned`, as shown:
