    The first job may take up to 20 minutes. Since the default compute settings have a minimum node size of 0, the designer must allocate resources after being idle. Successive jobs take less time, since the nodes are already allocated. To speed up the running time, you can create a compute resources with a minimum node size of 1 or greater.

After the job finishes, you can check the results of each module:

1. Right-click the module whose output you want to see.
1. Select either **Visualize**, **View Output**, or **View Log**.

    - **Visualize**: Preview the results dataset.
    - **View Output**: Open a link to the output storage location. Use this to explore or download the output. 
    - **View Log**: View driver and system logs. Use the **70_driver_log** to see information related to your user-submitted script such as errors and exceptions.

> [!IMPORTANT]
> Designer components use open source Python packages to implement machine learning algorithms. However Studio (classic) uses a Microsoft internal C# library. Therefore, prediction result may vary between the designer and Studio (classic). 


## Save trained model to use in another pipeline

Sometimes you may want to save the model trained in a pipeline and use the model in another pipeline later. In Studio (classic), all trained models are saved in "Trained Models" category in the module list. In designer, the trained models are automatically registered as file dataset with a system generated name. Naming convention follows "MD - pipeline draft name - component name - Trained model ID" pattern. 

To give a trained model a meaningful name, you can register the output of **Train Model** component as a **file dataset**. Give it the name you want, for example linear-regression-model. 

![Screenshot showing how to save trained model.](./media/migrate-rebuild-experiment/save-model.png)

You can find the trained model in "Dataset" category in the component list or search it by name. Then connect the trained model to a **Score Model** component to use it for prediction. 

![Screenshot showing how to find trained model.](./media/migrate-rebuild-experiment/search-model-in-list.png)


## Next steps

In this article, you learned how to rebuild a Studio (classic) experiment in Azure Machine Learning. The next step is to [rebuild web services in Azure Machine Learning](migrate-rebuild-web-service.md).


See the other articles in the Studio (classic) migration series:

1. [Migration overview](migrate-overview.md).
1. [Migrate dataset](migrate-register-dataset.md).
1. **Rebuild a Studio (classic) training pipeline**.
1. [Rebuild a Studio (classic) web service](migrate-rebuild-web-service.md).
1. [Integrate an Azure Machine Learning web service with client apps](migrate-rebuild-integrate-with-client-app.md).
1. [Migrate Execute R Script](migrate-execute-r-script.md).