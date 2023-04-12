
This YAML example, `2-sai-deployment.yml`,

* Specifies that the type of endpoint you want to create is an `online` endpoint.
* Indicates that the endpoint has an associated deployment called `blue`.
* Configures the details of the deployment such as, which model to deploy and which environment and scoring script to use.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
model:
  path: ../../model-1/model/
code_configuration:
  code: ../../model-1/onlinescoring/
  scoring_script: score_managedidentity.py
environment: 
  conda_file: ../../model-1/environment/conda-managedidentity.yml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest
instance_type: Standard_DS3_v2
instance_count: 1
environment_variables:
  STORAGE_ACCOUNT_NAME: "storage_place_holder"
  STORAGE_CONTAINER_NAME: "container_place_holder"
  FILE_NAME: "file_place_holder"
  UAI_CLIENT_ID: "uai_client_id_place_holder"
```

# [System-assigned (Python)](#tab/system-identity-python)

To deploy an online endpoint with the Python SDK (v2), objects may be used to define the configuration as below. Alternatively, YAML files may be loaded using the `.load` method. 

The following Python endpoint object: 

* Assigns the name by which you want to refer to the endpoint to the variable `endpoint_name. 
* Specifies the type of authorization to use to access the endpoint `auth-mode="key"`.

```python
endpoint = ManagedOnlineEndpoint(name=endpoint_name, auth_mode="key")
```

This deployment object: 

* Specifies that the type of deployment you want to create is a `ManagedOnlineDeployment` via the class. 
* Indicates that the endpoint has an associated deployment called `blue`.
* Configures the details of the deployment such as the `name` and `instance_count` 
* Defines additional objects inline and associates them with the deployment for `Model`,`CodeConfiguration`, and `Environment`. 
* Includes environment variables needed for the system-assigned managed identity to access storage.  


```python
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=endpoint_name,
    model=Model(path="../../model-1/model/"),
    code_configuration=CodeConfiguration(
        code="../../model-1/onlinescoring/", scoring_script="score_managedidentity.py"
    ),
    environment=Environment(
        conda_file="../../model-1/environment/conda-managedidentity.yml",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
    ),
    instance_type="Standard_DS3_v2",
    instance_count=1,
    environment_variables={
        "STORAGE_ACCOUNT_NAME": storage_account_name,
        "STORAGE_CONTAINER_NAME": storage_container_name,
        "FILE_NAME": file_name,
    },
)
```

# [User-assigned (Python)](#tab/user-identity-python)

To deploy an online endpoint with the Python SDK (v2), objects may be used to define the configuration as below. Alternatively, YAML files may be loaded using the `.load` method. 

For a user-assigned identity, we will define the endpoint configuration below once the User-Assigned Managed Identity has been created. 

This deployment object: 

* Specifies that the type of deployment you want to create is a `ManagedOnlineDeployment` via the class. 
* Indicates that the endpoint has an associated deployment called `blue`.
* Configures the details of the deployment such as the `name` and `instance_count` 
* Defines additional objects inline and associates them with the deployment for `Model`,`CodeConfiguration`, and `Environment`. 
* Includes environment variables needed for the user-assigned managed identity to access storage. 
* Adds a placeholder environment variable for `UAI_CLIENT_ID`, which will be added after creating one and before actually deploying this configuration. 


```python
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=endpoint_name,
    model=Model(path="../../model-1/model/"),
    code_configuration=CodeConfiguration(
        code="../../model-1/onlinescoring/", scoring_script="score_managedidentity.py"
    ),
    environment=Environment(
        conda_file="../../model-1/environment/conda-managedidentity.yml",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
    ),
    instance_type="Standard_DS3_v2",
    instance_count=1,
    environment_variables={
        "STORAGE_ACCOUNT_NAME": storage_account_name,
        "STORAGE_CONTAINER_NAME": storage_container_name,
        "FILE_NAME": file_name,
        # We will update this after creating an identity
        "UAI_CLIENT_ID": "uai_client_id_place_holder",
    },
)
```
