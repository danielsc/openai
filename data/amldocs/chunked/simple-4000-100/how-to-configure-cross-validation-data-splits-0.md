
# Configure training, validation, cross-validation and test data in automated machine learning

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

In this article, you learn the different options for configuring training data and validation data splits along with cross-validation settings for your automated machine learning, automated ML, experiments.

In Azure Machine Learning, when you use automated ML to build multiple ML models, each child run needs to validate the related model by calculating the quality metrics for that model, such as accuracy or AUC weighted. These metrics are calculated by comparing the predictions made with each model with real labels from past observations in the validation data. [Learn more about how metrics are calculated based on validation type](#metric-calculation-for-cross-validation-in-machine-learning). 

Automated ML experiments perform model validation automatically. The following sections describe how you can further customize validation settings with the [Azure Machine Learning Python SDK](/python/api/overview/azure/ml/). 

For a low-code or no-code experience, see [Create your automated machine learning experiments in Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md#create-and-run-experiment). 

## Prerequisites

For this article you need,

* An Azure Machine Learning workspace. To create the workspace, see [Create workspace resources](quickstart-create-resources.md).

* Familiarity with setting up an automated machine learning experiment with the Azure Machine Learning SDK. Follow the [tutorial](tutorial-auto-train-image-models.md) or [how-to](how-to-configure-auto-train.md) to see the fundamental automated machine learning experiment design patterns.

* An understanding of train/validation data splits and cross-validation as machine learning concepts. For a high-level explanation,

    * [About training, validation and test data in machine learning](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7)

    * [Understand Cross Validation in machine learning](https://towardsdatascience.com/understanding-cross-validation-419dbd47e9bd) 

[!INCLUDE [automl-sdk-version](../../includes/machine-learning-automl-sdk-version.md)]

## Default data splits and cross-validation in machine learning

Use the [AutoMLConfig](/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig.automlconfig) object to define your experiment and training settings. In the following code snippet, notice that only the required parameters are defined, that is the parameters for `n_cross_validations` or `validation_data` are **not** included.

> [!NOTE]
> The default data splits and cross-validation are not supported in forecasting scenarios. 

```python
data = "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/creditcard.csv"

dataset = Dataset.Tabular.from_delimited_files(data)

automl_config = AutoMLConfig(compute_target = aml_remote_compute,
                             task = 'classification',
                             primary_metric = 'AUC_weighted',
                             training_data = dataset,
                             label_column_name = 'Class'
                            )
```

If you do not explicitly specify either a `validation_data` or `n_cross_validations` parameter, automated ML applies default techniques depending on the number of rows provided in the single dataset `training_data`.

|Training&nbsp;data&nbsp;size| Validation technique |
|---|-----|
|**Larger&nbsp;than&nbsp;20,000&nbsp;rows**| Train/validation data split is applied. The default is to take 10% of the initial training data set as the validation set. In turn, that validation set is used for metrics calculation.
|**Smaller&nbsp;than&nbsp;20,000&nbsp;rows**| Cross-validation approach is applied. The default number of folds depends on the number of rows. <br> **If the dataset is less than 1,000 rows**, 10 folds are used. <br> **If the rows are between 1,000 and 20,000**, then three folds are used.
