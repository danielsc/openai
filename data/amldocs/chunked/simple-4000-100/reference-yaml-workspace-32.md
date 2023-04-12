| `public_network_access` | string | Whether public endpoint access is allowed if the workspace will be using Private Link. For more information, see [Enable public access when behind VNets](how-to-configure-private-link.md#enable-public-access). | `enabled`, `disabled` | `disabled` |

## Remarks

The `az ml workspace` command can be used for managing Azure Machine Learning workspaces.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/resources/workspace). Several are shown below.

## YAML: basic

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-basic-prod
location: eastus
display_name: Basic workspace-example
description: This example shows a YML configuration for a basic workspace. In case you use this configuration to deploy a new workspace, since no existing dependent resources are specified, these will be automatically created.
hbi_workspace: false
tags:
  purpose: demonstration
```

## YAML: with existing resources

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-basicex-prod
location: eastus
display_name: Bring your own dependent resources-example
description: This configuration specifies a workspace configuration with existing dependent resources
storage_account: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Storage/storageAccounts/<STORAGE_ACCOUNT>
container_registry: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ContainerRegistry/registries/<CONTAINER_REGISTRY>
key_vault: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.KeyVault/vaults/<KEY_VAULT>
application_insights: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.insights/components/<APP_INSIGHTS>
tags:
  purpose: demonstration
```

## YAML: customer-managed key

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-cmkexample-prod
location: eastus
display_name: Customer managed key encryption-example
description: This configurations shows how to create a workspace that uses customer-managed keys for encryption.
customer_managed_key: 
  key_vault: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.KeyVault/vaults/<KEY_VAULT>
  key_uri: https://<KEY_VAULT>.vault.azure.net/keys/<KEY_NAME>/<KEY_VERSION>
tags:
  purpose: demonstration

```

## YAML: private link

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-privatelink-prod
location: eastus
display_name: Private Link endpoint workspace-example
description: When using private link, you must set the image_build_compute property to a cluster name to use for Docker image environment building. You can also specify whether the workspace should be accessible over the internet.
image_build_compute: cpu-compute
public_network_access: Disabled
tags:
  purpose: demonstration
```

## YAML: high business impact

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-hbiexample-prod
location: eastus
display_name: High business impact-example
description: This configuration shows how to configure a workspace with the hbi flag enabled. This flag specifies whether to reduce telemetry collection and enable additional encryption when high-business-impact data is used.
hbi_workspace: true
tags:
  purpose: demonstration

```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
