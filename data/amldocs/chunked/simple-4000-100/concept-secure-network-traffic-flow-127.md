__Outbound__ communication from a deployment can be secured on a per-deployment basis by using the `egress_public_network_access` flag. Outbound communication in this case is from the deployment to Azure Container Registry, storage blob, and workspace. Setting the flag to `true` will restrict communication with these resources to the virtual network.

> [!NOTE]
> For secure outbound communication, a private endpoint is created for each deployment where `egress_public_network_access` is set to `disabled`.

Visibility of the endpoint is also governed by the `public_network_access` flag of the Azure Machine Learning workspace. If this flag is `disabled`, then the scoring endpoints can only be accessed from virtual networks that contain a private endpoint for the workspace. If it is `enabled`, then the scoring endpoint can be accessed from the virtual network and public networks.

### Supported configurations

| Configuration | Inbound </br> (Endpoint property) | Outbound </br> (Deployment property) | Supported? |
| -------- | -------------------------------- | --------------------------------- | --------- |
| secure inbound with secure outbound | `public_network_access` is disabled | `egress_public_network_access` is disabled   | Yes |
| secure inbound with public outbound | `public_network_access` is disabled | `egress_public_network_access` is enabled  | Yes |
| public inbound with secure outbound | `public_network_access` is enabled | `egress_public_network_access` is disabled    | Yes |
| public inbound with public outbound | `public_network_access` is enabled | `egress_public_network_access` is enabled  | Yes |

## Scenario: Use Azure Kubernetes Service

For information on the outbound configuration required for Azure Kubernetes Service, see the connectivity requirements section of [How to secure inference](how-to-secure-inferencing-vnet.md).

> [!NOTE]
> The Azure Kubernetes Service load balancer is not the same as the load balancer created by Azure Machine Learning. If you want to host your model as a secured application, only available on the VNet, use the internal load balancer created by Azure Machine Learning. If you want to allow public access, use the public load balancer created by Azure Machine Learning.

If your model requires extra inbound or outbound connectivity, such as to an external data source, use a network security group or your firewall to allow the traffic.

## Scenario: Use Docker images managed by Azure ML

Azure Machine Learning provides Docker images that can be used to train models or perform inference. If you don't specify your own images, the ones provided by Azure Machine Learning are used. These images are hosted on the Microsoft Container Registry (MCR). They're also hosted on a geo-replicated Azure Container Registry named `viennaglobal.azurecr.io`.

If you provide your own docker images, such as on an Azure Container Registry that you provide, you don't need the outbound communication with MCR or `viennaglobal.azurecr.io`.

> [!TIP]
> If your Azure Container Registry is secured in the VNet, it cannot be used by Azure Machine Learning to build Docker images. Instead, you must designate an Azure Machine Learning compute cluster to build images. For more information, see [How to secure a workspace in a virtual network](how-to-secure-workspace-vnet.md#enable-azure-container-registry-acr).

:::image type="content" source="./media/concept-secure-network-traffic-flow/azure-machine-learning-docker-images.png" alt-text="Diagram of traffic flow when using provided Docker images":::
## Next steps

Now that you've learned how network traffic flows in a secured configuration, learn more about securing Azure ML in a virtual network by reading the [Virtual network isolation and privacy overview](how-to-network-security-overview.md) article.

For information on best practices, see the [Azure Machine Learning best practices for enterprise security](/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-enterprise-security) article.
