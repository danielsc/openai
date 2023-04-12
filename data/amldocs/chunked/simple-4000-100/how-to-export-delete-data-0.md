

# Export or delete your Machine Learning service workspace data

In Azure Machine Learning, you can export or delete your workspace data using either the portal graphical interface or the Python SDK. This article describes both options.

[!INCLUDE [GDPR-related guidance](../../includes/gdpr-dsr-and-stp-note.md)]

[!INCLUDE [GDPR-related guidance](../../includes/gdpr-intro-sentence.md)]

## Control your workspace data

In-product data stored by Azure Machine Learning is available for export and deletion. You can export and delete data with Azure Machine Learning studio, the CLI, and the SDK. Additionally, you can access telemetry data through the Azure Privacy portal.

In Azure Machine Learning, personal data consists of user information in job history documents.

## Delete high-level resources using the portal

When you create a workspace, Azure creates several resources within the resource group:

- The workspace itself
- A storage account
- A container registry
- An Applications Insights instance
- A key vault

To delete these resources, selecting them from the list and choose **Delete**:

> [!IMPORTANT]
> If the resource is configured for soft delete, the data won't actually delete unless you optionally select to delete the resource permanently. For more information, see the following articles:
> * [Workspace soft-deletion](concept-soft-delete.md).
> * [Soft delete for blobs](../storage/blobs/soft-delete-blob-overview.md).
> * [Soft delete in Azure Container Registry](../container-registry/container-registry-soft-delete-policy.md).
> * [Azure log analytics workspace](../azure-monitor/logs/delete-workspace.md).
> * [Azure Key Vault soft-delete](../key-vault/general/soft-delete-overview.md).

:::image type="content" source="media/how-to-export-delete-data/delete-resource-group-resources.png" alt-text="Screenshot of portal, with delete icon highlighted.":::

Job history documents, which may contain personal user information, are stored in the storage account in blob storage, in `/azureml` subfolders. You can download and delete the data from the portal.

:::image type="content" source="media/how-to-export-delete-data/storage-account-folders.png" alt-text="Screenshot of azureml directory in storage account, within the portal.":::

## Export and delete machine learning resources using Azure Machine Learning studio

Azure Machine Learning studio provides a unified view of your machine learning resources - for example, notebooks, data assets, models, and jobs. Azure Machine Learning studio emphasizes preservation of a record of your data and experiments. You can delete computational resources such as pipelines and compute resources with the browser. For these resources, navigate to the resource in question and choose **Delete**.

You can unregister data assets and archive jobs, but these operations don't delete the data. To entirely remove the data, data assets and job data require deletion at the storage level. Storage level deletion happens in the portal, as described earlier. Azure ML Studio can handle individual deletion. Job deletion deletes the data of that job.

Azure ML Studio can handle training artifact downloads from experimental jobs. Choose the relevant **Job**. Choose **Output + logs**, and navigate to the specific artifacts you wish to download. Choose **...** and **Download**, or select **Download all**.

To download a registered model, navigate to the **Model** and choose **Download**.

:::image type="contents" source="media/how-to-export-delete-data/model-download.png" alt-text="Screenshot of studio model page with download option highlighted.":::

## Next steps

Learn more about [Managing a workspace](how-to-manage-workspace.md).