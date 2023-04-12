Once you have the scikit-Learn pipeline, all that is left to call is the `fit()` method to train the model:

```python
def train_model(X, y, sample_weights):
    
    logger.info("Running train_model")
    model_pipeline = build_model_pipeline()
    
    model = model_pipeline.fit(X, y)
    return model
```

The return value from `train_model()` is the model fitted/trained on the input data.

The main code that runs all the previous functions is the following:

```python
def main(training_dataset_id=None):
    from azureml.core.run import Run
    
    # The following code is for when running this code as part of an AzureML script run.
    run = Run.get_context()
    setup_instrumentation(run)
    
    df = get_training_dataset(training_dataset_id)
    X, y, sample_weights = prepare_data(df)
    split_ratio = 0.1
    try:
        (X_train, y_train, sample_weights_train), (X_valid, y_valid, sample_weights_valid) = split_dataset(X, y, sample_weights, split_ratio, should_stratify=True)
    except Exception:
        (X_train, y_train, sample_weights_train), (X_valid, y_valid, sample_weights_valid) = split_dataset(X, y, sample_weights, split_ratio, should_stratify=False)

    model = train_model(X_train, y_train, sample_weights_train)
    
    metrics = calculate_metrics(model, X, y, sample_weights, X_test=X_valid, y_test=y_valid)
    
    print(metrics)
    for metric in metrics:
        run.log(metric, metrics[metric])
```

Once you have the trained model, you can use it for making predictions with the predict() method. If your experiment is for a time series model, use the forecast() method for predictions. 

```python
y_pred = model.predict(X)
```

Finally, the model is serialized and saved as a `.pkl` file named "model.pkl":

```python
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    run.upload_file('outputs/model.pkl', 'model.pkl')
```

## script_run_notebook.ipynb

The `script_run_notebook.ipynb` notebook serves as an easy way to execute `script.py` on an Azure ML compute.
This notebook is similar to the existing automated ML sample notebooks however, there are a couple of key differences as explained in the following sections.

### Environment

Typically, the training environment for an automated ML run is automatically set by the SDK. However, when running a custom script run like the generated code, automated ML is no longer driving the process, so the environment must be specified for the command job to succeed.

Code generation reuses the environment that was used in the original automated ML experiment, if possible. Doing so guarantees that the training script run doesn't fail due to missing dependencies, and has a side benefit of not needing a Docker image rebuild, which saves time and compute resources.

If you make changes to `script.py` that require additional dependencies, or you would like to use your own environment, you need to update the environment in the `script_run_notebook.ipynb` accordingly.


### Submit the experiment

Since the generated code isn’t driven by automated ML anymore, instead of creating and submitting an AutoML Job, you need to create a `Command Job` and provide the generated code (script.py) to it. 

The following example contains the parameters and regular dependencies needed to run a Command Job, such as compute, environment, etc.
```python
from azure.ai.ml import command, Input

# To test with new training / validation datasets, replace the default dataset id(s) taken from parent run below
training_dataset_id = '<DATASET_ID>'

dataset_arguments = {'training_dataset_id': training_dataset_id}
command_str = 'python script.py --training_dataset_id ${{inputs.training_dataset_id}}'

command_job = command(
    code=project_folder,
    command=command_str,
    environment='AutoML-Non-Prod-DNN:25',
    inputs=dataset_arguments,
    compute='automl-e2e-cl2',
    experiment_name='build_70775722_9249eda8'
)
 
returned_job = ml_client.create_or_update(command_job)
print(returned_job.studio_url) # link to naviagate to submitted run in AzureML Studio
```
