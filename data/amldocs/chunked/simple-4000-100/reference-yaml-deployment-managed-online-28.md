| `app_insights_enabled` | boolean | Whether to enable integration with the Azure Application Insights instance associated with your workspace. | | `false` |
| `scale_settings` | object | The scale settings for the deployment. Currently only the `default` scale type is supported, so you don't need to specify this property. <br><br> With this `default` scale type, you can either manually scale the instance count up and down after deployment creation by updating the `instance_count` property, or create an [autoscaling policy](how-to-autoscale-endpoints.md). | | |
| `scale_settings.type` | string | The scale type. | `default` | `default` |
| `request_settings` | object | Scoring request settings for the deployment. See [RequestSettings](#requestsettings) for the set of configurable properties. | | |
| `liveness_probe` | object | Liveness probe settings for monitoring the health of the container regularly. See [ProbeSettings](#probesettings) for the set of configurable properties. | | |
| `readiness_probe` | object | Readiness probe settings for validating if the container is ready to serve traffic. See [ProbeSettings](#probesettings) for the set of configurable properties. | | |
| `egress_public_network_access` | string | This flag secures the deployment by restricting communication between the deployment and the Azure resources used by it. Set to `disabled` to ensure that the download of the model, code, and images needed by your deployment are secured with a private endpoint. This flag is applicable only for managed online endpoints. | `enabled`, `disabled` | `enabled` |

### RequestSettings

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `request_timeout_ms` | integer | The scoring timeout in milliseconds. | `5000` |
| `max_concurrent_requests_per_instance` | integer | The maximum number of concurrent requests per instance allowed for the deployment. <br><br> Set to the number of requests that your model can process concurrently on a single node. Setting this value higher than your model's actual concurrency can lead to higher latencies. Setting this value too low may lead to under utilized nodes. Setting too low may also result in requests being rejected with a 429 HTTP status code, as the system will opt to fail fast. <br><br> For more information, see [Troubleshooting online endpoints: HTTP status codes](how-to-troubleshoot-online-endpoints.md#http-status-codes). | `1` |
| `max_queue_wait_ms` | integer | The maximum amount of time in milliseconds a request will stay in the queue. | `500` |

### ProbeSettings

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `initial_delay` | integer | The number of seconds after the container has started before the probe is initiated. Minimum value is `1`. | `10` |
| `period` | integer | How often (in seconds) to perform the probe. | `10` |
| `timeout` | integer | The number of seconds after which the probe times out. Minimum value is `1`. | `2` |
| `success_threshold` | integer | The minimum consecutive successes for the probe to be considered successful after having failed. Minimum value is `1` for readiness probe. The value for liveness probe is fixed as `1`. | `1` |
| `failure_threshold` | integer | When a probe fails, the system will try `failure_threshold` times before giving up. Giving up in the case of a liveness probe means the container will be restarted. In the case of a readiness probe the container will be marked Unready. Minimum value is `1`. | `30` |

## Remarks

The `az ml online-deployment` commands can be used for managing Azure Machine Learning managed online deployments.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online). Several are shown below.

## YAML: basic

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
