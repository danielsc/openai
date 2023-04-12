In most applications, customers have a need to understand their forecasts at a macro and micro level of the business; whether that is predicting sales of products at different geographic locations, or understanding the expected workforce demand for different organizations at a company. The ability to train a machine learning model to intelligently forecast on hierarchy data is essential. 

A hierarchical time series is a structure in which the series have nested attributes. Geographic or product catalog attributes are natural examples. The following example shows data with unique attributes that form a hierarchy. Our hierarchy is defined by: the product type such as headphones or tablets, the product category which splits product types into accessories and devices, and the region the products are sold in. 

![Example raw data table for hierarchical data](./media/how-to-auto-train-forecast/hierarchy-data-table.svg)
 
To further visualize this, the leaf levels of the hierarchy contain all the time series with unique combinations of attribute values. Each higher level in the hierarchy considers one less dimension for defining the time series and aggregates each set of child nodes from the lower level into a parent node.
 
![Hierarchy visual for data](./media/how-to-auto-train-forecast/data-tree.svg)

The hierarchical time series solution is built on top of the Many Models Solution and share a similar configuration setup.

The following code demonstrates the key parameters to set up your hierarchical time series forecasting runs. See the [Hierarchical time series- Automated ML notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-hierarchical-timeseries/auto-ml-forecasting-hierarchical-timeseries.ipynb), for an end to end example. 

```python

from azureml.train.automl.runtime._hts.hts_parameters import HTSTrainParameters

model_explainability = True

engineered_explanations = False # Define your hierarchy. Adjust the settings below based on your dataset.
hierarchy = ["state", "store_id", "product_category", "SKU"]
training_level = "SKU"# Set your forecast parameters. Adjust the settings below based on your dataset.
time_column_name = "date"
label_column_name = "quantity"
forecast_horizon = 7


automl_settings = {"task" : "forecasting",
                   "primary_metric" : "normalized_root_mean_squared_error",
                   "label_column_name": label_column_name,
                   "time_column_name": time_column_name,
                   "forecast_horizon": forecast_horizon,
                   "hierarchy_column_names": hierarchy,
                   "hierarchy_training_level": training_level,
                   "track_child_runs": False,
                   "pipeline_fetch_max_batch_size": 15,
                   "model_explainability": model_explainability,# The following settings are specific to this sample and should be adjusted according to your own needs.
                   "iteration_timeout_minutes" : 10,
                   "iterations" : 10,
                   "n_cross_validations" : "auto", # Could be customized as an integer
                   "cv_step_size" : "auto", # Could be customized as an integer
                   }

hts_parameters = HTSTrainParameters(
    automl_settings=automl_settings,
    hierarchy_column_names=hierarchy,
    training_level=training_level,
    enable_engineered_explanations=engineered_explanations
)
```

## Example notebooks

See the [forecasting sample notebooks](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs) for detailed code examples of advanced forecasting configuration including:

* [deep learning models](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-forecasting-github-dau/auto-ml-forecasting-github-dau.ipynb)
* [holiday detection and featurization](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-forecasting-task-bike-share/auto-ml-forecasting-bike-share.ipynb)
