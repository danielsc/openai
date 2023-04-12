As you can see in this training script, once the model is trained, the model file is saved and registered to the workspace. Now you can use the registered model in inferencing endpoints.


For the environment of this step, you'll use one of the built-in (curated) Azure ML environments. The tag `azureml`, tells the system to use look for the name in curated environments.

First, create the *yaml* file describing the component:

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=train.yml)]

Now create and register the component:

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=train_component)]

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=update-train_component)]

## Create the pipeline from components

Now that both your components are defined and registered, you can start implementing the pipeline.

Here, you'll use *input data*, *split ratio* and *registered model name* as input variables. Then call the components and connect them via their inputs/outputs identifiers. The outputs of each step can be accessed via the `.outputs` property.

The Python functions returned by `load_component()` work as any regular Python function that we'll use within a pipeline to call each step.

To code the pipeline, you use a specific `@dsl.pipeline` decorator that identifies the Azure ML pipelines. In the decorator, we can specify the pipeline description and default resources like compute and storage. Like a Python function, pipelines can have inputs. You can then create multiple instances of a single pipeline with different inputs.

Here, we used *input data*, *split ratio* and *registered model name* as input variables. We then call the components and connect them via their inputs/outputs identifiers. The outputs of each step can be accessed via the `.outputs` property.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=pipeline)]

Now use your pipeline definition to instantiate a pipeline with your dataset, split rate of choice and the name you picked for your model.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=registered_model_name)]

## Submit the job 

It's now time to submit the job to run in Azure ML. This time you'll use `create_or_update`  on `ml_client.jobs`.

Here you'll also pass an experiment name. An experiment is a container for all the iterations one does on a certain project. All the jobs submitted under the same experiment name would be listed next to each other in Azure ML studio.

Once completed, the pipeline will register a model in your workspace as a result of training.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=returned_job)]

An output of "False" is expected from the above cell.  You can track the progress of your pipeline, by using the link generated in the cell above.

When you select on each component, you'll see more information about the results of that component. 
There are two important parts to look for at this stage:
* `Outputs+logs` > `user_logs` > `std_log.txt`
This section shows the script run sdtout.

    :::image type="content" source="media/tutorial-pipeline-python-sdk/user-logs.jpg" alt-text="Screenshot of std_log.txt." lightbox="media/tutorial-pipeline-python-sdk/user-logs.jpg":::


* `Outputs+logs` > `Metric`
This section shows different logged metrics. In this example. mlflow `autologging`, has automatically logged the training metrics.

    :::image type="content" source="media/tutorial-pipeline-python-sdk/metrics.jpg" alt-text="Screenshot shows logged metrics.txt." lightbox="media/tutorial-pipeline-python-sdk/metrics.jpg":::

## Deploy the model as an online endpoint

Now deploy your machine learning model as a web service in the Azure cloud, an [`online endpoint`](concept-endpoints.md).
