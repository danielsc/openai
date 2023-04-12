When working with REST APIs, we recommend to using either a [service principal](#running-jobs-using-a-service-principal) or a [managed identity](#running-jobs-using-a-managed-identity) to interact with the API.


### Running jobs using a service principal

In this case, we want to execute a batch endpoint using a service principal already created in Azure Active Directory. To complete the authentication, you will have to create a secret to perform the authentication. Follow these steps:

# [Azure CLI](#tab/cli)

1. Create a secret to use for authentication as explained at [Option 2: Create a new application secret](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret). 
1. To authenticate using a service principal, use the following command. For more details see [Sign in with Azure CLI](/cli/azure/authenticate-azure-cli).

    ```azurecli
    az login --service-principal -u <app-id> -p <password-or-cert> --tenant <tenant>
    ```

1. Once authenticated, use the following command to run a batch deployment job:

    ```azurecli
    az ml batch-endpoint invoke --name $ENDPOINT_NAME --input https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/
    ```

# [Python](#tab/sdk)

1. Create a secret to use for authentication as explained at [Option 2: Create a new application secret](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret).
1. To authenticate using a service principal, indicate the tenant ID, client ID and client secret of the service principal using environment variables as demonstrated:

    ```python
    from azure.ai.ml import MLClient
    from azure.identity import EnvironmentCredential

    os.environ["AZURE_TENANT_ID"] = "<TENANT_ID>"
    os.environ["AZURE_CLIENT_ID"] = "<CLIENT_ID>"
    os.environ["AZURE_CLIENT_SECRET"] = "<CLIENT_SECRET>"

    subscription_id = "<subscription>"
    resource_group = "<resource-group>"
    workspace = "<workspace>"

    ml_client = MLClient(EnvironmentCredential(), subscription_id, resource_group, workspace)
    ```

1. Once authenticated, use the following command to run a batch deployment job:

    ```python
    job = ml_client.batch_endpoints.invoke(
            endpoint_name, 
            input=Input(path="https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci")
        )
    ```

# [REST](#tab/rest)

1. Create a secret to use for authentication as explained at [Option 2: Create a new application secret](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret). 

1. Use the login service from Azure to get an authorization token. Authorization tokens are issued to a particular scope. The resource type for Azure Machine learning is `https://ml.azure.com`. The request would look as follows:
    
    __Request__:
    
    ```http
    POST /{TENANT_ID}/oauth2/token HTTP/1.1
    Host: login.microsoftonline.com
    ```
    
    __Body__:
    
    ```
    grant_type=client_credentials&client_id=<CLIENT_ID>&client_secret=<CLIENT_SECRET>&resource=https://ml.azure.com
    ```
    
    > [!IMPORTANT]
    > Notice that the resource scope for invoking a batch endpoints (`https://ml.azure.com1) is different from the resource scope used to manage them. All management APIs in Azure use the resource scope `https://management.azure.com`, including Azure Machine Learning.

3. Once authenticated, use the query to run a batch deployment job:
    
    __Request__:
    
    ```http
    POST jobs HTTP/1.1
    Host: <ENDPOINT_URI>
    Authorization: Bearer <TOKEN>
    Content-Type: application/json
    ```
    __Body:__
        
    ```json
    {
        "properties": {
    	    "InputData": {
    		"mnistinput": {
    		    "JobInputType" : "UriFolder",
    		    "Uri":  "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci"
    	        }
            }
        }
    }
    ```


### Running jobs using a managed identity
