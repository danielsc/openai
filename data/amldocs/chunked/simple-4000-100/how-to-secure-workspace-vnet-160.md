Azure Machine Learning uses an associated Key Vault instance to store the following credentials:
* The associated storage account connection string
* Passwords to Azure Container Repository instances
* Connection strings to data stores

Azure key vault can be configured to use either a private endpoint or service endpoint. To use Azure Machine Learning experimentation capabilities with Azure Key Vault behind a virtual network, use the following steps:

> [!TIP]
> Regardless of whether you use a private endpoint or service endpoint, the key vault must be in the same network as the private endpoint of the workspace.

# [Private endpoint](#tab/pe)

For information on using a private endpoint with Azure Key Vault, see [Integrate Key Vault with Azure Private Link](../key-vault/general/private-link-service.md#establish-a-private-link-connection-to-key-vault-using-the-azure-portal).


# [Service endpoint](#tab/se)

1. Go to the Key Vault that's associated with the workspace.

1. On the __Key Vault__ page, in the left pane, select __Networking__.

1. On the __Firewalls and virtual networks__ tab, do the following actions:
    1. Under __Allow access from__, select __Allow public access from specific virtual networks and IP addresses__.
    1. Under __Virtual networks__, select __Add a virtual network__, __Add existing virtual networks__, and add the virtual network/subnet where your experimentation compute resides.
    1. Verify that __Allow trusted Microsoft services to bypass this firewall__ is checked, and then select __Apply__.

    :::image type="content" source="./media/how-to-enable-virtual-network/key-vault-firewalls-and-virtual-networks-page.png" alt-text="The Firewalls and virtual networks section in the Key Vault pane":::

For more information, see [Configure Azure Key Vault network settings](../key-vault/general/how-to-azure-key-vault-network-security.md).


## Enable Azure Container Registry (ACR)

> [!TIP]
> If you did not use an existing Azure Container Registry when creating the workspace, one may not exist. By default, the workspace will not create an ACR instance until it needs one. To force the creation of one, train or deploy a model using your workspace before using the steps in this section.

Azure Container Registry can be configured to use a private endpoint. Use the following steps to configure your workspace to use ACR when it is in the virtual network:

1. Find the name of the Azure Container Registry for your workspace, using one of the following methods:

    # [Azure CLI](#tab/cli)

    [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

    If you've [installed the Machine Learning extension v2 for Azure CLI](how-to-configure-cli.md), you can use the `az ml workspace show` command to show the workspace information. The v1 extension does not return this information.

    ```azurecli-interactive
    az ml workspace show -n yourworkspacename -g resourcegroupname --query 'container_registry'
    ```

    This command returns a value similar to `"/subscriptions/{GUID}/resourceGroups/{resourcegroupname}/providers/Microsoft.ContainerRegistry/registries/{ACRname}"`. The last part of the string is the name of the Azure Container Registry for the workspace.

    # [Python SDK](#tab/python)

    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

    The following code snippet demonstrates how to get the container registry information using the [Azure Machine Learning SDK](/python/api/overview/azure/ai-ml-readme):

   ```python
    # import required libraries
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential

    subscription_id = "<your subscription ID>"
    resource_group = "<your resource group name>"
    workspace = "<your workspace name>"

    ml_client = MLClient(
        DefaultAzureCredential(), subscription_id, resource_group, workspace
    )
    
    # Get workspace info
    ws=ml_client.workspaces.get(name=workspace)
    print(ws.container_registry)
    ```
