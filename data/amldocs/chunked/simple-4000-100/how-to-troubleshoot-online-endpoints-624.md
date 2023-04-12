Kubernetes online deployments support autoscaling, which allows replicas to be added to support extra load, more information you can find in [AzureML inference router](how-to-kubernetes-inference-routing-azureml-fe.md). Decisions to scale up/down is based off of utilization of the current container replicas.

There are two things that can help prevent 503 status codes:
> [!TIP]
> These two approaches can be used individually or in combination.

* Change the utilization level at which autoscaling creates new replicas. You can adjust the utilization target by setting the `autoscale_target_utilization` to a lower value.

    > [!IMPORTANT]
    > This change does not cause replicas to be created *faster*. Instead, they are created at a lower utilization threshold. Instead of waiting until the service is 70% utilized, changing the value to 30% causes replicas to be created when 30% utilization occurs.
    
    If the Kubernetes online endpoint is already using the current max replicas and you're still seeing 503 status codes, increase the `autoscale_max_replicas` value to increase the maximum number of replicas.

* Change the minimum number of replicas. Increasing the minimum replicas provides a larger pool to handle the incoming spikes.

    To increase the number of instances, you could calculate the required replicas following below code.

    ```python
    from math import ceil
    # target requests per second
    target_rps = 20
    # time to process the request (in seconds, choose appropriate percentile)
    request_process_time = 10
    # Maximum concurrent requests per instance
    max_concurrent_requests_per_instance = 1
    # The target CPU usage of the model container. 70% in this example
    target_utilization = .7
    
    concurrent_requests = target_rps * request_process_time / target_utilization
    
    # Number of instance count
    instance_count = ceil(concurrent_requests / max_concurrent_requests_per_instance)
    ```

    > [!NOTE]
    > If you receive request spikes larger than the new minimum replicas can handle, you may receive 503 again. For example, as traffic to your endpoint increases, you may need to increase the minimum replicas.

#### How to calculate instance count
To increase the number of instances, you can calculate the required replicas by using the following code:
```python
from math import ceil
# target requests per second
target_rps = 20
# time to process the request (in seconds, choose appropriate percentile)
request_process_time = 10
# Maximum concurrent requests per instance
max_concurrent_requests_per_instance = 1
# The target CPU usage of the model container. 70% in this example
target_utilization = .7

concurrent_requests = target_rps * request_process_time / target_utilization

# Number of instance count
instance_count = ceil(concurrent_requests / max_concurrent_requests_per_instance)
```

### Blocked by CORS policy

Online endpoints (v2) currently do not support [Cross-Origin Resource Sharing](https://developer.mozilla.org/docs/Web/HTTP/CORS) (CORS) natively. If your web application tries to invoke the endpoint without proper handling of the CORS preflight requests, you'll see the following error message: 

```
Access to fetch at 'https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score' from origin http://{your-url} has been blocked by CORS policy: Response to preflight request doesn't pass access control check. No 'Access-control-allow-origin' header is present on the request resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with the CORS disabled.
```
We recommend that you use Azure Functions, Azure Application Gateway, or any service as an interim layer to handle CORS preflight requests.

## Common network isolation issues

[!INCLUDE [network isolation issues](../../includes/machine-learning-online-endpoint-troubleshooting.md)]

## Troubleshoot inference server
In this section, we'll provide basic troubleshooting tips for [Azure Machine Learning inference HTTP server](how-to-inference-server-http.md). 
