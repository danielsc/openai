

## Define the endpoint and deployment

# [Azure CLI](#tab/azure-cli)

The following snippet shows the *endpoints/online/managed/sample/endpoint.yml* file: 

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-endpoint
auth_mode: key


```

> [!NOTE]
> For a full description of the YAML, see [Online endpoint YAML reference](reference-yaml-endpoint-online.md).

The reference for the endpoint YAML format is described in the following table. To learn how to specify these attributes, see the YAML example in [Prepare your system](#prepare-your-system) or the [online endpoint YAML reference](reference-yaml-endpoint-online.md). For information about limits related to managed endpoints, see [Manage and increase quotas for resources with Azure Machine Learning](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).

| Key         | Description                                                                                                                                                                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$schema`   | (Optional) The YAML schema. To see all available options in the YAML file, you can view the schema in the preceding example in a browser.                                                                                                                   |
| `name`      | The name of the endpoint. It must be unique in the Azure region.<br>Naming rules are defined under [managed online endpoint limits](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).                                               |
| `auth_mode` | Use `key` for key-based authentication. Use `aml_token` for Azure Machine Learning token-based authentication. `key` doesn't expire, but `aml_token` does expire. (Get the most recent token by using the `az ml online-endpoint get-credentials` command.) |

The example contains all the files needed to deploy a model on an online endpoint. To deploy a model, you must have:

- Model files (or the name and version of a model that's already registered in your workspace). In the example, we have a scikit-learn model that does regression.
- The code that's required to score the model. In this case, we have a *score.py* file.
- An environment in which your model runs. As you'll see, the environment might be a Docker image with Conda dependencies, or it might be a Dockerfile.
- Settings to specify the instance type and scaling capacity.

The following snippet shows the *endpoints/online/managed/sample/blue-deployment.yml* file, with all the required inputs: 

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
endpoint_name: my-endpoint
model:
  path: ../../model-1/model/
code_configuration:
  code: ../../model-1/onlinescoring/
  scoring_script: score.py
environment: 
  conda_file: ../../model-1/environment/conda.yml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest
instance_type: Standard_DS3_v2
instance_count: 1

```

The table describes the attributes of a `deployment`:

| Key                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
