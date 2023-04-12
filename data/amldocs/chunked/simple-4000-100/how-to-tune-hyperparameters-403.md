The `command_job` is called as a function so we can apply the parameter expressions to the sweep inputs. The `sweep` function is then configured with `trial`, `sampling-algorithm`, `objective`, `limits`, and `compute`. The above code snippet is taken from the sample notebook [Run hyperparameter sweep on a Command or CommandComponent](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/lightgbm/iris/lightgbm-iris-sweep.ipynb). In this sample, the `learning_rate` and `boosting` parameters will be tuned. Early stopping of jobs will be determined by a `MedianStoppingPolicy`, which stops a job whose primary metric value is worse than the median of the averages across all training jobs.(see [MedianStoppingPolicy class reference](/python/api/azure-ai-ml/azure.ai.ml.sweep.medianstoppingpolicy)).

To see how the parameter values are received, parsed, and passed to the training script to be tuned, refer to this [code sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/lightgbm/iris/src/main.py)

> [!Important]
> Every hyperparameter sweep job restarts the training from scratch, including rebuilding the model and _all the data loaders_. You can minimize 
> this cost by using an Azure Machine Learning pipeline or manual process to do as much data preparation as possible prior to your training jobs. 

## Submit hyperparameter tuning experiment

After you define your hyperparameter tuning configuration, [submit the job](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-create-or-update):

```Python
# submit the sweep
returned_sweep_job = ml_client.create_or_update(sweep_job)
# get a URL for the status of the job
returned_sweep_job.services["Studio"].endpoint
```

## Visualize hyperparameter tuning jobs

You can visualize all of your hyperparameter tuning jobs in the [Azure Machine Learning studio](https://ml.azure.com). For more information on how to view an experiment in the portal, see [View job records in the studio](how-to-log-view-metrics.md#view-the-experiment-in-the-web-portal).

- **Metrics chart**: This visualization tracks the metrics logged for each hyperdrive child job over the duration of hyperparameter tuning. Each line represents a child job, and each point measures the primary metric value at that iteration of runtime.  

    :::image type="content" source="media/how-to-tune-hyperparameters/hyperparameter-tuning-metrics.png" alt-text="Hyperparameter tuning metrics chart":::

- **Parallel Coordinates Chart**: This visualization shows the correlation between primary metric performance and individual hyperparameter values. The chart is interactive via movement of axes (click and drag by the axis label), and by highlighting values across a single axis (click and drag vertically along a single axis to highlight a range of desired values). The parallel coordinates chart includes an axis on the rightmost portion of the chart that plots the best metric value corresponding to the hyperparameters set for that job instance. This axis is provided in order to project the chart gradient legend onto the data in a more readable fashion.

    :::image type="content" source="media/how-to-tune-hyperparameters/hyperparameter-tuning-parallel-coordinates.png" alt-text="Hyperparameter tuning parallel coordinates chart":::

- **2-Dimensional Scatter Chart**: This visualization shows the correlation between any two individual hyperparameters along with their associated primary metric value.

    :::image type="content" source="media/how-to-tune-hyperparameters/hyperparameter-tuning-2-dimensional-scatter.png" alt-text="Hyparameter tuning 2-dimensional scatter chart":::

- **3-Dimensional Scatter Chart**: This visualization is the same as 2D but allows for three hyperparameter dimensions of correlation with the primary metric value. You can also click and drag to reorient the chart to view different correlations in 3D space.

    :::image type="content" source="media/how-to-tune-hyperparameters/hyperparameter-tuning-3-dimensional-scatter.png" alt-text="Hyparameter tuning 3-dimensional scatter chart":::
