To tune the model's hyperparameters, define the parameter space in which to search during training. You'll do this by replacing some of the parameters (`kernel` and `penalty`) passed to the training job with special inputs from the `azure.ml.sweep` package.

```python
from azure.ai.ml.sweep import Choice

# we will reuse the command_job created before. we call it as a function so that we can apply inputs
# we do not apply the 'iris_csv' input again -- we will just use what was already defined earlier
job_for_sweep = job(
    kernel=Choice(values=["linear", "rbf", "poly", "sigmoid"]),
    penalty=Choice(values=[0.5, 1, 1.5]),
)
```

Then, you'll configure sweep on the command job, using some sweep-specific parameters, such as the primary metric to watch and the sampling algorithm to use.

In the following code we use random sampling to try different configuration sets of hyperparameters in an attempt to maximize our primary metric, `Accuracy`.

```python
sweep_job = job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm="random",
    primary_metric="Accuracy",
    goal="Maximize",
    max_total_trials=12,
    max_concurrent_trials=4,
)
```

Now, you can submit this job as before. This time, you'll be running a sweep job that sweeps over your train job.

```python
returned_sweep_job = ml_client.create_or_update(sweep_job)

# stream the output and wait until the job is finished
ml_client.jobs.stream(returned_sweep_job.name)

# refresh the latest status of the job after streaming
returned_sweep_job = ml_client.jobs.get(name=returned_sweep_job.name)
```

You can monitor the job by using the studio user interface link that is presented during the job run.


## Find and register the best model

Once all the runs complete, you can find the run that produced the model with the highest accuracy.

```python
from azure.ai.ml.entities import Model

if returned_sweep_job.status == "Completed":

    # First let us get the run which gave us the best result
    best_run = returned_sweep_job.properties["best_child_run_id"]

    # lets get the model from this run
    model = Model(
        # the script stores the model as "sklearn-iris-flower-classify-model"
        path="azureml://jobs/{}/outputs/artifacts/paths/sklearn-iris-flower-classify-model/".format(
            best_run
        ),
        name="run-model-example",
        description="Model created from run.",
        type="custom_model",
    )

else:
    print(
        "Sweep job status: {}. Please wait until it completes".format(
            returned_sweep_job.status
        )
    )
```

You can then register this model.

```python
registered_model = ml_client.models.create_or_update(model=model)
```


## Deploy the model

After you've registered your model, you can deploy it the same way as any other registered model in Azure ML. For more information about deployment, see [Deploy and score a machine learning model with managed online endpoint using Python SDK v2](how-to-deploy-managed-online-endpoint-sdk-v2.md).


## Next steps

In this article, you trained and registered a scikit-learn model, and you learned about deployment options. See these other articles to learn more about Azure Machine Learning.

* [Track run metrics during training](how-to-log-view-metrics.md)
* [Tune hyperparameters](how-to-tune-hyperparameters.md)