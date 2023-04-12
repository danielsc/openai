
# Quickstart: Run Jupyter notebooks in studio

Get started with Azure Machine Learning by using Jupyter notebooks to learn more about the Python SDK.

In this quickstart, you'll learn how to run notebooks on a *compute instance* in Azure Machine Learning studio.  A compute instance is an online compute resource that has a development environment already installed and ready to go.  

You'll also learn where to find sample notebooks to help jump-start your path to training and deploying models with Azure Machine Learning.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- Run the [Quickstart: Create workspace resources you need to get started with Azure Machine Learning](quickstart-create-resources.md) to create a workspace and a compute instance.

## Create a new notebook

Create a new notebook in studio.

1. Sign into [Azure Machine Learning studio](https://ml.azure.com).
1. Select your workspace, if it isn't already open.
1. On the left, select **Notebooks**.
1. Select **Create new file**.
    
    :::image type="content" source="media/quickstart-run-notebooks/create-new-file.png" alt-text="Screenshot: create a new notebook file.":::

1. Name your new notebook **my-new-notebook.ipynb**.


## Create a markdown cell

1. On the upper right of each notebook cell is a toolbar of actions you can use for that cell.  Select the **Convert to markdown cell** tool to change the cell to markdown.

    :::image type="content" source="media/quickstart-run-notebooks/convert-to-markdown.png" alt-text="Screenshot: Convert to markdown.":::

1. Double-click on the cell to open it.
1. Inside the cell, type:

    ```markdown
    # Testing a new notebook
    Use markdown cells to add nicely formatted content to the notebook.
    ```

## Create a code cell

1. Just below the cell, select **+ Code** to create a new code cell.
1. Inside this cell, add:

    ```python
    print("Hello, world!")
    ```

## Run the code

1. If you stopped your compute instance at the end of the [Quickstart: Create workspace resources you need to get started with Azure Machine Learning](quickstart-create-resources.md), start it again now:

    :::image type="content" source="media/quickstart-run-notebooks/start-compute.png" alt-text="Screenshot: Start a compute instance.":::

1.  Wait until the compute instance is "Running".  When it is running, the **Compute instance** dot is green.  You can also see the status after the compute instance name.  You may have to select the arrow to see the full name.

    :::image type="content" source="media/quickstart-run-notebooks/compute-running.png" alt-text="Screenshot: Compute is running.":::

1. You can run code cells either by using **Shift + Enter**, or by selecting the **Run cell** tool to the right of the cell.  Use one of these methods to run the cell now.

    :::image type="content" source="media/quickstart-run-notebooks/run-cell.png" alt-text="Screenshot: run cell tool.":::

1. The brackets to the left of the cell now have a number inside.  The number represents the order in which cells were run.  Since this is the first cell you've run, you'll see `[1]` next to the cell.  You also see the output of the cell, `Hello, world!`.

1. Run the cell again.  You'll see the same output (since you didn't change the code), but now the brackets contain `[2]`. As your notebook gets larger, these numbers help you understand what code was run, and in what order.

## Run a second code cell

1. Add a second code cell:

    ```python
    two = 1 + 1
    print("One plus one is ",two)
    ```

1. Run the new cell.  
1. Your notebook now looks like:

    :::image type="content" source="media/quickstart-run-notebooks/notebook.png" alt-text="Screenshot: Notebook contents.":::

## See your variables

Use the **Variable explorer** to see the variables that are defined in your session.  

1. Select the **"..."** in the notebook toolbar.
1. Select **Variable explorer**.
