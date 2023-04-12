You may also want to encrypt [diagnostic information logged from your deployed endpoint](how-to-enable-app-insights.md) into your Azure Application Insights instance.

## Encryption in transit

Azure Machine Learning uses TLS to secure internal communication between various Azure Machine Learning microservices. All Azure Storage access also occurs over a secure channel.

To secure external calls made to the scoring endpoint, Azure Machine Learning uses TLS. For more information, see [Use TLS to secure a web service through Azure Machine Learning](./v1/how-to-secure-web-service.md).

## Data collection and handling

### Microsoft collected data

Microsoft may collect non-user identifying information like resource names (for example the dataset name, or the machine learning experiment name), or job environment variables for diagnostic purposes. All such data is stored using Microsoft-managed keys in storage hosted in Microsoft owned subscriptions and follows [Microsoft's standard Privacy policy and data handling standards](https://privacy.microsoft.com/privacystatement). This data is kept within the same region as your workspace.

Microsoft also recommends not storing sensitive information (such as account key secrets) in environment variables. Environment variables are logged, encrypted, and stored by us. Similarly when naming your jobs, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.

You may opt out from diagnostic data being collected by setting the `hbi_workspace` parameter to `TRUE` while provisioning the workspace. This functionality is supported when using the AzureML Python SDK, the Azure CLI, REST APIs, or Azure Resource Manager templates.

## Using Azure Key Vault

Azure Machine Learning uses the Azure Key Vault instance associated with the workspace to store credentials of various kinds:

* The associated storage account connection string
* Passwords to Azure Container Repository instances
* Connection strings to data stores

SSH passwords and keys to compute targets like Azure HDInsight and VMs are stored in a separate key vault that's associated with the Microsoft subscription. Azure Machine Learning doesn't store any passwords or keys provided by users. Instead, it generates, authorizes, and stores its own SSH keys to connect to VMs and HDInsight to run the experiments.

Each workspace has an associated system-assigned managed identity that has the same name as the workspace. This managed identity has access to all keys, secrets, and certificates in the key vault.

## Next steps

* [Connect to Azure storage](how-to-access-data.md)
* [Get data from a datastore](how-to-create-register-datasets.md)
* [Connect to data](v1/how-to-connect-data-ui.md)
* [Train with datasets](v1/how-to-train-with-datasets.md)
* [Customer-managed keys](concept-customer-managed-keys.md).
