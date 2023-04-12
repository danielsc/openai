1. Run the pipeline; it will take a few minutes to finish. The pipeline should create the following artifacts:
   * Resource Group for your Workspace including Storage Account, Container Registry, Application Insights, Keyvault and the Azure Machine Learning Workspace itself.
   * In the workspace, there's also a compute cluster created.
   
1. Now the Operationalizing Loop of the MLOps Architecture is deployed.
    ![Screenshot of ADO Infra Pipeline screen.](./media/how-to-setup-mlops-azureml/ADO-infra-pipeline.png)

    > [!NOTE]
    > The **Unable move and reuse existing repository to required location** warnings may be ignored.

## Deploying model training pipeline and moving to test environment

1. Go to ADO pipelines
   
   ![Screenshot of ADO Pipelines.](./media/how-to-setup-mlops-azureml/ADO-pipelines.png)

1. Select **New Pipeline**.
   
   ![Screenshot of ADO New Pipeline button.](./media/how-to-setup-mlops-azureml/ADO-new-pipeline.png)
   
1. Select **Azure Repos Git**.
   
   ![Screenshot of ADO Where's your code.](./media/how-to-setup-mlops-azureml/ado-wheresyourcode.png)
   
1. Select the repository that you cloned in from the previous section `mlopsv2`
   
1. Select **Existing Azure Pipeline YAML File**
   
   ![Screenshot of ADO Pipeline page on configure step.](./media/how-to-setup-mlops-azureml/ADO-configure-pipelines.png)
   
1. Select `main` as a branch and choose `/mlops/devops-pipelines/deploy-model-training-pipeline.yml`, then select **Continue**.  

1. **Save and Run** the pipeline
   
> [!NOTE]
> At this point, the infrastructure is configured and the Prototyping Loop of the MLOps Architecture is deployed. you're ready to move to our trained model to production.      

## Moving to production environment and deploying model 
         
**Prepare Data**
   - This component takes multiple taxi datasets (yellow and green) and merges/filters the data, and prepare the train/val and evaluation datasets.
   - Input: Local data under ./data/ (multiple .csv files)
   - Output: Single prepared dataset (.csv) and train/val/test datasets.

**Train Model**
   - This component trains a Linear Regressor with the training set.
   - Input: Training dataset
   - Output: Trained model (pickle format)
   
**Evaluate Model**
   - This component uses the trained model to predict taxi fares on the test set.
   - Input: ML model and Test dataset
   - Output: Performance of model and a deploy flag whether to deploy or not.
   - This component compares the performance of the model with all previous deployed models on the new test dataset and decides whether to promote or not model into production. Promoting model into production happens by registering the model in AML workspace.

**Register Model**
   - This component scores the model based on how accurate the predictions are in the test set.
   - Input: Trained model and the deploy flag.
   - Output: Registered model in Azure Machine Learning.

### Deploy ML model endpoint
1. Go to ADO pipelines
   
   ![Screenshot of ADO Pipelines.](./media/how-to-setup-mlops-azureml/ADO-pipelines.png)

1. Select **New Pipeline**.
   
   ![Screenshot of ADO New Pipeline button for endpoint.](./media/how-to-setup-mlops-azureml/ADO-new-pipeline.png)
   
1. Select **Azure Repos Git**.
   
   ![Screenshot of ADO Where's your code.](./media/how-to-setup-mlops-azureml/ado-wheresyourcode.png)
   
1. Select the repository that you cloned in from the previous section `mlopsv2`
   
1. Select **Existing Azure Pipeline YAML File**
   
   ![Screenshot of Azure DevOps Pipeline page on configure step.](./media/how-to-setup-mlops-azureml/ADO-configure-pipelines.png)
   
1. Select `main` as a branch and choose Managed Online Endpoint `/mlops/devops-pipelines/deploy-online-endpoint-pipeline.yml` then select **Continue**.  
   
1. Online endpoint names need to be unique, so change `taxi-online-$(namespace)$(postfix)$(environment)` to another unique name and then select **Run**. No need to change the default if it doesn't fail.
