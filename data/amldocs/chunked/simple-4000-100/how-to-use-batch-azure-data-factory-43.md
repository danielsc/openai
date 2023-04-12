1. Create a secret to use for authentication as explained at [Option 2: Create a new application secret](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret).
1. Take note of the `client secret` generated.
1. Take note of the `client ID` and the `tenant id` as explained at [Get tenant and app ID values for signing in](../active-directory/develop/howto-create-service-principal-portal.md#option-2-create-a-new-application-secret).
1. Grant access for the service principal you created to your workspace as explained at [Grant access](../role-based-access-control/quickstart-assign-role-user-portal.md#grant-access). In this example the service principal will require:

   1. Permission in the workspace to read batch deployments and perform actions over them.
   1. Permissions to read/write in data stores.

## About the pipeline

We are going to create a pipeline in Azure Data Factory that can invoke a given batch endpoint over some data. The pipeline will communicate with Azure Machine Learning batch endpoints using REST. To know more about how to use the REST API of batch endpoints read [Deploy models with REST for batch scoring](how-to-deploy-batch-with-rest.md). 

The pipeline will look as follows:

# [Using a Managed Identity](#tab/mi)

:::image type="content" source="./media/how-to-use-batch-adf/pipeline-diagram-mi.png" alt-text="Diagram that shows th high level structure of the pipeline we are creating.":::

It is composed of the following activities:

* __Run Batch-Endpoint__: It's a Web Activity that uses the batch endpoint URI to invoke it. It passes the input data URI where the data is located and the expected output file.
* __Wait for job__: It's a loop activity that checks the status of the created job and waits for its completion, either as **Completed** or **Failed**. This activity, in turns, uses the following activities:
  * __Check status__: It's a Web Activity that queries the status of the job resource that was returned as a response of the __Run Batch-Endpoint__ activity. 
  * __Wait__: It's a Wait Activity that controls the polling frequency of the job's status. We set a default of 120 (2 minutes).

The pipeline requires the following parameters to be configured:

| Parameter             | Description  | Sample value |
| --------------------- | -------------|------------- |
| `endpoint_uri`        | The endpoint scoring URI  | `https://<endpoint_name>.<region>.inference.ml.azure.com/jobs` |
| `poll_interval`       | The number of seconds to wait before checking the job status for completion. Defaults to `120`.  | `120` |
| `endpoint_input_uri`  | The endpoint's input data. Multiple data input types are supported. Ensure that the manage identity you are using for executing the job has access to the underlying location. Alternative, if using Data Stores, ensure the credentials are indicated there.  | `azureml://datastores/.../paths/.../data/` |
| `endpoint_input_type`  | The type of the input data you are providing. Currently batch endpoints support folders (`UriFolder`) and File (`UriFile`). Defaults to `UriFolder`.  | `UriFolder` |
| `endpoint_output_uri` | The endpoint's output data file. It must be a path to an output file in a Data Store attached to the Machine Learning workspace. Not other type of URIs is supported. You can use the default Azure Machine Learning data store, named `workspaceblobstore`. | `azureml://datastores/workspaceblobstore/paths/batch/predictions.csv` |

# [Using a Service Principal](#tab/sp)

:::image type="content" source="./media/how-to-use-batch-adf/pipeline-diagram.png" alt-text="Diagram that shows th high level structure of the pipeline we are creating.":::

It is composed of the following activities:

* __Authorize__: It's a Web Activity that uses the service principal created in [Authenticating against batch endpoints](#authenticating-against-batch-endpoints) to obtain an authorization token. This token will be used to invoke the endpoint later.
