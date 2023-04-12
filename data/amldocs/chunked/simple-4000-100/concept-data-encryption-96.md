* [AciWebservice.deploy_configuration()](/python/api/azureml-core/azureml.core.webservice.aci.aciwebservice#deploy-configuration-cpu-cores-none--memory-gb-none--tags-none--properties-none--description-none--location-none--auth-enabled-none--ssl-enabled-none--enable-app-insights-none--ssl-cert-pem-file-none--ssl-key-pem-file-none--ssl-cname-none--dns-name-label-none--primary-key-none--secondary-key-none--collect-model-data-none--cmk-vault-base-url-none--cmk-key-name-none--cmk-key-version-none-) reference

* [Where and how to deploy](./v1/how-to-deploy-and-where.md)

For more information on using a customer-managed key with ACI, see [Encrypt deployment data](../container-instances/container-instances-encrypt-data.md).

### Azure Kubernetes Service

You may encrypt a deployed Azure Kubernetes Service resource using customer-managed keys at any time. For more information, see [Bring your own keys with Azure Kubernetes Service](../aks/azure-disk-customer-managed-keys.md). 

This process allows you to encrypt both the Data and the OS Disk of the deployed virtual machines in the Kubernetes cluster.

> [!IMPORTANT]
> This process only works with AKS K8s version 1.17 or higher. Azure Machine Learning added support for AKS 1.17 on Jan 13, 2020.

### Machine Learning Compute

**Compute cluster**
The OS disk for each compute node stored in Azure Storage is encrypted with Microsoft-managed keys in Azure Machine Learning storage accounts. This compute target is ephemeral, and clusters are typically scaled down when no jobs are queued. The underlying virtual machine is de-provisioned, and the OS disk is deleted. Azure Disk Encryption is not enabled for workspaces by default. If the workspace was created with the `hbi_workspace` parameter set to `TRUE`, then the OS disk is encrypted. 

Each virtual machine also has a local temporary disk for OS operations. If you want, you can use the disk to stage training data. If the workspace was created with the `hbi_workspace` parameter set to `TRUE`, the temporary disk is encrypted. This environment is short-lived (only during your job,) and encryption support is limited to system-managed keys only.

**Compute instance**
The OS disk for compute instance is encrypted with Microsoft-managed keys in Azure Machine Learning storage accounts. If the workspace was created with the `hbi_workspace` parameter set to `TRUE`, the local OS and temporary disks on compute instance are encrypted with Microsoft managed keys. Customer managed key encryption is not supported for OS and temporary disks.

For more information, see [Customer-managed keys](concept-customer-managed-keys.md).

### Azure Data Factory

The Azure Data Factory pipeline is used to ingest data for use with Azure Machine Learning. Azure Data Factory encrypts data at rest, including entity definitions and any data cached while runs are in progress. By default, data is encrypted with a randomly generated Microsoft-managed key that is uniquely assigned to your data factory. 

For information on how to use customer managed keys for encryption use [Encrypt Azure Data Factory with customer managed keys](../data-factory/enable-customer-managed-key.md) .


### Azure Databricks

Azure Databricks can be used in Azure Machine Learning pipelines. By default, the Databricks File System (DBFS) used by Azure Databricks is encrypted using a Microsoft-managed key. To configure Azure Databricks to use customer-managed keys, see [Configure customer-managed keys on default (root) DBFS](/azure/databricks/security/customer-managed-keys-dbfs).

### Microsoft-generated data

When using services such as Automated Machine Learning, Microsoft may generate a transient, pre-processed data for training multiple models. This data is stored in a datastore in your workspace, which allows you to enforce access controls and encryption appropriately.

You may also want to encrypt [diagnostic information logged from your deployed endpoint](how-to-enable-app-insights.md) into your Azure Application Insights instance.
