Model performance   | Supported (not forecasting) | Supported (not forecasting)  | Supported | Supported |
Dataset explorer  | Supported (not forecasting)   | Not supported. Since sparse data isn’t uploaded and UI has issues rendering sparse data. | Supported | Not supported. Since sparse data isn’t uploaded and UI has issues rendering sparse data. |
 Aggregate feature importance | Supported | Supported | Supported | Supported |
 Individual feature importance| Supported (not forecasting)   | Not supported. Since sparse data isn’t uploaded and UI has issues rendering sparse data. | Supported | Not supported. Since sparse data isn’t uploaded and UI has issues rendering sparse data. |

* **Forecasting models not supported with model explanations**: Interpretability, best model explanation, isn’t available for AutoML forecasting experiments that recommend the following algorithms as the best model: TCNForecaster, AutoArima, Prophet, ExponentialSmoothing, Average, Naive, Seasonal Average, and Seasonal Naive. AutoML Forecasting regression models support explanations. However, in the explanation dashboard, the "Individual feature importance" tab isn’t supported for forecasting because of complexity in their data pipelines.

* **Local explanation for data index**: The explanation dashboard doesn’t support relating local importance values to a row identifier from the original validation dataset if that dataset is greater than 5000 datapoints as the dashboard randomly downsamples the data. However, the dashboard shows raw dataset feature values for each datapoint passed into the dashboard under the Individual feature importance tab. Users can map local importances back to the original dataset through matching the raw dataset feature values. If the validation dataset size is less than 5000 samples, the `index` feature in AzureML studio will correspond to the index in the validation dataset.

* **What-if/ICE plots not supported in studio**: What-If and Individual Conditional Expectation (ICE) plots aren’t supported in Azure Machine Learning studio under the Explanations tab since the uploaded explanation needs an active compute to recalculate predictions and probabilities of perturbed features. It’s currently supported in Jupyter notebooks when run as a widget using the SDK.

## Next steps

[Techniques for model interpretability in Azure ML](how-to-machine-learning-interpretability.md)

[Check out Azure Machine Learning interpretability sample notebooks](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/explain-model)
