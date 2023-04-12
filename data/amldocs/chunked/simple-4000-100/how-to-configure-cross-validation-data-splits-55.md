|**Smaller&nbsp;than&nbsp;20,000&nbsp;rows**| Cross-validation approach is applied. The default number of folds depends on the number of rows. <br> **If the dataset is less than 1,000 rows**, 10 folds are used. <br> **If the rows are between 1,000 and 20,000**, then three folds are used.


## Provide validation data

In this case, you can either start with a single data file and split it into training data and validation data sets or you can provide a separate data file for the validation set. Either way, the `validation_data` parameter in your `AutoMLConfig` object assigns which data to use as your validation set. This parameter only accepts data sets in the form of an [Azure Machine Learning dataset](./v1/how-to-create-register-datasets.md) or pandas dataframe.   

> [!NOTE]
> The `validation_data` parameter requires the `training_data` and `label_column_name` parameters to be set as well. You can only set one validation parameter, that is you can only specify either `validation_data` or `n_cross_validations`, not both.

The following code example explicitly defines which portion of the provided data in `dataset` to use for training and validation.

```python
data = "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/creditcard.csv"

dataset = Dataset.Tabular.from_delimited_files(data)

training_data, validation_data = dataset.random_split(percentage=0.8, seed=1)

automl_config = AutoMLConfig(compute_target = aml_remote_compute,
                             task = 'classification',
                             primary_metric = 'AUC_weighted',
                             training_data = training_data,
                             validation_data = validation_data,
                             label_column_name = 'Class'
                            )
```

## Provide validation set size

In this case, only a single dataset is provided for the experiment. That is, the `validation_data` parameter is **not** specified, and the provided dataset is assigned to the  `training_data` parameter.  

In your `AutoMLConfig` object, you can set the `validation_size` parameter to hold out a portion of the training data for validation. This means that the validation set will be split by automated ML from the initial `training_data` provided. This value should be between 0.0 and 1.0 non-inclusive (for example, 0.2 means 20% of the data is held out for validation data).

> [!NOTE]
> The `validation_size` parameter is not supported in forecasting scenarios. 

See the following code example:

```python
data = "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/creditcard.csv"

dataset = Dataset.Tabular.from_delimited_files(data)

automl_config = AutoMLConfig(compute_target = aml_remote_compute,
                             task = 'classification',
                             primary_metric = 'AUC_weighted',
                             training_data = dataset,
                             validation_size = 0.2,
                             label_column_name = 'Class'
                            )
```

## K-fold cross-validation

To perform k-fold cross-validation, include the `n_cross_validations` parameter and set it to a value. This parameter sets how many cross validations to perform, based on the same number of folds.

> [!NOTE]
> The `n_cross_validations` parameter is not supported in classification scenarios that use deep neural networks.
> For forecasting scenarios, see how cross validation is applied in [Set up AutoML to train a time-series forecasting model](how-to-auto-train-forecast.md#training-and-validation-data).
 
In the following code, five folds for cross-validation are defined. Hence, five different trainings, each training using 4/5 of the data, and each validation using 1/5 of the data with a different holdout fold each time.

As a result, metrics are calculated with the average of the five validation metrics.

```python
data = "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/creditcard.csv"

dataset = Dataset.Tabular.from_delimited_files(data)

automl_config = AutoMLConfig(compute_target = aml_remote_compute,
                             task = 'classification',
                             primary_metric = 'AUC_weighted',
                             training_data = dataset,
                             n_cross_validations = 5
                             label_column_name = 'Class'
                            )
```
