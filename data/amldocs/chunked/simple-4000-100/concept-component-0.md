# What is an Azure Machine Learning component?

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

An Azure Machine Learning component is a self-contained piece of code that does one step in a machine learning pipeline. A component is analogous to a function - it has a name, inputs, outputs, and a body. Components are the building blocks of the [Azure Machine Learning pipelines](concept-ml-pipelines.md).

A component consists of three parts:

- Metadata: name, display_name, version, type, etc.
- Interface: input/output specifications (name, type, description, default value, etc.).
- Command, Code & Environment: command, code and environment required to run the component.

:::image type="content" source="./media/concept-component/component.png" alt-text="Diagram of what a component looks like and how it looks in a pipeline. In addition to screenshots of a component in the C L I, S D K, and portal U I." lightbox = "./media/concept-component/component.png":::

## Why should I use a component?

It's a good engineering practice to build a machine learning pipeline to split a complete machine learning task into a multi-step workflow. Such that, everyone can work on the specific step independently. In Azure Machine Learning, a component represents one reusable step in a pipeline.  Components are designed to help improve the productivity of pipeline building. Specifically, components offer:  

- **Well-defined interface**: Components require a well-defined interface (input and output). The interface allows the user to build steps and connect steps easily. The interface also hides the complex logic of a step and removes the burden of understanding how the step is implemented.

- **Share and reuse**: As the building blocks of a pipeline, components can be easily shared and reused across pipelines, workspaces, and subscriptions. Components built by one team can be discovered and used by another team.  

- **Version control**: Components are versioned. The component producers can keep improving components and publish new versions. Consumers can use specific component versions in their pipelines. This gives them compatibility and reproducibility.

Unit testable: A component is a self-contained piece of code. It's easy to write unit test for a component.

## Component and Pipeline

A machine learning pipeline is the workflow for a full machine learning task. Components are the building blocks of a machine learning pipeline. When you're thinking of a component, it must be under the context of pipeline.  

To build components, the first thing is to define the machine learning pipeline. This requires breaking down the full machine learning task into a multi-step workflow. Each step is a component. For example, considering a simple machine learning task of using historical data to train a sales forecasting model, you may want to build a sequential workflow with data processing, model training, and model evaluation steps. For complex tasks, you may want to further break down. For example, split one single data processing step into data ingestion, data cleaning, data pre-processing, and feature engineering steps.  

Once the steps in the workflow are defined, the next thing is to specify how each step is connected in the pipeline. For example, to connect your data processing step and model training step, you may want to define a data processing component to output a folder that contains the processed data. A training component takes a folder as input and outputs a folder that contains the trained model. These inputs and outputs definition will become part of your component interface definition.

Now, it's time to develop the code of executing a step. You can use your preferred languages (python, R, etc.). The code must be able to be executed by a shell command. During the development, you may want to add a few inputs to control how this step is going to be executed. For example, for a training step, you may like to add learning rate, number of epochs as the inputs to control the training. These additional inputs plus the inputs and outputs required to connect with other steps are the interface of the component. The argument of a shell command is used to pass inputs and outputs to the code. The environment to execute the command and the code needs to be specified. The environment could be a curated AzureML environment, a docker image or a conda environment.
