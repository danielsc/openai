
# Create, run, and delete Azure ML resources using REST



There are several ways to manage your Azure ML resources. You can use the [portal](https://portal.azure.com/), [command-line interface](/cli/azure), or [Python SDK](https://aka.ms/sdk-v2-install). Or, you can choose the REST API. The REST API uses HTTP verbs in a standard way to create, retrieve, update, and delete resources. The REST API works with any language or tool that can make HTTP requests. REST's straightforward structure often makes it a good choice in scripting environments and for MLOps automation. 

In this article, you learn how to:

> [!div class="checklist"]
> * Retrieve an authorization token
> * Create a properly-formatted REST request using service principal authentication
> * Use GET requests to retrieve information about Azure ML's hierarchical resources
> * Use PUT and POST requests to create and modify resources
> * Use PUT requests to create Azure ML workspaces
> * Use DELETE requests to clean up resources 

## Prerequisites

- An **Azure subscription** for which you have administrative rights. If you don't have such a subscription, try the [free or paid personal subscription](https://azure.microsoft.com/free/)
- An [Azure Machine Learning Workspace](quickstart-create-resources.md).
- Administrative REST requests use service principal authentication. Follow the steps in [Set up authentication for Azure Machine Learning resources and workflows](./how-to-setup-authentication.md#service-principal-authentication) to create a service principal in your workspace
- The **curl** utility. The **curl** program is available in the [Windows Subsystem for Linux](/windows/wsl/install-win10) or any UNIX distribution. In PowerShell, **curl** is an alias for **Invoke-WebRequest** and `curl -d "key=val" -X POST uri` becomes `Invoke-WebRequest -Body "key=val" -Method POST -Uri uri`. 

## Retrieve a service principal authentication token

Administrative REST requests are authenticated with an OAuth2 implicit flow. This authentication flow uses a token provided by your subscription's service principal. To retrieve this token, you'll need:

- Your tenant ID (identifying the organization to which your subscription belongs)
- Your client ID (which will be associated with the created token)
- Your client secret (which you should safeguard)

You should have these values from the response to the creation of your service principal. Getting these values is discussed in [Set up authentication for Azure Machine Learning resources and workflows](./how-to-setup-authentication.md#service-principal-authentication). If you're using your company subscription, you might not have permission to create a service principal. In that case, you should use either a [free or paid personal subscription](https://azure.microsoft.com/free/).

To retrieve a token:

1. Open a terminal window
1. Enter the following code at the command line
1. Substitute your own values for `<YOUR-TENANT-ID>`, `<YOUR-CLIENT-ID>`, and `<YOUR-CLIENT-SECRET>`. Throughout this article, strings surrounded by angle brackets are variables you'll have to replace with your own appropriate values.
1. Run the command

```bash
curl -X POST https://login.microsoftonline.com/<YOUR-TENANT-ID>/oauth2/token \
-d "grant_type=client_credentials&resource=https%3A%2F%2Fmanagement.azure.com%2F&client_id=<YOUR-CLIENT-ID>&client_secret=<YOUR-CLIENT-SECRET>" \
```

The response should provide an access token good for one hour:

```json
{
    "token_type": "Bearer",
    "expires_in": "3599",
    "ext_expires_in": "3599",
    "expires_on": "1578523094",
    "not_before": "1578519194",
    "resource": "https://management.azure.com/",
    "access_token": "YOUR-ACCESS-TOKEN"
}
```

Make note of the token, as you'll use it to authenticate all administrative requests. You'll do so by setting an Authorization header in all requests:

```bash
curl -h "Authorization:Bearer <YOUR-ACCESS-TOKEN>" ...more args...
```

> [!NOTE]
> The value starts with the string "Bearer " including a single space before you add the token.
