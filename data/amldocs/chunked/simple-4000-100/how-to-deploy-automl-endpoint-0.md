
# How to deploy an AutoML model to an online endpoint

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

In this article, you'll learn how to deploy an AutoML-trained machine learning model to an online (real-time inference) endpoint. Automated machine learning, also referred to as automated ML or AutoML, is the process of automating the time-consuming, iterative tasks of developing a machine learning model. For more, see [What is automated machine learning (AutoML)?](concept-automated-ml.md).

In this article you'll know how to deploy AutoML trained machine learning model to online endpoints using: 

- Azure Machine Learning studio
- Azure Machine Learning CLI v2
- Azure Machine Learning Python SDK v2

## Prerequisites

An AutoML-trained machine learning model. For more, see [Tutorial: Train a classification model with no-code AutoML in the Azure Machine Learning studio](tutorial-first-experiment-automated-ml.md) or [Tutorial: Forecast demand with automated machine learning](tutorial-automated-ml-forecast.md).

## Deploy from Azure Machine Learning studio and no code

Deploying an AutoML-trained model from the Automated ML page is a no-code experience. That is, you don't need to prepare a scoring script and environment, both are auto generated. 

1. Go to the Automated ML page in the studio
1. Select your experiment and run
1. Choose the Models tab
1. Select the model you want to deploy 
1. Once you select a model, the Deploy button will light up with a drop-down menu
1. Select *Deploy to real-time endpoint* option

   :::image type="content" source="media/how-to-deploy-automl-endpoint/deploy-button.png" lightbox="media/how-to-deploy-automl-endpoint/deploy-button.png" alt-text="Screenshot showing the Deploy button's drop-down menu":::

   The system will generate the Model and Environment needed for the deployment. 

   :::image type="content" source="media/how-to-deploy-automl-endpoint/model.png" lightbox="media/how-to-deploy-automl-endpoint/model.png" alt-text="Screenshot showing the generated Model":::

   :::image type="content" source="media/how-to-deploy-automl-endpoint/environment.png" lightbox="media/how-to-deploy-automl-endpoint/environment.png" alt-text="Screenshot showing the generated Environment":::

5. Complete the wizard to deploy the model to an online endpoint

 :::image type="content" source="media/how-to-deploy-automl-endpoint/complete-wizard.png" lightbox="media/how-to-deploy-automl-endpoint/complete-wizard.png"  alt-text="Screenshot showing the review-and-create page":::


## Deploy manually from the studio or command line

If you wish to have more control over the deployment, you can download the training artifacts and deploy them. 

To download the components you'll need for deployment:

1. Go to your Automated ML experiment and run in your machine learning workspace
1. Choose the Models tab
1. Select the model you wish to use. Once you select a model, the *Download* button will become enabled
1. Choose *Download*

:::image type="content" source="media/how-to-deploy-automl-endpoint/download-model.png" lightbox="media/how-to-deploy-automl-endpoint/download-model.png" alt-text="Screenshot showing the selection of the model and download button":::

You'll receive a zip file containing:
* A conda environment specification file named `conda_env_<VERSION>.yml`
* A Python scoring file named `scoring_file_<VERSION>.py`
* The model itself, in a Python `.pkl` file named `model.pkl`

To deploy using these files, you can use either the studio or the Azure CLI.

# [Studio](#tab/Studio)

1. Go to the Models page in Azure Machine Learning studio

1. Select + Register Model option

1. Register the model you downloaded from Automated ML run

1. Go to Environments page, select Custom environment, and select + Create option to create an environment for your deployment. Use the downloaded conda yaml to create a custom environment

1. Select the model, and from the Deploy drop-down option, select Deploy to real-time endpoint
