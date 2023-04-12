    ![Screenshot showing the Endpoints tab with the Test endpoint button](./media/migrate-rebuild-web-service/test-realtime-endpoint.png)

## Publish a pipeline endpoint for batch prediction or retraining

You can also use your training pipeline to create a **pipeline endpoint** instead of a real-time endpoint. Use **pipeline endpoints** to perform either batch prediction or retraining.

Pipeline endpoints replace Studio (classic) **batch execution endpoints**  and **retraining web services**.

### Publish a pipeline endpoint for batch prediction

Publishing a batch prediction endpoint is similar to the real-time endpoint.

Use the following steps to publish a pipeline endpoint for batch prediction:

1. Run your completed training pipeline at least once.

1. After the job completes, at the top of the canvas, select **Create inference pipeline** > **Batch inference pipeline**.

    ![Screenshot showing the create inference pipeline button on a training pipeline](./media/migrate-rebuild-web-service/create-inference-pipeline.png)
        
    The designer converts the training pipeline into a batch inference pipeline. A similar conversion also occurs in Studio (classic).

    In the designer, this step also [registers the trained model to your Azure Machine Learning workspace](v1/how-to-deploy-and-where.md#registermodel).

1. Select **Submit** to run the batch inference pipeline and verify that it successfully completes.

1. After you verify the inference pipeline, select **Publish**.
 
1. Create a new pipeline endpoint or select an existing one.
    
    A new pipeline endpoint creates a new REST endpoint for your pipeline. 

    If you select an existing pipeline endpoint, you don't overwrite the existing pipeline. Instead, Azure Machine Learning versions each pipeline in the endpoint. You can specify which version to run in your REST call. You must also set a default pipeline if the REST call doesn't specify a version.


 ### Publish a pipeline endpoint for retraining

To publish a pipeline endpoint for retraining, you must already have a pipeline draft that trains a model. For more information on building a training pipeline, see [Rebuild a Studio (classic) experiment](migrate-rebuild-experiment.md).

To reuse your pipeline endpoint for retraining, you must create a **pipeline parameter** for your input dataset. This lets you dynamically set your training dataset, so that you can retrain your model.

Use the following steps to publish retraining pipeline endpoint:

1. Run your training pipeline at least once.
1. After the run completes, select the dataset module.
1. In the module details pane, select **Set as pipeline parameter**.
1. Provide a descriptive name like "InputDataset".    

    ![Screenshot highlighting how to create a pipeline parameter](./media/migrate-rebuild-web-service/create-pipeline-parameter.png)

    This creates a pipeline parameter for your input dataset. When you call your pipeline endpoint for training, you can specify a new dataset to retrain the model.

1. Select **Publish**.

    ![Screenshot highlighting the Publish button on a training pipeline](./media/migrate-rebuild-web-service/create-retraining-pipeline.png)


## Call your pipeline endpoint from the studio

After you create your batch inference or retraining pipeline endpoint, you can call your endpoint directly from your browser.

1. Go to the **Pipelines** tab, and select **Pipeline endpoints**.
1. Select the pipeline endpoint you want to run.
1. Select **Submit**.

    You can specify any pipeline parameters after you select **Submit**.

## Next steps

In this article, you learned how to rebuild a Studio (classic) web service in Azure Machine Learning. The next step is to [integrate your web service with client apps](migrate-rebuild-integrate-with-client-app.md).


See the other articles in the Studio (classic) migration series:

1. [Migration overview](migrate-overview.md).
1. [Migrate dataset](migrate-register-dataset.md).
1. [Rebuild a Studio (classic) training pipeline](migrate-rebuild-experiment.md).
