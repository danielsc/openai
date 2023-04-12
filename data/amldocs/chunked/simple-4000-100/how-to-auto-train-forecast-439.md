Repeat the necessary steps to load this future data to a data frame and then run `best_run.forecast_quantiles(test_dataset)` to predict future values.

> [!NOTE]
> In-sample predictions are not supported for forecasting with automated ML when `target_lags` and/or `target_rolling_window_size` are enabled.

## Forecasting at scale

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

> [!IMPORTANT]
> Many models and hierarchical time series are currently only supported in AzureML v1. Support for AzureML v2 is forthcoming.

There are scenarios where a single machine learning model is insufficient and multiple machine learning models are needed. For instance, predicting sales for each individual store for a brand, or tailoring an experience to individual users. Building a model for each instance can lead to improved results on many machine learning problems. 

Grouping is a concept in time series forecasting that allows time series to be combined to train an individual model per group. This approach can be particularly helpful if you have time series that require smoothing, filling or entities in the group that can benefit from history or trends from other entities. Many models and hierarchical time series forecasting are solutions powered by automated machine learning for these large scale forecasting scenarios. 

### Many models

The Azure Machine Learning many models solution with automated machine learning allows users to train and manage millions of models in parallel. The Many Models Solution Accelerator uses [Azure Machine Learning pipelines](concept-ml-pipelines.md) to train the model. Specifically, a [Pipeline](/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline%28class%29) object and [ParalleRunStep](/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallelrunstep) are used and require specific configuration parameters set through the [ParallelRunConfig](/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallelrunconfig). 


The following diagram shows the workflow for the many models solution. 

![Many models concept diagram](./media/how-to-auto-train-forecast/many-models.svg)

The following code demonstrates the key parameters users need to set up their many models run. See the [Many Models- Automated ML notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-many-models/auto-ml-forecasting-many-models.ipynb) for a many models forecasting example 

```python
from azureml.train.automl.runtime._many_models.many_models_parameters import ManyModelsTrainParameters

partition_column_names = ['Store', 'Brand']
automl_settings = {"task" : 'forecasting',
                   "primary_metric" : 'normalized_root_mean_squared_error',
                   "iteration_timeout_minutes" : 10, #This needs to be changed based on the dataset. Explore how long training is taking before setting this value 
                   "iterations" : 15,
                   "experiment_timeout_hours" : 1,
                   "label_column_name" : 'Quantity',
                   "n_cross_validations" : "auto", # Could be customized as an integer
                   "cv_step_size" : "auto", # Could be customized as an integer
                   "time_column_name": 'WeekStarting',
                   "max_horizon" : 6,
                   "track_child_runs": False,
                   "pipeline_fetch_max_batch_size": 15,}

mm_paramters = ManyModelsTrainParameters(automl_settings=automl_settings, partition_column_names=partition_column_names)

```

### Hierarchical time series forecasting

In most applications, customers have a need to understand their forecasts at a macro and micro level of the business; whether that is predicting sales of products at different geographic locations, or understanding the expected workforce demand for different organizations at a company. The ability to train a machine learning model to intelligently forecast on hierarchy data is essential. 
