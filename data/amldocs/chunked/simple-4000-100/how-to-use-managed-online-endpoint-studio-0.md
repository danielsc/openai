
# Create and use managed online endpoints in the studio

Learn how to use the studio to create and manage your managed online endpoints in Azure Machine Learning. Use managed online endpoints to streamline production-scale deployments. For more information on managed online endpoints, see [What are endpoints](concept-endpoints.md).

In this article, you learn how to:

> [!div class="checklist"]
> * Create a managed online endpoint
> * View managed online endpoints
> * Add a deployment to a managed online endpoint
> * Update managed online endpoints
> * Delete managed online endpoints and deployments

## Prerequisites
- An Azure Machine Learning workspace. For more information, see [Create workspace resources](quickstart-create-resources.md).
- The examples repository - Clone the [AzureML Example repository](https://github.com/Azure/azureml-examples). This article uses the assets in `/cli/endpoints/online`.

## Create a managed online endpoint

Use the studio to create a managed online endpoint directly in your browser. When you create a managed online endpoint in the studio, you must define an initial deployment. You can't create an empty managed online endpoint.

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. In the left navigation bar, select the **Endpoints** page.
1. Select **+ Create**.

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/endpoint-create-managed-online-endpoint.png" lightbox="media/how-to-create-managed-online-endpoint-studio/endpoint-create-managed-online-endpoint.png" alt-text="A screenshot for creating managed online endpoint from the Endpoints tab.":::

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/online-endpoint-wizard.png" lightbox="media/how-to-create-managed-online-endpoint-studio/online-endpoint-wizard.png" alt-text="A screenshot of a managed online endpoint create wizard.":::

### Register the model

A model registration is a logical entity in the workspace that may contain a single model file, or a directory containing multiple files. The steps in this article assume that you've registered the [model folder](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/model-1/model) that contains the model.

To register the example model using Azure Machine Learning studio, use the following steps:

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. In the left navigation bar, select the **Models** page.
1. Select **Register**, and then **From local files**.
1. Select __Unspecified type__ for the __Model type__, then select __Browse__, and __Browse folder__.

    :::image type="content" source="media/how-to-create-managed-online-endpoint-studio/register-model-folder.png" alt-text="A screenshot of the browse folder option.":::

1. Select the `\azureml-examples\cli\endpoints\online\model-1\model` folder from the local copy of the repo you downloaded earlier. When prompted, select __Upload__. Once the upload completes, select __Next__.
1. Enter a friendly __Name__ for the model. The steps in this article assume it's named `model-1`.
1. Select __Next__, and then __Register__ to complete registration.

For more information on working with registered models, see [Register and work with models](how-to-manage-models.md).

### Follow the setup wizard to configure your managed online endpoint.

You can also create a managed online endpoint from the **Models** page in the studio. This is an easy way to add a model to an existing managed online deployment.

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. In the left navigation bar, select the **Models** page.
1. Select a model by checking the circle next to the model name.
1. Select **Deploy** > **Deploy to real-time endpoint**.

    :::image type="content" source="media/how-to-create-managed-online-endpoint-studio/deploy-from-models-page.png" lightbox="media/how-to-create-managed-online-endpoint-studio/deploy-from-models-page.png" alt-text="A screenshot of creating a managed online endpoint from the Models UI.":::
