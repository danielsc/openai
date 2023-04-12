| `instance_count` | integer | The number of instances to use for the deployment. Specify the value based on the workload you expect. This field is only required if you're using the `default` scale type (`scale_settings.type: default`). <br><br> `instance_count` can be updated after deployment creation using `az ml online-deployment update` command. | | |
| `app_insights_enabled` | boolean | Whether to enable integration with the Azure Application Insights instance associated with your workspace. | | `false` |
| `scale_settings` | object | The scale settings for the deployment. The two types of scale settings supported are the `default` scale type and the `target_utilization` scale type. <br><br> With the `default` scale type (`scale_settings.type: default`), you can manually scale the instance count up and down after deployment creation by updating the `instance_count` property. <br><br> To configure the `target_utilization` scale type (`scale_settings.type: target_utilization`), see [TargetUtilizationScaleSettings](#targetutilizationscalesettings) for the set of configurable properties. | | |
| `scale_settings.type` | string | The scale type. | `default`, `target_utilization` | `target_utilization` |
| `request_settings` | object | Scoring request settings for the deployment. See [RequestSettings](#requestsettings) for the set of configurable properties. | | |
| `liveness_probe` | object | Liveness probe settings for monitoring the health of the container regularly. See [ProbeSettings](#probesettings) for the set of configurable properties. | | |
| `readiness_probe` | object | Readiness probe settings for validating if the container is ready to serve traffic. See [ProbeSettings](#probesettings) for the set of configurable properties. | | |
| `resources` | object | Container resource requirements. | | |
| `resources.requests` | object | Resource requests for the container. See [ContainerResourceRequests](#containerresourcerequests) for the set of configurable properties. | | |
| `resources.limits` | object | Resource limits for the container. See [ContainerResourceLimits](#containerresourcelimits) for the set of configurable properties. | | |

### RequestSettings

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `request_timeout_ms` | integer | The scoring timeout in milliseconds. | `5000` |
| `max_concurrent_requests_per_instance` | integer | The maximum number of concurrent requests per instance allowed for the deployment. <br><br> **Do not change this setting from the default value unless instructed by Microsoft Technical Support or a member of the Azure ML team.** | `1` |
| `max_queue_wait_ms` | integer | The maximum amount of time in milliseconds a request will stay in the queue. | `500` |

### ProbeSettings

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `period` | integer | How often (in seconds) to perform the probe. | `10` |
| `initial_delay` | integer | The number of seconds after the container has started before the probe is initiated. Minimum value is `1`. | `10` |
| `timeout` | integer | The number of seconds after which the probe times out. Minimum value is `1`. | `2` |
| `success_threshold` | integer | The minimum consecutive successes for the probe to be considered successful after having failed. Minimum value is `1`. | `1` |
| `failure_threshold` | integer | When a probe fails, the system will try `failure_threshold` times before giving up. Giving up in the case of a liveness probe means the container will be restarted. In the case of a readiness probe the container will be marked Unready. Minimum value is `1`. | `30` |

### TargetUtilizationScaleSettings

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `type` | const | The scale type | `target_utilization` |
| `min_instances` | integer | The minimum number of instances to use. | `1` |
| `max_instances` | integer | The maximum number of instances to scale to. | `1` |
