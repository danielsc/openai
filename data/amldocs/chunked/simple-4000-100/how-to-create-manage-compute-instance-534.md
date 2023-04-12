
## Assign managed identity

You can assign a system- or user-assigned [managed identity](../active-directory/managed-identities-azure-resources/overview.md) to a compute instance, to authenticate against other Azure resources such as storage. Using managed identities for authentication helps improve workspace security and management. For example, you can allow users to access training data only when logged in to a compute instance. Or use a common user-assigned managed identity to permit access to a specific storage account. 

You can create compute instance with managed identity from Azure ML Studio:

1.	Fill out the form to [create a new compute instance](?tabs=azure-studio#create).
1.	Select **Next: Advanced Settings**.
1.	Enable **Assign a managed identity**.
1.  Select **System-assigned** or **User-assigned** under **Identity type**.
1.  If you selected **User-assigned**, select subscription and name of the identity.

You can use V2 CLI to create compute instance with assign system-assigned managed identity:

```azurecli
az ml compute create --name myinstance --identity-type SystemAssigned --type ComputeInstance --resource-group my-resource-group --workspace-name my-workspace
```

You can also use V2 CLI with yaml file, for example to create a compute instance with user-assigned managed identity:

```azurecli
azure ml compute create --file compute.yaml --resource-group my-resource-group --workspace-name my-workspace
```

The identity definition is contained in compute.yaml file:

```yaml
https://azuremlschemas.azureedge.net/latest/computeInstance.schema.json
name: myinstance
type: computeinstance
identity:
  type: user_assigned
  user_assigned_identities: 
    - resource_id: identity_resource_id
```

Once the managed identity is created, grant the managed identity at least Storage Blob Data Reader role on the storage account of the datastore, see [Accessing storage services](how-to-identity-based-service-authentication.md?tabs=cli#accessing-storage-services). Then, when you work on the compute instance, the managed identity is used automatically to authenticate against datastores.

> [!NOTE]
> The name of the created system managed identity will be in the format /workspace-name/computes/compute-instance-name in your Azure Active Directory. 

You can also use the managed identity manually to authenticate against other Azure resources. The following example shows how to use it to get an Azure Resource Manager access token:

```python
import requests

def get_access_token_msi(resource):
    client_id = os.environ.get("DEFAULT_IDENTITY_CLIENT_ID", None)
    resp = requests.get(f"{os.environ['MSI_ENDPOINT']}?resource={resource}&clientid={client_id}&api-version=2017-09-01", headers={'Secret': os.environ["MSI_SECRET"]})
    resp.raise_for_status()
    return resp.json()["access_token"]

arm_access_token = get_access_token_msi("https://management.azure.com")
```

To use Azure CLI with the managed identity for authentication, specify the identity client ID as the username when logging in: 
```azurecli
az login --identity --username $DEFAULT_IDENTITY_CLIENT_ID
```

> [!NOTE]
> You cannot use ```azcopy``` when trying to use managed identity. ```azcopy login --identity``` will not work.

## Add custom applications such as RStudio or Posit Workbench (preview)

> [!IMPORTANT]
> Items marked (preview) below are currently in public preview.
> The preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

You can set up other applications, such as RStudio, or Posit Workbench (formerly RStudio Workbench), when creating a compute instance. Follow these steps in studio to set up a custom application on your compute instance

1.	Fill out the form to [create a new compute instance](?tabs=azure-studio#create)
