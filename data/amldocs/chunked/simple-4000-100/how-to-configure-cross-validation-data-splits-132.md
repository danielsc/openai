## Monte Carlo cross-validation

To perform Monte Carlo cross validation, include both the `validation_size` and `n_cross_validations` parameters in your `AutoMLConfig` object. 

For Monte Carlo cross validation, automated ML sets aside the portion of the training data specified by the `validation_size` parameter for validation, and then assigns the rest of the data for training. This process is then repeated based on the value specified in the `n_cross_validations` parameter; which generates new training and validation splits, at random, each time.

> [!NOTE]
> The Monte Carlo cross-validation is not supported in forecasting scenarios.

The follow code defines, 7 folds for cross-validation and 20% of the training data should be used for validation. Hence, 7 different trainings, each training uses 80% of the data, and each validation uses 20% of the data with a different holdout fold each time.

```python
data = "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/creditcard.csv"

dataset = Dataset.Tabular.from_delimited_files(data)

automl_config = AutoMLConfig(compute_target = aml_remote_compute,
                             task = 'classification',
                             primary_metric = 'AUC_weighted',
                             training_data = dataset,
                             n_cross_validations = 7
                             validation_size = 0.2,
                             label_column_name = 'Class'
                            )
```

## Specify custom cross-validation data folds

You can also provide your own cross-validation (CV) data folds. This is considered a more advanced scenario because you are specifying which columns to split and use for validation.  Include custom CV split columns in your training data, and specify which columns by populating the column names in the `cv_split_column_names` parameter. Each column represents one cross-validation split, and is filled with integer values 1 or 0--where 1 indicates the row should be used for training and 0 indicates the row should be used for validation.

> [!NOTE]
> The `cv_split_column_names` parameter is not supported in forecasting scenarios. 


The following code snippet contains bank marketing data with two CV split columns 'cv1' and 'cv2'.

```python
data = "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_with_cv.csv"

dataset = Dataset.Tabular.from_delimited_files(data)

automl_config = AutoMLConfig(compute_target = aml_remote_compute,
                             task = 'classification',
                             primary_metric = 'AUC_weighted',
                             training_data = dataset,
                             label_column_name = 'y',
                             cv_split_column_names = ['cv1', 'cv2']
                            )
```

> [!NOTE]
> To use `cv_split_column_names` with `training_data` and `label_column_name`, please upgrade your Azure Machine Learning Python SDK version 1.6.0 or later. For previous SDK versions, please refer to using `cv_splits_indices`, but note that it is used with `X` and `y` dataset input only. 


## Metric calculation for cross validation in machine learning

When either k-fold or Monte Carlo cross validation is used, metrics are computed on each validation fold and then aggregated. The aggregation operation is an average for scalar metrics and a sum for charts. Metrics computed during cross validation are based on all folds and therefore all samples from the training set. [Learn more about metrics in automated machine learning](how-to-understand-automated-ml.md).

When either a custom validation set or an automatically selected validation set is used, model evaluation metrics are computed from only that validation set, not the  training data.

## Provide test data (preview)

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

You can also provide test data to evaluate the recommended model that automated ML generates for you upon completion of the experiment. When you provide test data it's considered a separate from training and validation, so as to not bias the results of the test run of the recommended model. [Learn more about training, validation and test data in automated ML.](concept-automated-ml.md#training-validation-and-test-data)
