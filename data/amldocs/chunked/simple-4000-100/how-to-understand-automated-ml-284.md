The mAP, precision and recall values are logged at an epoch-level for image object detection/instance segmentation models. The mAP, precision and recall metrics are also logged at a class level with the name 'per_label_metrics'. The 'per_label_metrics' should be viewed as a table. 

> [!NOTE]
> Epoch-level metrics for precision, recall and per_label_metrics are not available when using the 'coco' method.

![Epoch-level charts for object detection](./media/how-to-understand-automated-ml/image-object-detection-map.png)

## Model explanations and feature importances

While model evaluation metrics and charts are good for measuring the general quality of a model, inspecting which dataset features a model used to make its predictions is essential when practicing responsible AI. That's why automated ML provides a model explanations dashboard to measure and report the relative contributions of dataset features. See how to [view the explanations dashboard in the Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md#model-explanations-preview).

For a code first experience, see how to set up [model explanations for automated ML experiments with the Azure Machine Learning Python SDK](how-to-machine-learning-interpretability-automl.md).

> [!NOTE]
> Interpretability, best model explanation, is not available for automated ML forecasting experiments that recommend the following algorithms as the best model or ensemble: 
> * TCNForecaster
> * AutoArima
> * ExponentialSmoothing
> * Prophet
> * Average 
> * Naive
> * Seasonal Average 
> * Seasonal Naive

## Next steps
* Try the [automated machine learning model explanation sample notebooks](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/explain-model).
* For automated ML specific questions, reach out to askautomatedml@microsoft.com.
