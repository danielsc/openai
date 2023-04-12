Use the **Variable explorer** to see the variables that are defined in your session.  

1. Select the **"..."** in the notebook toolbar.
1. Select **Variable explorer**.
    
    :::image type="content" source="media/quickstart-run-notebooks/variable-explorer.png" alt-text="Screenshot: Variable explorer tool.":::":::

    The explorer appears at the bottom.  You currently have one variable, `two`, assigned.

1. Add another code cell:

    ```python
    three = 1+two
    ```

1. Run this cell to see the variable `three` appear in the variable explorer.

## Learn from sample notebooks

There are sample notebooks available in studio to help you learn more about Azure Machine Learning.  To find these samples:

1. Still in the **Notebooks** section, select **Samples** at the top.

    :::image type="content" source="media/quickstart-run-notebooks/samples.png" alt-text="Screenshot: Sample notebooks.":::

1. The **SDK v1** folder can be used with the previous, v1 version of the SDK. If you're just starting, you won't need these samples.
1. Use notebooks in the **SDK v2** folder for examples that show the current version of the SDK, v2.
1. Select the notebook **SDK v2/tutorials/azureml-in-a-day/azureml-in-a-day.ipynb**.  You'll see a read-only version of the notebook.  
1. To get your own copy, you can select **Clone this notebook**.  This action will also copy the rest of the folder's content for that notebook.  No need to do that now, though, as you're going to instead clone the whole folder.

## Clone tutorials folder

You can also clone an entire folder.  The **tutorials** folder is a good place to start learning more about how Azure Machine Learning works.

1. Open the **SDK v2** folder.
1. Select the **"..."** at the right of **tutorials** folder to get the menu, then select **Clone**.
    
    :::image type="content" source="media/quickstart-run-notebooks/clone-folder.png" alt-text="Screenshot: clone v2 tutorials folder.":::

1. Your new folder is now displayed in the **Files** section.  
1. Run the notebooks in this folder to learn more about using the Python SDK v2 to train and deploy models.

## Clean up resources

If you plan to continue now to the next tutorial, skip to [Next steps](#next-steps).

### Delete all resources

[!INCLUDE [aml-delete-resource-group](../../includes/aml-delete-resource-group.md)]

## Next steps

> [!div class="nextstepaction"]
> [Tutorial: Azure Machine Learning in a day](tutorial-azure-ml-in-a-day.md)
>
