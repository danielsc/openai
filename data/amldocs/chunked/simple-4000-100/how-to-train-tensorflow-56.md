
If you prefer to use a browser to sign in and authenticate, you should uncomment the following code and use it instead.

```python
# Handle to the workspace
# from azure.ai.ml import MLClient

# Authentication package
# from azure.identity import InteractiveBrowserCredential
# credential = InteractiveBrowserCredential()
```

Next, get a handle to the workspace by providing your Subscription ID, Resource Group name, and workspace name. To find these parameters:

1. Look for your workspace name in the upper-right corner of the Azure Machine Learning studio toolbar.
2. Select your workspace name to show your Resource Group and Subscription ID.
3. Copy the values for Resource Group and Subscription ID into the code.

```python
# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id="<SUBSCRIPTION_ID>",
    resource_group_name="<RESOURCE_GROUP>",
    workspace_name="<AML_WORKSPACE_NAME>",
)
```

The result of running this script is a workspace handle that you'll use to manage other resources and jobs.

> [!NOTE]
> - Creating `MLClient` will not connect the client to the workspace. The client initialization is lazy and will wait for the first time it needs to make a call. In this article, this will happen during compute creation.

### Create a compute resource to run the job

AzureML needs a compute resource to run a job. This resource can be single or multi-node machines with Linux or Windows OS, or a specific compute fabric like Spark.

In the following example script, we provision a Linux [`compute cluster`](./how-to-create-attach-compute-cluster.md?tabs=python). You can see the [`Azure Machine Learning pricing`](https://azure.microsoft.com/pricing/details/machine-learning/) page for the full list of VM sizes and prices. Since we need a GPU cluster for this example, let's pick a *STANDARD_NC6* model and create an AzureML compute.

```python
from azure.ai.ml.entities import AmlCompute

gpu_compute_target = "gpu-cluster"

try:
    # let's see if the compute target already exists
    gpu_cluster = ml_client.compute.get(gpu_compute_target)
    print(
        f"You already have a cluster named {gpu_compute_target}, we'll reuse it as is."
    )

except Exception:
    print("Creating a new gpu compute target...")

    # Let's create the Azure ML compute object with the intended parameters
    gpu_cluster = AmlCompute(
        # Name assigned to the compute cluster
        name="gpu-cluster",
        # Azure ML Compute is the on-demand VM service
        type="amlcompute",
        # VM Family
        size="STANDARD_NC6",
        # Minimum running nodes when there is no job running
        min_instances=0,
        # Nodes in cluster
        max_instances=4,
        # How many seconds will the node running after the job termination
        idle_time_before_scale_down=180,
        # Dedicated or LowPriority. The latter is cheaper but there is a chance of job termination
        tier="Dedicated",
    )

    # Now, we pass the object to MLClient's create_or_update method
    gpu_cluster = ml_client.begin_create_or_update(gpu_cluster).result()

print(
    f"AMLCompute with name {gpu_cluster.name} is created, the compute size is {gpu_cluster.size}"
)
```

### Create a job environment

To run an AzureML job, you'll need an environment. An AzureML [environment](concept-environments.md) encapsulates the dependencies (such as software runtime and libraries) needed to run your machine learning training script on your compute resource. This environment is similar to a Python environment on your local machine.

AzureML allows you to either use a curated (or ready-made) environment—useful for common training and inference scenarios—or create a custom environment using a Docker image or a Conda configuration. 

In this article, you'll reuse the curated AzureML environment `AzureML-tensorflow-2.7-ubuntu20.04-py38-cuda11-gpu`. You'll use the latest version of this environment using the `@latest` directive.

```python
curated_env_name = "AzureML-tensorflow-2.7-ubuntu20.04-py38-cuda11-gpu@latest"
```
