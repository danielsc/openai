> With the previous extension (`azure-cli-ml`, sometimes called 'CLI v1'), only some of the commands communicate with the Azure Resource Manager. Specifically, commands that create, update, delete, list, or show Azure resources. Operations such as submitting a training job communicate directly with the Azure Machine Learning workspace. If your workspace is [secured with a private endpoint](how-to-configure-private-link.md), that is enough to secure commands provided by the `azure-cli-ml` extension.

# [Public workspace](#tab/public)

If your Azure Machine Learning workspace is public (that is, not behind a virtual network), then there is no additional configuration required. Communications are secured using HTTPS/TLS 1.2

# [Private workspace](#tab/private)

If your Azure Machine Learning workspace uses a private endpoint and virtual network, choose one of the following configurations to use:

* If you are __OK__ with the CLI v2 communication over the public internet, use the following `--public-network-access` parameter for the `az ml workspace update` command to enable public network access. For example, the following command updates a workspace for public network access:

    ```azurecli
    az ml workspace update --name myworkspace --public-network-access enabled
    ```

* If you are __not OK__ with the CLI v2 communication over the public internet, you can use an Azure Private Link to increase security of the communication. Use the following links to secure communications with Azure Resource Manager by using Azure Private Link.

    1. [Secure your Azure Machine Learning workspace inside a virtual network using a private endpoint](how-to-configure-private-link.md).
    2. [Create a Private Link for managing Azure resources](../azure-resource-manager/management/create-private-link-access-portal.md). 
    3. [Create a private endpoint](../azure-resource-manager/management/create-private-link-access-portal.md#create-private-endpoint) for the Private Link created in the previous step.

    > [!IMPORTANT]
    > To configure the private link for Azure Resource Manager, you must be the _subscription owner_ for the Azure subscription, and an _owner_ or _contributor_ of the root management group. For more information, see [Create a private link for managing Azure resources](../azure-resource-manager/management/create-private-link-access-portal.md).


## Next steps

- [Train models using CLI (v2)](how-to-train-model.md)
- [Set up the Visual Studio Code Azure Machine Learning extension](how-to-setup-vs-code.md)
- [Train an image classification TensorFlow model using the Azure Machine Learning Visual Studio Code extension](tutorial-train-deploy-image-classification-model-vscode.md)
- [Explore Azure Machine Learning with examples](samples-notebooks.md)
