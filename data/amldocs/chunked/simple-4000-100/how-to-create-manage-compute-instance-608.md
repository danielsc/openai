You can set up other applications, such as RStudio, or Posit Workbench (formerly RStudio Workbench), when creating a compute instance. Follow these steps in studio to set up a custom application on your compute instance

1.	Fill out the form to [create a new compute instance](?tabs=azure-studio#create)
1.	Select **Next: Advanced Settings**
1.	Select **Add application** under the **Custom application setup (RStudio Workbench, etc.)** section
 
:::image type="content" source="media/how-to-create-manage-compute-instance/custom-service-setup.png" alt-text="Screenshot showing Custom Service Setup.":::

### Setup Posit Workbench (formerly RStudio Workbench)

RStudio is one of the most popular IDEs among R developers for ML and data science projects. You can easily set up Posit Workbench, which provides access to RStudio along with other development tools, to run on your compute instance, using your own Posit license, and access the rich feature set that Posit Workbench offers

1.	Follow the steps listed above to **Add application** when creating your compute instance.
1.	Select **Posit Workbench (bring your own license)** in the **Application** dropdown and enter your Posit Workbench license key in the **License key** field. You can get your Posit Workbench license or trial license [from posit](https://posit.co). 
1. Select **Create** to add Posit Workbench application to your compute instance.
 
:::image type="content" source="media/how-to-create-manage-compute-instance/rstudio-workbench.png" alt-text="Screenshot shows Posit Workbench settings." lightbox="media/how-to-create-manage-compute-instance/rstudio-workbench.png":::

[!INCLUDE [private link ports](../../includes/machine-learning-private-link-ports.md)]

> [!NOTE]
> * Support for accessing your workspace file store from Posit Workbench is not yet available.
> * When accessing multiple instances of Posit Workbench, if you see a "400 Bad Request. Request Header Or Cookie Too Large" error, use a new browser or access from a browser in incognito mode.
 

### Setup RStudio (open source)

To use RStudio, set up a custom application as follows:

1.	Follow the steps listed above to **Add application** when creating your compute instance.
1.	Select **Custom Application** on the **Application** dropdown 
1.	Configure the **Application name** you would like to use.
1. Set up the application to run on **Target port** `8787` - the docker image for RStudio open source listed below needs to run on this Target port. 

1. Set up the application to be accessed on **Published port** `8787` - you can configure the application to be accessed on a different Published port if you wish.
1. Point the **Docker image** to `ghcr.io/azure/rocker-rstudio-ml-verse:latest`. 

1. Select **Create** to set up RStudio as a custom application on your compute instance.

:::image type="content" source="media/how-to-create-manage-compute-instance/rstudio-open-source.png" alt-text="Screenshot shows form to set up RStudio as a custom application" lightbox="media/how-to-create-manage-compute-instance/rstudio-open-source.png":::

[!INCLUDE [private link ports](../../includes/machine-learning-private-link-ports.md)]
 
### Setup other custom applications

Set up other custom applications on your compute instance by providing the application on a Docker image.

1. Follow the steps listed above to **Add application** when creating your compute instance.
1. Select **Custom Application** on the **Application** dropdown. 
1. Configure the **Application name**, the **Target port** you wish to run the application on, the **Published port** you wish to access the application on and the **Docker image** that contains your application.
1. Optionally, add **Environment variables**  you wish to use for your application.
1. Use **Bind mounts** to add access to the files in your default storage account: 
   * Specify **/home/azureuser/cloudfiles** for **Host path**.  
   * Specify **/home/azureuser/cloudfiles** for the **Container path**.
