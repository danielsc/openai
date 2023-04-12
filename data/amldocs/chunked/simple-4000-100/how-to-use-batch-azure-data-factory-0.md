
# Run batch endpoints from Azure Data Factory

[!INCLUDE [ml v2](../../includes/machine-learning-dev-v2.md)]

Big data requires a service that can orchestrate and operationalize processes to refine these enormous stores of raw data into actionable business insights. [Azure Data Factory](../data-factory/introduction.md) is a managed cloud service that's built for these complex hybrid extract-transform-load (ETL), extract-load-transform (ELT), and data integration projects.

Azure Data Factory allows the creation of pipelines that can orchestrate multiple data transformations and manage them as a single unit. Batch endpoints are an excellent candidate to become a step in such processing workflow. In this example, learn how to use batch endpoints in Azure Data Factory activities by relying on the Web Invoke activity and the REST API.

## Prerequisites

* This example assumes that you have a model correctly deployed as a batch endpoint. Particularly, we are using the *heart condition classifier* created in the tutorial [Using MLflow models in batch deployments](how-to-mlflow-batch.md).
* An Azure Data Factory resource created and configured. If you have not created your data factory yet, follow the steps in [Quickstart: Create a data factory by using the Azure portal and Azure Data Factory Studio](../data-factory/quickstart-create-data-factory-portal.md) to create one.  
* After creating it, browse to the data factory in the Azure portal:

   :::image type="content" source="../data-factory/media/doc-common-process/data-factory-home-page.png" alt-text="Screenshot of the home page for the Azure Data Factory, with the Open Azure Data Factory Studio tile.":::

* Select **Open** on the **Open Azure Data Factory Studio** tile to launch the Data Integration application in a separate tab.

## Authenticating against batch endpoints

Azure Data Factory can invoke the REST APIs of batch endpoints by using the [Web Invoke](../data-factory/control-flow-web-activity.md) activity. Batch endpoints support Azure Active Directory for authorization and hence the request made to the APIs require a proper authentication handling.

You can use a service principal or a [managed identity](../active-directory/managed-identities-azure-resources/overview.md) to authenticate against Batch Endpoints. We recommend using a managed identity as it simplifies the use of secrets.

# [Using a Managed Identity](#tab/mi)

1. You can use Azure Data Factory managed identity to communicate with Batch Endpoints. In this case, you only need to make sure that your Azure Data Factory resource was deployed with a managed identity.
2. If you don't have an Azure Data Factory resource or it was already deployed without a managed identity, please follow the following steps to create it: [Managed identity for Azure Data Factory](../data-factory/data-factory-service-identity.md#system-assigned-managed-identity).

   > [!WARNING]
   > Notice that changing the resource identity once deployed is not possible in Azure Data Factory. Once the resource is created, you will need to recreate it if you need to change the identity of it.

3. Once deployed, grant access for the managed identity of the resource you created to your Azure Machine Learning workspace as explained at [Grant access](../role-based-access-control/quickstart-assign-role-user-portal.md#grant-access). In this example the service principal will require:

   1. Permission in the workspace to read batch deployments and perform actions over them.
   1. Permissions to read/write in data stores.
   2. Permissions to read in any cloud location (storage account) indicated as a data input.

# [Using a Service Principal](#tab/sp)

1. Create a service principal following the steps at [Register an application with Azure AD and create a service principal](../active-directory/develop/howto-create-service-principal-portal.md#register-an-application-with-azure-ad-and-create-a-service-principal).
1. Create a secret to use for authentication as explained at [Option 2: Create a new application secret](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret).
