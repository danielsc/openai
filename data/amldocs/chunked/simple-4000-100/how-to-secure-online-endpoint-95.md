    :::image type="content" source="media/how-to-secure-online-endpoint/endpoint-disable-public-network-access.png" alt-text="A screenshot of how to disable public network access for an endpoint." lightbox="media/how-to-secure-online-endpoint/endpoint-disable-public-network-access.png":::


When `public_network_access` is `Disabled`, inbound scoring requests are received using the [private endpoint of the Azure Machine Learning workspace](./how-to-configure-private-link.md), and the endpoint can't be reached from public networks.

> [!NOTE]
> You can update (enable or disable) the `public_network_access` flag of an online endpoint after creating it.

## Outbound (resource access)

To restrict communication between a deployment and external resources, including the Azure resources it uses, set the deployment's `egress_public_network_access` flag to `disabled`. Use this flag to ensure that the download of the model, code, and images needed by your deployment are secured with a private endpoint. Note that disabling the flag alone is not enough — your workspace must also have a private link that allows access to Azure resources via a private endpoint. See the [Prerequisites](#prerequisites) for more details.

> [!WARNING]
> You cannot update (enable or disable) the `egress_public_network_access` flag after creating the deployment. Attempting to change the flag while updating the deployment will fail with an error.

> [!NOTE]
> For online deployments with `egress_public_network_access` flag set to `disabled`, access from the deployments to Microsoft Container Registry (MCR) is restricted. If you want to leverage container images from MCR (such as when using curated environment or mlflow no-code deployment), recommendation is to push the images into the Azure Container Registry (ACR) which is attached with the workspace. The images in this ACR is accessible to secured deployments via the private endpoints which are automatically created on behalf of you when you set `egress_public_network_access` flag to `disabled`. For a quick example, please refer to this [custom container example](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/custom-container/minimal/single-model).

# [Azure CLI](#tab/cli)

```azurecli
az ml online-deployment create -f deployment.yml --set egress_public_network_access=disabled
```

# [Python](#tab/python)

```python
blue_deployment = ManagedOnlineDeployment(name='blue', 
                                          endpoint_name='my-online-endpoint', 
                                          model=model, 
                                          code_configuration=CodeConfiguration(code_local_path='./model-1/onlinescoring/',
                                                                               scoring_script='score.py'),
                                          environment=env, 
                                          instance_type='Standard_DS2_v2', 
                                          instance_count=1, 
                                          egress_public_network_access="disabled"
                                          # egress_public_network_access="enabled" 
) 
                              
ml_client.begin_create_or_update(blue_deployment) 
```

# [Studio](#tab/azure-studio)

1. Follow the steps in the **Create deployment** setup wizard to the **Deployment** step.
1. Disable the **Egress public network access** flag.

    :::image type="content" source="media/how-to-secure-online-endpoint/deployment-disable-egress-public-network-access.png" alt-text="A screenshot of how to disable the egress public network access for a deployment." lightbox="media/how-to-secure-online-endpoint/deployment-disable-egress-public-network-access.png":::


The deployment communicates with these resources over the private endpoint:

* The Azure Machine Learning workspace
* The Azure Storage blob that is the default storage for the workspace
* The Azure Container Registry for the workspace
