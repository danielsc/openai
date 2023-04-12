The model explanations dashboard provides an overall analysis of the trained model along with its predictions and explanations. It also lets you drill into an individual data point and its individual feature importance. [Learn more about the explanation dashboard visualizations](how-to-machine-learning-interpretability-aml.md#visualizations).

To get explanations for a particular model, 

1. On the **Models** tab, select the model you want to understand. 
1. Select the **Explain model** button, and provide a compute that can be used to generate the explanations.
1. Check the **Child jobs** tab for the status. 
1. Once complete, navigate to the **Explanations (preview)** tab which contains the explanations dashboard. 

    ![Model explanation dashboard](media/how-to-use-automated-ml-for-ml-models/model-explanation-dashboard.png)

## Edit and submit jobs (preview)

>[!IMPORTANT]
> The ability to copy, edit and submit a new experiment based on an existing experiment is a preview feature. This capability is an [experimental](/python/api/overview/azure/ml/#stable-vs-experimental) preview feature, and may change at any time.

In scenarios where you would like to create a new experiment based on the settings of an existing experiment, automated ML provides the option to do so with the **Edit and submit** button in the studio UI.  

This functionality is limited to experiments initiated from the studio UI and requires the data schema for the new experiment to match that of the original experiment. 

The **Edit and submit** button opens the **Create a new Automated ML job** wizard with the data, compute and experiment settings pre-populated. You can go through each form and edit selections as needed for your new experiment. 

## Deploy your model

Once you have the best model at hand, it is time to deploy it as a web service to predict on new data.

>[!TIP]
> If you are looking to deploy a model that was generated via the `automl` package with the Python SDK, you must [register your model](./v1/how-to-deploy-and-where.md) to the workspace. 
>
> Once you're model is registered, find it in the studio by selecting **Models** on the left pane. Once you open your model, you can select the **Deploy** button at the top of the screen, and then follow the instructions as described in **step 2** of the **Deploy your model** section.

Automated ML helps you with deploying the model without writing code:

1. You have a couple options for deployment. 

    + Option 1: Deploy the best model, according to the metric criteria you defined. 
        1. After the experiment is complete, navigate to the parent job page by selecting **Job 1** at the top of the screen. 
        1.  Select the model listed in the **Best model summary** section. 
        1. Select **Deploy** on the top left of the window. 

    + Option 2: To deploy a specific model iteration from this experiment.
        1. Select the desired model from the **Models** tab
        1. Select **Deploy** on the top left of the window.

1. Populate the **Deploy model** pane.

    Field| Value
    ----|----
    Name| Enter a unique name for your deployment.
    Description| Enter a description to better identify what this deployment is for.
    Compute type| Select the type of endpoint you want to deploy: [*Azure Kubernetes Service (AKS)*](../aks/intro-kubernetes.md) or [*Azure Container Instance (ACI)*](../container-instances/container-instances-overview.md).
    Compute name| *Applies to AKS only:* Select the name of the AKS cluster you wish to deploy to.
    Enable authentication | Select to allow for token-based or key-based authentication.
    Use custom deployment assets| Enable this feature if you want to upload your own scoring script and environment file. Otherwise, automated ML provides these assets for you by default. [Learn more about scoring scripts](./v1/how-to-deploy-and-where.md).

    >[!Important]
    > File names must be under 32 characters and must begin and end with alphanumerics. May include dashes, underscores, dots, and alphanumerics between. Spaces are not allowed.
