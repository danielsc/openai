
```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: green
endpoint_name: my-endpoint
model:
  path: ../../model-2/model/
code_configuration:
  code: ../../model-2/onlinescoring/
  scoring_script: score.py
environment:
  conda_file: ../../model-2/environment/conda.yml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest
instance_type: Standard_DS3_v2
instance_count: 1

```

## YAML: system-assigned identity

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
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

```

## YAML: user-assigned identity

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

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
