    ![Screenshot showing how to connect the Export Data components](media/how-to-designer-transform-data/export-data-pipeline.png).

1. Select the **Export Data** component connected to the *left*-most port of the **Split Data** component.

    For the **Split Data** component, the output port order matters. The first output port contains the rows where the regular expression is true. In this case, the first port contains rows for US-based income, and the second port contains rows for non-US based income.

1. In the component details pane to the right of the canvas, set the following options:
    
    **Datastore type**: Azure Blob Storage

    **Datastore**: Select an existing datastore, or select "New datastore" to create one now.

    **Path**: `/data/us-income`

    **File format**: csv

    > [!NOTE]
    > This article assumes that you have access to a datastore registered to the current Azure Machine Learning workspace. See [Connect to Azure storage services](v1/how-to-connect-data-ui.md#create-datastores) for datastore setup instructions.

    You can create a datastore if you don't have one now. For example purposes, this article will save the datasets to the default blob storage account associated with the workspace. It will save the datasets into the `azureml` container, in a new folder named `data`.

1.  Select the **Export Data** component connected to the *right*-most port of the **Split Data** component.

1. To the right of the canvas in the component details pane, set the following options:
    
    **Datastore type**: Azure Blob Storage

    **Datastore**: Select the same datastore as above

    **Path**: `/data/non-us-income`

    **File format**: csv

1. Verify that the **Export Data** component connected to the left port of the **Split Data** has the **Path** `/data/us-income`.

1. Verify that the **Export Data** component connected to the right port has the **Path** `/data/non-us-income`.

    Your pipeline and settings should look like this:
    
    ![Screenshot showing how to configure the Export Data components](media/how-to-designer-transform-data/us-income-export-data.png).

### Submit the job

Now that you set up your pipeline to split and export the data, submit a pipeline job.

1. Select **Submit** at the top of the canvas.

1. Select **Create new** in the **Set up pipeline job**, to create an experiment.

    Experiments logically group related pipeline jobs together. If you run this pipeline in the future, you should use the same experiment for logging and tracking purposes.

1. Provide a descriptive experiment name - for example "split-census-data".

1. Select **Submit**.

## View results

After the pipeline finishes running, you can navigate to your Azure portal blob storage to view your results. You can also view the intermediary results of the **Split Data** component to confirm that your data has been split correctly.

1. Select the **Split Data** component.

1. In the component details pane to the right of the canvas, select **Outputs + logs**.

1. Select the visualize icon ![visualize icon](media/how-to-designer-transform-data/visualize-icon.png) next to **Results dataset1**.

1. Verify that the "native-country" column contains only the value "United-States".

1. Select the visualize icon ![visualize icon](media/how-to-designer-transform-data/visualize-icon.png) next to **Results dataset2**.

1. Verify that the "native-country" column does not contain the value "United-States".

## Clean up resources

To continue with part two of this [Retrain models with Azure Machine Learning designer](how-to-retrain-designer.md) how-to, skip this section.

[!INCLUDE [aml-ui-cleanup](../../includes/aml-ui-cleanup.md)]

## Next steps

In this article, you learned how to transform a dataset, and save it to a registered datastore.

Continue to the next part of this how-to series with [Retrain models with Azure Machine Learning designer](how-to-retrain-designer.md), to use your transformed datasets and pipeline parameters to train machine learning models.