    :::image type="content" source="media/how-to-tune-hyperparameters/hyperparameter-tuning-3-dimensional-scatter.png" alt-text="Hyparameter tuning 3-dimensional scatter chart":::


## Find the best trial job

Once all of the hyperparameter tuning jobs have completed, retrieve your best trial outputs:

```Python
# Download best trial model output
ml_client.jobs.download(returned_sweep_job.name, output_name="model")
```

You can use the CLI to download all default and named outputs of the best trial job and logs of the sweep job.
```
az ml job download --name <sweep-job> --all
```

Optionally, to solely download the best trial output
```
az ml job download --name <sweep-job> --output-name model
```   
    
## References

- [Hyperparameter tuning example](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/lightgbm/iris/src/main.py)
- [CLI (v2) sweep job YAML schema here](reference-yaml-job-sweep.md#parameter-expressions)

## Next steps
* [Track an experiment](how-to-log-view-metrics.md)
* [Deploy a trained model](how-to-deploy-online-endpoints.md)
