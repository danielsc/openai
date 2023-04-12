
# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
# parallel task to process file data
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
    max_concurrency_per_instance=1,
    mini_batch_size="1",
    mini_batch_error_threshold=1,
    retry_settings=dict(max_retries=2, timeout=60),
    logging_level="DEBUG",
    task=RunFunction(
        code="./src",
        entry_script="file_batch_inference.py",
        program_arguments="--job_output_path ${{outputs.job_output_path}}",
        environment="azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu:1",
    ),
)
```

> [!IMPORTANT]
> Run(mini_batch) function requires a return of either a dataframe, list, or tuple item. Parallel job will use the count of that return to measure the success items under that mini-batch. Ideally mini-batch count should be equal to the return list count if all items have well processed in this mini-batch.

> [!IMPORTANT]
> If you want to parse arguments in Init() or Run(mini_batch) function, use "parse_known_args" instead of "parse_args" for avoiding exceptions. See the [iris_score](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/parallel-run/Code/iris_score.py) example for entry script with argument parser.

### Consider automation settings

Azure ML parallel job exposes numerous settings to automatically control the job without manual intervention. See the following table for the details.

| Key | Type | Description | Allowed values | Default value | Set in attribute | Set in program arguments |
|--|--|--|--|--|--|--|
| mini batch error threshold | integer | Define the number of failed **mini batches** that could be ignored in this parallel job. If the count of failed mini-batch is higher than this threshold, the parallel job will be marked as failed.<br><br>Mini-batch is marked as failed if:<br>- the count of return from run() is less than mini-batch input count.<br>- catch exceptions in custom run() code.<br><br>"-1" is the default number, which means to ignore all failed mini-batch during parallel job. | [-1, int.max] | -1 | mini_batch_error_threshold | N/A |
| mini batch max retries | integer | Define the number of retries when mini-batch is failed or timeout. If all retries are failed, the mini-batch will be marked as failed to be counted by `mini_batch_error_threshold` calculation. | [0, int.max] | 2 | retry_settings.max_retries | N/A |
| mini batch timeout | integer | Define the timeout in seconds for executing custom run() function. If the execution time is higher than this threshold, the mini-batch will be aborted, and marked as a failed mini-batch to trigger retry. | (0, 259200] | 60 | retry_settings.timeout | N/A |
| item error threshold | integer | The threshold of failed **items**. Failed items are counted by the number gap between inputs and returns from each mini-batch. If the sum of failed items is higher than this threshold, the parallel job will be marked as failed.<br><br>Note: "-1" is the default number, which means to ignore all failures during parallel job. | [-1, int.max] | -1 | N/A | --error_threshold |
| allowed failed percent | integer | Similar to `mini_batch_error_threshold` but uses the percent of failed mini-batches instead of the count. | [0, 100] | 100 | N/A | --allowed_failed_percent |
| overhead timeout | integer | The timeout in second for initialization of each mini-batch. For example, load mini-batch data and pass it to run() function. | (0, 259200] | 600 | N/A | --task_overhead_timeout |
