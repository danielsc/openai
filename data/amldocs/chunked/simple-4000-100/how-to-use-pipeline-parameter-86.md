You can attach the same component parameters of duplicated components to the same pipeline parameter if you want to alter the value at one time when triggering the pipeline job.

The following example has duplicated **Clean Missing Data** component. For each **Clean Missing Data** component, attach **Replacement value** to pipeline parameter **replace-missing-value**:

1. Select the **Clean Missing Data** component.

1. In the component detail pane, to the right of the canvas, set the **Cleaning mode** to "Custom substitution value".

1. Mouseover the **Replacement value** field.

1. Select the ellipses (**...**) that appear.

1. Select the pipeline parameter `replace-missing-value`.

   ![Screenshot that shows how to attach a pipeline parameter](media/how-to-use-pipeline-parameter/attach-replace-value-to-pipeline-parameter.png)

You have successfully attached the **Replacement value** field to your pipeline parameter. 


### Detach component parameter to pipeline parameter

After you attach **Replacement value** to pipeline parameter, it is non-actionable.

You can detach component parameter to pipeline parameter by clicking the ellipses (**...**) next to the component parameter, and select **Detach from pipeline parameter**.

 ![Screenshot that shows non-actionable after attaching to pipeline parameter](media/how-to-use-pipeline-parameter/non-actionable-module-parameter.png)

## Update and delete pipeline parameters

In this section, you learn how to update and delete pipeline parameters.

### Update pipeline parameters

Use the following steps to update a component pipeline parameter:

1. At the top of the canvas, select the gear icon.
1. In the **Pipeline parameters** section, you can view and update the name and default value for all of your pipeline parameter.

### Delete a dataset pipeline parameter

Use the following steps to delete a dataset pipeline parameter:

1. Select the dataset component.
1. Uncheck the option **Set as pipeline parameter**.


### Delete component pipeline parameters

Use the following steps to delete a component pipeline parameter:

1. At the top of the canvas, select the gear icon.

1. Select the ellipses (**...**) next to the pipeline parameter.

    This view shows you which components the pipeline parameter is attached to.

    ![Screenshot that shows the current pipeline parameter applied to a component](media/how-to-use-pipeline-parameter/delete-pipeline-parameter2.png)

1. Select **Delete parameter** to delete the pipeline parameter.

    > [!NOTE]
    > Deleting a pipeline parameter will cause all attached component parameters to be detached and the value of detached component parameters will keep current pipeline parameter value.     

## Trigger a pipeline job with pipeline parameters 

In this section, you learn how to submit a pipeline job while setting pipeline parameters.

### Resubmit a pipeline job

After submitting a pipeline with pipeline parameters, you can resubmit a pipeline job with different parameters:

1. Go to pipeline detail page. In the **Pipeline job overview** window, you can check current pipeline parameters and values.

1. Select **Resubmit**.
1. In the **Setup pipeline job**, specify your new pipeline parameters. 

![Screenshot that shows resubmit pipeline with pipeline parameters](media/how-to-use-pipeline-parameter/resubmit-pipeline-run.png)

### Use published pipelines

You can also publish a pipeline to use its pipeline parameters. A **published pipeline** is a pipeline that has been deployed to a compute resource, which client applications can invoke via a REST endpoint.

Published endpoints are especially useful for retraining and batch prediction scenarios. For more information, see [How to retrain models in the designer](how-to-retrain-designer.md) or [Run batch predictions in the designer](how-to-run-batch-predictions-designer.md).

## Next steps

In this article, you learned how to create pipeline parameters in the designer. Next, see how you can use pipeline parameters to [retrain models](how-to-retrain-designer.md) or perform [batch predictions](how-to-run-batch-predictions-designer.md).
