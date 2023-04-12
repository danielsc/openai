You can also provide test data to evaluate the recommended model that automated ML generates for you upon completion of the experiment. When you provide test data it's considered a separate from training and validation, so as to not bias the results of the test run of the recommended model. [Learn more about training, validation and test data in automated ML.](concept-automated-ml.md#training-validation-and-test-data)

> [!WARNING]
> This feature is not available for the following automated ML scenarios
>  * [Computer vision tasks](how-to-auto-train-image-models.md)
>  * [Many models and hiearchical time series forecasting training (preview)](how-to-auto-train-forecast.md)
>  * [Forecasting tasks where deep learning neural networks (DNN) are enabled](how-to-auto-train-forecast.md#enable-deep-learning)
>  * [Automated ML runs from local computes or Azure Databricks clusters](how-to-configure-auto-train.md#compute-to-run-experiment)

Test datasets must be in the form of an [Azure Machine Learning TabularDataset](./v1/how-to-create-register-datasets.md#tabulardataset). You can specify a test dataset with the `test_data` and `test_size` parameters in your `AutoMLConfig` object.  These parameters are mutually exclusive and can not be specified at the same time or with `cv_split_column_names` or `cv_splits_indices`.

With the `test_data` parameter, specify an existing dataset to pass into your `AutoMLConfig` object. 

```python
automl_config = AutoMLConfig(task='forecasting',
                             ...
                             # Provide an existing test dataset
                             test_data=test_dataset,
                             ...
                             forecasting_parameters=forecasting_parameters)
```

To use a train/test split instead of providing test data directly, use the `test_size` parameter when creating the `AutoMLConfig`. This parameter must be a floating point value between 0.0 and 1.0 exclusive, and specifies the percentage of the training dataset that should be used for the test dataset.

```python
automl_config = AutoMLConfig(task = 'regression',
                             ...
                             # Specify train/test split
                             training_data=training_data,
                             test_size=0.2)
```

> [!Note]
> For regression tasks, random sampling is used.<br>
> For classification tasks, stratified sampling is used, but random sampling is used as a fall back when stratified sampling is not feasible. <br>
> Forecasting does not currently support specifying a test dataset using a train/test split with the `test_size` parameter.


Passing the `test_data` or `test_size` parameters into the `AutoMLConfig`, automatically triggers a remote test run upon completion of your experiment. This test run uses the provided test data to evaluate the best model that automated ML recommends. Learn more about [how to get the predictions from the test run](./v1/how-to-configure-auto-train-v1.md#test-models-preview).

## Next steps

* [Prevent imbalanced data and overfitting](concept-manage-ml-pitfalls.md).

* How to [Auto-train a time-series forecast model](how-to-auto-train-forecast.md).
