> A request can bypass the configured traffic load balancing by including an HTTP header of `azureml-model-deployment`. Set the header value to the name of the deployment you want the request to route to.

:::image type="content" source="media/concept-endpoints/traffic-allocation.png" alt-text="Screenshot showing slider interface to set traffic allocation between deployments.":::

:::image type="content" source="media/concept-endpoints/endpoint-concept.png" alt-text="Diagram showing an endpoint splitting traffic to two deployments.":::

Traffic to one deployment can also be mirrored (or copied) to another deployment. Mirroring traffic (also called shadowing) is useful when you want to test for things like response latency or error conditions without impacting live clients; for example, when implementing a blue/green deployment where 100% of the traffic is routed to blue and 10% is mirrored to the green deployment. With mirroring, the results of the traffic to the green deployment aren't returned to the clients but metrics and logs are collected. Testing the new deployment with traffic mirroring/shadowing is also known as [shadow testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/shadow-testing/), and the functionality is currently a __preview__ feature.

:::image type="content" source="media/concept-endpoints/endpoint-concept-mirror.png" alt-text="Diagram showing an endpoint mirroring traffic to a deployment.":::

Learn how to [safely rollout to online endpoints](how-to-safely-rollout-online-endpoints.md).

### Application Insights integration

All online endpoints integrate with Application Insights to monitor SLAs and diagnose issues. 

However [managed online endpoints](#managed-online-endpoints-vs-kubernetes-online-endpoints) also include out-of-box integration with Azure Logs and Azure Metrics.

### Security

- Authentication: Key and Azure ML Tokens
- Managed identity: User assigned and system assigned
- SSL by default for endpoint invocation

### Autoscaling

Autoscale automatically runs the right amount of resources to handle the load on your application. Managed endpoints support autoscaling through integration with the [Azure monitor autoscale](../azure-monitor/autoscale/autoscale-overview.md) feature. You can configure metrics-based scaling (for instance, CPU utilization >70%), schedule-based scaling (for example, scaling rules for peak business hours), or a combination.

:::image type="content" source="media/concept-endpoints/concept-autoscale.png" alt-text="Screenshot showing that autoscale flexibly provides between min and max instances, depending on rules.":::

### Visual Studio Code debugging

Visual Studio Code enables you to interactively debug endpoints.

:::image type="content" source="media/concept-endpoints/visual-studio-code-full.png" alt-text="Screenshot of endpoint debugging in VSCode." lightbox="media/concept-endpoints/visual-studio-code-full.png" :::

### Private endpoint support

Optionally, you can secure communication with a managed online endpoint by using private endpoints.

You can configure security for inbound scoring requests and outbound communications with the workspace and other services separately. Inbound communications use the private endpoint of the Azure Machine Learning workspace. Outbound communications use private endpoints created per deployment.

For more information, see [Secure online endpoints](how-to-secure-online-endpoint.md).

## Managed online endpoints vs Kubernetes online endpoints

There are two types of online endpoints: **managed online endpoints** and **Kubernetes online endpoints**. 

Managed online endpoints help to deploy your ML models in a turnkey manner. Managed online endpoints work with powerful CPU and GPU machines in Azure in a scalable, fully managed way. Managed online endpoints take care of serving, scaling, securing, and monitoring your models, freeing you from the overhead of setting up and managing the underlying infrastructure. The main example in this doc uses managed online endpoints for deployment. 
