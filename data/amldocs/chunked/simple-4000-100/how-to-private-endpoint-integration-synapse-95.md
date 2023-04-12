    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/contributor-role.png" alt-text="Screenshot of selecting contributor.":::

1. Select __User, group, or service principal__, and then __+ Select members__. Enter the name of the identity created earlier, select it, and then use the __Select__ button.

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/add-role-assignment.png" alt-text="Screenshot of assigning the role.":::

1. Select __Review + assign__, verify the information, and then select the __Review + assign__ button.

    > [!TIP]
    > It may take several minutes for the Azure Machine Learning workspace to update the credentials cache. Until it has been updated, you may receive errors when trying to access the Azure Machine Learning workspace from Synapse.

## Verify connectivity

1. From Azure Synapse Studio, select __Develop__, and then __+ Notebook__.

    :::image type="content" source="./media/how-to-private-endpoint-integration-synapse/add-synapse-notebook.png" alt-text="Screenshot of adding a notebook.":::

1. In the __Attach to__ field, select the Apache Spark pool for your Azure Synapse workspace, and enter the following code in the first cell:

    ```python
    from notebookutils.mssparkutils import azureML

    # getWorkspace() takes the linked service name,
    # not the Azure Machine Learning workspace name.
    ws = azureML.getWorkspace("AzureMLService1")

    print(ws.name)
    ```

    > [!IMPORTANT]
    > This code snippet connects to the linked workspace using SDK v1, and then prints the workspace info. In the printed output, the value displayed is the name of the Azure Machine Learning workspace, not the linked service name that was used in the `getWorkspace()` call. For more information on using the `ws` object, see the [Workspace](/python/api/azureml-core/azureml.core.workspace.workspace) class reference.

## Next steps

* [Quickstart: Create a new Azure Machine Learning linked service in Synapse](../synapse-analytics/machine-learning/quickstart-integrate-azure-machine-learning.md).
* [Link Azure Synapse Analytics and Azure Machine Learning workspaces](v1/how-to-link-synapse-ml-workspaces.md).