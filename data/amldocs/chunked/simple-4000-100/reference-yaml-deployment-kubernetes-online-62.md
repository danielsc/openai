| `min_instances` | integer | The minimum number of instances to use. | `1` |
| `max_instances` | integer | The maximum number of instances to scale to. | `1` |
| `target_utilization_percentage` | integer | The target CPU usage for the autoscaler. | `70` |
| `polling_interval` | integer | How often the autoscaler should attempt to scale the deployment, in seconds. | `1` |


### ContainerResourceRequests

| Key | Type | Description |
| --- | ---- | ----------- |
| `cpu` | string | The number of CPU cores requested for the container. |
| `memory` | string | The memory size requested for the container |
| `nvidia.com/gpu` | string | The number of Nvidia GPU cards requested for the container |

### ContainerResourceLimits

| Key | Type | Description |
| --- | ---- | ----------- |
| `cpu` | string | The limit for the number of CPU cores for the container. |
| `memory` | string | The limit for the memory size for the container. |
| `nvidia.com/gpu` | string | The limit for the number of Nvidia GPU cards for the container |

## Remarks

The `az ml online-deployment` commands can be used for managing Azure Machine Learning Kubernetes online deployments.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online).

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
