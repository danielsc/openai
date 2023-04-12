
# Upgrade parallel run step to SDK v2

In SDK v2, "Parallel run step" is consolidated into job concept as `parallel job`. Parallel job keeps the same target to empower users to accelerate their job execution by distributing repeated tasks on powerful multi-nodes compute clusters. On top of parallel run step, v2 parallel job provides extra benefits:

- Flexible interface, which allows user to define multiple custom inputs and outputs for your parallel job. You can connect them with other steps to consume or manage their content in your entry script 
- Simplify input schema, which replaces `Dataset` as input by using v2 `data asset` concept. You can easily use your local files or blob directory URI as the inputs to parallel job.
- More powerful features are under developed in v2 parallel job only. For example, resume the failed/canceled parallel job to continue process the failed or unprocessed mini-batches by reusing the successful result to save duplicate effort.

To upgrade your current sdk v1 parallel run step to v2, you'll need to 

- Use `parallel_run_function` to create parallel job by replacing `ParallelRunConfig` and `ParallelRunStep` in v1.
- Upgrade your v1 pipeline to v2. Then invoke your v2 parallel job as a step in your v2 pipeline. See [how to upgrade pipeline from v1 to v2](migrate-to-v2-execution-pipeline.md) for the details about pipeline upgrade.

> Note: User __entry script__ is compatible between v1 parallel run step and v2 parallel job. So you can keep using the same entry_script.py when you upgrade your parallel run job.

This article gives a comparison of scenario(s) in SDK v1 and SDK v2. In the following examples, we'll build a parallel job to predict input data in a pipelines job. You'll see how to build a parallel job, and how to use it in a pipeline job for both SDK v1 and SDK v2.

## Prerequisites

 - Prepare your SDK v2 environment: [Install the Azure ML SDK v2 for Python](/python/api/overview/azure/ai-ml-readme)
 - Understand the basis of SDK v2 pipeline: [How to create Azure ML pipeline with Python SDK v2](how-to-create-component-pipeline-python.md)


## Create parallel step
* SDK v1

    ```python
    # Create the configuration to wrap the inference script
    from azureml.pipeline.steps import ParallelRunStep, ParallelRunConfig
    
    parallel_run_config = ParallelRunConfig(
        source_directory=scripts_folder,
        entry_script=script_file,
        mini_batch_size=PipelineParameter(name="batch_size_param", default_value="5"),
        error_threshold=10,
        output_action="append_row",
        append_row_file_name="mnist_outputs.txt",
        environment=batch_env,
        compute_target=compute_target,
        process_count_per_node=PipelineParameter(name="process_count_param", default_value=2),
        node_count=2
    )
    
    # Create the Parallel run step
    parallelrun_step = ParallelRunStep(
        name="predict-digits-mnist",
        parallel_run_config=parallel_run_config,
        inputs=[ input_mnist_ds_consumption ],
        output=output_dir,
        allow_reuse=False
    )
    ```

* SDK v2

    ```python
    # parallel job to process file data
    file_batch_inference = parallel_run_function(
        name="file_batch_score",
        display_name="Batch Score with File Dataset",
        description="parallel component for batch score",
        inputs=dict(
            job_data_path=Input(
                type=AssetTypes.MLTABLE,
                description="The data to be split and scored in parallel",
            )
        ),
        outputs=dict(job_output_path=Output(type=AssetTypes.MLTABLE)),
        input_data="${{inputs.job_data_path}}",
        instance_count=2,
        mini_batch_size="1",
        mini_batch_error_threshold=1,
        max_concurrency_per_instance=1,
        task=RunFunction(
            code="./src",
            entry_script="file_batch_inference.py",
            program_arguments="--job_output_path ${{outputs.job_output_path}}",
            environment="azureml:AzureML-sklearn-0.24-ubuntu18.04-py37-cpu:1",
        ),
    )
    ```
