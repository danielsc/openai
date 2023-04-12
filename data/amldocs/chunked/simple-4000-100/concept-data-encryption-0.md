
# Data encryption with Azure Machine Learning

Azure Machine Learning relies on a various of Azure data storage services and compute resources when training models and performing inferences. In this article, learn about the data encryption for each service both at rest and in transit.

> [!IMPORTANT]
> For production grade encryption during __training__, Microsoft recommends using Azure Machine Learning compute cluster. For production grade encryption during __inference__, Microsoft recommends using Azure Kubernetes Service.
>
> Azure Machine Learning compute instance is a dev/test environment. When using it, we recommend that you store your files, such as notebooks and scripts, in a file share. Your data should be stored in a datastore.

## Encryption at rest

Azure Machine Learning end to end projects integrates with services like Azure Blob Storage, Azure Cosmos DB, Azure SQL Database etc. The article describes encryption method of such services.

### Azure Blob storage

Azure Machine Learning stores snapshots, output, and logs in the Azure Blob storage account (default storage account) that's tied to the Azure Machine Learning workspace and your subscription. All the data stored in Azure Blob storage is encrypted at rest with Microsoft-managed keys.

For information on how to use your own keys for data stored in Azure Blob storage, see [Azure Storage encryption with customer-managed keys in Azure Key Vault](../storage/common/customer-managed-keys-configure-key-vault.md).

Training data is typically also stored in Azure Blob storage so that it's accessible to training compute targets. This storage isn't managed by Azure Machine Learning but mounted to compute targets as a remote file system.

If you need to __rotate or revoke__ your key, you can do so at any time. When rotating a key, the storage account will start using the new key (latest version) to encrypt data at rest. When revoking (disabling) a key, the storage account takes care of failing requests. It usually takes an hour for the rotation or revocation to be effective.

For information on regenerating the access keys, see [Regenerate storage access keys](how-to-change-storage-access-key.md).

### Azure Data Lake Storage

[!INCLUDE [Note](../../includes/data-lake-storage-gen1-rename-note.md)]

**ADLS Gen2**
Azure Data Lake Storage Gen 2 is built on top of Azure Blob Storage and is designed for enterprise big data analytics. ADLS Gen2 is used as a datastore for Azure Machine Learning. Same as Azure Blob Storage the data at rest is encrypted with Microsoft-managed keys.

For information on how to use your own keys for data stored in Azure Data Lake Storage, see [Azure Storage encryption with customer-managed keys in Azure Key Vault](../storage/common/customer-managed-keys-configure-key-vault.md).

### Azure Relational Databases

Azure Machine Learning services support data from different data sources such as Azure SQL Database, Azure PostgreSQL and Azure MYSQL. 

**Azure SQL Database**
Transparent Data Encryption protects Azure SQL Database against threat of malicious offline activity by encrypting data at rest. By default, TDE is enabled for all newly deployed SQL Databases with Microsoft managed keys.

For information on how to use customer managed keys for transparent data encryption, see [Azure SQL Database Transparent Data Encryption](/azure/azure-sql/database/transparent-data-encryption-tde-overview) . 

**Azure Database for PostgreSQL**
Azure PostgreSQL uses Azure Storage encryption to encrypt data at rest by default using Microsoft managed keys. It is similar to Transparent Data Encryption (TDE) in other databases such as SQL Server.

For information on how to use customer managed keys for transparent data encryption, see [Azure Database for PostgreSQL Single server data encryption with a customer-managed key](../postgresql/single-server/concepts-data-encryption-postgresql.md).

**Azure Database for MySQL**
Azure Database for MySQL is a relational database service in the Microsoft cloud based on the MySQL Community Edition database engine. The Azure Database for MySQL service uses the FIPS 140-2 validated cryptographic module for storage encryption of data at-rest. 
