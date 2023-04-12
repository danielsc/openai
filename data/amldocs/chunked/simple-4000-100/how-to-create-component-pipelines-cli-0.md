
# Create and run machine learning pipelines using components with the Azure Machine Learning CLI

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]


In this article, you learn how to create and run [machine learning pipelines](concept-ml-pipelines.md) by using the Azure CLI and components (for more, see [What is an Azure Machine Learning component?](concept-component.md)). You can create pipelines without using components, but components offer the greatest amount of flexibility and reuse. AzureML Pipelines may be defined in YAML and run from the CLI, authored in Python, or composed in AzureML Studio Designer with a drag-and-drop UI. This document focuses on the CLI.

## Prerequisites

- If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

- An Azure Machine Learning workspace. [Create workspace resources](quickstart-create-resources.md).

- [Install and set up the Azure CLI extension for Machine Learning](how-to-configure-cli.md).

- Clone the examples repository:

    ```azurecli-interactive
    git clone https://github.com/Azure/azureml-examples --depth 1
    cd azureml-examples/cli/jobs/pipelines-with-components/basics
    ```

### Suggested pre-reading

- [What is Azure Machine Learning pipeline](./concept-ml-pipelines.md)
- [What is Azure Machine Learning component](./concept-component.md)

## Create your first pipeline with component

Let's create your first pipeline with component using an example. This section aims to give you an initial impression of what pipeline and component look like in AzureML with a concrete example.

From the `cli/jobs/pipelines-with-components/basics` directory of the [`azureml-examples` repository](https://github.com/Azure/azureml-examples), navigate to the `3b_pipeline_with_data` subdirector. There are three types of files in this directory. Those are the files you'll need to create when building your own pipeline.

- **pipeline.yml**: This YAML file defines the machine learning pipeline. This YAML file describes how to break a full machine learning task into a multistep workflow. For example, considering a simple machine learning task of using historical data to train a sales forecasting model, you may want to build a sequential workflow with data processing, model training, and model evaluation steps.  Each step is a component that has well defined interface and can be developed, tested, and optimized independently. The pipeline YAML also defines how the child steps connect to other steps in the pipeline, for example the model training step generate a model file and the model file will pass to a model evaluation step.

- **component.yml**:  This YAML file defines the component. It packages following information:
  - Metadata: name, display name, version, description, type etc. The metadata helps to describe and manage the component.
  - Interface: inputs and outputs. For example, a model training component will take training data and number of epochs as input, and generate a trained model file as output. Once the interface is defined, different teams can develop and test the component independently.
  - Command, code & environment: the command, code and environment to run the component.    Command is the shell command to execute the component. Code usually refers to a source  code directory. Environment could be an AzureML environment(curated or customer created), docker image or conda environment.  

- **component_src**: This is the source code directory for a specific component. It contains the source code that will be executed in the component. You can use your preferred language(Python, R...). The code must be executed by a shell command. The source code can take a few inputs from shell command line to control how this step is going to be executed. For example, a training step may take training data, learning rate, number of epochs to control the training process. The argument of a shell command is used to pass inputs and outputs to the code. 
