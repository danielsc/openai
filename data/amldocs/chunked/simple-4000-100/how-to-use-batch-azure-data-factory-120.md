1. You will be prompted to select a `zip` file. Uses [the following template if using managed identities](https://azuremlexampledata.blob.core.windows.net/data/templates/batch-inference/Run-BatchEndpoint-MI.zip) or [the following one if using a service principal](https://azuremlexampledata.blob.core.windows.net/data/templates/batch-inference/Run-BatchEndpoint-SP.zip).

1. A preview of the pipeline will show up in the portal. Click __Use this template__.

1. The pipeline will be created for you with the name __Run-BatchEndpoint__.

1. Configure the parameters of the batch deployment you are using:

  # [Using a Managed Identity](#tab/mi)
  
  :::image type="content" source="./media/how-to-use-batch-adf/pipeline-params-mi.png" alt-text="Screenshot of the pipeline parameters expected for the resulting pipeline.":::
  
  # [Using a Service Principal](#tab/sp)

  :::image type="content" source="./media/how-to-use-batch-adf/pipeline-params.png" alt-text="Screenshot of the pipeline parameters expected for the resulting pipeline.":::
  
  
  > [!WARNING]
  > Ensure that your batch endpoint has a default deployment configured before submitting a job to it. The created pipeline will invoke the endpoint and hence a default deployment needs to be created and configured.

  > [!TIP]
  > For best reusability, use the created pipeline as a template and call it from within other Azure Data Factory pipelines by leveraging the [Execute pipeline activity](../data-factory/control-flow-execute-pipeline-activity.md). In that case, do not configure the parameters in the inner pipeline but pass them as parameters from the outer pipeline as shown in the following image:
  > 
  > :::image type="content" source="./media/how-to-use-batch-adf/pipeline-run.png" alt-text="Screenshot of the pipeline parameters expected for the resulting pipeline when invoked from another pipeline.":::

7. Your pipeline is ready to be used.


## Limitations

When calling Azure Machine Learning batch deployments consider the following limitations:

### Data inputs

* Only Azure Machine Learning data stores or Azure Storage Accounts (Azure Blob Storage, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2) are supported as inputs. If your input data is in another source, use the Azure Data Factory Copy activity before the execution of the batch job to sink the data to a compatible store.
* Batch endpoint jobs don't explore nested folders and hence can't work with nested folder structures. If your data is distributed in multiple folders, notice that you will have to flatten the structure.
* Make sure that your scoring script provided in the deployment can handle the data as it is expected to be fed into the job. If the model is MLflow, read the limitation in terms of the file type supported by the moment at [Using MLflow models in batch deployments](how-to-mlflow-batch.md).


### Data outputs
   
* Only registered Azure Machine Learning data stores are supported by the moment. We recommend you to register the storage account your Azure Data Factory is using as a Data Store in Azure Machine Learning. In that way, you will be able to write back to the same storage account from where you are reading.
* Only Azure Blob Storage Accounts are supported for outputs. For instance, Azure Data Lake Storage Gen2 isn't supported as output in batch deployment jobs. If you need to output the data to a different location/sink, use the Azure Data Factory Copy activity after the execution of the batch job.   

## Next steps

* [Use low priority VMs in batch deployments](how-to-use-low-priority-batch.md)
* [Authorization on batch endpoints](how-to-authenticate-batch-endpoint.md)
* [Network isolation in batch endpoints](how-to-secure-batch-endpoint.md)
