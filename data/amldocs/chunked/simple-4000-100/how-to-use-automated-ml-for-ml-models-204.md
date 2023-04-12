>  * [Many models and hiearchical time series forecasting training (preview)](how-to-auto-train-forecast.md)
>  * [Forecasting tasks where deep learning neural networks (DNN) are enabled](how-to-auto-train-forecast.md#enable-deep-learning)
>  * [Automated ML jobs from local computes or Azure Databricks clusters](how-to-configure-auto-train.md#compute-to-run-experiment)

To view the test job metrics of the recommended model,
 
1. Navigate to the **Models** page, select the best model. 
1. Select the **Test results (preview)** tab. 
1. Select the job you want, and view the **Metrics** tab.
    ![Test results tab of automatically tested, recommended model](./media/how-to-use-automated-ml-for-ml-models/test-best-model-results.png)
    
To view the test predictions used to calculate the test metrics, 

1. Navigate to the bottom of the page and select the link under **Outputs dataset** to open the dataset. 
1. On the **Datasets** page, select the **Explore** tab to view the predictions from the test job.
    1. Alternatively, the prediction file can also be viewed/downloaded from the **Outputs + logs** tab, expand the **Predictions** folder to locate your `predicted.csv` file.

Alternatively, the predictions file can also be viewed/downloaded from the Outputs + logs tab, expand Predictions folder to locate your predictions.csv file.

The model test job generates the predictions.csv file that's stored in the default datastore created with the workspace. This datastore is visible to all users with the same subscription. Test jobs are not recommended for scenarios if any of the information used for or created by the test job needs to remain private.

## Test an existing automated ML model (preview)

>[!IMPORTANT]
> Testing your models with a test dataset to evaluate generated models is a preview feature. This capability is an [experimental](/python/api/overview/azure/ml/#stable-vs-experimental) preview feature, and may change at any time.

> [!WARNING]
> This feature is not available for the following automated ML scenarios
>  * [Computer vision tasks](how-to-auto-train-image-models.md)
>  * [Many models and hiearchical time series forecasting training (preview)](how-to-auto-train-forecast.md)
>  * [Forecasting tasks where deep learning neural networks (DNN) are enabled](how-to-auto-train-forecast.md#enable-deep-learning)
>  * [Automated ML runs from local computes or Azure Databricks clusters](how-to-configure-auto-train.md#compute-to-run-experiment)

After your experiment completes, you can test the model(s) that automated ML generates for you. If you want to test a different automated ML generated model, not the recommended model, you can do so with the following steps. 

1. Select an existing automated ML experiment job.  
1. Navigate to the **Models** tab of the job and select the completed model you want to test.
1. On the model **Details** page, select the **Test model(preview)** button to open the **Test model** pane.
1. On the **Test model** pane, select the compute cluster and a test dataset you want to use for your test job. 
1. Select the **Test** button. The schema of the test dataset should match the training dataset, but the **target column** is optional.
1. Upon successful creation of model test job, the **Details** page displays a success message. Select the **Test results** tab to see the progress of the job.

1. To view the results of the test job, open the **Details** page and follow the steps in the [view results of the remote test job](#view-remote-test-job-results-preview) section. 

    ![Test model form](./media/how-to-use-automated-ml-for-ml-models/test-model-form.png)
    

## Model explanations (preview)

To better understand your model, you can see which data features (raw or engineered) influenced the model's predictions with the model explanations dashboard. 

The model explanations dashboard provides an overall analysis of the trained model along with its predictions and explanations. It also lets you drill into an individual data point and its individual feature importance. [Learn more about the explanation dashboard visualizations](how-to-machine-learning-interpretability-aml.md#visualizations).
