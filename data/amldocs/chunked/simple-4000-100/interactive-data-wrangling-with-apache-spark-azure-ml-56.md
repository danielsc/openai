    >  - Azure Blob storage container shared access signature (SAS) tokens
    >  - Azure Data Lake Storage (ADLS) Gen 2 storage account service principal credentials
    >    - tenant ID 
    >    - client ID and 
    >    - secret
    > 
    >  on the respective user interfaces while creating Azure Key Vault secrets for them.
1. Navigate back to the **Create a secret** screen.
1. In the **Secret value** textbox, enter the access key credential for the Azure storage account, which was copied to the clipboard in the earlier step.
1. Select **Create**.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/create-a-secret.png" alt-text="Screenshot showing the Azure secret creation screen.":::

> [!TIP]
> [Azure CLI](../key-vault/secrets/quick-create-cli.md) and [Azure Key Vault secret client library for Python](../key-vault/secrets/quick-create-python.md#sign-in-to-azure) can also create Azure Key Vault secrets.

## Add role assignments in Azure storage accounts

Before we begin interactive data wrangling, we must ensure that our data is accessible in the Notebooks. First, for

- the user identity of the Notebooks session logged-in user or
- a service principal

assign **Reader** and **Storage Blob Data Reader** roles. However, in certain scenarios, we might want to write the wrangled data back to the Azure storage account. The **Reader** and **Storage Blob Data Reader** roles provide read-only access to the user identity or service principal. To enable read and write access, assign **Contributor** and **Storage Blob Data Contributor** roles to the user identity or service principal. To assign appropriate roles to the user identity or service principal:

1. Navigate to the storage account page in the Microsoft Azure portal
1. Select **Access Control (IAM)** from the left panel.
1. Select **Add role assignment**.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/storage-account-add-role-assignment.png" alt-text="Screenshot showing the Azure access keys screen.":::

1. Search for a desired role: **Storage Blob Data Contributor**, in this example.
1. Select the desired role: **Storage Blob Data Contributor**, in this example.
1. Select **Next**.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/add-role-assignment-choose-role.png" alt-text="Screenshot showing the Azure add role assignment screen.":::

1. Select **User, group, or service principal**.
1. Select **+ Select members**.
1. In the textbox under **Select**, search for the user identity or service principal.
1. Select the user identity or service principal from the list so that it shows under **Selected members**.
1. Select the appropriate user identity or service principal.
1. Select **Next**.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/add-role-assignment-choose-members.png" alt-text="Screenshot showing the Azure add role assignment screen Members tab.":::

1. Select **Review + Assign**.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/add-role-assignment-review-and-assign.png" alt-text="Screenshot showing the Azure add role assignment screen review and assign tab.":::

Data in the Azure storage account should become accessible once the user identity or service principal has appropriate roles assigned.

> [!NOTE]
> If an [attached Synapse Spark pool](./how-to-manage-synapse-spark-pool.md) points to a Synapse Spark pool in an Azure Synapse workspace that has a managed virtual network associated with it, [a managed private endpoint to storage account should be configured](../synapse-analytics/security/connect-to-a-secure-storage-account.md) to ensure data access. 

## Interactive Data Wrangling with Apache Spark

Azure Machine Learning offers Managed (Automatic) Spark compute, and [attached Synapse Spark pool](./how-to-manage-synapse-spark-pool.md), for interactive data wrangling with Apache Spark, in Azure Machine Learning Notebooks. The Managed (Automatic) Spark compute does not require creation of resources in the Azure Synapse workspace. Instead, a fully managed automatic Spark compute becomes directly available in the Azure Machine Learning Notebooks. Using a Managed (Automatic) Spark compute is the easiest approach to access a Spark cluster in Azure Machine Learning.
