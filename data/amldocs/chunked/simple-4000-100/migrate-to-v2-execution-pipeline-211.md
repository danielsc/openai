|step in SDK v1| job type in SDK v2| component type in SDK v2|
|--------------|-------------------|-------------------------|
|`adla_step`|None|None|
|`automl_step`|`automl` job|`automl` component|
|`azurebatch_step`| None| None|
|`command_step`| `command` job|`command` component|
|`data_transfer_step`| coming soon | coming soon|
|`databricks_step`| coming soon|coming soon|
|`estimator_step`| command job|`command` component|
|`hyper_drive_step`|`sweep` job| `sweep` component|
|`kusto_step`| None|None|
|`module_step`|None|command component|
|`mpi_step`| command job|command component|
|`parallel_run_step`|`Parallel` job| `Parallel` component|
|`python_script_step`| `command` job|command component|
|`r_script_step`| `command` job|`command` component|
|`synapse_spark_step`| coming soon|coming soon|

## Related documents

For more information, see the documentation here:

* [steps in SDK v1](/python/api/azureml-pipeline-steps/azureml.pipeline.steps?view=azure-ml-py&preserve-view=true)
* [Create and run machine learning pipelines using components with the Azure Machine Learning SDK v2](how-to-create-component-pipeline-python.md)
* [Build a simple ML pipeline for image classification (SDK v1)](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/using-pipelines/image-classification.ipynb)
* [OutputDatasetConfig](/python/api/azureml-core/azureml.data.output_dataset_config.outputdatasetconfig?view=azure-ml-py&preserve-view=true)
* [`mldesigner`](https://pypi.org/project/mldesigner/)
