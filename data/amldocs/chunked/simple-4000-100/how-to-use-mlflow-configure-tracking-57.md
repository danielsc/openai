> When submitting jobs using Azure ML CLI v2, you can set the experiment name using the property `experiment_name` in the YAML definition of the job. You don't have to configure it on your training script. See [YAML: display name, experiment name, description, and tags](reference-yaml-job-command.md#yaml-display-name-experiment-name-description-and-tags) for details.


# [MLflow SDK](#tab/mlflow)

To configure the experiment you want to work on use MLflow command [`mlflow.set_experiment()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_experiment).
    
```Python
experiment_name = 'experiment_with_mlflow'
mlflow.set_experiment(experiment_name)
```

# [Using environment variables](#tab/environ)

You can also set one of the MLflow environment variables [MLFLOW_EXPERIMENT_NAME or MLFLOW_EXPERIMENT_ID](https://mlflow.org/docs/latest/cli.html#cmdoption-mlflow-run-arg-uri) with the experiment name. 

```bash
export MLFLOW_EXPERIMENT_NAME="experiment_with_mlflow"
```


## Next steps

Now that your environment is connected to your workspace in Azure Machine Learning, you can start to work with it.

- [Track ML experiments and models with MLflow](how-to-use-mlflow-cli-runs.md)
- [Manage models registries in Azure Machine Learning with MLflow]()
- [Train with MLflow Projects (Preview)](how-to-train-mlflow-projects.md)
- [Guidelines for deploying MLflow models](how-to-deploy-mlflow-models.md)
