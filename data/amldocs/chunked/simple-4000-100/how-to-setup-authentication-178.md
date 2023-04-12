1. From the [Azure portal](https://portal.azure.com), select your workspace and then select __Access Control (IAM)__.
1. Select __Add__, __Add Role Assignment__ to open the __Add role assignment page__.
1. Select the role you want to assign the managed identity. For example, Reader. For detailed steps, see [Assign Azure roles using the Azure portal](../role-based-access-control/role-assignments-portal.md).

### Managed identity with compute cluster

For more information, see [Set up managed identity for compute cluster](how-to-create-attach-compute-cluster.md#set-up-managed-identity).

<a id="service-principal-authentication"></a>

## Use service principal authentication

# [Python SDK v2](#tab/sdk)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Authenticating with a service principal uses the [Azure Identity package for Python](/python/api/overview/azure/identity-readme). The `DefaultAzureCredential` class looks for the following environment variables and uses the values when authenticating as the service principal:

* `AZURE_CLIENT_ID` - The client ID returned when you created the service principal.
* `AZURE_TENANT_ID` - The tenant ID returned when you created the service principal.
* `AZURE_CLIENT_SECRET` - The password/credential generated for the service principal.

> [!TIP]
> During development, consider using the [python-dotenv](https://pypi.org/project/python-dotenv/) package to set these environment variables. Python-dotenv loads environment variables from `.env` files. The standard `.gitignore` file for Python automatically excludes `.env` files, so they shouldn't be checked into any GitHub repos during development.

The following example demonstrates using python-dotenv to load the environment variables from a `.env` file and then using `DefaultAzureCredential` to create the credential object:

```python
from dotenv import load_dotenv

if ( os.environ['ENVIRONMENT'] == 'development'):
    print("Loading environment variables from .env file")
    load_dotenv(".env")

from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
# Check if given credential can get token successfully.
credential.get_token("https://management.azure.com/.default")
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

You can use a service principal for Azure CLI commands. For more information, see [Sign in using a service principal](/cli/azure/create-an-azure-service-principal-azure-cli#sign-in-using-a-service-principal).


The service principal can also be used to authenticate to the Azure Machine Learning [REST API](/rest/api/azureml/). You use the Azure Active Directory [client credentials grant flow](../active-directory/develop/v2-oauth2-client-creds-grant-flow.md), which allow service-to-service calls for headless authentication in automated workflows. 

> [!IMPORTANT]
> If you are currently using Azure Active Directory Authentication Library (ADAL) to get credentials, we recommend that you [Migrate to the Microsoft Authentication Library (MSAL)](../active-directory/develop/msal-migration.md). ADAL support ended June 30, 2022.
