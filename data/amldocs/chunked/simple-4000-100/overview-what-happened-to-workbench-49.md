You won't lose any code or work. In the older version, projects are cloud entities with a local directory. In the latest version, you attach local directories to the Azure Machine Learning workspace by using a local config file. See a [diagram of the latest architecture](v1/concept-azure-machine-learning-architecture.md).

Much of the project content was already on your local machine. So you just need to create a config file in that directory and reference it in your code to connect to your workspace. To continue using the local directory containing your files and scripts, specify the directory's name in the ['experiment.submit'](/python/api/azureml-core/azureml.core.experiment.experiment) Python command or using the `az ml project attach` CLI command.  For example:


[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

```python
run = exp.submit(source_directory=script_folder,
                 script='train.py', run_config=run_config_system_managed)
```

[Create a workspace](how-to-manage-workspace.md) to get started.

## What about my registered models and images?

The models that you registered in your old model registry must be migrated to your new workspace if you want to continue to use them. To migrate your models, download the models and re-register them in your new workspace.

The images that you created in your old image registry cannot be directly migrated to the new workspace. In most cases, the model can be deployed without having to create an image. If needed, you can create an image for the model in the new workspace. For more information, see [Manage, register, deploy, and monitor machine learning models](concept-model-management-and-deployment.md).

## What about deployed web services?

Now that support for the old CLI has ended, you can no longer redeploy models or manage the web services you originally deployed with your Model Management account. However, those web services will continue to work for as long as Azure Container Service (ACS) is still supported.

In the latest version, models are deployed as web services to Azure Container Instances (ACI) or Azure Kubernetes Service (AKS) clusters. You can also deploy to FPGAs.

Learn more in these articles:
+ [Where and how to deploy models](./v1/how-to-deploy-and-where.md)
+ [Tutorial: Train and deploy a model](tutorial-train-deploy-notebook.md)

## Next steps

Learn about the [latest architecture for Azure Machine Learning](v1/concept-azure-machine-learning-architecture.md).

For an overview of the service, read [What is Azure Machine Learning?](overview-what-is-azure-machine-learning.md).

Start with [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md).  Then use these resources to create your first experiment with your preferred method:

  + [Tutorial: Azure Machine Learning in a day](tutorial-azure-ml-in-a-day.md)
  + [Use a Jupyter notebook to train image classification models](tutorial-train-deploy-notebook.md)
  + [Use automated machine learning](tutorial-designer-automobile-price-train-score.md) 
  + [Use the designer's drag & drop capabilities](tutorial-first-experiment-automated-ml.md) 
  + [Train models](how-to-train-model.md)
