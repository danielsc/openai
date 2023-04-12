
# Rebuild a Studio (classic) web service in Azure Machine Learning

[!INCLUDE [ML Studio (classic) retirement](../../includes/machine-learning-studio-classic-deprecation.md)]

In this article, you learn how to rebuild an ML Studio (classic) web service as an **endpoint** in Azure Machine Learning.

Use Azure Machine Learning pipeline endpoints to make predictions, retrain models, or run any generic pipeline. The REST endpoint lets you run pipelines from any platform. 

This article is part of the Studio (classic) to Azure Machine Learning migration series. For more information on migrating to Azure Machine Learning, see the [migration overview article](migrate-overview.md).

> [!NOTE]
> This migration series focuses on the drag-and-drop designer. For more information on deploying models programmatically, see [Deploy machine learning models in Azure](v1/how-to-deploy-and-where.md).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- An Azure Machine Learning workspace. [Create workspace resources](quickstart-create-resources.md).
- An Azure Machine Learning training pipeline. For more information, see [Rebuild a Studio (classic) experiment in Azure Machine Learning](migrate-rebuild-experiment.md).

## Real-time endpoint vs pipeline endpoint

Studio (classic) web services have been replaced by **endpoints** in Azure Machine Learning. Use the following table to choose which endpoint type to use:

|Studio (classic) web service| Azure Machine Learning replacement
|---|---|
|Request/respond web service (real-time prediction)|Real-time endpoint|
|Batch web service (batch prediction)|Pipeline endpoint|
|Retraining web service (retraining)|Pipeline endpoint| 


## Deploy a real-time endpoint

In Studio (classic), you used a **REQUEST/RESPOND web service** to deploy a model for real-time predictions. In Azure Machine Learning, you use a **real-time endpoint**.

There are multiple ways to deploy a model in Azure Machine Learning. One of the simplest ways is to use the designer to automate the deployment process. Use the following steps to deploy a model as a real-time endpoint:

1. Run your completed training pipeline at least once.
1. After the job completes, at the top of the canvas, select **Create inference pipeline** > **Real-time inference pipeline**.

    ![Create realtime inference pipeline](./media/migrate-rebuild-web-service/create-inference-pipeline.png)
        
    The designer converts the training pipeline into a real-time inference pipeline. A similar conversion also occurs in Studio (classic).

    In the designer, the conversion step also [registers the trained model to your Azure Machine Learning workspace](v1/how-to-deploy-and-where.md#registermodel).

1. Select **Submit** to run the real-time inference pipeline, and verify that it runs successfully.

1. After you verify the inference pipeline, select **Deploy**.

1. Enter a name for your endpoint and a compute type.

    The following table describes your deployment compute options in the designer:

    | Compute target | Used for | Description | Creation |
    | ----- |  ----- | ----- | -----  |
    |[Azure Kubernetes Service (AKS)](v1/how-to-deploy-azure-kubernetes-service.md) |Real-time inference|Large-scale, production deployments. Fast response time and service autoscaling.| User-created. For more information, see [Create compute targets](how-to-create-attach-compute-studio.md). |
    |[Azure Container Instances](v1/how-to-deploy-azure-container-instance.md)|Testing or development | Small-scale, CPU-based workloads that require less than 48 GB of RAM.| Automatically created by Azure Machine Learning.

### Test the real-time endpoint

After deployment completes, you can see more details and test your endpoint:

1. Go the **Endpoints** tab.
1. Select your endpoint.
1. Select the **Test** tab.
    
    ![Screenshot showing the Endpoints tab with the Test endpoint button](./media/migrate-rebuild-web-service/test-realtime-endpoint.png)
