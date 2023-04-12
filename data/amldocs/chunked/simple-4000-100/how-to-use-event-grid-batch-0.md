
# Invoking batch endpoints from Event Grid events in storage

[!INCLUDE [ml v2](../../includes/machine-learning-dev-v2.md)]

Event Grid is a fully managed service that enables you to easily manage events across many different Azure services and applications. It simplifies building event-driven and serverless applications. In this tutorial we are going to learn how to create a Logic App that can subscribe to the Event Grid event associated with new files created in a storage account and trigger a batch endpoint to process the given file.

The workflow will work in the following way:

1. It will be triggered when a new blob is created in a specific storage account.
2. Since the storage account can contain multiple data assets, event filtering will be applied to only react to events happening in a specific folder inside of it. Further filtering can be done is needed.
3. It will get an authorization token to invoke batch endpoints using the credentials from a Service Principal.
4. It will trigger the batch endpoint (default deployment) using the newly created file as input.

> [!IMPORTANT]
> When using Logic App connected with event grid to invoke batch deployment, a job for each file that triggers the event of *blog created* will be generated. However, keep in mind that batch deployments distribute the work at the file level. Since this execution is specifying only one file, then, there will not be any parallelization happening in the deployment. Instead, you will be taking advantage of the capability of batch deployments of executing multiple scoring jobs under the same compute cluster. If you need to run jobs on entire folders in an automatic fashion, we recommend you to switch to [Invoking batch endpoints from Azure Data Factory](how-to-use-batch-azure-data-factory.md).

## Prerequisites

* This example assumes that you have a model correctly deployed as a batch endpoint. Particularly, we are using the *heart condition classifier* created in the tutorial [Using MLflow models in batch deployments](how-to-mlflow-batch.md).
* This example assumes that your batch deployment runs in a compute cluster called `cpu-cluster`.
* The Logic App we are creating will communicate with Azure Machine Learning batch endpoints using REST. To know more about how to use the REST API of batch endpoints read [Deploy models with REST for batch scoring](how-to-deploy-batch-with-rest.md). 

## Authenticating against batch endpoints

Azure Logic Apps can invoke the REST APIs of batch endpoints by using the [HTTP](../connectors/connectors-native-http.md) activity. Batch endpoints support Azure Active Directory for authorization and hence the request made to the APIs require a proper authentication handling.

We recommend to using a service principal for authentication and interaction with batch endpoints in this scenario. 

1. Create a service principal following the steps at [Register an application with Azure AD and create a service principal](../active-directory/develop/howto-create-service-principal-portal.md#register-an-application-with-azure-ad-and-create-a-service-principal).
1. Create a secret to use for authentication as explained at [Option 2: Create a new application secret](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret).
1. Take note of the `client secret` generated.
1. Take note of the `client ID` and the `tenant id` as explained at [Get tenant and app ID values for signing in](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret).
1. Grant access for the service principal you created to your workspace as explained at [Grant access](../role-based-access-control/quickstart-assign-role-user-portal.md#grant-access). In this example the service principal will require:

   1. Permission in the workspace to read batch deployments and perform actions over them.
   1. Permissions to read/write in data stores. 

## Enabling data access
