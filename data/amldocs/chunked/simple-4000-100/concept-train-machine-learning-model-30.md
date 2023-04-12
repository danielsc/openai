* [Configure a development environment for Azure Machine Learning](how-to-configure-environment.md)

### Submit a command

A generic training job with Azure Machine Learning can be defined using the [command()](/python/api/azure-ai-ml/azure.ai.ml#azure-ai-ml-command). The command is then used, along with your training script(s) to train a model on the specified compute target.

You may start with a command for your local computer, and then switch to one for a cloud-based compute target as needed. When changing the compute target, you only change the compute parameter in the command that you use. A run also logs information about the training job, such as the inputs, outputs, and logs.

* [Tutorial: Train your first ML model](tutorial-1st-experiment-sdk-train.md)
* [Examples: Jupyter Notebook and Python examples of training models](https://github.com/Azure/azureml-examples)

### Automated Machine Learning

Define the iterations, hyperparameter settings, featurization, and other settings. During training, Azure Machine Learning tries different algorithms and parameters in parallel. Training stops once it hits the exit criteria you defined.

> [!TIP]
> In addition to the Python SDK, you can also use Automated ML through [Azure Machine Learning studio](https://ml.azure.com).

* [What is automated machine learning?](concept-automated-ml.md)
* [Tutorial: Create your first classification model with automated machine learning](tutorial-first-experiment-automated-ml.md)
* [How to: Configure automated ML experiments in Python](how-to-configure-auto-train.md)
* [How to: Create, explore, and deploy automated machine learning experiments with Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md)

### Machine learning pipeline

Machine learning pipelines can use the previously mentioned training methods. Pipelines are more about creating a workflow, so they encompass more than just the training of models. 

* [What are ML pipelines in Azure Machine Learning?](concept-ml-pipelines.md)
* [Tutorial: Create production ML pipelines with Python SDK v2 in a Jupyter notebook](tutorial-pipeline-python-sdk.md)


### Understand what happens when you submit a training job

The Azure training lifecycle consists of:

1. Zipping the files in your project folder and upload to the cloud.
    
    > [!TIP]
    > [!INCLUDE [amlinclude-info](../../includes/machine-learning-amlignore-gitignore.md)]

1. Scaling up your compute cluster 
1. Building or downloading the dockerfile to the compute node 
    1. The system calculates a hash of: 
        - The base image 
        - Custom docker steps (see [Deploy a model using a custom Docker base image](./how-to-deploy-custom-container.md))
        - The conda definition YAML (see [Manage Azure Machine Learning environments with the CLI (v2)](how-to-manage-environments-v2.md)))
    1. The system uses this hash as the key in a lookup of the workspace Azure Container Registry (ACR)
    1. If it is not found, it looks for a match in the global ACR
    1. If it is not found, the system builds a new image (which will be cached and registered with the workspace ACR)
1. Downloading your zipped project file to temporary storage on the compute node
1. Unzipping the project file
1. The compute node executing `python <entry script> <arguments>`
1. Saving logs, model files, and other files written to `./outputs` to the storage account associated with the workspace
1. Scaling down compute, including removing temporary storage 


## Azure Machine Learning designer

The designer lets you train models using a drag and drop interface in your web browser.

+ [What is the designer?](concept-designer.md)
+ [Tutorial: Predict automobile price](tutorial-designer-automobile-price-train-score.md)

## Azure CLI

The machine learning CLI is an extension for the Azure CLI. It provides cross-platform CLI commands for working with Azure Machine Learning. Typically, you use the CLI to automate tasks, such as training a machine learning model.
