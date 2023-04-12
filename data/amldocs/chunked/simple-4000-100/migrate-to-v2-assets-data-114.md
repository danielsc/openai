    
    ```python
    from azure.ai.ml.entities import Data
    from azure.ai.ml.constants import AssetTypes
    
    # my_path must point to folder containing MLTable artifact (MLTable file + data
    # Supported paths include:
    # local: './<path>'
    # blob:  'https://<account_name>.blob.core.windows.net/<container_name>/<path>'
    # ADLS gen2: 'abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/'
    # Datastore: 'azureml://datastores/<data_store_name>/paths/<path>'
    
    my_path = '<path>'
    
    my_data = Data(
        path=my_path,
        type=AssetTypes.MLTABLE,
        description="<description>",
        name="<name>",
        version='<version>'
    )
    
    ml_client.data.create_or_update(my_data)
    ```

## Use data in an experiment/job

* SDK v1

    ```python
    from azureml.core import ScriptRunConfig
    
    src = ScriptRunConfig(source_directory=script_folder,
                          script='train_titanic.py',
                          # pass dataset as an input with friendly name 'titanic'
                          arguments=['--input-data', titanic_ds.as_named_input('titanic')],
                          compute_target=compute_target,
                          environment=myenv)
                                 
    # Submit the run configuration for your training run
    run = experiment.submit(src)
    run.wait_for_completion(show_output=True)
    ```

* SDK v2

    ```python
    from azure.ai.ml import command
    from azure.ai.ml.entities import Data
    from azure.ai.ml import Input, Output
    from azure.ai.ml.constants import AssetTypes
    
    # Possible Asset Types for Data:
    # AssetTypes.URI_FILE
    # AssetTypes.URI_FOLDER
    # AssetTypes.MLTABLE
    
    # Possible Paths for Data:
    # Blob: https://<account_name>.blob.core.windows.net/<container_name>/<folder>/<file>
    # Datastore: azureml://datastores/paths/<folder>/<file>
    # Data Asset: azureml:<my_data>:<version>
    
    my_job_inputs = {
        "raw_data": Input(type=AssetTypes.URI_FOLDER, path="<path>")
    }
    
    my_job_outputs = {
        "prep_data": Output(type=AssetTypes.URI_FOLDER, path="<path>")
    }
    
    job = command(
        code="./src",  # local path where the code is stored
        command="python process_data.py --raw_data ${{inputs.raw_data}} --prep_data ${{outputs.prep_data}}",
        inputs=my_job_inputs,
        outputs=my_job_outputs,
        environment="<environment_name>:<version>",
        compute="cpu-cluster",
    )
    
    # submit the command
    returned_job = ml_client.create_or_update(job)
    # get a URL for the status of the job
    returned_job.services["Studio"].endpoint
    ```

## Mapping of key functionality in SDK v1 and SDK v2

|Functionality in SDK v1|Rough mapping in SDK v2|
|-|-|
|[Method/API in SDK v1](/python/api/azureml-core/azureml.data)|[Method/API in SDK v2](/python/api/azure-ai-ml/azure.ai.ml.entities)|

## Next steps

For more information, see the documentation here:
* [Data in Azure Machine Learning](concept-data.md?tabs=uri-file-example%2Ccli-data-create-example)
* [Create data_assets](how-to-create-data-assets.md?tabs=CLI)
* [Read and write data in a job](how-to-read-write-data-v2.md)
* [V2 datastore operations](/python/api/azure-ai-ml/azure.ai.ml.operations.datastoreoperations)
