

### 2. Create a compute resource for training

An AzureML compute cluster is a fully managed compute resource that can be used to run the training job. In the following examples, a compute cluster named `cpu-compute` is created.

# [Python SDK](#tab/python)

```python
from azure.ai.ml.entities import AmlCompute

# specify aml compute name.
cpu_compute_target = "cpu-cluster"

try:
    ml_client.compute.get(cpu_compute_target)
except Exception:
    print("Creating a new cpu compute target...")
    compute = AmlCompute(
        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4
    )
    ml_client.compute.begin_create_or_update(compute).result()
```

# [Azure CLI](#tab/azurecli)

```azurecli
az ml compute create -n cpu-cluster --type amlcompute --min-instances 0 --max-instances 4
```

# [REST API](#tab/restapi)

```bash
curl -X PUT \
  "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/computes/$COMPUTE_NAME?api-version=$API_VERSION" \
  -H "Authorization:Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "location": "'$LOCATION'",
    "properties": {
        "computeType": "AmlCompute",
        "properties": {
            "vmSize": "Standard_D2_V2",
            "vmPriority": "Dedicated",
            "scaleSettings": {
                "maxNodeCount": 4,
                "minNodeCount": 0,
                "nodeIdleTimeBeforeScaleDown": "PT30M"
            }
        }
    }
}'
```

> [!TIP]
> While a response is returned after a few seconds, this only indicates that the creation request has been accepted. It can take several minutes for the cluster creation to finish.


### 4. Submit the training job

# [Python SDK](#tab/python)

To run this script, you'll use a `command`. The command will be run by submitting it as a `job` to Azure ML. 

```python
from azure.ai.ml import command, Input

# define the command
command_job = command(
    code="./src",
    command="python main.py --iris-csv ${{inputs.iris_csv}} --learning-rate ${{inputs.learning_rate}} --boosting ${{inputs.boosting}}",
    environment="AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu@latest",
    inputs={
        "iris_csv": Input(
            type="uri_file",
            path="https://azuremlexamples.blob.core.windows.net/datasets/iris.csv",
        ),
        "learning_rate": 0.9,
        "boosting": "gbdt",
    },
    compute="cpu-cluster",
)
```

```python
# submit the command
returned_job = ml_client.jobs.create_or_update(command_job)
# get a URL for the status of the job
returned_job.studio_url
```

In the above examples, you configured:
- `code` - path where the code to run the command is located
- `command` -  command that needs to be run
- `environment` - the environment needed to run the training script. In this example, we use a curated or ready-made environment provided by AzureML called `AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu`. We use the latest version of this environment by using the `@latest` directive. You can also use custom environments by specifying a base docker image and specifying a conda yaml on top of it.
- `inputs` - dictionary of inputs using name value pairs to the command. The key is a name for the input within the context of the job and the value is the input value. Inputs are referenced in the `command` using the `${{inputs.<input_name>}}` expression. To use files or folders as inputs, you can use the `Input` class.

For more information, see the [reference documentation](/python/api/azure-ai-ml/azure.ai.ml#azure-ai-ml-command).

When you submit the job, a URL is returned to the job status in the AzureML studio. Use the studio UI to view the job progress. You can also use `returned_job.status` to check the current status of the job.

# [Azure CLI](#tab/azurecli)

The `az ml job create` command used in this example requires a YAML job definition file. The contents of the file used in this example are:
