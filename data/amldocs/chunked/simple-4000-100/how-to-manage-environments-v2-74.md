Curated environments are provided by Azure ML and are available in your workspace by default. Azure ML routinely updates these environments with the latest framework version releases and maintains them for bug fixes and security patches. They're backed by cached Docker images, which reduce job preparation cost and model deployment time.

You can use these curated environments out of the box for training or deployment by referencing a specific environment using the `azureml:<curated-environment-name>:<version>` or `azureml:<curated-environment-name>@latest` syntax. You can also use them as reference for your own custom environments by modifying the Dockerfiles that back these curated environments.

You can see the set of available curated environments in the Azure ML studio UI, or by using the CLI (v2) via `az ml environments list`.

## Create an environment

You can define an environment from a Docker image, a Docker build context, and a conda specification with Docker image. 

### Create an environment from a Docker image

To define an environment from a Docker image, provide the image URI of the image hosted in a registry such as Docker Hub or Azure Container Registry. 

# [Azure CLI](#tab/cli)

The following example is a YAML specification file for an environment defined from a Docker image. An image from the official PyTorch repository on Docker Hub is specified via the `image` property in the YAML file.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json
name: docker-image-example
image: pytorch/pytorch:latest
description: Environment created from a Docker image.

```

To create the environment:

```cli
az ml environment create --file assets/environment/docker-image.yml
```

# [Python SDK](#tab/python)

The following example creates an environment from a Docker image. An image from the official PyTorch repository on Docker Hub is specified via the `image` property.

```python
env_docker_image = Environment(
    image="pytorch/pytorch:latest",
    name="docker-image-example",
    description="Environment created from a Docker image.",
)
ml_client.environments.create_or_update(env_docker_image)
```


> [!TIP]
> Azure ML maintains a set of CPU and GPU Ubuntu Linux-based base images with common system dependencies. For example, the GPU images contain Miniconda, OpenMPI, CUDA, cuDNN, and NCCL. You can use these images for your environments, or use their corresponding Dockerfiles as reference when building your own custom images.
>  
> For the set of base images and their corresponding Dockerfiles, see the [AzureML-Containers repo](https://github.com/Azure/AzureML-Containers).

### Create an environment from a Docker build context

Instead of defining an environment from a prebuilt image, you can also define one from a Docker [build context](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#understand-build-context). To do so, specify the directory that will serve as the build context. This directory should contain a Dockerfile and any other files needed to build the image.

# [Azure CLI](#tab/cli)

The following example is a YAML specification file for an environment defined from a build context. The local path to the build context folder is specified in the `build.path` field, and the relative path to the Dockerfile within that build context folder is specified in the `build.dockerfile_path` field. If `build.dockerfile_path` is omitted in the YAML file, Azure ML will look for a Dockerfile named `Dockerfile` at the root of the build context.

In this example, the build context contains a Dockerfile named `Dockerfile` and a `requirements.txt` file that is referenced within the Dockerfile for installing Python packages.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json
name: docker-context-example
build:
  path: docker-contexts/python-and-pip

```

To create the environment:

```cli
az ml environment create --file assets/environment/docker-context.yml
```
