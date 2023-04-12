| `mirror_traffic` | string | Percentage of live traffic to mirror to a deployment. Mirroring traffic doesn't change the results returned to clients. The mirrored percentage of traffic is copied and submitted to the specified deployment so you can gather metrics and logging without impacting clients. For example, to check if latency is within acceptable bounds and that there are no HTTP errors. It's represented by a dictionary with a single key-value pair, where the key represents the deployment name and the value represents the percentage of traffic to mirror to the deployment. For more information, see [Test a deployment with mirrored traffic](how-to-safely-rollout-online-endpoints.md#test-the-deployment-with-mirrored-traffic-preview).

## Remarks

The `az ml online-endpoint` commands can be used for managing Azure Machine Learning online endpoints.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online). Several are shown below.

## YAML: basic

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-endpoint
auth_mode: key


```

## YAML: system-assigned identity

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-sai-endpoint
auth_mode: key

```

## YAML: user-assigned identity

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-uai-endpoint
auth_mode: key
identity:
  type: user_assigned
  user_assigned_identities:
    - resource_id: user_identity_ARM_id_place_holder

```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
- Learn how to [deploy a model with a managed online endpoint](how-to-deploy-online-endpoints.md)
- [Troubleshooting managed online endpoints deployment and scoring (preview)](./how-to-troubleshoot-online-endpoints.md)
