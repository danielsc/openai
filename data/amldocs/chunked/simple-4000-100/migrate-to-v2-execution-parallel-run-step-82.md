
## Use parallel step in pipeline

* SDK v1

    ```python
    # Run pipeline with parallel run step
    from azureml.core import Experiment
    
    pipeline = Pipeline(workspace=ws, steps=[parallelrun_step])
    experiment = Experiment(ws, 'digit_identification')
    pipeline_run = experiment.submit(pipeline)
    pipeline_run.wait_for_completion(show_output=True)
    ```

* SDK v2

    ```python
    @pipeline()
    def parallel_in_pipeline(pipeline_job_data_path, pipeline_score_model):
    
        prepare_file_tabular_data = prepare_data(input_data=pipeline_job_data_path)
        # output of file & tabular data should be type MLTable
        prepare_file_tabular_data.outputs.file_output_data.type = AssetTypes.MLTABLE
        prepare_file_tabular_data.outputs.tabular_output_data.type = AssetTypes.MLTABLE
    
        batch_inference_with_file_data = file_batch_inference(
            job_data_path=prepare_file_tabular_data.outputs.file_output_data
        )
        # use eval_mount mode to handle file data
        batch_inference_with_file_data.inputs.job_data_path.mode = (
            InputOutputModes.EVAL_MOUNT
        )
        batch_inference_with_file_data.outputs.job_output_path.type = AssetTypes.MLTABLE
    
        batch_inference_with_tabular_data = tabular_batch_inference(
            job_data_path=prepare_file_tabular_data.outputs.tabular_output_data,
            score_model=pipeline_score_model,
        )
        # use direct mode to handle tabular data
        batch_inference_with_tabular_data.inputs.job_data_path.mode = (
            InputOutputModes.DIRECT
        )
    
        return {
            "pipeline_job_out_file": batch_inference_with_file_data.outputs.job_output_path,
            "pipeline_job_out_tabular": batch_inference_with_tabular_data.outputs.job_output_path,
        }
    
    pipeline_job_data_path = Input(
        path="./dataset/", type=AssetTypes.MLTABLE, mode=InputOutputModes.RO_MOUNT
    )
    pipeline_score_model = Input(
        path="./model/", type=AssetTypes.URI_FOLDER, mode=InputOutputModes.DOWNLOAD
    )
    # create a pipeline
    pipeline_job = parallel_in_pipeline(
        pipeline_job_data_path=pipeline_job_data_path,
        pipeline_score_model=pipeline_score_model,
    )
    pipeline_job.outputs.pipeline_job_out_tabular.type = AssetTypes.URI_FILE
    
    # set pipeline level compute
    pipeline_job.settings.default_compute = "cpu-cluster"
    
    # run pipeline job
    pipeline_job = ml_client.jobs.create_or_update(
        pipeline_job, experiment_name="pipeline_samples"
    )
    ```
    
## Mapping of key functionality in SDK v1 and SDK v2

|Functionality in SDK v1|Rough mapping in SDK v2|
|-|-|
|[azureml.pipeline.steps.parallelrunconfig](/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallelrunconfig)<br>[azureml.pipeline.steps.parallelrunstep](/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallelrunstep)|[azure.ai.ml.parallel](/python/api/azure-ai-ml/azure.ai.ml.parallel)|
|[OutputDatasetConfig](/python/api/azureml-core/azureml.data.output_dataset_config.outputdatasetconfig)|[Output](/python/api/azure-ai-ml/azure.ai.ml.output)|
|[dataset as_mount](/python/api/azureml-core/azureml.data.filedataset#azureml-data-filedataset-as-mount)|[Input](/python/api/azure-ai-ml/azure.ai.ml.input)|

## Parallel job configurations and settings mapping

| SDK v1| SDK v2| Description |
|-------|-------|-------------|
|ParallelRunConfig.environment|parallel_run_function.task.environment|Environment that training job will run in. |
|ParallelRunConfig.entry_script|parallel_run_function.task.entry_script |User script that will be run in parallel on multiple nodes. |
|ParallelRunConfig.error_threshold| parallel_run_function.error_threshold |The number of failed mini batches that could be ignored in this parallel job. If the count of failed mini-batch is higher than this threshold, the parallel job will be marked as failed.<br><br>"-1" is the default number, which means to ignore all failed mini-batch during parallel job.|
