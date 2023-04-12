        1. Select **Next** to populate the **Configure settings form**.
        
            Field | Description | Value for tutorial
            ----|---|---
            Compute name |	A unique name that identifies your compute context. | automl-compute
            Min / Max nodes| To profile data, you must specify 1 or more nodes.|Min nodes: 1<br>Max nodes: 6
            Idle seconds before scale down | Idle time before  the cluster is automatically scaled down to the minimum node count.|120 (default)
            Advanced settings | Settings to configure and authorize a virtual network for your experiment.| None               

        1. Select **Create** to create your compute target. 

            **This takes a couple minutes to complete.** 

             ![Settings page](./media/tutorial-first-experiment-automated-ml/compute-settings.png)

        1. After creation, select your new compute target from the drop-down list.

    1. Select **Next**.

1. On the **Select task and settings** form, complete the setup for your automated ML experiment by specifying the machine learning task type and configuration settings.
    
    1.  Select **Classification** as the machine learning task type.

    1. Select **View additional configuration settings** and populate the fields as follows. These settings are to better control the training job. Otherwise, defaults are applied based on experiment selection and data.

        Additional&nbsp;configurations|Description|Value&nbsp;for&nbsp;tutorial
        ------|---------|---
        Primary metric| Evaluation metric that the machine learning algorithm will be measured by.|AUC_weighted
        Explain best model| Automatically shows explainability on the best model created by automated ML.| Enable
        Blocked algorithms | Algorithms you want to exclude from the training job| None
        Additional&nbsp;classification settings | These settings help improve the accuracy of your model |Positive class label: None
        Exit criterion| If a criteria is met, the training job is stopped. |Training&nbsp;job&nbsp;time (hours): 1 <br> Metric&nbsp;score&nbsp;threshold: None
        Concurrency| The maximum number of parallel iterations executed per iteration| Max&nbsp;concurrent&nbsp;iterations: 5
        
        Select **Save**.
    1. Select **Next**.
    
1. On the **[Optional] Validate and test** form, 
    1. Select k-fold cross-validation as your **Validation type**.
    1.  Select 2 as your **Number of cross validations**.

1. Select **Finish** to run the experiment. The **Job Detail**  screen opens with the **Job status** at the top as the experiment preparation begins. This status updates as the experiment progresses. Notifications also appear in the top right corner of the studio to inform you of the status of your experiment.

>[!IMPORTANT]
> Preparation takes **10-15 minutes** to prepare the experiment run.
> Once running, it takes **2-3 minutes more for each iteration**.  <br> <br>
> In production, you'd likely walk away for a bit. But for this tutorial, we suggest you start exploring the tested algorithms on the **Models** tab as they complete while the others are still running. 

##  Explore models

Navigate to the **Models** tab to see the algorithms (models) tested. By default, the models are ordered by metric score as they complete. For this tutorial, the model that scores the highest based on the chosen **AUC_weighted** metric is at the top of the list.

While you wait for all of the experiment models to finish, select the **Algorithm name** of a completed model to explore its performance details. 

The following navigates through the **Details** and the **Metrics** tabs to view the selected model's properties, metrics, and performance charts. 

![Run iteration detail](./media/tutorial-first-experiment-automated-ml/run-detail.gif)

## Model explanations

While you wait for the models to complete, you can also take a look at model explanations and see which data features (raw or engineered) influenced a particular model's predictions. 
