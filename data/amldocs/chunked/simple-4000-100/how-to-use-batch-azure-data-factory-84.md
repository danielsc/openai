* __Authorize__: It's a Web Activity that uses the service principal created in [Authenticating against batch endpoints](#authenticating-against-batch-endpoints) to obtain an authorization token. This token will be used to invoke the endpoint later.
* __Run Batch-Endpoint__: It's a Web Activity that uses the batch endpoint URI to invoke it. It passes the input data URI where the data is located and the expected output file.
* __Wait for job__: It's a loop activity that checks the status of the created job and waits for its completion, either as **Completed** or **Failed**. This activity, in turns, uses the following activities:
  * __Check status__: It's a Web Activity that queries the status of the job resource that was returned as a response of the __Run Batch-Endpoint__ activity. 
  * __Wait__: It's a Wait Activity that controls the polling frequency of the job's status. We set a default of 120 (2 minutes).

The pipeline requires the following parameters to be configured:

| Parameter             | Description  | Sample value |
| --------------------- | -------------|------------- |
| `tenant_id`           | Tenant ID where the endpoint is deployed  | `00000000-0000-0000-00000000` |
| `client_id`           | The client ID of the service principal used to invoke the endpoint  | `00000000-0000-0000-00000000` |
| `client_secret`       | The client secret of the service principal used to invoke the endpoint  | `ABCDEFGhijkLMNOPQRstUVwz` |
| `endpoint_uri`        | The endpoint scoring URI  | `https://<endpoint_name>.<region>.inference.ml.azure.com/jobs` |
| `poll_interval`       | The number of seconds to wait before checking the job status for completion. Defaults to `120`.  | `120` |
| `endpoint_input_uri`  | The endpoint's input data. Multiple data input types are supported. Ensure that the manage identity you are using for executing the job has access to the underlying location. Alternative, if using Data Stores, ensure the credentials are indicated there.  | `azureml://datastores/.../paths/.../data/` |
| `endpoint_input_type`  | The type of the input data you are providing. Currently batch endpoints support folders (`UriFolder`) and File (`UriFile`). Defaults to `UriFolder`.  | `UriFolder` |
| `endpoint_output_uri` | The endpoint's output data file. It must be a path to an output file in a Data Store attached to the Machine Learning workspace. Not other type of URIs is supported. You can use the default Azure Machine Learning data store, named `workspaceblobstore`. | `azureml://datastores/workspaceblobstore/paths/batch/predictions.csv` |


> [!WARNING]
> Remember that `endpoint_output_uri` should be the path to a file that doesn't exist yet. Otherwise, the job will fail with the error *the path already exists*.

## Steps

To create this pipeline in your existing Azure Data Factory and invoke batch endpoints, follow these steps:

1. Ensure the compute where the batch endpoint is running has permissions to mount the data Azure Data Factory is providing as input. Notice that access is still granted by the identity that invokes the endpoint (in this case Azure Data Factory). However, the compute where the batch endpoint runs needs to have permission to mount the storage account your Azure Data Factory provide. See [Accessing storage services](how-to-identity-based-service-authentication.md#accessing-storage-services) for details.

1. Open Azure Data Factory Studio and under __Factory Resources__ click the plus sign.

1. Select __Pipeline__ > __Import from pipeline template__

1. You will be prompted to select a `zip` file. Uses [the following template if using managed identities](https://azuremlexampledata.blob.core.windows.net/data/templates/batch-inference/Run-BatchEndpoint-MI.zip) or [the following one if using a service principal](https://azuremlexampledata.blob.core.windows.net/data/templates/batch-inference/Run-BatchEndpoint-SP.zip).

1. A preview of the pipeline will show up in the portal. Click __Use this template__.

