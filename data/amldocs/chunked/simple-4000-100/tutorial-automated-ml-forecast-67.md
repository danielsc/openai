        Column headers| Indicates how the headers of the dataset, if any, will be treated.| Only first file has headers
        Skip rows | Indicates how many, if any, rows are skipped in the dataset.| None

    1. The **Schema** form allows for further configuration of your data for this experiment. 
    
        1. For this example, choose to ignore the **casual** and **registered** columns. These columns are a breakdown of the  **cnt** column so, therefore we don't include them.

        1. Also for this example, leave the defaults for the **Properties** and **Type**. 
        
        1. Select **Next**.

    1. On the **Confirm details** form, verify the information matches what was previously  populated on the **Basic info** and **Settings and preview** forms.

    1. Select **Create** to complete the creation of your dataset.

    1. Select your dataset once it appears in the list.

    1. Select  **Next**.

## Configure job

After you load and configure your data, set up your remote compute target and select which column in your data you want to predict.

1. Populate the **Configure job** form as follows:
    1. Enter an experiment name: `automl-bikeshare`

    1. Select **cnt** as the target column, what you want to predict. This column indicates the number of total bike share rentals.

    1. Select **compute cluster** as your compute type. 

    1. Select **+New** to configure your compute target. Automated ML only supports Azure Machine Learning compute. 

        1. Populate the **Select virtual machine** form to set up your compute.

            Field | Description | Value for tutorial
            ----|---|---
            Virtual&nbsp;machine&nbsp;tier |Select what priority your experiment should have| Dedicated
            Virtual&nbsp;machine&nbsp;type| Select the virtual machine type for your compute.|CPU (Central Processing Unit)
            Virtual&nbsp;machine&nbsp;size| Select the virtual machine size for your compute. A list of recommended sizes is provided based on your data and experiment type. |Standard_DS12_V2
        
        1. Select **Next** to populate the **Configure settings form**.
        
             Field | Description | Value for tutorial
            ----|---|---
            Compute name |	A unique name that identifies your compute context. | bike-compute
            Min / Max nodes| To profile data, you must specify 1 or more nodes.|Min nodes: 1<br>Max nodes: 6
            Idle seconds before scale down | Idle time before  the cluster is automatically scaled down to the minimum node count.|120 (default)
            Advanced settings | Settings to configure and authorize a virtual network for your experiment.| None 
  
        1. Select **Create** to get the compute target. 

            **This takes a couple minutes to complete.** 

        1. After creation, select your new compute target from the drop-down list.

    1. Select **Next**.

## Select forecast settings

Complete the setup for your automated ML experiment by specifying the machine learning task type and configuration settings.

1. On the **Task type and settings** form, select **Time series forecasting** as the machine learning task type.

1. Select **date** as your **Time column** and leave **Time series identifiers** blank. 

1. The **Frequency** is how often your historic data is collected. Keep **Autodetect** selected. 
1.
1. The **forecast horizon** is the length of time into the future you want to predict.  Deselect **Autodetect** and type 14 in the field. 

1. Select **View additional configuration settings** and populate the fields as follows. These settings are to better control the training job and specify settings for your forecast. Otherwise, defaults are applied based on experiment selection and data.

    Additional&nbsp;configurations|Description|Value&nbsp;for&nbsp;tutorial
    ------|---------|---
    Primary metric| Evaluation metric that the machine learning algorithm will be measured by.|Normalized root mean squared error
