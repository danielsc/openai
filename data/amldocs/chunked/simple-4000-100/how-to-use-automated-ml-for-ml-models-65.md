    1. The **Schema** form is intelligently populated based on the selections in the **Settings and preview** form. Here configure the data type for each column, review the column names, and select which columns to **Not include** for your experiment. 
            
        Select **Next.**

    1. The **Confirm details** form is a summary of the information previously populated in the **Basic info** and **Settings and preview** forms. You also have the option to create a data profile for your dataset using a profiling enabled compute. Learn more about [data profiling](v1/how-to-connect-data-ui.md#profile).

        Select **Next**.
1. Select your newly created dataset once it appears. You are also able to view a preview of the dataset and sample statistics. 

1. On the **Configure job** form, select **Create new** and enter **Tutorial-automl-deploy** for the experiment name.

1. Select a target column; this is the column that you would like to do predictions on.

1. Select a compute type for the data profiling and training job. You can select a [compute cluster](concept-compute-target.md#azure-machine-learning-compute-managed) or [compute instance](concept-compute-instance.md). 
    
1. Select a compute from the dropdown list of your existing computes.  To create a new compute, follow the instructions in step 8.

1. Select **Create a new compute** to configure your compute context for this experiment.

    Field|Description
    ---|---
    Compute name| Enter a unique name that identifies your compute context.
    Virtual machine priority| Low priority virtual machines are cheaper but don't guarantee the compute nodes. 
    Virtual machine type| Select CPU or GPU for virtual machine type.
    Virtual machine size| Select the virtual machine size for your compute.
    Min / Max nodes| To profile data, you must specify 1 or more nodes. Enter the maximum number of nodes for your compute. The default is 6 nodes for an AzureML Compute.
    Advanced settings | These settings allow you to configure a user account and existing virtual network for your experiment. 
    
    Select **Create**. Creation of a new compute can take a few minutes.

    >[!NOTE]
    > Your compute name will indicate if the compute you select/create is *profiling enabled*. (See the section [data profiling](v1/how-to-connect-data-ui.md#profile) for more details).

    Select **Next**.

1. On the **Task type and settings** form, select the task type: classification, regression, or forecasting. See [supported task types](concept-automated-ml.md#when-to-use-automl-classification-regression-forecasting-computer-vision--nlp) for more information.

    1. For **classification**, you can also enable deep learning.
    
        If deep learning is enabled, validation is limited to _train_validation split_. [Learn more about validation options](how-to-configure-cross-validation-data-splits.md).

    1. For **forecasting** you can, 
    
        1. Enable deep learning.
    
        1. Select *time column*: This column contains the time data to be used.

        1. Select *forecast horizon*: Indicate how many time units (minutes/hours/days/weeks/months/years) will the model be able to predict to the future. The further the model is required to predict into the future, the less accurate it becomes. [Learn more about forecasting and forecast horizon](how-to-auto-train-forecast.md).

1. (Optional) View addition configuration settings: additional settings you can use to better control the training job. Otherwise, defaults are applied based on experiment selection and data. 

    Additional configurations|Description
    ------|------
    Primary metric| Main metric used for scoring your model. [Learn more about model metrics](how-to-configure-auto-train.md#primary-metric).
    Explain best model | Select to enable or disable, in order to show explanations for the recommended best model. <br> This functionality is not currently available for [certain forecasting algorithms](how-to-machine-learning-interpretability-automl.md#interpretability-during-training-for-the-best-model). 
