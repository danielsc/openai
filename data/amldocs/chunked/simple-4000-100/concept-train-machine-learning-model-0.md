
# Train models with Azure Machine Learning

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
> [!div class="op_single_selector" title1="Select the Azure Machine Learning version you are using:"]
> * [v1](v1/concept-train-machine-learning-model-v1.md)
> * [v2 (current)](concept-train-machine-learning-model.md)

Azure Machine Learning provides several ways to train your models, from code-first solutions using the SDK to low-code solutions such as automated machine learning and the visual designer. Use the following list to determine which training method is right for you:

+ [Azure Machine Learning SDK for Python](#python-sdk): The Python SDK provides several ways to train models, each with different capabilities.

    | Training method | Description |
    | ----- | ----- |
    | [command()](#submit-a-command) | A **typical way to train models** is to submit a command() that includes a training script, environment, and compute information. |
    | [Automated machine learning](#automated-machine-learning) | Automated machine learning allows you to **train models without extensive data science or programming knowledge**. For people with a data science and programming background, it provides a way to save time and resources by automating algorithm selection and hyperparameter tuning. You don't have to worry about defining a job configuration when using automated machine learning. |
    | [Machine learning pipeline](#machine-learning-pipeline) | Pipelines are not a different training method, but a **way of defining a workflow using modular, reusable steps** that can include training as part of the workflow. Machine learning pipelines support using automated machine learning and run configuration to train models. Since pipelines are not focused specifically on training, the reasons for using a pipeline are more varied than the other training methods. Generally, you might use a pipeline when:<br>* You want to **schedule unattended processes** such as long running training jobs or data preparation.<br>* Use **multiple steps** that are coordinated across heterogeneous compute resources and storage locations.<br>* Use the pipeline as a **reusable template** for specific scenarios, such as retraining or batch scoring.<br>* **Track and version data sources, inputs, and outputs** for your workflow.<br>* Your workflow is **implemented by different teams that work on specific steps independently**. Steps can then be joined together in a pipeline to implement the workflow. |

+ **Designer**: Azure Machine Learning designer provides an easy entry-point into machine learning for building proof of concepts, or for users with little coding experience. It allows you to train models using a drag and drop web-based UI. You can use Python code as part of the design, or train models without writing any code.

+ **Azure CLI**: The machine learning CLI provides commands for common tasks with Azure Machine Learning, and is often used for **scripting and automating tasks**. For example, once you've created a training script or pipeline, you might use the Azure CLI to start a training job on a schedule or when the data files used for training are updated. For training models, it provides commands that submit training jobs. It can submit jobs using run configurations or pipelines.

Each of these training methods can use different types of compute resources for training. Collectively, these resources are referred to as [__compute targets__](concept-compute-target.md). A compute target can be a local machine or a cloud resource, such as an Azure Machine Learning Compute, Azure HDInsight, or a remote virtual machine.

## Python SDK

The Azure Machine Learning SDK for Python allows you to build and run machine learning workflows with Azure Machine Learning. You can interact with the service from an interactive Python session, Jupyter Notebooks, Visual Studio Code, or other IDE.

* [Install/update the SDK](/python/api/overview/azure/ai-ml-readme)
* [Configure a development environment for Azure Machine Learning](how-to-configure-environment.md)
