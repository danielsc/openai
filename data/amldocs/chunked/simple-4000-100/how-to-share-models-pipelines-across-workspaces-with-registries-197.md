Make sure you are in the folder `cli/jobs/pipelines-with-components/nyc_taxi_data_regression`. You'll find the component definition file `train.yml` that packages a Scikit Learn training script `train_src/train.py` and the [curated environment](resource-curated-environments.md) `AzureML-sklearn-0.24-ubuntu18.04-py37-cpu`. We'll use the Scikit Learn environment created in pervious step instead of the curated environment. You can edit `environment` field in the `train.yml` to refer to your Scikit Learn environment. The resulting component definition file `train.yml` will be similar to the following example: 

```YAML
# <component>
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
name: train_linear_regression_model
display_name: TrainLinearRegressionModel
version: 1
type: command
inputs:
  training_data: 
    type: uri_folder
  test_split_ratio:
    type: number
    min: 0
    max: 1
    default: 0.2
outputs:
  model_output:
    type: mlflow_model
  test_data:
    type: uri_folder
code: ./train_src
environment: azureml://registries/<registry-name>/environments/SKLearnEnv/versions/1`
command: >-
  python train.py 
  --training_data ${{inputs.training_data}} 
  --test_data ${{outputs.test_data}} 
  --model_output ${{outputs.model_output}}
  --test_split_ratio ${{inputs.test_split_ratio}}

```

If you used different name or version, the more generic representation looks like this: `environment: azureml://registries/<registry-name>/environments/<sklearn-environment-name>/versions/<sklearn-environment-version>`, so make sure you replace the `<registry-name>`,  `<sklearn-environment-name>` and `<sklearn-environment-version>` accordingly. You then run the `az ml component create` command to create the component as follows.

```azurecli
az ml component create --file train.yml --registry-name <registry-name>
```

> [!TIP]
> The same the CLI command `az ml component create` can be used to create components in a workspace or registry. Running the command with `--workspace-name` command creates the component in a workspace whereas running the command with `--registry-name` creates the component in the registry.

If you prefer to not edit the `train.yml`, you can override the environment name on the CLI as follows:

```azurecli
az ml component create --file train.yml --registry-name <registry-name>` --set environment=azureml://registries/<registry-name>/environments/SKLearnEnv/versions/1
# or if you used a different name or version, replace `<sklearn-environment-name>` and `<sklearn-environment-version>` accordingly
az ml component create --file train.yml --registry-name <registry-name>` --set environment=azureml://registries/<registry-name>/environments/<sklearn-environment-name>/versions/<sklearn-environment-version>
```

> [!TIP]
> If you get an error that the name of the component already exists in the registry, you can either edit the version in `train.yml` or override the version on the CLI with a random version.

Note down the `name` and `version` of the component from the output of the `az ml component create` command and use them with `az ml component show` commands as follows. You'll need the `name` and `version` in the next section when you create submit a training job in the workspace.

```azurecli 
az ml component show --name <component_name> --version <component_version> --registry-name <registry-name>
```
 You can also use `az ml component list --registry-name <registry-name>` to list all components in the registry.

# [Python SDK](#tab/python)

Review the component definition file `train.yml` and the Python code `train_src/train.py` to train a regression model using Scikit Learn available in the `cli/jobs/pipelines-with-components/nyc_taxi_data_regression` folder. Load the component object from the component definition file `train.yml`. 

```python
parent_dir = "../../../../cli/jobs/pipelines-with-components/nyc_taxi_data_regression"
train_model = load_component(path=parent_dir + "/train.yml")
print(train_model)
```
