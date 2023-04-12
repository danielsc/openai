While you wait for the models to complete, you can also take a look at model explanations and see which data features (raw or engineered) influenced a particular model's predictions. 

These model explanations can be generated on demand, and are summarized in the model explanations dashboard  that's part of the **Explanations (preview)** tab.

To generate model explanations, 
 
1. Select **Job 1** at the top to navigate back to the **Models** screen. 
1. Select the **Models** tab.
1. For this tutorial, select the first **MaxAbsScaler, LightGBM** model.
1. Select the **Explain model** button at the top. On the right, the **Explain model** pane appears. 
1. Select the **automl-compute** that you created previously. This compute cluster initiates a child job to generate the model explanations.
1. Select **Create** at the bottom. A green success message appears towards the top of your screen. 
    >[!NOTE]
    > The explainability job takes about 2-5 minutes to complete.
1. Select the **Explanations (preview)** button. This tab populates once the explainability run completes.
1. On the left hand side, expand the pane and select the row that says **raw** under **Features**. 
1. Select the **Aggregate feature importance** tab on the right. This chart shows which data features influenced the predictions of the selected model. 

    In this example, the *duration* appears to have the most influence on the predictions of this model.
    
    ![Model explanation dashboard](media/tutorial-first-experiment-automated-ml/model-explanation-dashboard.png)

## Deploy the best model

The automated machine learning interface allows you to deploy the best model as a web service in a few steps. Deployment is the integration of the model so it can predict on new data and identify potential areas of opportunity. 

For this experiment, deployment to a web service means that the financial institution now has an iterative and scalable web solution for identifying potential fixed term deposit customers. 

Check to see if your experiment run is complete. To do so,  navigate back to the parent job page by selecting **Job 1** at the top of your screen. A **Completed** status is shown on the top left of the screen. 

Once the experiment run is complete, the **Details** page is populated with a **Best model summary** section. In this experiment context, **VotingEnsemble** is considered the best model, based on the **AUC_weighted** metric.  

We deploy this model, but be advised, deployment takes about 20 minutes to complete. The deployment process entails several steps including registering the model, generating resources, and configuring them for the web service.

1. Select **VotingEnsemble** to open the model-specific page.

1. Select the **Deploy** menu in the top-left and select **Deploy to web service**.

1. Populate the **Deploy a model** pane as follows:

    Field| Value
    ----|----
    Deployment name| my-automl-deploy
    Deployment description| My first automated machine learning experiment deployment
    Compute type | Select Azure Container Instance (ACI)
    Enable authentication| Disable. 
    Use custom deployments| Disable. Allows for the default driver file (scoring script) and environment file to be auto-generated. 
    
    For this example, we use the defaults provided in the *Advanced* menu. 

1. Select **Deploy**.  

    A green success message appears at the top of the **Job** screen, and in the **Model summary** pane, a status message appears under **Deploy status**. Select **Refresh** periodically to check the deployment status.
    
Now you have an operational web service to generate predictions. 

Proceed to the [**Next Steps**](#next-steps) to learn more about how to consume your new web service, and test your predictions using Power BI's built in Azure Machine Learning support.

## Clean up resources

Deployment files are larger than data and experiment files, so they cost more to store. Delete only the deployment files to minimize costs to your account, or if you want to keep your workspace and experiment files. Otherwise, delete the entire resource group, if you don't plan to use any of the files.  
