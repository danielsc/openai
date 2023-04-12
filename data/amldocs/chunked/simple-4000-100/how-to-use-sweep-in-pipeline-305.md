
### Python SDK

The Python SDK example can be found in [azureml-example repo](https://github.com/Azure/azureml-examples). Navigate to *azureml-examples/sdk/jobs/pipelines/1c_pipeline_with_hyperparameter_sweep* to check the example.

In Azure Machine Learning Python SDK v2, you can enable hyperparameter tuning for any command component by calling `.sweep()` method.

Below code snippet shows how to enable sweep for `train_model`.

```python
train_component_func = load_component(source="./train.yml")
score_component_func = load_component(source="./predict.yml")

# define a pipeline
@pipeline()
def pipeline_with_hyperparameter_sweep():
    """Tune hyperparameters using sample components."""
    train_model = train_component_func(
        data=Input(
            type="uri_file",
            path="wasbs://datasets@azuremlexamples.blob.core.windows.net/iris.csv",
        ),
        c_value=Uniform(min_value=0.5, max_value=0.9),
        kernel=Choice(["rbf", "linear", "poly"]),
        coef0=Uniform(min_value=0.1, max_value=1),
        degree=3,
        gamma="scale",
        shrinking=False,
        probability=False,
        tol=0.001,
        cache_size=1024,
        verbose=False,
        max_iter=-1,
        decision_function_shape="ovr",
        break_ties=False,
        random_state=42,
    )
    sweep_step = train_model.sweep(
        primary_metric="training_f1_score",
        goal="minimize",
        sampling_algorithm="random",
        compute="cpu-cluster",
    )
    sweep_step.set_limits(max_total_trials=20, max_concurrent_trials=10, timeout=7200)

    score_data = score_component_func(
        model=sweep_step.outputs.model_output, test_data=sweep_step.outputs.test_data
    )


pipeline_job = pipeline_with_hyperparameter_sweep()

# set pipeline level compute
pipeline_job.settings.default_compute = "cpu-cluster"
```

 We first load `train_component_func` defined in `train.yml` file. When creating `train_model`, we add `c_value`, `kernel` and `coef0` into search space(line 15-17). Line 30-35 defines the primary metric, sampling algorithm etc.

## Check pipeline job with sweep step in Studio

After you submit a pipeline job, the SDK or CLI widget will give you a web URL link to Studio UI. The link will guide you to the pipeline graph view by default.

To check details of the sweep step, double click the sweep step and navigate to the **child job** tab in the panel on the right.

:::image type="content" source="./media/how-to-use-sweep-in-pipeline/pipeline-view.png" alt-text="Screenshot of the pipeline with child job and the train_model node highlighted." lightbox= "./media/how-to-use-sweep-in-pipeline/pipeline-view.png":::

This will link you to the sweep job page as seen in the below screenshot. Navigate to **child job** tab, here you can see the metrics of all child jobs and list of all child jobs.

:::image type="content" source="./media/how-to-use-sweep-in-pipeline/sweep-job.png" alt-text="Screenshot of the job page on the child jobs tab." lightbox= "./media/how-to-use-sweep-in-pipeline/sweep-job.png":::

If a child jobs failed, select the name of that child job to enter detail page of that specific child job (see screenshot below). The useful debug information is under **Outputs + Logs**.

:::image type="content" source="./media/how-to-use-sweep-in-pipeline/child-run.png" alt-text="Screenshot of the output + logs tab of a child run." lightbox= "./media/how-to-use-sweep-in-pipeline/child-run.png":::

## Sample notebooks

- [Build pipeline with sweep node](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/pipelines/1c_pipeline_with_hyperparameter_sweep/pipeline_with_hyperparameter_sweep.ipynb)
- [Run hyperparameter sweep on a command job](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/lightgbm/iris/lightgbm-iris-sweep.ipynb)

## Next steps

- [Track an experiment](how-to-log-view-metrics.md)
- [Deploy a trained model](how-to-deploy-online-endpoints.md)
