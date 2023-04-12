### Set up source repository with Azure DevOps
   
1. Open the project you created in [Azure DevOps](https://dev.azure.com/)
   
1. Open the Repos section and select **Import Repository**

    ![Screenshot of Azure DevOps import repo first time.](./media/how-to-setup-mlops-azureml/import_repo_first_time.png)

1. Enter https://github.com/Azure/mlops-v2-ado-demo into the Clone URL field. Select import at the bottom of the page

    ![Screenshot of Azure DevOps import MLOps demo repo.](./media/how-to-setup-mlops-azureml/import_repo_Git_template.png)

1. Open the **Project settings** at the bottom of the left hand navigation pane

1.  Under the Repos section, select **Repositories**. Select the repository you created in **Step 6.** Select the **Security** tab

1. Under the User permissions section, select the **mlopsv2 Build Service** user. Change the permission **Contribute** permission to **Allow** and the **Create branch** permission to **Allow**.
   ![Screenshot of Azure DevOps permissions.](./media/how-to-setup-mlops-azureml/ado-permissions-repo.png)

1. Open the **Pipelines** section in the left hand navigation pane and select on the 3 vertical dots next to the **Create Pipelines** button. Select **Manage Security**

   ![Screenshot of Pipeline security.](./media/how-to-setup-mlops-azureml/ado-open-pipelinesSecurity.png)

1. Select the **mlopsv2 Build Service** account for your project under the Users section. Change the permission **Edit build pipeline** to **Allow**

   ![Screenshot of Add security.](./media/how-to-setup-mlops-azureml/ado-add-pipelinesSecurity.png)

> [!NOTE]
> This finishes the prerequisite section and the deployment of the solution accelerator can happen accordingly.


## Deploying infrastructure via Azure DevOps
This step deploys the training pipeline to the Azure Machine Learning workspace created in the previous steps. 

> [!TIP]
> Make sure you understand the [Architectural Patterns](/azure/architecture/data-guide/technology-choices/machine-learning-operations-v2) of the solution accelerator before you checkout the MLOps v2 repo and deploy the infrastructure. In examples you'll use the [classical ML project type](/azure/architecture/data-guide/technology-choices/machine-learning-operations-v2#classical-machine-learning-architecture).

### Run Azure infrastructure pipeline
1. Go to your repository, `mlops-v2-ado-demo`, and select the **config-infra-prod.yml** file.

    > [!IMPORTANT]
    > Make sure you've selected the **main** branch of the repo.
   
   ![Screenshot of Repo in ADO.](./media/how-to-setup-mlops-azureml/ADO-repo.png)
   
   This config file uses the namespace and postfix values the names of the artifacts to ensure uniqueness. Update the following section in the config to your liking.
   
   ```
    namespace: [5 max random new letters]
    postfix: [4 max random new digits]
    location: eastus
   ```
   > [!NOTE]
   > If you are running a Deep Learning workload such as CV or NLP, ensure your GPU compute is available in your deployment zone.

1. Select Commit and push code to get these values into the pipeline. 

1. Go to Pipelines section 
   
   ![Screenshot of ADO Pipelines.](./media/how-to-setup-mlops-azureml/ADO-pipelines.png)
   
1. Select **New Pipeline**.
   
   ![Screenshot of ADO New Pipeline button for infra.](./media/how-to-setup-mlops-azureml/ADO-new-pipeline.png)
   
1. Select **Azure Repos Git**.
   
   ![Screenshot of ADO Where's your code.](./media/how-to-setup-mlops-azureml/ado-wheresyourcode.png)
   
1. Select the repository that you cloned in from the previous section `mlops-v2-ado-demo`
   
1. Select **Existing Azure Pipeline YAML File**
   
   ![Screenshot of Azure DevOps Pipeline page on configure step.](./media/how-to-setup-mlops-azureml/ADO-configure-pipelines.png)
   
   
1. Select the `main` branch and choose `mlops/devops-pipelines/cli-ado-deploy-infra.yml`, then select **Continue**. 

1. Run the pipeline; it will take a few minutes to finish. The pipeline should create the following artifacts:
