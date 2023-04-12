1. Online endpoint names need to be unique, so change `taxi-online-$(namespace)$(postfix)$(environment)` to another unique name and then select **Run**. No need to change the default if it doesn't fail.

   ![Screenshot of Azure DevOps batch deploy script.](./media/how-to-setup-mlops-azureml/ADO-batch-pipeline.png)
   
> [!IMPORTANT]
> If the run fails due to an existing online endpoint name, recreate the pipeline as described previously and change **[your endpoint-name]** to **[your endpoint-name (random number)]**
   
1. When the run completes, you'll see output similar to the following image:
   
   ![Screenshot of ADO Pipeline batch run result page.](./media/how-to-setup-mlops-azureml/ADO-batch-pipeline-run.png)
   
   Now the Prototyping Loop is connected to the Operationalizing Loop of the MLOps Architecture and inference has been run.

## Clean up resources

1. If you're not going to continue to use your pipeline, delete your Azure DevOps project. 
1. In Azure portal, delete your resource group and Azure Machine Learning instance.

## Next steps

* [Install and set up Python SDK v2](https://aka.ms/sdk-v2-install)
* [Install and set up Python CLI v2](how-to-configure-cli.md)
* [Azure MLOps (v2) solution accelerator](https://github.com/Azure/mlops-v2) on GitHub
* Learn more about [Azure Pipelines with Azure Machine Learning](how-to-devops-machine-learning.md)
* Learn more about [GitHub Actions with Azure Machine Learning](how-to-github-actions-machine-learning.md)
* Deploy MLOps on Azure in Less Than an Hour - [Community MLOps V2 Accelerator video](https://www.youtube.com/watch?v=5yPDkWCMmtk)
