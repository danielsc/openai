  * If you go directly to your workspace from a share link from the SDK or the Azure portal, you can't view the standard **Overview** page that has subscription information in the extension. In this scenario, you also can't switch to another workspace. To view another workspace, go directly to [Azure Machine Learning studio](https://ml.azure.com) and search for the workspace name.
  * All assets (Data, Experiments, Computes, and so on) are available only in [Azure Machine Learning studio](https://ml.azure.com). They're *not* available from the Azure portal.
  * Attempting to export a template for a workspace from the Azure portal may return an error similar to the following text: `Could not get resource of the type <type>. Resources of this type will not be exported.` As a workaround, use one of the templates provided at [https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices) as the basis for your template.

### Workspace diagnostics

[!INCLUDE [machine-learning-workspace-diagnostics](../../includes/machine-learning-workspace-diagnostics.md)]

### Resource provider errors

[!INCLUDE [machine-learning-resource-provider](../../includes/machine-learning-resource-provider.md)]
 

### Deleting the Azure Container Registry

The Azure Machine Learning workspace uses Azure Container Registry (ACR) for some operations. It will automatically create an ACR instance when it first needs one.

[!INCLUDE [machine-learning-delete-acr](../../includes/machine-learning-delete-acr.md)]

## Examples

Examples in this article come from [workspace.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/resources/workspace/workspace.ipynb).

## Next steps

Once you have a workspace, learn how to [Train and deploy a model](tutorial-train-deploy-notebook.md).

To learn more about planning a workspace for your organization's requirements, see [Organize and set up Azure Machine Learning](/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-resource-organization).

* If you need to move a workspace to another Azure subscription, see [How to move a workspace](how-to-move-workspace.md).



For information on how to keep your Azure ML up to date with the latest security updates, see [Vulnerability management](concept-vulnerability-management.md).
