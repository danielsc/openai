
> [!TIP]
> `version=$(date +%s)` works only in Linux. Replace `$version` with a random number if this does not work.

Note down the `name` and `version` of the environment from the output of the `az ml environment create` command and use them with `az ml environment show` commands as follows. You'll need the `name` and `version` in the next section when you create a component in the registry.

```azurecli
az ml environment show --name SKLearnEnv --version 1 --registry-name <registry-name>
```

> [!TIP]
> If you used a different environment name or version, replace the `--name` and `--version` parameters accordingly.

 You can also use `az ml environment list --registry-name <registry-name>` to list all environments in the registry.

# [Python SDK](#tab/python)

> [!TIP]
> The same `MLClient.environments.create_or_update()` can be used to create environments in either a workspace or a registry depending on the target it has been initialized with. Since you work wth both workspace and registry in this document, you have initialized `ml_client_workspace` and `ml_client_registry` to work with workspace and registry respectively. 


We'll create an environment that uses the `python:3.8` docker image and installs Python packages required to run a training job using the SciKit Learn framework. The `Dockerfile` with base image and list of Python packages to install is available in `cli/jobs/pipelines-with-components/nyc_taxi_data_regression/env_train`. Initialize the environment object and create the environment.

```python
env_docker_context = Environment(
    build=BuildContext(path="../../../../cli/jobs/pipelines-with-components/nyc_taxi_data_regression/env_train/"),
    name="SKLearnEnv",
    version=str(1),
    description="Scikit Learn environment",
)
ml_client_registry.environments.create_or_update(env_docker_context)
```

> [!TIP]
> If you get an error that an environment with this name and version already exists in the registry, specify a different version for the `version` parameter.

Note down the `name` and `version` of the environment from the output and pass them to the `ml_client_registry.environments.get()` method to fetch the environment from registry. 

You can also use `ml_client_registry.environments.list()` to list all environments in the registry.


You can browse all environments in the AzureML studio. Make sure you navigate to the global UI and look for the __Registries__ entry.

:::image type="content" source="./media/how-to-share-models-pipelines-across-workspaces-with-registries/environment-in-registry.png" lightbox="./media/how-to-share-models-pipelines-across-workspaces-with-registries/environment-in-registry.png" alt-text="Screenshot of environments in the registry.":::

 
## Create a component in registry

Components are reusable building blocks of Machine Learning pipelines in AzureML. You can package the code, command, environment, input interface and output interface of an individual pipeline step into a component. Then you can reuse the component across multiple pipelines without having to worry about porting dependencies and code each time you write a different pipeline.

Creating a component in a workspace allows you to use the component in any pipeline job within that workspace. Creating a component in a registry allows you to use the component in any pipeline in any workspace within your organization. Creating components in a registry is a great way to build modular reusable utilities or shared training tasks that can be used for experimentation by different teams within your organization.

For more information on components, see the following articles:
* [Component concepts](concept-component.md)
* [How to use components in pipelines (CLI)](how-to-create-component-pipelines-cli.md)
* [How to use components in pipelines (SDK)](how-to-create-component-pipeline-python.md)

# [Azure CLI](#tab/cli)

Make sure you are in the folder `cli/jobs/pipelines-with-components/nyc_taxi_data_regression`. You'll find the component definition file `train.yml` that packages a Scikit Learn training script `train_src/train.py` and the [curated environment](resource-curated-environments.md) `AzureML-sklearn-0.24-ubuntu18.04-py37-cpu`. We'll use the Scikit Learn environment created in pervious step instead of the curated environment. You can edit `environment` field in the `train.yml` to refer to your Scikit Learn environment. The resulting component definition file `train.yml` will be similar to the following example: 
