
# Use pipeline parameters to retrain models in the designer


In this how-to article, you learn how to use Azure Machine Learning designer to retrain a machine learning model using pipeline parameters. You will use published pipelines to automate your workflow and set parameters to train your model on new data. Pipeline parameters let you re-use existing pipelines for different jobs.  

In this article, you learn how to:

> [!div class="checklist"]
> * Train a machine learning model.
> * Create a pipeline parameter.
> * Publish your training pipeline.
> * Retrain your model with new parameters.

## Prerequisites

* An Azure Machine Learning workspace
* Complete part 1 of this how-to series, [Transform data in the designer](how-to-designer-transform-data.md)

[!INCLUDE [machine-learning-missing-ui](../../includes/machine-learning-missing-ui.md)]

This article also assumes that you have some knowledge of building pipelines in the designer. For a guided introduction, complete the [tutorial](tutorial-designer-automobile-price-train-score.md). 

### Sample pipeline

The pipeline used in this article is an altered version of a sample pipeline [Income prediction](samples-designer.md#classification) in the designer homepage. The pipeline uses the [Import Data](algorithm-module-reference/import-data.md) component instead of the sample dataset to show you how to train models using your own data.

![Screenshot that shows the modified sample pipeline with a box highlighting the Import Data component](./media/how-to-retrain-designer/modified-sample-pipeline.png)

## Create a pipeline parameter

Pipeline parameters are used to build versatile pipelines which can be resubmitted later with varying parameter values. Some common scenarios are updating datasets or some hyper-parameters for retraining. Create pipeline parameters to dynamically set variables at runtime. 

Pipeline parameters can be added to data source or component parameters in a pipeline. When the pipeline is resubmitted, the values of these parameters can be specified.

For this example, you will change the training data path from a fixed value to a parameter, so that you can retrain your model on different data. You can also add other component parameters as pipeline parameters according to your use case.

1. Select the **Import Data** component.

    > [!NOTE]
    > This example uses the Import Data component to access data in a registered datastore. However, you can follow similar steps if you use alternative data access patterns.

1. In the component detail pane, to the right of the canvas, select your data source.

1. Enter the path to your data. You can also select **Browse path** to browse your file tree. 

1. Mouseover the **Path** field, and select the ellipses above the **Path** field that appear.

1. Select **Add to pipeline parameter**.

1. Provide a parameter name and a default value.

   ![Screenshot that shows how to create a pipeline parameter](media/how-to-retrain-designer/add-pipeline-parameter.png)

1. Select **Save**.

   > [!NOTE]
   > You can also detach a component parameter from pipeline parameter in the component detail pane, similar to adding pipeline parameters.
   >
   > You can inspect and edit your pipeline parameters by selecting the **Settings** gear icon next to the title of your pipeline draft. 
   >    - After detaching, you can delete the pipeline parameter in the **Setings** pane.
   >    - You can also add a pipeline parameter in the **Settings** pane, and then apply it on some component parameter.

1. Submit the pipeline job.

## Publish a training pipeline

Publish a pipeline to a pipeline endpoint to easily reuse your pipelines in the future. A pipeline endpoint creates a REST endpoint to invoke pipeline in the future. In this example, your pipeline endpoint lets you reuse your pipeline to retrain a model on different data.

1. Select **Publish** above the designer canvas.
1. Select or create a pipeline endpoint.

   > [!NOTE]
   > You can publish multiple pipelines to a single endpoint. Each pipeline in a given endpoint is given a version number, which you can specify when you call the pipeline endpoint.
