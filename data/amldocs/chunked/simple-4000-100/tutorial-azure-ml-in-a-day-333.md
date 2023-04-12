
As you can see in this script, once the model is trained, the model file is saved and registered to the workspace. Now you can use the registered model in inferencing endpoints.

## Configure the command

Now that you have a script that can perform the desired tasks, you'll use the general purpose **command** that can run command line actions. This command line action can be directly calling system commands or by running a script. 

Here, you'll create input variables to specify the input data, split ratio, learning rate and registered model name.  The command script will:
* Use the compute created earlier to run this command.
* Use the environment created earlier - you can use the `@latest` notation to indicate the latest version of the environment when the command is run.
* Configure some metadata like display name, experiment name etc. An *experiment* is a container for all the iterations you do on a certain project. All the jobs submitted under the same experiment name would be listed next to each other in Azure ML studio.
* Configure the command line action itself - `python main.py` in this case. The inputs/outputs are accessible in the command via the `${{ ... }}` notation.


```python
from azure.ai.ml import command
from azure.ai.ml import Input

registered_model_name = "credit_defaults_model"

job = command(
    inputs=dict(
        data=Input(
            type="uri_file",
            path="https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls",
        ),
        test_train_ratio=0.2,
        learning_rate=0.25,
        registered_model_name=registered_model_name,
    ),
    code="./src/",  # location of source code
    command="python main.py --data ${{inputs.data}} --test_train_ratio ${{inputs.test_train_ratio}} --learning_rate ${{inputs.learning_rate}} --registered_model_name ${{inputs.registered_model_name}}",
    environment="aml-scikit-learn@latest",
    compute="cpu-cluster",
    experiment_name="train_model_credit_default_prediction",
    display_name="credit_default_prediction",
)
```

## Submit the job 

It's now time to submit the job to run in AzureML. This time you'll use `create_or_update`  on `ml_client.jobs`.

```python
ml_client.create_or_update(job)
```

## View job output and wait for job completion

View the job in AzureML studio by selecting the link in the output of the previous cell.

The output of this job will look like this in the AzureML studio. Explore the tabs for various details like metrics, outputs etc. Once completed, the job will register a model in your workspace as a result of training. 

![Screenshot that shows the job overview](media/tutorial-azure-ml-in-a-day/view-job.gif "Overview of the job.")

> [!IMPORTANT]
> Wait until the status of the job is complete before returning to this notebook to continue. The job will take 2 to 3 minutes to run. It could take longer (up to 10 minutes) if the compute cluster has been scaled down to zero nodes and custom environment is still building.

## Deploy the model as an online endpoint

Now deploy your machine learning model as a web service in the Azure cloud, an [`online endpoint`](concept-endpoints.md).

To deploy a machine learning service, you usually need:

* The model assets (file, metadata) that you want to deploy. You've already registered these assets in your training job.
* Some code to run as a service. The code executes the model on a given input request. This entry script receives data submitted to a deployed web service and passes it to the model, then returns the model's response to the client. The script is specific to your model. The entry script must understand the data that the model expects and returns. With an MLFlow model, as in this tutorial, this script is automatically created for you. Samples of scoring scripts can be found [here](https://github.com/Azure/azureml-examples/tree/sdk-preview/sdk/endpoints/online).


## Create a new online endpoint

Now that you have a registered model and an inference script, it's time to create your online endpoint. The endpoint name needs to be unique in the entire Azure region. For this tutorial, you'll create a unique name using [`UUID`](https://en.wikipedia.org/wiki/Universally_unique_identifier).
