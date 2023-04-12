> Check [Loading models from registry](how-to-manage-models-mlflow.md#loading-models-from-registry) for more ways to reference models from the registry. 

Once the model is loaded, you can use to score new data:

```python
#Load Scoring Data into Spark Dataframe 
scoreDf = spark.table({table_name}).where({required_conditions}) 

#Make Prediction 
preds = (scoreDf 
           .withColumn('target_column_name', pyfunc_udf('Input_column1', 'Input_column2', ' Input_column3', …)) 
        ) 

display(preds) 
```

## Clean up resources

If you wish to keep your Azure Databricks workspace, but no longer need the Azure ML workspace, you can delete the Azure ML workspace. This action results in unlinking your Azure Databricks workspace and the Azure ML workspace. 

If you don't plan to use the logged metrics and artifacts in your workspace, the ability to delete them individually is unavailable at this time. Instead, delete the resource group that contains the storage account and workspace, so you don't incur any charges:

1. In the Azure portal, select **Resource groups** on the far left.

   ![Delete in the Azure portal](./media/how-to-use-mlflow-azure-databricks/delete-resources.png)

1. From the list, select the resource group you created.

1. Select **Delete resource group**.

1. Enter the resource group name. Then select **Delete**.

## Next steps
* [Deploy MLflow models as an Azure web service](how-to-deploy-mlflow-models.md). 
* [Manage your models](concept-model-management-and-deployment.md).
* [Track experiment jobs with MLflow and Azure Machine Learning](how-to-use-mlflow.md). 
* Learn more about [Azure Databricks and MLflow](/azure/databricks/applications/mlflow/).
