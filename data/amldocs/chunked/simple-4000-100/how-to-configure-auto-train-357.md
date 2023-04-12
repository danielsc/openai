In case of compute instance, `max_concurrent_trials` can be set to be the same as number of cores on the compute instance VM.

## Explore models and metrics

Automated ML offers options for you to monitor and evaluate your training results. 

* For definitions and examples of the performance charts and metrics provided for each run, see [Evaluate automated machine learning experiment results](how-to-understand-automated-ml.md).

* To get a featurization summary and understand what features were added to a particular model, see [Featurization transparency](how-to-configure-auto-features.md#featurization-transparency). 

From Azure Machine Learning UI at the model's page you can also view the hyperparameters used when training a particular model and also view and customize the internal model's training code used. 

## Register and deploy models

After you test a model and confirm you want to use it in production, you can register it for later use.


> [!TIP]
> For registered models, one-click deployment is available via the [Azure Machine Learning studio](https://ml.azure.com). See [how to deploy registered models from the studio](how-to-use-automated-ml-for-ml-models.md#deploy-your-model). 

## AutoML in pipelines

To leverage AutoML in your MLOps workflows, you can add AutoML Job steps to your [AzureML Pipelines](./how-to-create-component-pipeline-python.md). This allows you to automate your entire workflow by hooking up your data prep scripts to AutoML and then registering and validating the resulting best model.

Below is a [sample pipeline](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines/1h_automl_in_pipeline/automl-classification-bankmarketing-in-pipeline) with an AutoML classification component and a command component that shows the resulting AutoML output. Note how the inputs (training & validation data) and the outputs (best model) are referenced in different steps.

``` python
# Define pipeline
@pipeline(
    description="AutoML Classification Pipeline",
    )
def automl_classification(
    classification_train_data,
    classification_validation_data
):
    # define the automl classification task with automl function
    classification_node = classification(
        training_data=classification_train_data,
        validation_data=classification_validation_data,
        target_column_name="y",
        primary_metric="accuracy",
        # currently need to specify outputs "mlflow_model" explictly to reference it in following nodes 
        outputs={"best_model": Output(type="mlflow_model")},
    )
    # set limits and training
    classification_node.set_limits(max_trials=1)
    classification_node.set_training(enable_stack_ensemble=False, enable_vote_ensemble=False)

    command_func = command(
        inputs=dict(
            automl_output=Input(type="mlflow_model")
        ),
        command="ls ${{inputs.automl_output}}",
        environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu:latest"
    )
    show_output = command_func(automl_output=classification_node.outputs.best_model)


pipeline_classification = automl_classification(
    classification_train_data=Input(path="./training-mltable-folder/", type="mltable"),
    classification_validation_data=Input(path="./validation-mltable-folder/", type="mltable"),
)

# ...
# Note that the above is only a snippet from the bankmarketing example you can find in our examples repo -> https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines/1h_automl_in_pipeline/automl-classification-bankmarketing-in-pipeline

```

For more examples on how to do include AutoML in your pipelines, please check out our [examples repo](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines/1h_automl_in_pipeline/).

## Next steps

+ Learn more about [how and where to deploy a model](./how-to-deploy-online-endpoints.md).