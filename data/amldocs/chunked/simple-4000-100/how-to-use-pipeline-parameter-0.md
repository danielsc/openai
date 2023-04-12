
# Use pipeline parameters in the designer to build versatile pipelines

Use pipeline parameters to build flexible pipelines in the designer. Pipeline parameters let you dynamically set values at runtime to encapsulate pipeline logic and reuse assets.

Pipeline parameters are especially useful when resubmitting a pipeline job, [retraining models](how-to-retrain-designer.md), or [performing batch predictions](how-to-run-batch-predictions-designer.md).

In this article, you learn how to do the following:

> [!div class="checklist"]
> * Create pipeline parameters
> * Delete and manage pipeline parameters
> * Trigger pipeline jobs while adjusting pipeline parameters

## Prerequisites

* An Azure Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md).

* For a guided introduction to the designer, complete the [designer tutorial](tutorial-designer-automobile-price-train-score.md). 

[!INCLUDE [machine-learning-missing-ui](../../includes/machine-learning-missing-ui.md)]

## Create pipeline parameter

There are three ways to create a pipeline parameter in the designer:
- Create a pipeline parameter in the settings panel, and bind it to a component.
- Promote a component parameter to a pipeline parameter.
- Promote a dataset to a pipeline parameter

> [!NOTE]
> Pipeline parameters only support basic data types like `int`, `float`, and `string`.

### Option 1: Create a pipeline parameter in the settings panel

In this section, you create a pipeline parameter in the settings panel.

In this example, you create a pipeline parameter that defines how a pipeline fills in missing data using the **Clean missing data** component.

1. Next to the name of your pipeline draft, select the **gear icon** to open the **Settings** panel.

1. In the **Pipeline parameters** section, select the **+** icon.

1.  Enter a name for the parameter and a default value. 

    For example, enter `replace-missing-value` as parameter name and `0` as default value.

   ![Screenshot that shows how to create a pipeline parameter](media/how-to-use-pipeline-parameter/create-pipeline-parameter.png)


After you create a pipeline parameter, you must [attach it to the component parameter](#attach-component-parameter-to-pipeline-parameter) that you want to dynamically set.

### Option 2: Promote a component parameter

The simplest way to create a pipeline parameter for a component value is to promote a component parameter. Use the following steps to promote a component parameter to a pipeline parameter:

1. Select the component you want to attach a pipeline parameter to.
1. In the component detail pane, mouseover the parameter you want to specify.
1. Select the ellipses (**...**) that appear.
1. Select **Add to pipeline parameter**.

    ![Screenshot that shows how to promote component parameter to pipeline parameter1](media/how-to-use-pipeline-parameter/promote-module-para-to-pipeline-para.png)

1. Enter a parameter name and default value.
1. Select **Save**

You can now specify new values for this parameter anytime you submit this pipeline.

### Option 3: Promote a dataset to a pipeline parameter

If you want to submit your pipeline with variable datasets, you must promote your dataset to a pipeline parameter:

1. Select the dataset you want to turn into a pipeline parameter.

1. In the detail panel of dataset, check **Set as pipeline parameter**.

   ![Screenshot that shows how to set dataset as pipeline parameter](media/how-to-use-pipeline-parameter/set-dataset-as-pipeline-parameter.png)

You can now specify a different dataset by using the pipeline parameter the next time you run the pipeline.

## Attach and detach component parameter to pipeline parameter 

In this section, you will learn how to attach and detach component parameter to pipeline parameter.

### Attach component parameter to pipeline parameter

You can attach the same component parameters of duplicated components to the same pipeline parameter if you want to alter the value at one time when triggering the pipeline job.
