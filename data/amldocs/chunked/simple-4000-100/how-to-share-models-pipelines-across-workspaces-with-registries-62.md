The code examples in this article are based on the `nyc_taxi_data_regression` sample in the [examples repository](https://github.com/Azure/azureml-examples). To use these files on your development environment, use the following commands to clone the repository and change directories to the example:

```bash
git clone https://github.com/Azure/azureml-examples
cd azureml-examples
# changing branch is temporary until samples merge to main
git checkout mabables/registry
```

# [Azure CLI](#tab/cli)

For the CLI example, change directories to `cli/jobs/pipelines-with-components/nyc_taxi_data_regression` in your local clone of the [examples repository](https://github.com/Azure/azureml-examples).

```bash
cd cli/jobs/pipelines-with-components/nyc_taxi_data_regression
```

# [Python SDK](#tab/python)

For the Python SDK example, use the `nyc_taxi_data_regression` sample from the [examples repository](https://github.com/Azure/azureml-examples). The sample notebook, [share-models-components-environments.ipynb,](https://github.com/Azure/azureml-examples/tree/main/sdk/python/assets/assets-in-registry/share-models-components-environments.ipynb) is available in the `sdk/python/assets/assets-in-registry` folder. All the sample YAML for components, model training code, sample data for training and inference is available in `cli/jobs/pipelines-with-components/nyc_taxi_data_regression`. Change to the `sdk/resources/registry` directory and open the `share-models-components-environments.ipynb` notebook if you'd like to step through a notebook to try out the code in this document.


### Create SDK connection

> [!TIP]
> This step is only needed when using the Python SDK.

Create a client connection to both the AzureML workspace and registry:

```python
ml_client_workspace = MLClient( credential=credential,
    subscription_id = "<workspace-subscription>",
    resource_group_name = "<workspace-resource-group",
    workspace_name = "<workspace-name>")
print(ml_client_workspace)

ml_client_registry = MLClient ( credential=credential,
        registry_name = "<registry-name>")
print(ml_client_registry)
```

## Create environment in registry

Environments define the docker container and Python dependencies required to run training jobs or deploy models. For more information on environments, see the following articles:

* [Environment concepts](./concept-environments.md)
* [How to create environments (CLI)](./how-to-manage-environments-v2.md) articles. 

# [Azure CLI](#tab/cli)

> [!TIP]
> The same CLI command `az ml environment create` can be used to create environments in a workspace or registry. Running the command with `--workspace-name` command creates the environment in a workspace whereas running the command with `--registry-name` creates the environment in the registry.

We'll create an environment that uses the `python:3.8` docker image and installs Python packages required to run a training job using the SciKit Learn framework. If you've cloned the examples repo and are in the folder `cli/jobs/pipelines-with-components/nyc_taxi_data_regression`, you should be able to see environment definition file `env_train.yml` that references the docker file `env_train/Dockerfile`. The `env_train.yml` is shown below for your reference:

```YAML
$schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json
name: SKLearnEnv
version: 1
build:
  path: ./env_train
```

Create the environment using the `az ml environment create` as follows

```azurecli 
az ml environment create --file env_train.yml --registry-name <registry-name>
```

If you get an error that an environment with this name and version already exists in the registry, you can either edit the `version` field in `env_train.yml` or specify a different version on the CLI that overrides the version value in `env_train.yml`.

```azurecli 
# use shell epoch time as the version
version=$(date +%s)
az ml environment create --file env_train.yml --registry-name <registry-name> --set version=$version
```
