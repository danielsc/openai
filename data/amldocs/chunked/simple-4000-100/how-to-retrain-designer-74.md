   > You can publish multiple pipelines to a single endpoint. Each pipeline in a given endpoint is given a version number, which you can specify when you call the pipeline endpoint.

1. Select **Publish**.

## Retrain your model

Now that you have a published training pipeline, you can use it to retrain your model on new data. You can submit jobs from a pipeline endpoint from the studio workspace or programmatically.

### Submit jobs by using the studio portal

Use the following steps to submit a parameterized pipeline endpoint job from the studio portal:

1. Go to the **Endpoints** page in your studio workspace.
1. Select the **Pipeline endpoints** tab. Then, select your pipeline endpoint.
1. Select the **Published pipelines** tab. Then, select the pipeline version that you want to run.
1. Select **Submit**.
1. In the setup dialog box, you can specify the parameters values for the job. For this example, update the data path to train your model using a non-US dataset.

![Screenshot that shows how to set up a parameterized pipeline job in the designer](./media/how-to-retrain-designer/published-pipeline-run.png)

### Submit jobs by using code

You can find the REST endpoint of a published pipeline in the overview panel. By calling the endpoint, you can retrain the published pipeline.

To make a REST call, you need an OAuth 2.0 bearer-type authentication header. For information about setting up authentication to your workspace and making a parameterized REST call, see [Build an Azure Machine Learning pipeline for batch scoring](tutorial-pipeline-batch-scoring-classification.md#publish-and-run-from-a-rest-endpoint).

## Next steps

In this article, you learned how to create a parameterized training pipeline endpoint using the designer.

For a complete walkthrough of how you can deploy a model to make predictions, see the [designer tutorial](tutorial-designer-automobile-price-train-score.md) to train and deploy a regression model.

For how to publish and submit a job to pipeline endpoint using the SDK v1, see [this article](v1/how-to-deploy-pipelines.md).
