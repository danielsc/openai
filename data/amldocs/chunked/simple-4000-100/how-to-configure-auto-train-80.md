  - file: ./bank_marketing_train_data.csv
transformations:
  - read_delimited:
        delimiter: ','
        encoding: 'ascii'
```

Therefore, the MLTable folder would have the MLTable definition file plus the data file (the bank_marketing_train_data.csv file in this case).

The following shows two ways of creating an MLTable.
- A. Providing your training data and MLTable definition file from your local folder and it will be automatically uploaded into the cloud (default Workspace Datastore)
- B. Providing a MLTable already registered and uploaded into the cloud.

```Python
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import automl, Input

# A. Create MLTable for training data from your local directory
my_training_data_input = Input(
    type=AssetTypes.MLTABLE, path="./data/training-mltable-folder"
)

# B. Remote MLTable definition
my_training_data_input  = Input(type=AssetTypes.MLTABLE, path="azureml://datastores/workspaceblobstore/paths/Classification/Train")
```

### Training, validation, and test data

You can specify separate **training data and validation data sets**, however training data must be provided to the `training_data` parameter in the factory function of your automated ML job.

If you don't explicitly specify a `validation_data` or `n_cross_validation` parameter, automated ML applies default techniques to determine how validation is performed. This determination depends on the number of rows in the dataset assigned to your `training_data` parameter. 

|Training&nbsp;data&nbsp;size| Validation technique |
|---|-----|
|**Larger&nbsp;than&nbsp;20,000&nbsp;rows**| Train/validation data split is applied. The default is to take 10% of the initial training data set as the validation set. In turn, that validation set is used for metrics calculation.
|**Smaller&nbsp;than&nbsp;or&nbsp;equal&nbsp;to&nbsp;20,000&nbsp;rows**| Cross-validation approach is applied. The default number of folds depends on the number of rows. <br> **If the dataset is fewer than 1,000 rows**, 10 folds are used. <br> **If the rows are equal to or between 1,000 and 20,000**, then three folds are used.


## Compute to run experiment


Automated ML jobs with the Python SDK v2 (or CLI v2) are currently only supported on Azure ML remote compute (cluster or compute instance).

[Learn more about creating compute with the Python SDKv2 (or CLIv2).](./how-to-train-model.md).
 
<a name='configure-experiment'></a>

## Configure your experiment settings

There are several options that you can use to configure your automated ML experiment. These configuration parameters are set in your task method. You can also set job training settings and [exit criteria](#exit-criteria) with the `set_training()` and `set_limits()` functions, respectively. 

The following example shows the required parameters for a classification task that specifies accuracy as the [primary metric](#primary-metric) and 5 cross-validation folds.

```python
# note that the below is a code snippet -- you might have to modify the variable values to run it successfully
classification_job = automl.classification(
    compute=my_compute_name,
    experiment_name=my_exp_name,
    training_data=my_training_data_input,
    target_column_name="y",
    primary_metric="accuracy",
    n_cross_validations=5,
    enable_model_explainability=True,
    tags={"my_custom_tag": "My custom value"}
)

# Limits are all optional

classification_job.set_limits(
    timeout_minutes=600, 
    trial_timeout_minutes=20, 
    max_trials=5,
    enable_early_termination=True,
)

# Training properties are optional
classification_job.set_training(
    blocked_training_algorithms=["LogisticRegression"], 
    enable_onnx_compatible_models=True
)
```

### Select your machine learning task type (ML problem)

Before you can submit your automated ML job, you need to determine the kind of machine learning problem you're solving. This problem determines which function your automated ML job uses and what model algorithms it applies.
