## Save and checkpoint a notebook

Azure Machine Learning creates a checkpoint file when you create an *ipynb* file.

In the notebook toolbar, select the menu and then **File&gt;Save and checkpoint** to manually save the notebook and it will add a checkpoint file associated with the notebook.

:::image type="content" source="media/how-to-run-jupyter-notebooks/file-save.png" alt-text="Screenshot of save tool in notebook toolbar":::

Every notebook is autosaved every 30 seconds. AutoSave updates only the initial *ipynb* file, not the checkpoint file.
 
Select **Checkpoints** in the notebook menu to create a named checkpoint and to revert the notebook to a saved checkpoint.

## Export a notebook

In the notebook toolbar, select the menu and then **Export As** to export the notebook as any of the supported types:

* Notebook
* Python
* HTML
* LaTeX

:::image type="content" source="media/how-to-run-jupyter-notebooks/export-notebook.png" alt-text="Export a notebook to your computer":::

The exported file is saved on your computer.

## Run a notebook or Python script

To run a notebook or a Python script, you first connect to a running [compute instance](concept-compute-instance.md).

* If you don't have a compute instance, use these steps to create one:

    1. In the notebook or script toolbar, to the right of the Compute dropdown, select **+ New Compute**. Depending on your screen size, this may be located under a **...** menu.
        :::image type="content" source="media/how-to-run-jupyter-notebooks/new-compute.png" alt-text="Create a new compute":::
    1. Name the Compute and choose a **Virtual Machine Size**. 
    1. Select **Create**.
    1. The compute instance is connected to the file automatically.  You can now run the notebook cells or the Python script using the tool to the left of the compute instance.

* If you have a stopped compute instance, select  **Start compute** to the right of the Compute dropdown. Depending on your screen size, this may be located under a **...** menu.

    :::image type="content" source="media/how-to-run-jupyter-notebooks/start-compute.png" alt-text="Start compute instance":::
    
Once you're connected to a compute instance, use the toolbar to run all cells in the notebook, or Control + Enter to run a single selected cell. 

Only you can see and use the compute instances you create.  Your **User files** are stored separately from the VM and are shared among all compute instances in the workspace.

## Explore variables in the notebook

On the notebook toolbar, use the **Variable explorer** tool to show the name, type, length, and sample values for all variables that have been created in your notebook.

:::image type="content" source="media/how-to-run-jupyter-notebooks/variable-explorer.png" alt-text="Screenshot: Variable explorer tool":::

Select the tool to show the variable explorer window.

:::image type="content" source="media/how-to-run-jupyter-notebooks/variable-explorer-window.png" alt-text="Screenshot: Variable explorer window":::

## Navigate with a TOC

On the notebook toolbar, use the  **Table of contents** tool to display or hide the table of contents.  Start a markdown cell with a heading to add it to the table of contents. Select an entry in the table to scroll to that cell in the notebook.  

:::image type="content" source="media/how-to-run-jupyter-notebooks/table-of-contents.png" alt-text="Screenshot: Table of contents in the notebook":::

## Change the notebook environment

The notebook toolbar allows you to change the environment on which your notebook runs.  

These actions won't change the notebook state or the values of any variables in the notebook:

|Action  |Result  |
|---------|---------| --------|
|Stop the kernel     |  Stops any running cell. Running a cell will automatically restart the kernel. |
|Navigate to another workspace section     |     Running cells are stopped. |

These actions will reset the notebook state and will reset all variables in the notebook.
