    1. On the **Datastore and file selection** form, select the default datastore that was automatically set up during your workspace creation, **workspaceblobstore (Azure Blob Storage)**. This is where you'll upload your data file to make it available to your workspace.

    1. Select **Upload files** from the **Upload** drop-down.
    
    1. Choose the **bankmarketing_train.csv** file on your local computer. This is the file you downloaded as a [prerequisite](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv).

    1. Select **Next** on the bottom left, to  upload it to the default container that was automatically set up during your workspace creation.  
    
       When the upload is complete, the **Settings and preview** form is pre-populated based on the file type. 
       
    1. Verify that the **Settings and preview** form is populated as follows and select **Next**.
        
        Field|Description| Value for tutorial
        ---|---|---
        File format|Defines the layout and type of data stored in a file.| Delimited
        Delimiter|One or more characters for specifying the boundary between&nbsp; separate, independent regions in plain text or other data streams. |Comma
        Encoding|Identifies what bit to character schema table to use to read your dataset.| UTF-8
        Column headers| Indicates how the headers of the dataset, if any, will be treated.| All files have same headers
        Skip rows | Indicates how many, if any, rows are skipped in the dataset.| None

    1. The **Schema** form allows for further configuration of your data for this experiment. For this example, select the toggle switch for the **day_of_week**, so as to not include it. Select **Next**.
         ![Schema form](./media/tutorial-first-experiment-automated-ml/schema-tab-config.gif)
    1. On the **Confirm details** form, verify the information matches what was previously  populated on the **Basic info, Datastore and file selection** and **Settings and preview** forms.
    
    1. Select **Create** to complete the creation of your dataset.
    
    1. Select your dataset once it appears in the list.
    
    1. Review the **Data preview**  to ensure you didn't include **day_of_week** then, select **Close**.

    1. Select  **Next**.

## Configure job

After you load and configure your data, you can set up your experiment. This setup includes experiment design tasks such as, selecting the size of your compute environment and specifying what column you want to predict. 

1. Select the **Create new** radio button.

1. Populate the **Configure Job** form as follows:
    1. Enter this experiment name: `my-1st-automl-experiment`

    1. Select **y** as the target column, what you want to predict. This column indicates whether the client subscribed to a term deposit or not.
    
    1. Select **compute cluster** as your compute type. 
    
    1.  **+New** to configure your compute target. A compute target is a local or cloud-based resource environment used to run your training script or host your service deployment. For this experiment, we use a cloud-based compute. 
        1. Populate the **Select virtual machine** form to set up your compute.

            Field | Description | Value for tutorial
            ----|---|---
            Location | Your region that you'd like to run the machine from |West US 2
            Virtual&nbsp;machine&nbsp;tier |Select what priority your experiment should have| Dedicated
            Virtual&nbsp;machine&nbsp;type| Select the virtual machine type for your compute.|CPU (Central Processing Unit)
            Virtual&nbsp;machine&nbsp;size| Select the virtual machine size for your compute. A list of recommended sizes is provided based on your data and experiment type. |Standard_DS12_V2
        
        1. Select **Next** to populate the **Configure settings form**.
        
            Field | Description | Value for tutorial
            ----|---|---
