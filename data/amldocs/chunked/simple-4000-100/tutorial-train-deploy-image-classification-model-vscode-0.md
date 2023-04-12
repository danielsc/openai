
# Train an image classification TensorFlow model using the Azure Machine Learning Visual Studio Code Extension (preview)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Learn how to train an image classification model to recognize hand-written numbers using TensorFlow and the Azure Machine Learning Visual Studio Code Extension.

In this tutorial, you learn the following tasks:

> [!div class="checklist"]
> * Understand the code
> * Create a workspace
> * Create a GPU cluster for training
> * Train a model

## Prerequisites

- Azure subscription. If you don't have one, sign up to try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/). If you're using the free subscription, only CPU clusters are supported.
- Install [Visual Studio Code](https://code.visualstudio.com/docs/setup/setup-overview), a lightweight, cross-platform code editor.
- Azure Machine Learning Studio Visual Studio Code extension. For install instructions see the [Setup Azure Machine Learning Visual Studio Code extension guide](./how-to-setup-vs-code.md)
- CLI (v2). For installation instructions, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md)
-  Clone the community driven repository
    ```bash
        git clone https://github.com/Azure/azureml-examples.git
    ```

## Understand the code

The code for this tutorial uses TensorFlow to train an image classification machine learning model that categorizes handwritten digits from 0-9. It does so by creating a neural network that takes the pixel values of 28 px x 28 px image as input and outputs a list of 10 probabilities, one for each of the digits being classified. Below is a sample of what the data looks like.  

![MNIST Digits](./media/tutorial-train-deploy-image-classification-model-vscode/digits.png)

## Create a workspace

The first thing you have to do to build an application in Azure Machine Learning is to create a workspace. A workspace contains the resources to train models as well as the trained models themselves. For more information, see [what is a workspace](./concept-workspace.md).

1. Open the *azureml-examples/cli/jobs/single-step/tensorflow/mnist* directory from the community driven repository in Visual Studio Code.
1. On the Visual Studio Code activity bar, select the **Azure** icon to open the Azure Machine Learning view.
1. In the Azure Machine Learning view, right-click your subscription node and select **Create Workspace**.

    > [!div class="mx-imgBorder"]
    > ![Create workspace](./media/tutorial-train-deploy-image-classification-model-vscode/create-workspace.png)

1. A specification file appears. Configure the specification file with the following options.

    ```yml
    $schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
    name: TeamWorkspace
    location: WestUS2
    display_name: team-ml-workspace
    description: A workspace for training machine learning models
    tags:
      purpose: training
      team: ml-team
    ```

    The specification file creates a workspace called `TeamWorkspace` in the `WestUS2` region. The rest of the options defined in the specification file provide friendly naming, descriptions, and tags for the workspace.

1. Right-click the specification file and select **Azure ML: Execute YAML**. Creating a resource uses the configuration options defined in the YAML specification file and submits a job using the CLI (v2). At this point, a request to Azure is made to create a new workspace and dependent resources in your account. After a few minutes, the new workspace appears in your subscription node.
1. Set `TeamWorkspace` as your default workspace. Doing so places resources and jobs you create in the workspace by default. Select the **Set Azure ML Workspace** button on the Visual Studio Code status bar and follow the prompts to set `TeamWorkspace` as your default workspace.

For more information on workspaces, see [how to manage resources in VS Code](how-to-manage-resources-vscode.md).
