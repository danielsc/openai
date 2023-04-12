The result of running this script is a workspace handle that you'll use to manage other resources and jobs.

> [!NOTE]
> Creating `MLClient` will not connect the client to the workspace. The client initialization is lazy and will wait for the first time it needs to make a call. In this article, this will happen during compute creation.

### Create a compute resource to run the job

AzureML needs a compute resource to run a job. This resource can be single or multi-node machines with Linux or Windows OS, or a specific compute fabric like Spark.

In the following example script, we provision a Linux [`compute cluster`](./how-to-create-attach-compute-cluster.md?tabs=python). You can see the [`Azure Machine Learning pricing`](https://azure.microsoft.com/pricing/details/machine-learning/) page for the full list of VM sizes and prices. We only need a basic cluster for this example; thus, we'll pick a Standard_DS3_v2 model with 2 vCPU cores and 7 GB RAM to create an AzureML compute.

```python
from azure.ai.ml.entities import AmlCompute

# Name assigned to the compute cluster
cpu_compute_target = "cpu-cluster"

try:
    # let's see if the compute target already exists
    cpu_cluster = ml_client.compute.get(cpu_compute_target)
    print(
        f"You already have a cluster named {cpu_compute_target}, we'll reuse it as is."
    )

except Exception:
    print("Creating a new cpu compute target...")

    # Let's create the Azure ML compute object with the intended parameters
    cpu_cluster = AmlCompute(
        name=cpu_compute_target,
        # Azure ML Compute is the on-demand VM service
        type="amlcompute",
        # VM Family
        size="STANDARD_DS3_V2",
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
    cpu_cluster = ml_client.compute.begin_create_or_update(cpu_cluster).result()

print(
    f"AMLCompute with name {cpu_cluster.name} is created, the compute size is {cpu_cluster.size}"
)
```

### Create a job environment

To run an AzureML job, you'll need an environment. An AzureML [environment](concept-environments.md) encapsulates the dependencies (such as software runtime and libraries) needed to run your machine learning training script on your compute resource. This environment is similar to a Python environment on your local machine.

AzureML allows you to either use a curated (or ready-made) environment or create a custom environment using a Docker image or a Conda configuration. In this article, you'll create a custom environment for your jobs, using a Conda YAML file.

#### Create a custom environment

To create your custom environment, you'll define your Conda dependencies in a YAML file. First, create a directory for storing the file. In this example, we've named the directory `env`.

```python
import os

dependencies_dir = "./env"
os.makedirs(dependencies_dir, exist_ok=True)
```

Then, create the file in the dependencies directory. In this example, we've named the file `conda.yml`.

```python
%%writefile {dependencies_dir}/conda.yml
name: sklearn-env
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pip=21.2.4
  - scikit-learn=0.24.2
  - scipy=1.7.1
  - pip:  
    - mlflow== 1.26.1
    - azureml-mlflow==1.42.0
```

The specification contains some usual packages (such as numpy and pip) that you'll use in your job.

Next, use the YAML file to create and register this custom environment in your workspace. The environment will be packaged into a Docker container at runtime.

```python
from azure.ai.ml.entities import Environment

custom_env_name = "sklearn-env"

job_env = Environment(
    name=custom_env_name,
    description="Custom environment for sklearn image classification",
    conda_file=os.path.join(dependencies_dir, "conda.yml"),
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
)
job_env = ml_client.environments.create_or_update(job_env)

print(
    f"Environment with name {job_env.name} is registered to workspace, the environment version is {job_env.version}"
)
```
