1. Navigate to [Azure Machine Learning studio](https://ml.azure.com).
1. Under **Manage**, select **Compute**.
1. Select the **Kubernetes clusters** tab.
1. Select **+New > Kubernetes**

   :::image type="content" source="media/how-to-attach-arc-kubernetes/kubernetes-attach.png" alt-text="Screenshot of settings for Kubernetes cluster to make available in your workspace.":::

1. Enter a compute name and select your Kubernetes cluster from the dropdown.

    * **(Optional)** Enter Kubernetes namespace, which defaults to `default`. All machine learning workloads will be sent to the specified Kubernetes namespace in the cluster. Compute attach won't create the Kubernetes namespace automatically or validate whether the kubernetes namespace exists. You need to verify that the specified namespace exists in your cluster, otherwise, any AzureML workloads submitted to this compute will fail.  

    * **(Optional)** Assign system-assigned or user-assigned managed identity. Managed identities eliminate the need for developers to manage credentials. For more information, see the [Assign managed identity](#assign-managed-identity-to-the-compute-target) section of this article.

    :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/configure-kubernetes-cluster-2.png" alt-text="Screenshot of settings for developer configuration of Kubernetes cluster.":::

1. Select **Attach**

    In the Kubernetes clusters tab, the initial state of your cluster is *Creating*. When the cluster is successfully attached, the state changes to *Succeeded*. Otherwise, the state changes to *Failed*.

    :::image type="content" source="media/how-to-attach-arc-kubernetes/kubernetes-creating.png" alt-text="Screenshot of attached settings for configuration of Kubernetes cluster.":::
   

## Assign managed identity to the compute target

A common challenge for developers is the management of secrets and credentials used to secure communication between different components of a solution. [Managed identities](../active-directory/managed-identities-azure-resources/overview.md) eliminate the need for developers to manage credentials.

To access Azure Container Registry (ACR) for a Docker image, and a Storage Account for training data, attach Kubernetes compute with a system-assigned or user-assigned managed identity enabled.

### Assign managed identity
- You can assign a managed identity to the compute in the compute attach step.
- If the compute has already been attached, you can update the settings to use a managed identity in Azure Machine Learning studio.
    - Go to [Azure Machine Learning studio](https://ml.azure.com). Select __Compute__, __Attached compute__, and select your attached compute.
    - Select the pencil icon to edit managed identity.

    :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/edit-identity.png" alt-text="Screenshot of updating identity of the Kubernetes compute from Azure portal.":::
    
    :::image type="content" source="media/how-to-attach-kubernetes-to-workspace/update-identity-2.png" alt-text="Screenshot of selecting identity of the Kubernetes compute from Azure portal.":::
     


### Assign Azure roles to managed identity
Azure offers a couple of ways to assign roles to a managed identity.
- [Use Azure portal to assign roles](../role-based-access-control/role-assignments-portal.md)
- [Use Azure CLI to assign roles](../role-based-access-control/role-assignments-cli.md)
- [Use Azure PowerShell to assign roles](../role-based-access-control/role-assignments-powershell.md)

If you are using the Azure portal to assign roles and have a **system-assigned managed identity**, **Select User**, **Group Principal** or **Service Principal**, you can search for the identity name by selecting **Select members**. The identity name needs to be formatted as: `<workspace name>/computes/<compute target name>`.

If you have user-assigned managed identity, select **Managed identity** to find the target identity.
