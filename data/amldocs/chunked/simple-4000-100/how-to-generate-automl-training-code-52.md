If you're using the Python SDKv2, you can also download the "script.py" and the "script_run_notebook.ipynb" by retrieving the best run via MLFlow & downloading the resulting artifacts. 

## script.py

The `script.py` file contains the core logic needed to train a model with the previously used hyperparameters. While intended to be executed in the context of an Azure ML script run, with some modifications, the model's training code can also be run standalone in your own on-premises environment.

The script can roughly be broken down into several the following parts: data loading, data preparation, data featurization, preprocessor/algorithm specification, and training.

### Data loading

The function `get_training_dataset()` loads the previously used dataset. It assumes that the script is run in an AzureML script run under the same workspace as the original experiment.

```python
def get_training_dataset(dataset_id):
    from azureml.core.dataset import Dataset
    from azureml.core.run import Run
    
    logger.info("Running get_training_dataset")
    ws = Run.get_context().experiment.workspace
    dataset = Dataset.get_by_id(workspace=ws, id=dataset_id)
    return dataset.to_pandas_dataframe()
```

When running as part of a script run, `Run.get_context().experiment.workspace` retrieves the correct workspace. However, if this script is run inside of a different workspace or run locally, you need to modify the script to [explicitly specify the appropriate workspace](/python/api/azureml-core/azureml.core.workspace.workspace).

Once the workspace has been retrieved, the original dataset is retrieved by its ID. Another dataset with exactly the same structure could also be specified by ID or name with the [`get_by_id()`](/python/api/azureml-core/azureml.core.dataset.dataset#get-by-id-workspace--id-) or [`get_by_name()`](/python/api/azureml-core/azureml.core.dataset.dataset#get-by-name-workspace--name--version--latest--), respectively. You can find the ID later on in the script, in a similar section as the following code.

```python
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--training_dataset_id', type=str, default='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx', help='Default training dataset id is populated from the parent run')
    args = parser.parse_args()
    
    main(args.training_dataset_id)
```

You can also opt to replace this entire function with your own data loading mechanism; the only constraints are that the return value must be a Pandas dataframe and that the data must have the same shape as in the original experiment.

### Data preparation code

The function `prepare_data()` cleans the data, splits out the feature and sample weight columns and prepares the data for use in training.
This function can vary depending on the type of dataset and the experiment task type: classification, regression, time-series forecasting, images or NLP tasks.

The following example shows that in general, the dataframe from the data loading step is passed in. The label column and sample weights, if originally specified, are extracted and rows containing `NaN` are dropped from the input data.

```python
def prepare_data(dataframe):
    from azureml.training.tabular.preprocessing import data_cleaning
    
    logger.info("Running prepare_data")
    label_column_name = 'y'
    
    # extract the features, target and sample weight arrays
    y = dataframe[label_column_name].values
    X = dataframe.drop([label_column_name], axis=1)
    sample_weights = None
    X, y, sample_weights = data_cleaning._remove_nan_rows_in_X_y(X, y, sample_weights,
     is_timeseries=False, target_column=label_column_name)
    
    return X, y, sample_weights
```

If you want to do any additional data preparation, it can be done in this step by adding your custom data preparation code.

### Data featurization code

The function `generate_data_transformation_config()` specifies the featurization step in the final scikit-learn pipeline. The featurizers from the original experiment are reproduced here, along with their parameters.
