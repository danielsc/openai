In the **Featurization** form, you can enable/disable automatic featurization and customize the automatic featurization settings for your experiment. To open this form, see step 10 in the [Create and run experiment](#create-and-run-experiment) section. 

The following table summarizes the customizations currently available via the studio. 

Column| Customization
---|---
Included | Specifies which columns to include for training.
Feature type| Change the value type for the selected column.
Impute with| Select what value to impute missing values with in your data.

![Azure Machine Learning studio custom featurization](media/how-to-use-automated-ml-for-ml-models/custom-featurization.png)

## Run experiment and view results

Select **Finish** to run your experiment. The experiment preparing process can take up to 10 minutes. Training jobs can take an additional 2-3 minutes more for each pipeline to finish running.

> [!NOTE]
> The algorithms automated ML employs have inherent randomness that can cause slight variation in a recommended model's final metrics score, like accuracy. Automated ML also performs operations on data such as train-test split, train-validation split or cross-validation when necessary. So if you run an experiment with the same configuration settings and primary metric multiple times, you'll likely see variation in each experiments final metrics score due to these factors. 

### View experiment details

The **Job Detail** screen opens to the **Details** tab. This screen shows you a summary of the experiment job including a status bar at the top next to the job number. 

The **Models** tab contains a list of the models created ordered by the metric score. By default, the model that scores the highest based on the chosen metric is at the top of the list. As the training job tries out more models, they are added to the list. Use this to get a quick comparison of the metrics for the models produced so far.

![Job detail](./media/how-to-use-automated-ml-for-ml-models/explore-models.gif)

### View training job details

Drill down on any of the completed models to see training job details. On the **Model** tab view details like a model summary and the hyperparameters used for the selected model. 

[![Hyperparameter details](media/how-to-use-automated-ml-for-ml-models/hyperparameter-button.png)](media/how-to-use-automated-ml-for-ml-models/hyperparameter-details.png)

 You can also see model specific performance metric charts on the **Metrics** tab. [Learn more about charts](how-to-understand-automated-ml.md).

![Iteration details](media/how-to-use-automated-ml-for-ml-models/iteration-details-expanded.png)

On the Data transformation tab, you can see a diagram of what data preprocessing, feature engineering, scaling techniques and the machine learning algorithm that were applied to generate this model.

>[!IMPORTANT]
> The Data transformation tab is in preview. This capability should be considered [experimental](/python/api/overview/azure/ml/#stable-vs-experimental) and may change at any time.

![Data transformation](./media/how-to-use-automated-ml-for-ml-models/data-transformation.png)

## View remote test job results (preview)

If you specified a test dataset or opted for a train/test split during your experiment setup-- on the **Validate and test** form, automated ML automatically tests the recommended model by default. As a result, automated ML calculates test metrics to determine the quality of the recommended model and its predictions. 

>[!IMPORTANT]
> Testing your models with a test dataset to evaluate generated models is a preview feature. This capability is an [experimental](/python/api/overview/azure/ml/#stable-vs-experimental) preview feature, and may change at any time.

> [!WARNING]
> This feature is not available for the following automated ML scenarios
>  * [Computer vision tasks](how-to-auto-train-image-models.md)
>  * [Many models and hiearchical time series forecasting training (preview)](how-to-auto-train-forecast.md)
