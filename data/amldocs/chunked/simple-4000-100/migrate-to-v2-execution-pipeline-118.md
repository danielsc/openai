
* SDK v2. [Full sample link](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/pipelines/1b_pipeline_with_python_function_components/pipeline_with_python_function_components.ipynb)

    ```python
    # import required libraries
    from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
    
    from azure.ai.ml import MLClient, Input
    from azure.ai.ml.dsl import pipeline
    
    try:
        credential = DefaultAzureCredential()
        # Check if given credential can get token successfully.
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:
        # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
        credential = InteractiveBrowserCredential()
    
    # Get a handle to workspace
    ml_client = MLClient.from_config(credential=credential)
    
    # Retrieve an already attached Azure Machine Learning Compute.
    cluster_name = "cpu-cluster"
    print(ml_client.compute.get(cluster_name))
    
    # Import components that are defined with Python function
    with open("src/components.py") as fin:
        print(fin.read())
    
    # You need to install mldesigner package to use command_component decorator.
    # Option 1: install directly
    # !pip install mldesigner
    
    # Option 2: install as an extra dependency of azure-ai-ml
    # !pip install azure-ai-ml[designer]
    
    # import the components as functions
    from src.components import train_model, score_data, eval_model
    
    cluster_name = "cpu-cluster"
    # define a pipeline with component
    @pipeline(default_compute=cluster_name)
    def pipeline_with_python_function_components(input_data, test_data, learning_rate):
        """E2E dummy train-score-eval pipeline with components defined via Python function components"""
    
        # Call component obj as function: apply given inputs & parameters to create a node in pipeline
        train_with_sample_data = train_model(
            training_data=input_data, max_epochs=5, learning_rate=learning_rate
        )
    
        score_with_sample_data = score_data(
            model_input=train_with_sample_data.outputs.model_output, test_data=test_data
        )
    
        eval_with_sample_data = eval_model(
            scoring_result=score_with_sample_data.outputs.score_output
        )
    
        # Return: pipeline outputs
        return {
            "eval_output": eval_with_sample_data.outputs.eval_output,
            "model_output": train_with_sample_data.outputs.model_output,
        }
    
    
    pipeline_job = pipeline_with_python_function_components(
        input_data=Input(
            path="wasbs://demo@dprepdata.blob.core.windows.net/Titanic.csv", type="uri_file"
        ),
        test_data=Input(
            path="wasbs://demo@dprepdata.blob.core.windows.net/Titanic.csv", type="uri_file"
        ),
        learning_rate=0.1,
    )
    
    # submit job to workspace
    pipeline_job = ml_client.jobs.create_or_update(
        pipeline_job, experiment_name="train_score_eval_pipeline"
    )
    ```

## Mapping of key functionality in SDK v1 and SDK v2

|Functionality in SDK v1|Rough mapping in SDK v2|
|-|-|
|[azureml.pipeline.core.Pipeline](/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline?view=azure-ml-py&preserve-view=true)|[azure.ai.ml.dsl.pipeline](/python/api/azure-ai-ml/azure.ai.ml.dsl#azure-ai-ml-dsl-pipeline)|
|[OutputDatasetConfig](/python/api/azureml-core/azureml.data.output_dataset_config.outputdatasetconfig?view=azure-ml-py&preserve-view=true)|[Output](/python/api/azure-ai-ml/azure.ai.ml.output)|
|[dataset as_mount](/python/api/azureml-core/azureml.data.filedataset?view=azure-ml-py#azureml-data-filedataset-as-mount&preserve-view=true)|[Input](/python/api/azure-ai-ml/azure.ai.ml.input)|

## Step and job/component type mapping

|step in SDK v1| job type in SDK v2| component type in SDK v2|
|--------------|-------------------|-------------------------|
