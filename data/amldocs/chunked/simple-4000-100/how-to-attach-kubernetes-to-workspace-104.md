If you have user-assigned managed identity, select **Managed identity** to find the target identity.

You can use Managed Identity to pull images from Azure Container Registry. Grant the __AcrPull__ role to the compute Managed Identity. For more information, see [Azure Container Registry roles and permissions](../container-registry/container-registry-roles.md).

You can use a managed identity to access Azure Blob:
- For read-only purpose, __Storage Blob Data Reader__ role should be granted to the compute managed identity.
- For read-write purpose, __Storage Blob Data Contributor__ role should be granted to the compute managed identity.

## Next steps

- [Create and manage instance types](./how-to-manage-kubernetes-instance-types.md)
- [AzureML inference router and connectivity requirements](./how-to-kubernetes-inference-routing-azureml-fe.md)
- [Secure AKS inferencing environment](./how-to-secure-kubernetes-inferencing-environment.md)