> AutoML doesn't support custom, or user-provided functions for the primary metric. You must choose one of the predefined primary metrics that AutoML supports. 

## How can I improve the accuracy of my model?

- Ensure that you're configuring AutoML the best way for your data. See the [model configuration](#what-modeling-configuration-should-i-use) answer for more information.
- Check out the [forecasting recipes notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-recipes-univariate/auto-ml-forecasting-univariate-recipe-experiment-settings.ipynb) for step-by-step guides on how to build and improve forecast models.  
- Evaluate the model using back-tests over several forecasting cycles. This procedure gives a more robust estimate of forecasting error and gives you a baseline to measure improvements against. See our [back-testing notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-backtest-single-model/auto-ml-forecasting-backtest-single-model.ipynb) for an example.
- If the data is noisy, consider aggregating it to a coarser frequency to increase the signal-to-noise ratio. See the [data aggregation](./how-to-auto-train-forecast.md#frequency--target-data-aggregation) guide for more information.
- Add new features that may help predict the target. Subject matter expertise can help greatly when selecting training data.
- Compare validation and test metric values and determine if the selected model is under-fitting or over-fitting the data. This knowledge can guide you to a better training configuration. For example, you might determine that you need to use more cross-validation folds in response to over-fitting.

## Will AutoML always select the same best model given the same training data and configuration?

[AutoML's model search process](./concept-automl-forecasting-sweeping.md#model-sweeping) is not deterministic, so it does not always select the same model given the same data and configuration.  

## How do I fix an Out-Of-Memory error?

There are two types of memory issues:
- RAM Out-of-Memory 
- Disk Out-of-Memory

First, ensure that you're configuring AutoML in the best way for your data. See the [model configuration](#what-modeling-configuration-should-i-use) answer for more information.

For default AutoML settings, RAM Out-of-Memory may be fixed by using compute nodes with more RAM. A useful rule-of-thumb is that the amount of free RAM should be at least 10 times larger than the raw data size to run AutoML with default settings. 

Disk Out-of-Memory errors may be resolved by deleting the compute cluster and creating a new one.

## What advanced forecasting scenarios are supported by AutoML?

We support the following advanced prediction scenarios:
- Quantile forecasts
- Robust model evaluation via [rolling forecasts](./how-to-auto-train-forecast.md#evaluating-model-accuracy-with-a-rolling-forecast)
- Forecasting beyond the forecast horizon
- Forecasting when there's a gap in time between training and forecasting periods.

See the [advanced forecasting scenarios notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-forecast-function/auto-ml-forecasting-function.ipynb) for examples and details.

## How do I view metrics from forecasting training jobs?

See our [metrics in studio UI](how-to-log-view-metrics.md#view-jobsruns-information-in-the-studio) guide for finding training and validation metric values. You can view metrics for any forecasting model trained in AutoML by navigating to a model from the AutoML job UI in the studio and clicking on the "metrics" tab.

:::image type="content" source="media/how-to-automl-forecasting-faq/metrics_UI.png" alt-text="A view of the metric interface for an AutoML forecasting model.":::

## How do I debug failures with forecasting training jobs?

If your AutoML forecasting job fails, you'll see an error message in the studio UI that may help to diagnose and fix the problem. The best source of information about the failure beyond the error message is the driver log for the job. Check out the [run logs](how-to-log-view-metrics.md#view-and-download-diagnostic-logs) guide for instructions on finding driver logs.
