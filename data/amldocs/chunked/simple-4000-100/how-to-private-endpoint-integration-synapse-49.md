* [Azure Synapse Analytics Managed Virtual Network](../synapse-analytics/security/synapse-workspace-managed-vnet.md)
* [Secure Azure Machine Learning workspace resources using virtual networks](how-to-network-security-overview.md).
* [Connect to a secure Azure storage account from your Synapse workspace](../synapse-analytics/security/connect-to-a-secure-storage-account.md).

## Configure Azure Synapse

> [!IMPORTANT]
> Before following these steps, you need an Azure Synapse workspace that is configured to use a managed virtual network. For more information, see [Azure Synapse Analytics Managed Virtual Network](../synapse-analytics/security/synapse-workspace-managed-vnet.md).

1. From Azure Synapse Studio, [Create a new Azure Machine Learning linked service](../synapse-analytics/machine-learning/quickstart-integrate-azure-machine-learning.md).
1. After creating and publishing the linked service, select __Manage__,  __Managed private endpoints__, and then __+ New__ in Azure Synapse Studio.

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/add-managed-private-endpoint.png" alt-text="Screenshot of the managed private endpoints dialog.":::

1. From the __New managed private endpoint__ page, search for __Azure Machine Learning__ and select the tile.

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/new-private-endpoint-select-machine-learning.png" alt-text="Screenshot of selecting Azure Machine Learning.":::

1. When prompted to select the Azure Machine Learning workspace, use the __Azure subscription__ and __Azure Machine Learning workspace__ you added previously as a linked service. Select __Create__ to create the endpoint.
    
    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/new-managed-private-endpoint.png" alt-text="Screenshot of the new private endpoint dialog.":::

1. The endpoint will be listed as __Provisioning__ until it has been created. Once created, the __Approval__ column will list a status of __Pending__. You'll approve the endpoint in the [Configure Azure Machine Learning](#configure-azure-machine-learning) section.

    > [!NOTE]
    > In the following screenshot, a managed private endpoint has been created for the Azure Data Lake Storage Gen 2 associated with this Synapse workspace. For information on how to create an Azure Data Lake Storage Gen 2 and enable a private endpoint for it, see [Provision and secure a linked service with Managed VNet](../synapse-analytics/data-integration/linked-service.md).

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/managed-private-endpoint-connections.png" alt-text="Screenshot of the managed private endpoints list.":::

### Create a Spark pool

To verify that the integration between Azure Synapse and Azure Machine Learning is working, you'll use an Apache Spark pool. For information on creating one, see [Create a Spark pool](../synapse-analytics/quickstart-create-apache-spark-pool-portal.md).

## Configure Azure Machine Learning

1. From the [Azure portal](https://portal.azure.com), select your __Azure Machine Learning workspace__, and then select __Networking__.
1. Select __Private endpoints__, and then select the endpoint you created in the previous steps. It should have a status of __pending__. Select __Approve__ to approve the endpoint connection.

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/approve-pending-private-endpoint.png" alt-text="Screenshot of the private endpoint approval.":::

1. From the left of the page, select __Access control (IAM)__. Select __+ Add__, and then select __Role assignment__.

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/workspace-role-assignment.png" alt-text="Screenshot of the role assignment.":::

1. Select __Contributor__, and then select __Next__.

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/contributor-role.png" alt-text="Screenshot of selecting contributor.":::
