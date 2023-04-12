## Register, package, and deploy models from anywhere

The following sections discuss how to register, package, and deploy models.

### Register and track machine learning models

With model registration, you can store and version your models in the Azure cloud, in your workspace. The model registry makes it easy to organize and keep track of your trained models.

> [!TIP]
> A registered model is a logical container for one or more files that make up your model. For example, if you have a model that's stored in multiple files, you can register them as a single model in your Machine Learning workspace. After registration, you can then download or deploy the registered model and receive all the files that were registered.

Registered models are identified by name and version. Each time you register a model with the same name as an existing one, the registry increments the version. More metadata tags can be provided during registration. These tags are then used when you search for a model. Machine Learning supports any model that can be loaded by using Python 3.5.2 or higher.

> [!TIP]
> You can also register models trained outside Machine Learning.

> [!IMPORTANT]
> * When you use the **Filter by** `Tags` option on the **Models** page of Azure Machine Learning Studio, instead of using `TagName : TagValue`, use `TagName=TagValue` without spaces.
> * You can't delete a registered model that's being used in an active deployment.

For more information, [Work with models in Azure Machine Learning](./how-to-manage-models.md).

### Package and debug models

Before you deploy a model into production, it's packaged into a Docker image. In most cases, image creation happens automatically in the background during deployment. You can manually specify the image.

If you run into problems with the deployment, you can deploy on your local development environment for troubleshooting and debugging.

For more information, see [How to troubleshoot online endpoints](how-to-troubleshoot-online-endpoints.md).

### Convert and optimize models

Converting your model to [Open Neural Network Exchange](https://onnx.ai) (ONNX) might improve performance. On average, converting to ONNX can double performance.

For more information on ONNX with Machine Learning, see [Create and accelerate machine learning models](concept-onnx.md).

### Use models

Trained machine learning models are deployed as [endpoints](concept-endpoints.md) in the cloud or locally. Deployments use CPU, GPU for inferencing.

When deploying a model as an endpoint, you provide the following items:

* The models that are used to score data submitted to the service or device.
* An entry script. This script accepts requests, uses the models to score the data, and returns a response.
* A Machine Learning environment that describes the pip and conda dependencies required by the models and entry script.
* Any other assets such as text and data that are required by the models and entry script.

You also provide the configuration of the target deployment platform. For example, the VM family type, available memory, and number of cores. When the image is created, components required by Azure Machine Learning are also added. For example, assets needed to run the web service.

#### Batch scoring

Batch scoring is supported through batch endpoints. For more information, see [endpoints](concept-endpoints.md).

#### Online endpoints

You can use your models with an online endpoint. Online endpoints can use the following compute targets:

* Managed online endpoints
* Azure Kubernetes Service
* Local development environment

To deploy the model to an endpoint, you must provide the following items:

* The model or ensemble of models.
* Dependencies required to use the model. Examples are a script that accepts requests and invokes the model and conda dependencies.
* Deployment configuration that describes how and where to deploy the model.

For more information, see [Deploy online endpoints](how-to-deploy-online-endpoints.md).
