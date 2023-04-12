If your AutoML forecasting job fails, you'll see an error message in the studio UI that may help to diagnose and fix the problem. The best source of information about the failure beyond the error message is the driver log for the job. Check out the [run logs](how-to-log-view-metrics.md#view-and-download-diagnostic-logs) guide for instructions on finding driver logs.

> [!NOTE]
> For Many Models or HTS job, training is usually on multi-node compute clusters. Logs for these jobs are present for each node IP address. You will need to search for error logs in each node in this case. The error logs, along with the driver logs, are in the `user_logs` folder for each node IP. 

## What is a workspace / environment / experiment/ compute instance / compute target? 

If you aren't familiar with Azure Machine Learning concepts, start with the ["What is AzureML"](overview-what-is-azure-machine-learning.md) article and the [workspaces](./concept-workspace.md) article.

## Next steps
* Learn more about [how to set up AutoML to train a time-series forecasting model](./how-to-auto-train-forecast.md).
* Learn about [calendar features for time series forecasting in AutoML](./concept-automl-forecasting-calendar-features.md).
* Learn about [how AutoML uses machine learning to build forecasting models](./concept-automl-forecasting-methods.md).
* Learn about [AutoML Forecasting Lagged Features](./concept-automl-forecasting-lags.md).
