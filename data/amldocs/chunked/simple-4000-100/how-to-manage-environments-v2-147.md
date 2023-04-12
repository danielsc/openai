
# [Python SDK](#tab/python)

In the following example, the local path to the build context folder is specified in the `path' parameter. Azure ML will look for a Dockerfile named `Dockerfile` at the root of the build context.

```python
env_docker_context = Environment(
    build=BuildContext(path="docker-contexts/python-and-pip"),
    name="docker-context-example",
    description="Environment created from a Docker context.",
)
ml_client.environments.create_or_update(env_docker_context)
```


Azure ML will start building the image from the build context when the environment is created. You can monitor the status of the build and view the build logs in the studio UI.

### Create an environment from a conda specification

You can define an environment using a standard conda YAML configuration file that includes the dependencies for the conda environment. See [Creating an environment manually](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually) for information on this standard format.

You must also specify a base Docker image for this environment. Azure ML will build the conda environment on top of the Docker image provided. If you install some Python dependencies in your Docker image, those packages won't exist in the execution environment thus causing runtime failures. By default, Azure ML will build a Conda environment with dependencies you specified, and will execute the job in that environment instead of using any Python libraries that you installed on the base image.

## [Azure CLI](#tab/cli)

The following example is a YAML specification file for an environment defined from a conda specification. Here the relative path to the conda file from the Azure ML environment YAML file is specified via the `conda_file` property. You can alternatively define the conda specification inline using the `conda_file` property, rather than defining it in a separate file.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json
name: docker-image-plus-conda-example
image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
conda_file: conda-yamls/pydata.yml
description: Environment created from a Docker image plus Conda environment.

```

To create the environment:

```cli
az ml environment create --file assets/environment/docker-image-plus-conda.yml
```

## [Python SDK](#tab/python)

The relative path to the conda file is specified using the `conda_file` parameter.

```python
env_docker_conda = Environment(
    image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04",
    conda_file="conda-yamls/pydata.yml",
    name="docker-image-plus-conda-example",
    description="Environment created from a Docker image plus Conda environment.",
)
ml_client.environments.create_or_update(env_docker_conda)
```


Azure ML will build the final Docker image from this environment specification when the environment is used in a job or deployment. You can also manually trigger a build of the environment in the studio UI.

## Manage environments

The SDK and CLI (v2) also allow you to manage the lifecycle of your Azure ML environment assets.

### List

List all the environments in your workspace:

# [Azure CLI](#tab/cli)

```cli
az ml environment list
```

# [Python SDK](#tab/python)

```python
envs = ml_client.environments.list()
for env in envs:
    print(env.name)
```


List all the environment versions under a given name:

# [Azure CLI](#tab/cli)

```cli
az ml environment list --name docker-image-example
```

# [Python SDK](#tab/python)

```python
envs = ml_client.environments.list(name="docker-image-example")
for env in envs:
    print(env.version)
```


### Show

Get the details of a specific environment:

# [Azure CLI](#tab/cli)

```cli
az ml environment show --name docker-image-example --version 1
```

# [Python SDK](#tab/python)

```python
env = ml_client.environments.get(name="docker-image-example", version="1")
print(env)
```

### Update

Update mutable properties of a specific environment:
