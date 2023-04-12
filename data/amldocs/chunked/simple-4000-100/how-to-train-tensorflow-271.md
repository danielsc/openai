We also define an early termination policy—the `BanditPolicy`. This policy operates by checking the job every two iterations. If the primary metric, `validation_acc`, falls outside the top ten percent range, AzureML will terminate the job. This saves the model from continuing to explore hyperparameters that show no promise of helping to reach the target metric.

```python
from azure.ai.ml.sweep import BanditPolicy

sweep_job = job_for_sweep.sweep(
    compute=gpu_compute_target,
    sampling_algorithm="random",
    primary_metric="validation_acc",
    goal="Maximize",
    max_total_trials=8,
    max_concurrent_trials=4,
    early_termination_policy=BanditPolicy(slack_factor=0.1, evaluation_interval=2),
)
```

Now, you can submit this job as before. This time, you'll be running a sweep job that sweeps over your train job.

```python
returned_sweep_job = ml_client.create_or_update(sweep_job)

# stream the output and wait until the job is finished
ml_client.jobs.stream(returned_sweep_job.name)

# refresh the latest status of the job after streaming
returned_sweep_job = ml_client.jobs.get(name=returned_sweep_job.name)
```

You can monitor the job by using the studio user interface link that is presented during the job run.

## Find and register the best model

Once all the runs complete, you can find the run that produced the model with the highest accuracy.

```python
from azure.ai.ml.entities import Model

if returned_sweep_job.status == "Completed":

    # First let us get the run which gave us the best result
    best_run = returned_sweep_job.properties["best_child_run_id"]

    # lets get the model from this run
    model = Model(
        # the script stores the model as "model"
        path="azureml://jobs/{}/outputs/artifacts/paths/outputs/model/".format(
            best_run
        ),
        name="run-model-example",
        description="Model created from run.",
        type="custom_model",
    )

else:
    print(
        "Sweep job status: {}. Please wait until it completes".format(
            returned_sweep_job.status
        )
    )
```

You can then register this model.

```python
registered_model = ml_client.models.create_or_update(model=model)
```


## Deploy the model as an online endpoint

After you've registered your model, you can deploy it as an [online endpoint](concept-endpoints.md)—that is, as a web service in the Azure cloud.

To deploy a machine learning service, you'll typically need:
- The model assets that you want to deploy. These assets include the model's file and metadata that you already registered in your training job.
- Some code to run as a service. The code executes the model on a given input request (an entry script). This entry script receives data submitted to a deployed web service and passes it to the model. After the model processes the data, the script returns the model's response to the client. The script is specific to your model and must understand the data that the model expects and returns. When you use an MLFlow model, AzureML automatically creates this script for you.

For more information about deployment, see [Deploy and score a machine learning model with managed online endpoint using Python SDK v2](how-to-deploy-managed-online-endpoint-sdk-v2.md).

### Create a new online endpoint

As a first step to deploying your model, you need to create your online endpoint. The endpoint name must be unique in the entire Azure region. For this article, you'll create a unique name using a universally unique identifier (UUID).

```python
import uuid

# Creating a unique name for the endpoint
online_endpoint_name = "tff-dnn-endpoint-" + str(uuid.uuid4())[:8]
```

```python
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
)

# create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Classify handwritten digits using a deep neural network (DNN) using TensorFlow",
    auth_mode="key",
)

endpoint = ml_client.begin_create_or_update(endpoint).result()

print(f"Endpint {endpoint.name} provisioning state: {endpoint.provisioning_state}")
```
