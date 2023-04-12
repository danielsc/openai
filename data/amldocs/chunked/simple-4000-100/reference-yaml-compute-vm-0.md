
# CLI (v2) attached Virtual Machine YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/vmCompute.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `type` | string | **Required.** The type of compute. | `virtualmachine` | |
| `name` | string | **Required.** Name of the compute. | | |
| `description` | string | Description of the compute. | | |
| `resource_id` | string | **Required.** Fully qualified resource ID of the Azure Virtual Machine to attach to the workspace as a compute target. | | |
| `ssh_settings` | object | SSH settings for connecting to the virtual machine. | | |
| `ssh_settings.admin_username` | string | The name of the administrator user account that can be used to SSH into the virtual machine. | | |
| `ssh_settings.admin_password` | string | The password of the administrator user account. **One of `admin_password` or `ssh_private_key_file` is required.** | | |
| `ssh_settings.ssh_private_key_file` | string | The local path to the SSH private key file of the administrator user account. **One of `admin_password` or `ssh_private_key_file` is required.** | | |
| `ssh_settings.ssh_port` | integer | The SSH port on the virtual machine. | | `22` |

## Remarks

The `az ml compute` command can be used for managing Virtual Machines (VM) attached to an Azure Machine Learning workspace.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/resources/compute). Several are shown below.

## YAML: basic

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/vmCompute.schema.json 
name: vm-example
type: virtualmachine
resource_id: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Compute/virtualMachines/<VM_NAME>
ssh_settings:
  admin_username: <admin_username>
  admin_password: <admin_password>
```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
