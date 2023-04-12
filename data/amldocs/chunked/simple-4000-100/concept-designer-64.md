A component is an algorithm that you can perform on your data. The designer has several components ranging from data ingress functions to training, scoring, and validation processes.

A component may have a set of parameters that you can use to configure the component's internal algorithms. When you select a component on the canvas, the component's parameters are displayed in the Properties pane to the right of the canvas. You can modify the parameters in that pane to tune your model. You can set the compute resources for individual components in the designer. 

:::image type="content" source="./media/concept-designer/properties.png" alt-text="Component properties":::


For some help navigating through the library of machine learning algorithms available, see [Algorithm & component reference overview](component-reference/component-reference.md). For help with choosing an algorithm, see the [Azure Machine Learning Algorithm Cheat Sheet](algorithm-cheat-sheet.md).

## <a name="compute"></a> Compute resources

Use compute resources from your workspace to run your pipeline and host your deployed models as online endpoints or pipeline endpoints (for batch inference). The supported compute targets are:

| Compute target | Training | Deployment |
| ---- |:----:|:----:|
| Azure Machine Learning compute | ✓ | |
| Azure Kubernetes Service | | ✓ |

Compute targets are attached to your [Azure Machine Learning workspace](concept-workspace.md). You manage your compute targets in your workspace in the [Azure Machine Learning studio](https://ml.azure.com).

## Deploy

To perform real-time inferencing, you must deploy a pipeline as an [online endpoint](concept-endpoints.md#what-are-online-endpoints). The online endpoint creates an interface between an external application and your scoring model. A call to an online endpoint returns prediction results to the application in real time. To make a call to an online endpoint, you pass the API key that was created when you deployed the endpoint. The endpoint is based on REST, a popular architecture choice for web programming projects.

Online endpoints must be deployed to an Azure Kubernetes Service cluster.

To learn how to deploy your model, see [Tutorial: Deploy a machine learning model with the designer](tutorial-designer-automobile-price-deploy.md).

[!INCLUDE [endpoints-option](../../includes/machine-learning-endpoints-preview-note.md)]

## Publish

You can also publish a pipeline to a **pipeline endpoint**. Similar to an online endpoint, a pipeline endpoint lets you submit new pipeline jobs from external applications using REST calls. However, you cannot send or receive data in real time using a pipeline endpoint.

Published pipelines are flexible, they can be used to train or retrain models, [perform batch inferencing](how-to-run-batch-predictions-designer.md), process new data, and much more. You can publish multiple pipelines to a single pipeline endpoint and specify which pipeline version to run.

A published pipeline runs on the compute resources you define in the pipeline draft for each component.

The designer creates the same [PublishedPipeline](/python/api/azureml-pipeline-core/azureml.pipeline.core.graph.publishedpipeline) object as the SDK.

## Next steps

* Learn the fundamentals of predictive analytics and machine learning with [Tutorial: Predict automobile price with the designer](tutorial-designer-automobile-price-train-score.md)
* Learn how to modify existing [designer samples](samples-designer.md) to adapt them to your needs.
