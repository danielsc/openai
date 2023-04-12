
# Create and run machine learning pipelines using components with the Azure Machine Learning studio

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

In this article, you'll learn how to create and run [machine learning pipelines](concept-ml-pipelines.md) by using the Azure Machine Learning studio and [Components](concept-component.md). You can create pipelines without using components, but components offer better amount of flexibility and reuse. Azure ML Pipelines may be defined in YAML and [run from the CLI](how-to-create-component-pipelines-cli.md), [authored in Python](how-to-create-component-pipeline-python.md), or composed in Azure ML Studio Designer with a drag-and-drop UI. This document focuses on the AzureML studio designer UI.

## Prerequisites

* If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

* An Azure Machine Learning workspace[Create workspace resources](quickstart-create-resources.md).

* [Install and set up the Azure CLI extension for Machine Learning](how-to-configure-cli.md).

* Clone the examples repository:

    ```azurecli-interactive
    git clone https://github.com/Azure/azureml-examples --depth 1
    cd azureml-examples/cli/jobs/pipelines-with-components/
    ```

## Register component in your workspace

>[!Note]
> Designer supports two type of components, classic prebuilt components and custom components. These two types of components are not compatible.  
>
>Classic prebuilt components provides prebuilt components majorly for data processing and traditional machine learning tasks like regression and classification. This type of component continues to be supported but will not have any new components added.
>
>
>Custom components allow you to provide your own code as a component. It supports sharing across workspaces and seamless authoring across Studio, CLI, and SDK interfaces.
>
>This article applies to custom components. 

To build pipeline using components in UI, you need to register components to your workspace first. You can use CLI or SDK to register components to your workspace, so that you can share and reuse the component within the workspace. Registered components support automatic versioning so you can update the component but assure that pipelines that require an older version will continue to work.  

In the example below take using CLI for example. If you want to learn more about how to build a component, see [Create and run pipelines using components with  CLI](how-to-create-component-pipelines-cli.md).

1. From the `cli/jobs/pipelines-with-components/basics` directory of the [`azureml-examples` repository](https://github.com/Azure/azureml-examples), navigate to the `1b_e2e_registered_components` subdirectory.

1. Register the components to AzureML workspace using following commands. Learn more about [ML components](concept-component.md).

    ```CLI
    az ml component create --file train.yml
    az ml component create --file score.yml
    az ml component create --file eval.yml
    ```

1. After register component successfully, you can see your component in the studio UI.

:::image type="content" source="./media/how-to-create-component-pipelines-ui/component-page.png" alt-text="Screenshot showing registered component in component page." lightbox ="./media/how-to-create-component-pipelines-ui/component-page.png":::

## Create pipeline using registered component

1. Create a new pipeline in the designer.

    :::image type="content" source="./media/how-to-create-component-pipelines-ui/new-pipeline.png" alt-text="Screenshot showing creating new pipeline in designer homepage." lightbox ="./media/how-to-create-component-pipelines-ui/new-pipeline.png":::

1. Set the default compute target of the pipeline. 

    Select the **Gear icon** ![Screenshot of the gear icon that is in the UI.](./media/tutorial-designer-automobile-price-train-score/gear-icon.png) at the top right of the canvas to open the **Settings** pane. Select the default compute target for your pipeline.
