:::image type="content" source="./media/how-to-create-data-assets/data-assets-create.png" alt-text="Screenshot highlights Create in the Data assets tab.":::

1. Give your data asset a name and optional description. Then, select the **Tabular** option under **Type**, in the **Dataset types** section of the dropdown.
    > [!NOTE]
    > You can also upload ZIP files as data assets. To upload a ZIP file, select **File** for **Type**, in the **Dataset types** section of the dropdown.
:::image type="content" source="./media/migrate-register-dataset/create-data-asset.png" alt-text="Screenshot shows data asset source choices.":::

1. For data source, select the "From local files" option to upload your dataset.

1. For file selection, first choose where you want your data to be stored in Azure. You will be selecting an Azure Machine Learning datastore. For more information on datastores, see [Connect to storage services](v1/how-to-access-data.md). Next, upload the dataset you downloaded earlier.

1. Follow the steps to set the data parsing settings and schema for your data asset.

1. Once you reach the Review step, click Create on the last page

## Import data from cloud sources

If your data is already in a cloud storage service, and you want to keep your data in its native location. You can use either of the following options:

|Ingestion method|Description|
|---| --- |
|Register an Azure Machine Learning dataset|Ingest data from local and online data sources (Blob, ADLS Gen1, ADLS Gen2, File share, SQL DB). <br><br>Creates a reference to the data source, which is lazily evaluated at runtime. Use this option if you repeatedly access this dataset and want to enable advanced data features like data versioning and monitoring.
|Import Data module|Ingest data from online data sources (Blob, ADLS Gen1, ADLS Gen2, File share, SQL DB). <br><br> The dataset is only imported to the current designer pipeline run.


>[!Note]
> Studio (classic) users should note that the following cloud sources are not natively supported in Azure Machine Learning:
> - Hive Query
> - Azure Table
> - Azure Cosmos DB
> - On-premises SQL Database
>
> We recommend that users migrate their data to a supported storage services using Azure Data Factory.  

### Register an Azure Machine Learning dataset

Use the following steps to register a dataset to Azure Machine Learning from a cloud service: 

1. [Create a datastore](v1/how-to-connect-data-ui.md#create-datastores), which links the cloud storage service to your Azure Machine Learning workspace. 

1. [Register a dataset](v1/how-to-connect-data-ui.md#create-data-assets). If you are migrating a Studio (classic) dataset, select the **Tabular** dataset setting.

After you register a dataset in Azure Machine Learning, you can use it in designer:
 
1. Create a new designer pipeline draft.
1. In the module palette to the left, expand the **Datasets** section.
1. Drag your registered dataset onto the canvas. 

### Use the Import Data module

Use the following steps to import data directly to your designer pipeline:

1. [Create a datastore](v1/how-to-connect-data-ui.md#create-datastores), which links the cloud storage service to your Azure Machine Learning workspace. 

After you create the datastore, you can use the [**Import Data**](algorithm-module-reference/import-data.md) module in the designer to ingest data from it:

1. Create a new designer pipeline draft.
1. In the module palette to the left, find the **Import Data** module and drag it to the canvas.
1. Select the **Import Data** module, and use the settings in the right panel to configure your data source.

## Next steps

In this article, you learned how to migrate a Studio (classic) dataset to Azure Machine Learning. The next step is to [rebuild a Studio (classic) training pipeline](migrate-rebuild-experiment.md).


See the other articles in the Studio (classic) migration series:

1. [Migration overview](migrate-overview.md).
1. **Migrate datasets**.
1. [Rebuild a Studio (classic) training pipeline](migrate-rebuild-experiment.md).
