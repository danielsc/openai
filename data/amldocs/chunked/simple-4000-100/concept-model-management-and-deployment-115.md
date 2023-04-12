* Deployment configuration that describes how and where to deploy the model.

For more information, see [Deploy online endpoints](how-to-deploy-online-endpoints.md).

#### Controlled rollout

When deploying to an online endpoint, you can use controlled rollout to enable the following scenarios:

* Create multiple versions of an endpoint for a deployment
* Perform A/B testing by routing traffic to different deployments within the endpoint.
* Switch between endpoint deployments by updating the traffic percentage in endpoint configuration.

For more information, see [Controlled rollout of machine learning models](./how-to-safely-rollout-online-endpoints.md).

### Analytics

Microsoft Power BI supports using machine learning models for data analytics. For more information, see [Machine Learning integration in Power BI (preview)](/power-bi/service-machine-learning-integration).

## Capture the governance data required for MLOps

Machine Learning gives you the capability to track the end-to-end audit trail of all your machine learning assets by using metadata. For example:

- [Machine Learning datasets](how-to-create-register-datasets.md) help you track, profile, and version data.
- [Interpretability](how-to-machine-learning-interpretability.md) allows you to explain your models, meet regulatory compliance, and understand how models arrive at a result for specific input.
- Machine Learning Job history stores a snapshot of the code, data, and computes used to train a model.
- The [Machine Learning Model Registry](./how-to-manage-models.md?tabs=use-local#create-a-model-in-the-model-registry) captures all the metadata associated with your model. For example, metadata includes which experiment trained it, where it's being deployed, and if its deployments are healthy.
- [Integration with Azure](how-to-use-event-grid.md) allows you to act on events in the machine learning lifecycle. Examples are model registration, deployment, data drift, and training (job) events.

> [!TIP]
> While some information on models and datasets is automatically captured, you can add more information by using _tags_. When you look for registered models and datasets in your workspace, you can use tags as a filter.

## Notify, automate, and alert on events in the machine learning lifecycle

Machine Learning publishes key events to Azure Event Grid, which can be used to notify and automate on events in the machine learning lifecycle. For more information, see [Use Event Grid](how-to-use-event-grid.md).

## Automate the machine learning lifecycle

You can use GitHub and Azure Pipelines to create a continuous integration process that trains a model. In a typical scenario, when a data scientist checks a change into the Git repo for a project, Azure Pipelines starts a training job. The results of the job can then be inspected to see the performance characteristics of the trained model. You can also create a pipeline that deploys the model as a web service.

The [Machine Learning extension](https://marketplace.visualstudio.com/items?itemName=ms-air-aiagility.vss-services-azureml) makes it easier to work with Azure Pipelines. It provides the following enhancements to Azure Pipelines:

* Enables workspace selection when you define a service connection.
* Enables release pipelines to be triggered by trained models created in a training pipeline.

For more information on using Azure Pipelines with Machine Learning, see:

* [Continuous integration and deployment of machine learning models with Azure Pipelines](/azure/devops/pipelines/targets/azure-machine-learning)
* [Machine Learning MLOps](https://github.com/Azure/mlops-v2) repository


## Next steps

Learn more by reading and exploring the following resources:

+ [Set up MLOps with Azure DevOps](how-to-setup-mlops-azureml.md)
+ [Learning path: End-to-end MLOps with Azure Machine Learning](/training/paths/build-first-machine-operations-workflow/)
+ [How to deploy a model to an online endpoint](how-to-deploy-online-endpoints.md) with Machine Learning
