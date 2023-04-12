1. Grant the workspace __managed identity__ a __Managed Identity Operator__ role on the __user-assigned managed identity__ from the previous step. This role allows the workspace to assign the user-assigned managed identity to ACR Task for building the managed environment. 

    1. Obtain the principal ID of workspace system-assigned managed identity:

        [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

        ```azurecli-interactive
        az ml workspace show -w <workspace name> -g <resource group> --query identityPrincipalId
        ```

    1. Grant the Managed Identity Operator role:

        ```azurecli-interactive
        az role assignment create --assignee <principal ID> --role managedidentityoperator --scope <user-assigned managed identity resource ID>
        ```

        The user-assigned managed identity resource ID is Azure resource ID of the user assigned identity, in the format `/subscriptions/<subscription ID>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<user-assigned managed identity name>`.

1. Specify the external ACR and client ID of the __user-assigned managed identity__ in workspace connections by using the `az ml connection` command. This command accepts a YAML file that provides information on the connection. The following example demonstrates the format for specifying a managed identity. Replace the `client_id` and `resource_id` values with the ones for your managed identity:

    [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
name: test_ws_conn_cr_managed
type: container_registry
target: https://test-feed.com
credentials:
  type: managed_identity
  client_id: client_id
  resource_id: resource_id
```

    The following command demonstrates how to use the YAML file to create a connection with your workspace. Replace `<yaml file>`, `<workspace name>`, and `<resource group>` with the values for your configuration:

    ```azurecli-interactive
    az ml connection create --file <yml file> --resource-group <resource group> --workspace-name <workspace>
    ```

1. Once the configuration is complete, you can use the base images from private ACR when building environments for training or inference. The following code snippet demonstrates how to specify the base image ACR and image name in an environment definition:

    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

    ```yml
    $schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json
    name: private-acr-example
    image: <acr url>/pytorch/pytorch:latest
    description: Environment created from private ACR.
    ```

## Next steps

* Learn more about [enterprise security in Azure Machine Learning](concept-enterprise-security.md)
* Learn about [data administration](how-to-administrate-data-authentication.md)
* Learn about [managed identities on compute cluster](how-to-create-attach-compute-cluster.md).
