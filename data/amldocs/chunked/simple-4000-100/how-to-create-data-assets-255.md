
# [Studio](#tab/Studio)

To create a Table data asset in the Azure Machine Learning studio, use the following steps. 

1. Navigate to [Azure Machine Learning studio](https://ml.azure.com)

1. Under **Assets** in the left navigation, select **Data**. On the Data assets tab, select **Create**
:::image type="content" source="./media/how-to-create-data-assets/data-assets-create.png" alt-text="Screenshot highlights Create in the Data assets tab.":::

1. Give your data asset a name and optional description. Then, select the **Table (mltable)** option under Type.
:::image type="content" source="./media/how-to-create-data-assets/create-data-asset-table-type.png" alt-text="In this screenshot, choose Table (mltable) in the Type dropdown.":::

1. You have a few options for your data source. If you already have the path to the folder you want to upload, choose **From a URI**. If your folder is already stored in Azure, choose **From Azure storage**. If you want to upload your folder from your local drive, choose **From local files**.
:::image type="content" source="./media/how-to-create-data-assets/create-data-asset.png" alt-text="This screenshot shows data asset source choices.":::

1. Follow the steps; once you reach the Review step, select **Create** on the last page

## Next steps

- [Read data in a job](how-to-read-write-data-v2.md#read-data-in-a-job)
- [Working with tables in Azure Machine Learning](how-to-mltable.md)
- [Access data from Azure cloud storage during interactive development](how-to-access-data-interactive.md)
