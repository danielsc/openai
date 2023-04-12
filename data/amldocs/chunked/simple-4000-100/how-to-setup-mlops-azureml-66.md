
1. Copy your edited commands into the Azure Shell and run them (**Ctrl** + **Shift** + **v**).

1. After running these commands, you'll be presented with information related to the service principal. Save this information to a safe location, it will be use later in the demo to configure Azure DevOps.

    ```json
    {
       "appId": "<application id>",
       "displayName": "Azure-ARM-dev-Sample_Project_Name",
       "password": "<password>",
       "tenant": "<tenant id>"
    }
    ```

1. Repeat **Step 3.** if you're creating service principals for Dev and Prod environments. For this demo, we'll be creating only one environment, which is Prod.

1. Close the Cloud Shell once the service principals are created. 
      

# [Create from Azure portal](#tab/azure-portal)

1. Navigate to [Azure App Registrations](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceTypeMicrosoft_AAD_IAM)

1. Select **New Registration**.

    ![Screenshot of service principal setup.](./media/how-to-setup-mlops-azureml/SP-setup-ownership-tab.png)

1. Go through the process of creating a Service Principle (SP) selecting **Accounts in any organizational directory (Any Azure AD directory - Multitenant)** and name it  **Azure-ARM-Dev-ProjectName**. Once created, repeat and create a new SP named **Azure-ARM-Prod-ProjectName**. Replace **ProjectName** with the name of your project so that the service principal can be uniquely identified. 

1. Go to **Certificates & Secrets** and add for each SP **New client secret**, then store the value and secret separately.

1. To assign the necessary permissions to these principals, select your respective [subscription](https://portal.azure.com/#view/Microsoft_Azure_BillingSubscriptionsBlade?) and go to IAM. Select **+Add** then select **Add Role Assignment**.

    ![Screenshot of the add role assignment page.](./media/how-to-setup-mlops-azureml/SP-setup-iam-tab.png)

1. Select Contributor and add members selecting + Select Members. Add the member **Azure-ARM-Dev-ProjectName** as create before.

    ![Screenshot of the add role assignment selection.](./media/how-to-setup-mlops-azureml/SP-setup-role-assignment.png)

1. Repeat step here, if you deploy Dev and Prod into the same subscription, otherwise change to the prod subscription and repeat with **Azure-ARM-Prod-ProjectName**. The basic SP setup is successfully finished.


### Set up Azure DevOps

1. Navigate to [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409&WebUserId=2ecdcbf9a1ae497d934540f4edce2b7d). 
   
2. Select **create a new project** (Name the project `mlopsv2` for this tutorial).
   
     ![Screenshot of ADO Project.](./media/how-to-setup-mlops-azureml/ado-create-project.png)
   
3. In the project under **Project Settings** (at the bottom left of the project page) select **Service Connections**.
   
4. Select **New Service Connection**.

     ![Screenshot of ADO New Service connection button.](./media/how-to-setup-mlops-azureml/create_first_service_connection.png)

5. Select **Azure Resource Manager**, select **Next**, select **Service principal (manual)**, select **Next** and select the Scope Level **Subscription**.

     - **Subscription Name** - Use the name of the subscription where your service principal is stored.
     - **Subscription Id** - Use the `subscriptionId` you used in **Step 1.** input as the Subscription ID
     - **Service Principal Id** - Use the `appId` from **Step 1.** output as the Service Principal ID
     - **Service principal key** - Use the `password` from **Step 1.** output as the Service Principal Key
     - **Tenant ID** - Use the `tenant` from **Step 1.** output as the Tenant ID


6. Name the service connection **Azure-ARM-Prod**.  
 
7. Select **Grant access permission to all pipelines**, then select **Verify and Save**. 

The Azure DevOps setup is successfully finished.

### Set up source repository with Azure DevOps
   
1. Open the project you created in [Azure DevOps](https://dev.azure.com/)
