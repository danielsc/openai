Delete the starter pipeline and replace it with the following YAML code. In this pipeline, you'll:

* Use the Python version task to set up Python 3.8 and install the SDK requirements.
* Use the Bash task to run bash scripts for the Azure Machine Learning SDK and CLI.
* Use the Azure CLI task to pass the values of your three variables and use papermill to run your Jupyter notebook and push output to AzureML. 

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.8'
- script: pip install -r sdk/python/dev-requirements.txt
  displayName: 'pip install notebook reqs'
- task: Bash@3
  inputs:
    filePath: 'sdk/python/setup.sh'
  displayName: 'set up sdk'

- task: Bash@3
  inputs:
    filePath: 'cli/setup.sh'
  displayName: 'set up CLI'

- task: AzureCLI@2
  inputs:
    azureSubscription: 'your-azure-subscription'
    scriptType: 'bash'
    scriptLocation: 'inlineScript'
    inlineScript: |
           sed -i -e "s/<SUBSCRIPTION_ID>/$(SUBSCRIPTION_ID)/g" sklearn-diabetes.ipynb
           sed -i -e "s/<RESOURCE_GROUP>/$(RESOURCE_GROUP)/g" sklearn-diabetes.ipynb
           sed -i -e "s/<AML_WORKSPACE_NAME>/$(AZUREML_WORKSPACE_NAME)/g" sklearn-diabetes.ipynb
           sed -i -e "s/DefaultAzureCredential/AzureCliCredential/g" sklearn-diabetes.ipynb
           papermill -k python sklearn-diabetes.ipynb sklearn-diabetes.output.ipynb
    workingDirectory: 'sdk/python/jobs/single-step/scikit-learn/diabetes'
```


## Step 7: Verify your pipeline run

1. Open your completed pipeline run and view the AzureCLI task. Check the task view to verify that the output task finished running. 
 
   :::image type="content" source="media/how-to-devops-machine-learning/machine-learning-azurecli-output.png" alt-text="Screenshot of machine learning output to AzureML.":::

1. Open Azure Machine Learning studio and navigate to the completed `sklearn-diabetes-example` job. On the **Metrics** tab, you should see the training results. 

    :::image type="content" source="media/how-to-devops-machine-learning/machine-learning-training-results.png" alt-text="Screenshot of training results.":::

## Clean up resources

If you're not going to continue to use your pipeline, delete your Azure DevOps project. In Azure portal, delete your resource group and Azure Machine Learning instance.