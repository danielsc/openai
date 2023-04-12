Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/resources/compute). Several are shown below.

## YAML: minimal

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: minimal-example
type: amlcompute

```

## YAML: basic

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: basic-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120

```

## YAML: custom location

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: location-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120
location: westus

```

## YAML: low priority

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: low-pri-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120
tier: low_priority

```

## YAML: SSH username and password

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: ssh-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120
ssh_settings:
  admin_username: example-user
  admin_password: example-password

```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
