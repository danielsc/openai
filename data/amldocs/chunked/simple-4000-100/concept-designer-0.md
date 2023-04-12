
# What is Azure Machine Learning designer? 

Azure Machine Learning designer is a drag-and-drop interface used to train and deploy models in Azure Machine Learning. This article describes the tasks you can do in the designer.

 - To get started with the designer, see [Tutorial: Train a no-code regression model](tutorial-designer-automobile-price-train-score.md). 
 - To learn about the components available in the designer, see the [Algorithm and component reference](./algorithm-module-reference/module-reference.md).

![Azure Machine Learning designer example](./media/concept-designer/designer-drag-and-drop.gif)

The designer uses your Azure Machine Learning [workspace](concept-workspace.md) to organize shared resources such as:

+ [Pipelines](#pipeline)
+ [Data](#data)
+ [Compute resources](#compute)
+ [Registered models](v1/concept-azure-machine-learning-architecture.md#models)
+ [Published pipelines](#publish)
+ [Real-time endpoints](#deploy)

## Model training and deployment

Use a visual canvas to build an end-to-end machine learning workflow. Train, test, and deploy models all in the designer:

+ Drag-and-drop [data assets](#data) and [components](#component) onto the canvas.
+ Connect the components to create a [pipeline draft](#pipeline-draft).
+ Submit a [pipeline run](#pipeline-job) using the compute resources in your Azure Machine Learning workspace.
+ Convert your **training pipelines** to **inference pipelines**.
+ [Publish](#publish) your pipelines to a REST **pipeline endpoint** to submit a new pipeline that runs with different parameters and data assets.
    + Publish a **training pipeline** to reuse a single pipeline to train multiple models while changing parameters and data assets.
    + Publish a **batch inference pipeline** to make predictions on new data by using a previously trained model.
+ [Deploy](#deploy) a **real-time inference pipeline** to an online endpoint to make predictions on new data in real time.

![Workflow diagram for training, batch inference, and real-time inference in the designer](./media/concept-designer/designer-workflow-diagram.png)

## Pipeline

A [pipeline](v1/concept-azure-machine-learning-architecture.md#ml-pipelines) consists of data assets and analytical components, which you connect. Pipelines have many uses: you can make a pipeline that trains a single model, or one that trains multiple models. You can create a pipeline that makes predictions in real time or in batch, or make a pipeline that only cleans data. Pipelines let you reuse your work and organize your projects.

### Pipeline draft

As you edit a pipeline in the designer, your progress is saved as a **pipeline draft**. You can edit a pipeline draft at any point by adding or removing components, configuring compute targets, creating parameters, and so on.

A valid pipeline has these characteristics:

* Data assets can only connect to components.
* components can only connect to either data assets or other components.
* All input ports for components must have some connection to the data flow.
* All required parameters for each component must be set.

When you're ready to run your pipeline draft, you submit a pipeline job.

### Pipeline job

Each time you run a pipeline, the configuration of the pipeline and its results are stored in your workspace as a **pipeline job**. You can go back to any pipeline job to inspect it for troubleshooting or auditing. **Clone** a pipeline job to create a new pipeline draft for you to edit.

Pipeline jobs are grouped into [experiments](v1/concept-azure-machine-learning-architecture.md#experiments) to organize job history. You can set the experiment for every pipeline job. 

## Data

A machine learning data asset makes it easy to access and work with your data. Several [sample data assets](samples-designer.md#datasets) are included in the designer for you to experiment with. You can [register](how-to-create-register-datasets.md) more data assets as you need them.

## Component

A component is an algorithm that you can perform on your data. The designer has several components ranging from data ingress functions to training, scoring, and validation processes.
