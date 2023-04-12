1. Grant the user identity access to storage resources. For example, grant StorageBlobReader access to the specific storage account you want to use or grant ACL-based permission to specific folders or files in Azure Data Lake Gen 2 storage.

1. Create an Azure Machine Learning datastore without cached credentials for the storage account. If a datastore has cached credentials, such as storage account key, those credentials are used instead of user identity.

1. Submit a training job with property **identity** set to **type: user_identity**, as shown in following job specification. During the training job, the authentication to storage happens via  the identity of the user that submits the job.

    > [!NOTE] 
    > If the **identity** property is left unspecified and datastore does not have cached credentials, then compute managed identity becomes the fallback option. 

    ```yaml
    command: |
    echo "--census-csv: ${{inputs.census_csv}}"
    python hello-census.py --census-csv ${{inputs.census_csv}}
    code: src
    inputs:
    census_csv:
        type: uri_file 
        path: azureml://datastores/mydata/paths/census.csv
    environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
    compute: azureml:cpu-cluster
    identity:
    type: user_identity
    ```

The following steps outline how to set up data access with user identity for training jobs on compute clusters from Python SDK.

1. Grant data access and create data store as described above for CLI.

1. Submit a training job with identity parameter set to [azure.ai.ml.UserIdentityConfiguration](/python/api/azure-ai-ml/azure.ai.ml.useridentityconfiguration). This parameter setting enables the job to access data on behalf of user submitting the job.

    ```python
    from azure.ai.ml import command
    from azure.ai.ml.entities import Data, UriReference
    from azure.ai.ml import Input
    from azure.ai.ml.constants import AssetTypes
    from azure.ai.ml import UserIdentityConfiguration
    
    # Specify the data location
    my_job_inputs = {
        "input_data": Input(type=AssetTypes.URI_FILE, path="<path-to-my-data>")
    }

    # Define the job
    job = command(
        code="<my-local-code-location>", 
        command="python <my-script>.py --input_data ${{inputs.input_data}}",
        inputs=my_job_inputs,
        environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu:9",
        compute="<my-compute-cluster-name>",
        identity= UserIdentityConfiguration() 
    )
    # submit the command
    returned_job = ml_client.jobs.create_or_update(job)
    ```

> [!IMPORTANT] 
> During job submission with authentication with user identity enabled, the code snapshots are protected against tampering by checksum validation. If you have existing pipeline components and intend to use them with authentication with user identity enabled, you may need to re-upload them. Otherwise the job may fail during checksum validation. 

### Work with virtual networks

By default, Azure Machine Learning can't communicate with a storage account that's behind a firewall or in a virtual network.

You can configure storage accounts to allow access only from within specific virtual networks. This configuration requires extra steps to ensure data isn't leaked outside of the network. This behavior is the same for credential-based data access. For more information, see [How to prevent data exfiltration](how-to-prevent-data-loss-exfiltration.md). 

If your storage account has virtual network settings, that dictates what identity type and permissions access is needed. For example for data preview and data profile, the virtual network settings determine what type of identity is used to authenticate data access. 
 
* In scenarios where only certain IPs and subnets are allowed to access the storage, then Azure Machine Learning uses the workspace MSI to accomplish data previews and profiles.

* If your storage is ADLS Gen 2 or Blob and has virtual network settings, customers can use either user identity or workspace MSI depending on the datastore settings defined during creation. 
