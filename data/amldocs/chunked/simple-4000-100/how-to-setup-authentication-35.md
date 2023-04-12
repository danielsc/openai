Once you've created the Azure AD accounts, see [Manage access to Azure Machine Learning workspace](how-to-assign-roles.md) for information on granting them access to the workspace and other operations in Azure Machine Learning.

## Use interactive authentication

# [Python SDK v2](#tab/sdk)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Interactive authentication uses the [Azure Identity package for Python](/python/api/overview/azure/identity-readme). Most examples use `DefaultAzureCredential` to access your credentials. When a token is needed, it requests one using multiple identities (`EnvironmentCredential`, `ManagedIdentityCredential`, `SharedTokenCacheCredential`, `VisualStudioCodeCredential`, `AzureCliCredential`, `AzurePowerShellCredential`) in turn, stopping when one provides a token. For more information, see the [DefaultAzureCredential](/python/api/azure-identity/azure.identity.defaultazurecredential) class reference.

The following is an example of using `DefaultAzureCredential` to authenticate. If authentication using `DefaultAzureCredential` fails, a fallback of authenticating through your web browser is used instead.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

try:
    credential = DefaultAzureCredential()
    # Check if given credential can get token successfully.
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:
    # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
    # This will open a browser page for
    credential = InteractiveBrowserCredential()
```

After the credential object has been created, the [MLClient](/python/api/azure-ai-ml/azure.ai.ml.mlclient) class is used to connect to the workspace. For example, the following code uses the `from_config()` method to load connection information:

```python
try:
    ml_client = MLClient.from_config(credential=credential)
except Exception as ex:
    # NOTE: Update following workspace information to contain
    #       your subscription ID, resource group name, and workspace name
    client_config = {
        "subscription_id": "<SUBSCRIPTION_ID>",
        "resource_group": "<RESOURCE_GROUP>",
        "workspace_name": "<AZUREML_WORKSPACE_NAME>",
    }

    # write and reload from config file
    import json, os

    config_path = "../.azureml/config.json"
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w") as fo:
        fo.write(json.dumps(client_config))
    ml_client = MLClient.from_config(credential=credential, path=config_path)

print(ml_client)
```

# [Azure CLI](#tab/cli)

When using the Azure CLI, the `az login` command is used to authenticate the CLI session. For more information, see [Get started with Azure CLI](/cli/azure/get-started-with-azure-cli).


## Configure a service principal

To use a service principal (SP), you must first create the SP. Then grant it access to your workspace. As mentioned earlier, Azure role-based access control (Azure RBAC) is used to control access, so you must also decide what access to grant the SP.

> [!IMPORTANT]
> When using a service principal, grant it the __minimum access required for the task__ it is used for. For example, you would not grant a service principal owner or contributor access if all it is used for is reading the access token for a web deployment.
>
> The reason for granting the least access is that a service principal uses a password to authenticate, and the password may be stored as part of an automation script. If the password is leaked, having the minimum access required for a specific tasks minimizes the malicious use of the SP.

The easiest way to create an SP and grant access to your workspace is by using the [Azure CLI](/cli/azure/install-azure-cli). To create a service principal and grant it access to your workspace, use the following steps:

> [!NOTE]
> You must be an admin on the subscription to perform all of these steps.
