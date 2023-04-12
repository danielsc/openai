> If you are currently using Azure Active Directory Authentication Library (ADAL) to get credentials, we recommend that you [Migrate to the Microsoft Authentication Library (MSAL)](../active-directory/develop/msal-migration.md). ADAL support ended June 30, 2022.

For information and samples on authenticating with MSAL, see the following articles:

* JavaScript - [How to migrate a JavaScript app from ADAL.js to MSAL.js](../active-directory/develop/msal-compare-msal-js-and-adal-js.md).
* Node.js - [How to migrate a Node.js app from Microsoft Authentication Library to MSAL](../active-directory/develop/msal-node-migration.md).
* Python - [Microsoft Authentication Library to MSAL migration guide for Python](../active-directory/develop/migrate-python-adal-msal.md).

## Use managed identity authentication

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Authenticating with a managed identity uses the [Azure Identity package for Python](/python/api/overview/azure/identity-readme). To authenticate to the workspace from a VM or compute cluster that is configured with a managed identity, use the `DefaultAzureCredential` class. This class automatically detects if a managed identity is being used, and uses the managed identity to authenticate to Azure services.

The following example demonstrates using the `DefaultAzureCredential` class to create the credential object, then using the `MLClient` class to connect to the workspace:

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
# Check if given credential can get token successfully.
credential.get_token("https://management.azure.com/.default")

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

## Use Conditional Access

> [!IMPORTANT]
> [Azure AD Conditional Access](/azure/active-directory/conditional-access/overview) is __not__ supported with Azure Machine Learning.

## Next steps

* [How to use secrets in training](how-to-use-secrets-in-runs.md).
* [How to authenticate to online endpoints](how-to-authenticate-online-endpoint.md).
