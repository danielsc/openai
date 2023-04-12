The UI experience to deploy extension is only available for **[Arc Kubernetes](../azure-arc/kubernetes/overview.md)**. If you have an AKS cluster without Azure Arc connection, you need to use CLI to deploy AzureML extension.

1. In the [Azure portal](https://portal.azure.com/#home), navigate to **Kubernetes - Azure Arc** and select your cluster.
1. Select **Extensions** (under **Settings**), and then select **+ Add**.

   :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/deploy-extension-from-ui.png" alt-text="Screenshot of adding new extension to the Arc-enabled Kubernetes cluster from Azure portal.":::

1. From the list of available extensions, select **Azure Machine Learning extension** to deploy the latest version of the extension.

   :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/deploy-extension-from-ui-extension-list.png" alt-text="Screenshot of selecting AzureML extension from Azure portal.":::

1. Follow the prompts to deploy the extension. You can customize the installation by configuring the installation in the tab of **Basics**, **Configurations** and **Advanced**.  For a detailed list of AzureML extension configuration settings, see [AzureML extension configuration settings](#review-azureml-extension-configuration-settings).

   :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/deploy-extension-from-ui-settings.png" alt-text="Screenshot of configuring AzureML extension settings from Azure portal.":::
1. On the **Review + create** tab, select **Create**.
   
   :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/deploy-extension-from-ui-create.png" alt-text="Screenshot of deploying new extension to the Arc-enabled Kubernetes cluster from Azure portal.":::

1. After the deployment completes, you're able to see the AzureML extension in **Extension** page.  If the extension installation succeeds, you can see **Installed** for the **Install status**.

   :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/deploy-extension-from-ui-extension-detail.png" alt-text="Screenshot of installed AzureML extensions listing in Azure portal.":::


### Verify AzureML extension deployment

1. Run the following CLI command to check AzureML extension details:

   ```azurecli
   az k8s-extension show --name <extension-name> --cluster-type connectedClusters --cluster-name <your-connected-cluster-name> --resource-group <resource-group>
   ```

1. In the response, look for "name" and "provisioningState": "Succeeded". Note it might show "provisioningState": "Pending" for the first few minutes.

1. If the provisioningState shows Succeeded, run the following command on your machine with the kubeconfig file pointed to your cluster to check that all pods under "azureml" namespace are in 'Running' state:

   ```bash
    kubectl get pods -n azureml
   ```

## Review AzureML extension component

Upon AzureML extension deployment completes, you can use `kubectl get deployments -n azureml` to see list of resources created in the cluster. It usually consists a subset of following resources per configuration settings specified. 

   |Resource name  |Resource type |Training |Inference |Training and Inference| Description | Communication with cloud|
   |--|--|--|--|--|--|--|
   |relayserver|Kubernetes deployment|**&check;**|**&check;**|**&check;**|Relay server is only created for Arc Kubernetes cluster, and **not** in AKS cluster. Relay server works with Azure Relay to communicate with the cloud services.|Receive the request of job creation, model deployment from cloud service; sync the job status with cloud service.|
   |gateway|Kubernetes deployment|**&check;**|**&check;**|**&check;**|The gateway is used to communicate and send data back and forth.|Send nodes and cluster resource information to cloud services.|
   |aml-operator|Kubernetes deployment|**&check;**|N/A|**&check;**|Manage the lifecycle of training jobs.| Token exchange with the cloud token service for authentication and authorization of Azure Container Registry.|
