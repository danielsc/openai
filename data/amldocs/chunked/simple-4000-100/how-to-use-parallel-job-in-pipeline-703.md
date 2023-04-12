
Finally use your parallel job as a step in your pipeline and bind its inputs/outputs with other steps:

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
```


## Submit pipeline job and check parallel step in Studio UI

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

You can submit your pipeline job with parallel step by using the CLI command:

```azurecli
az ml job create --file pipeline.yml
```

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

You can submit your pipeline job with parallel step by using `jobs.create_or_update` function of ml_client:

```python
pipeline_job = ml_client.jobs.create_or_update(
    pipeline_job, experiment_name="pipeline_samples"
)
pipeline_job
```


Once you submit your pipeline job, the SDK or CLI widget will give you a web URL link to the Studio UI. The link will guide you to the pipeline graph view by default. Double select the parallel step to open the right panel of your parallel job.

To check the settings of your parallel job, navigate to **Parameters** tab, expand **Run settings**, and check **Parallel** section:

:::image type="content" source="./media/how-to-use-parallel-job-in-pipeline/screenshot-for-parallel-job-settings.png" alt-text="Screenshot of Azure ML studio on the jobs tab showing the parallel job settings." lightbox ="./media/how-to-use-parallel-job-in-pipeline/screenshot-for-parallel-job-settings.png":::

To debug the failure of your parallel job, navigate to **Outputs + Logs** tab, expand **logs** folder from output directories on the left, and check **job_result.txt** to understand why the parallel job is failed. For more detail about logging structure of parallel job, see the **readme.txt** under the same folder.

:::image type="content" source="./media/how-to-use-parallel-job-in-pipeline/screenshot-for-parallel-job-result.png" alt-text="Screenshot of Azure ML studio on the jobs tab showing the parallel job results." lightbox ="./media/how-to-use-parallel-job-in-pipeline/screenshot-for-parallel-job-result.png":::

## Parallel job in pipeline examples

- Azure CLI + YAML:
    - [Iris prediction using parallel](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines/iris-batch-prediction-using-parallel) (tabular input)
