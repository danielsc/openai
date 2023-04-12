    Explain best model | Select to enable or disable, in order to show explanations for the recommended best model. <br> This functionality is not currently available for [certain forecasting algorithms](how-to-machine-learning-interpretability-automl.md#interpretability-during-training-for-the-best-model). 
    Blocked algorithm| Select algorithms you want to exclude from the training job. <br><br> Allowing algorithms is only available for [SDK experiments](how-to-configure-auto-train.md#supported-algorithms). <br> See the [supported algorithms for each task type](/python/api/azureml-automl-core/azureml.automl.core.shared.constants.supportedmodels).
    Exit criterion| When any of these criteria are met, the training job is stopped. <br> *Training job time (hours)*: How long to allow the training job to run. <br> *Metric score threshold*:  Minimum metric score for all pipelines. This ensures that if you have a defined target metric you want to reach, you do not spend more time on the training job than necessary.
    Concurrency| *Max concurrent iterations*: Maximum number of pipelines (iterations) to test in the training job. The job will not run more than the specified number of iterations. Learn more about how automated ML performs [multiple child jobs on clusters](how-to-configure-auto-train.md#multiple-child-runs-on-clusters).

1. (Optional) View featurization settings: if you choose to enable **Automatic featurization** in the **Additional configuration settings** form, default featurization techniques are applied. In the **View featurization settings** you can change these defaults and customize accordingly. Learn how to [customize featurizations](#customize-featurization). 

    ![Screenshot shows the Select task type dialog box with View featurization settings called out.](media/how-to-use-automated-ml-for-ml-models/view-featurization-settings.png)


1. The **[Optional] Validate and test** form allows you to do the following. 

    1. Specify the type of validation to be used for your training job. [Learn more about cross validation](how-to-configure-cross-validation-data-splits.md#prerequisites). 
    
        1. Forecasting tasks only supports k-fold cross validation.
    
    1. Provide a test dataset (preview) to evaluate the recommended model that automated ML generates for you at the end of your experiment. When you provide test data, a test job is automatically triggered at the end of your experiment. This test job is only job on the best model that was recommended by automated ML. Learn how to get the [results of the remote test job](#view-remote-test-job-results-preview).
    
        >[!IMPORTANT]
        > Providing a test dataset to evaluate generated models is a preview feature. This capability is an [experimental](/python/api/overview/azure/ml/#stable-vs-experimental) preview feature, and may change at any time.
        
        * Test data is considered a separate from training and validation, so as to not bias the results of the test job of the recommended model. [Learn more about bias during model validation](concept-automated-ml.md#training-validation-and-test-data).
        * You can either provide your own test dataset or opt to use a percentage of your training dataset. Test data must be in the form of an [Azure Machine Learning TabularDataset](./v1/how-to-create-register-datasets.md#tabulardataset).         
        * The schema of the test dataset should match the training dataset. The target column is optional, but if no target column is indicated no test metrics are calculated.
        * The test dataset should not be the same as the training dataset or the validation dataset.
        * Forecasting jobs do not support train/test split.
        
        ![Screenshot shows the form where to select validation data and test data](media/how-to-use-automated-ml-for-ml-models/validate-test-form.png)
        
## Customize featurization

In the **Featurization** form, you can enable/disable automatic featurization and customize the automatic featurization settings for your experiment. To open this form, see step 10 in the [Create and run experiment](#create-and-run-experiment) section. 
