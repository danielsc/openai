
# Tutorial: Designer - train a no-code regression model

Train a linear regression model that predicts car prices using the Azure Machine Learning designer. This tutorial is part one of a two-part series.

This tutorial uses the Azure Machine Learning designer, for more information, see [What is Azure Machine Learning designer?](concept-designer.md)

In part one of the tutorial, you learn how to:

> [!div class="checklist"]
> * Create a new pipeline.
> * Import data.
> * Prepare data.
> * Train a machine learning model.
> * Evaluate a machine learning model.

In [part two](tutorial-designer-automobile-price-deploy.md) of the tutorial, you deploy your model as a real-time inferencing endpoint to predict the price of any car based on technical specifications you send it. 

> [!NOTE]
>A completed version of this tutorial is available as a sample pipeline.
>
>To find it, go to the designer in your workspace. In the **New pipeline** section, select **Sample 1 - Regression: Automobile Price Prediction(Basic)**.

[!INCLUDE [machine-learning-missing-ui](../../includes/machine-learning-missing-ui.md)]

## Create a new pipeline

Azure Machine Learning pipelines organize multiple machine learning and data processing steps into a single resource. Pipelines let you organize, manage, and reuse complex machine learning workflows across projects and users.

To create an Azure Machine Learning pipeline, you need an Azure Machine Learning workspace. In this section, you learn how to create both these resources.

### Create a new workspace

You need an Azure Machine Learning workspace to use the designer. The workspace is the top-level resource for Azure Machine Learning, it provides a centralized place to work with all the artifacts you create in Azure Machine Learning. For instruction on creating a workspace, see [Create workspace resources](quickstart-create-resources.md).

> [!NOTE]
> If your workspace uses a Virtual network, there are additional configuration steps you must use to use the designer. For more information, see [Use Azure Machine Learning studio in an Azure virtual network](how-to-enable-studio-virtual-network.md)

### Create the pipeline

>[!Note]
> Designer supports two type of components, classic prebuilt components and custom components. These two types of components are not compatible.  
>
>Classic prebuilt components provides prebuilt components majorly for data processing and traditional machine learning tasks like regression and classification. This type of component continues to be supported but will not have any new components added.
>
>
>Custom components allow you to provide your own code as a component. It supports sharing across workspaces and seamless authoring across Studio, CLI, and SDK interfaces.
>
>This article applies to classic prebuilt components. 

1. Sign in to <a href="https://ml.azure.com?tabs=jre" target="_blank">ml.azure.com</a>, and select the workspace you want to work with.

1. Select **Designer** -> **Classic prebuilt**

    :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/launch-designer.png" alt-text="Screenshot of the visual workspace showing how to access the designer.":::

1. Select **Create a new pipeline using classic prebuilt components**.

1. Click the pencil icon beside the automatically generated pipeline draft name, rename it to *Automobile price prediction*. The name doesn't need to be unique.

![Screenshot of pencil icon to change pipeline draft name.](./media/tutorial-designer-automobile-price-train-score/change-pipeline-draft-name.png) 


## Set the default compute target

A pipeline jobs on a compute target, which is a compute resource that's attached to your workspace. After you create a compute target, you can reuse it for future jobs.


> [!Important]
> Attached compute is not supported, use [compute instances or clusters](concept-compute-target.md#azure-machine-learning-compute-managed) instead.

You can set a **Default compute target** for the entire pipeline, which will tell every component to use the same compute target by default. However, you can specify compute targets on a per-module basis.
