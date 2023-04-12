> You cannot delete a deployment that has allocated traffic. You must first [set traffic allocation](#update-deployment-traffic-allocation) for the deployment to 0% before deleting it.

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. In the left navigation bar, select the **Endpoints** page.
1. Select your managed online endpoint.
1. In the endpoint details page, find the deployment you want to delete.
1. Select the **delete icon**.

## Next steps

In this article, you learned how to use Azure Machine Learning managed online endpoints. See these next steps:

- [What are endpoints?](concept-endpoints.md)
- [How to deploy online endpoints with the Azure CLI](how-to-deploy-online-endpoints.md)
- [Deploy models with REST](how-to-deploy-with-rest.md)
- [How to monitor managed online endpoints](how-to-monitor-online-endpoints.md)
- [Troubleshooting managed online endpoints deployment and scoring](./how-to-troubleshoot-online-endpoints.md)
- [View costs for an Azure Machine Learning managed online endpoint](how-to-view-online-endpoints-costs.md)
- [Manage and increase quotas for resources with Azure Machine Learning](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints)
