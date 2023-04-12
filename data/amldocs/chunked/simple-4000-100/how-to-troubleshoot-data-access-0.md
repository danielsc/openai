
# Troubleshoot data access errors

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

In this guide, learn how to identify and resolve known issues with data access with the [Azure Machine Learning SDK](https://aka.ms/sdk-v2-install).

## Error Codes

Data access error codes are hierarchical. Error codes are delimited by the full stop character `.` and are more specific the more segments there are.

## ScriptExecution.DatabaseConnection

### ScriptExecution.DatabaseConnection.NotFound

The database or server defined in the datastore couldn't be found or no longer exists. Check if the database still exists in Azure portal or linked to from the Azure Machine Learning studio datastore details page. If it doesn't exist, recreating it with the same name will enable the existing datastore to be used. If a new server name or database is used, the datastore will have to be deleted, and recreated to use the new name.

### ScriptExecution.DatabaseConnection.Authentication

The authentication failed while trying to connect to the database. The authentication method is stored inside the datastore and supports SQL authentication, service principal, or no stored credential (identity based access). Enabling workspace MSI makes the authentication use the workspace MSI when previewing data in Azure Machine Learning studio. A SQL server user needs to be created for the service principal and workspace MSI (if applicable) and granted classic database permissions. More info can be found [here](/azure/azure-sql/database/authentication-aad-service-principal-tutorial#create-the-service-principal-user-in-azure-sql-database).

Contact your data admin to verify or add the correct permissions to the service principal or user identity.

Errors also include:

- ScriptExecution.DatabaseConnection.Authentication.AzureIdentityAccessTokenResolution.InvalidResource
  - The server under the subscription and resource group couldn't be found. Check that the subscription ID and resource group defined in the datastore matches that of the server and update the values if needed.
    > [!NOTE]
    > Use the subscription ID and resource group of the server and not of the workspace. If the datastore is cross subscription or cross resource group server, these will be different.
- ScriptExecution.DatabaseConnection.Authentication.AzureIdentityAccessTokenResolution.FirewallSettingsResolutionFailure
  - The identity doesn't have permission to read firewall settings of the target server. Contact your data admin to the Reader role to the workspace MSI.

## ScriptExecution.DatabaseQuery

### ScriptExecution.DatabaseQuery.TimeoutExpired

The executed SQL query took too long and timed out. The timeout can be specified at time of data asset creation. If a new timeout is needed, a new asset must be created, or a new version of the current asset must be created. In Azure Machine Learning studio SQL preview, there will have a fixed query timeout, but the defined value will always be honored for jobs.

## ScriptExecution.StreamAccess

### ScriptExecution.StreamAccess.Authentication

The authentication failed while trying to connect to the storage account. The authentication method is stored inside the datastore and depending on the datastore type, can support account key, SAS token, service principal or no stored credential (identity based access). Enabling workspace MSI makes the authentication use the workspace MSI when previewing data in Azure Machine Learning studio.

Contact your data admin to verify or add the correct permissions to the service principal or user identity.

> [!IMPORTANT]
> If identity based access is used, the required RBAC role is Storage Blob Data Reader. If workspace MSI is used for Azure Machine Learning studio preview, the required RBAC roles are Storage Blob Data Reader and Reader.

Errors also include:

- ScriptExecution.StreamAccess.Authentication.AzureIdentityAccessTokenResolution.FirewallSettingsResolutionFailure
  - The identity doesn't have permission to read firewall settings of the target storage account. Contact your data admin to the Reader role to the workspace MSI.
