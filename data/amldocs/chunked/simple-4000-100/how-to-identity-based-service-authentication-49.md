> For a workspace with [customer-managed keys for encryption](concept-data-encryption.md), you can pass in a user-assigned managed identity to authenticate from storage to Key Vault. Use the `user-assigned-identity-for-cmk-encryption` (CLI) or `user_assigned_identity_for_cmk_encryption` (SDK) parameters to pass in the managed identity. This managed identity can be the same or different as the workspace primary user assigned managed identity.

### Compute cluster

> [!NOTE]
> Azure Machine Learning compute clusters support only **one system-assigned identity** or **multiple user-assigned identities**, not both concurrently.

The **default managed identity** is the system-assigned managed identity or the first user-assigned managed identity.

During a run there are two applications of an identity:

1. The system uses an identity to set up the user's storage mounts, container registry, and datastores.

    * In this case, the system will use the default-managed identity.

1. You apply an identity to access resources from within the code for a submitted job:

    * In this case, provide the *client_id* corresponding to the managed identity you want to use to retrieve a credential.
    * Alternatively, get the user-assigned identity's client ID through the *DEFAULT_IDENTITY_CLIENT_ID* environment variable.

    For example, to retrieve a token for a datastore with the default-managed identity:

    ```python
    client_id = os.environ.get('DEFAULT_IDENTITY_CLIENT_ID')
    credential = ManagedIdentityCredential(client_id=client_id)
    token = credential.get_token('https://storage.azure.com/')
    ```

To configure a compute cluster with managed identity, use one of the following methods:

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli
az ml compute create -f create-cluster.yml
```

Where the contents of *create-cluster.yml* are as follows: 

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: basic-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120
identity:
  type: user_assigned
  user_assigned_identities: 
    - resource_id: "identity_resource_id"

```

For comparison, the following example is from a YAML file that creates a cluster that uses a system-assigned managed identity:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: basic-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120
identity:
  type: system_assigned

```

If you have an existing compute cluster, you can change between user-managed and system-managed identity. The following examples demonstrate how to change the configuration:

__User-assigned managed identity__

```azurecli
export MSI_NAME=my-cluster-identity
export COMPUTE_NAME=mycluster-msi

does_compute_exist()
{
  if [ -z $(az ml compute show -n $COMPUTE_NAME --query name) ]; then
    echo false
  else
    echo true
  fi
}

echo "Creating MSI $MSI_NAME"
# Get the resource id of the identity
IDENTITY_ID=$(az identity show --name "$MSI_NAME" --query id -o tsv | tail -n1 | tr -d "[:cntrl:]" || true)
if [[ -z $IDENTITY_ID ]]; then
    IDENTITY_ID=$(az identity create -n "$MSI_NAME" --query id -o tsv | tail -n1 | tr -d "[:cntrl:]")
fi
echo "MSI created: $MSI_NAME"
sleep 15 # Let the previous command finish: https://github.com/Azure/azure-cli/issues/8530


echo "Checking if compute $COMPUTE_NAME already exists"
if [ "$(does_compute_exist)" == "true" ]; then
  echo "Skipping, compute: $COMPUTE_NAME exists"
else
  echo "Provisioning compute: $COMPUTE_NAME"
  az ml compute create --name "$COMPUTE_NAME" --type amlcompute --identity-type user_assigned --user-assigned-identities "$IDENTITY_ID"
fi
az ml compute update --name "$COMPUTE_NAME" --identity-type user_assigned --user-assigned-identities "$IDENTITY_ID"

```

__System-assigned managed identity__

```azurecli
az ml compute update --name mycluster --identity-type system_assigned

```
