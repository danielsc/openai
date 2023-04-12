  - The identity doesn't have permission to read firewall settings of the target storage account. Contact your data admin to the Reader role to the workspace MSI.
- ScriptExecution.StreamAccess.Authentication.AzureIdentityAccessTokenResolution.PrivateEndpointResolutionFailure
  - The target storage account is using a virtual network but the logged in session isn't connecting to the workspace via a private endpoint. Add a private endpoint to the workspace and ensure that the virtual network or subnet of the private endpoint is allowed by the storage virtual network settings. Add the logged in session's public IP to the storage firewall allowlist.
- ScriptExecution.StreamAccess.Authentication.AzureIdentityAccessTokenResolution.NetworkIsolationViolated
  - The target storage account's firewall settings don't permit this data access. Check that your logged in session is within compatible network settings with the storage account. If Workspace MSI is used, check that it has Reader access to the storage account and to the private endpoints associated with the storage account.
- ScriptExecution.StreamAccess.Authentication.AzureIdentityAccessTokenResolution.InvalidResource
  - The storage account under the subscription and resource group couldn't be found. Check that the subscription ID and resource group defined in the datastore matches that of the storage account and update the values if needed.
    > [!NOTE]
    > Use the subscription ID and resource group of the server and not of the workspace. If the datastore is cross subscription or cross resource group server, these will be different.

### ScriptExecution.StreamAccess.NotFound

The specified file or folder path doesn't exist. Check that the provided path exists in Azure portal or if using a datastore, that the right datastore is used (including the datastore's account and container). If the storage account is an HNS enabled Blob storage, otherwise known as ADLS Gen2, or an `abfs[s]` URI, that storage ACLs may restrict particular folders or paths. This error will appear as a "NotFound" error instead of an "Authentication" error.

### ScriptExecution.StreamAccess.Validation

There were validation errors in the request for data access.

Errors also include:

- ScriptExecution.StreamAccess.Validation.TextFile-InvalidEncoding
  - The defined encoding for delimited file parsing isn't applicable for the underlying data. Update the encoding of the MLTable to match the encoding of the file(s).
- ScriptExecution.StreamAccess.Validation.StorageRequest-InvalidUri
  - The requested URI isn't well formatted. We support `abfs[s]`, `wasb[s]`, `https`, and `azureml` URIs.

## Next steps

- See more information on [data concepts in Azure Machine Learning](concept-data.md)

- [AzureML authentication to other services](how-to-identity-based-service-authentication.md).
- [Create datastores](how-to-datastore.md)
- [Read and write data in a job](how-to-read-write-data-v2.md)
