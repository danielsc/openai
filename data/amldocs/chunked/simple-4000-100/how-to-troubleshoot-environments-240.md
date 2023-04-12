* `base_dockerfile`
* `build_context`
* See [DockerSection](https://aka.ms/azureml/environment/docker-section-class)

*Applies to: Azure CLI & Python SDK v2*

You didn't specify one of the following options in your environment definition
* `image`
* `build`
* See [azure.ai.ml.entities.Environment](https://aka.ms/azureml/environment/environment-class-v2)
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

Choose which Docker option you'd like to use to build your environment, then populate that option in your environment definition.

*Applies to: Python SDK v1*

```python
from azureml.core import Environment
myenv = Environment(name="myEnv")
myenv.docker.base_image = "pytorch/pytorch:latest"
```

*Applies to: Python SDK v2*

```python
env_docker_image = Environment(
    image="pytorch/pytorch:latest",
    name="docker-image-example",
    description="Environment created from a Docker image.",
)
ml_client.environments.create_or_update(env_docker_image)
```

**Resources**
* [Create and manage reusable environments v2](https://aka.ms/azureml/environment/create-and-manage-reusable-environments)
* [Environment class v1](https://aka.ms/azureml/environment/environment-class-v1)

### Container registry credentials missing either username or password
<!--issueDescription-->

**Potential causes:**

* You've specified either a username or a password for your container registry in your environment definition, but not both

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Add the missing username or password to your environment definition to fix the issue

```python
myEnv.docker.base_image_registry.username = "username"
```

Alternatively, provide authentication via [workspace connections](https://aka.ms/azureml/environment/set-connection-v1)

```python
from azureml.core import Workspace
ws = Workspace.from_config()
ws.set_connection("connection1", "ACR", "<URL>", "Basic", "{'Username': '<username>', 'Password': '<password>'}")
```

*Applies to: Azure CLI extensions v1 & v2*

Create a workspace connection from a YAML specification file

```
az ml connection create --file connection.yml --resource-group my-resource-group --workspace-name my-workspace
```

> [!NOTE]
> * Providing credentials in your environment definition is no longer supported. Use workspace connections instead.
 
**Resources**
* [Python SDK v1 workspace connections](https://aka.ms/azureml/environment/set-connection-v1)
* [Python SDK v2 workspace connections](/python/api/azure-ai-ml/azure.ai.ml.entities.workspaceconnection)
* [Azure CLI workspace connections](/cli/azure/ml/connection)

### Multiple credentials for base image registry
<!--issueDescription-->

**Potential causes:**

* You've specified more than one set of credentials for your base image registry

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

If you're using workspace connections, view the connections you have set, and delete whichever one(s) you don't want to use

```python
from azureml.core import Workspace
ws = Workspace.from_config()
ws.list_connections()
ws.delete_connection("myConnection2")
```

If you've specified credentials in your environment definition, choose one set of credentials to use, and set all others to null

```python
myEnv.docker.base_image_registry.registry_identity = None
```

> [!NOTE]
> * Providing credentials in your environment definition is no longer supported. Use workspace connections instead.
 
**Resources**
* [Delete a workspace connection v1](https://aka.ms/azureml/environment/delete-connection-v1)
* [Python SDK v1 workspace connections](https://aka.ms/azureml/environment/set-connection-v1)
* [Python SDK v2 workspace connections](/python/api/azure-ai-ml/azure.ai.ml.entities.workspaceconnection)
