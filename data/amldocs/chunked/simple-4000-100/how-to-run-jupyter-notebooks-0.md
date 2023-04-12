
# Run Jupyter notebooks in your workspace

Learn how to run your Jupyter notebooks directly in your workspace in Azure Machine Learning studio. While you can launch [Jupyter](https://jupyter.org/) or [JupyterLab](https://jupyterlab.readthedocs.io), you can also edit and run your notebooks without leaving the workspace.

For information on how to create and manage files, including notebooks, see [Create and manage files in your workspace](how-to-manage-files.md).

> [!IMPORTANT]
> Features marked as (preview) are provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. 
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/) before you begin.
* A Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md).
* Your user identity must have access to your workspace's default storage account. Whether you can read, edit, or create notebooks depends on your [access level](how-to-assign-roles.md) to your workspace. For example, a Contributor can edit the notebook, while a Reader could only view it.

## Access notebooks from your workspace

Use the **Notebooks** section of your workspace to edit and run Jupyter notebooks.

1. Sign into [Azure Machine Learning studio](https://ml.azure.com)
1. Select your workspace, if it isn't already open
1. On the left, select **Notebooks**

## Edit a notebook

To edit a notebook, open any notebook located in the **User files** section of your workspace. Select the cell you wish to edit.  If you don't have any notebooks in this section, see [Create and manage files in your workspace](how-to-manage-files.md).

You can edit the notebook without connecting to a compute instance.  When you want to run the cells in the notebook, select or create a compute instance.  If you select a stopped compute instance, it will automatically start when you run the first cell.

When a compute instance is running, you can also use code completion, powered by [Intellisense](https://code.visualstudio.com/docs/editor/intellisense), in any Python notebook.

You can also launch Jupyter or JupyterLab from the notebook toolbar.  Azure Machine Learning doesn't provide updates and fix bugs from Jupyter or JupyterLab as they're Open Source products outside of the boundary of Microsoft Support.

## Focus mode

Use focus mode to expand your current view so you can focus on your active tabs. Focus mode hides the Notebooks file explorer.

1. In the terminal window toolbar, select **Focus mode** to turn on focus mode. Depending on your window width, the tool may be located under the **...** menu item in your toolbar.
1. While in focus mode, return to the standard view by selecting **Standard view**.

    :::image type="content" source="media/how-to-run-jupyter-notebooks/focusmode.gif" alt-text="Toggle focus mode / standard view":::

## Code completion (IntelliSense)

[IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) is a code-completion aid that includes many features: List Members, Parameter Info, Quick Info, and Complete Word. With only a few keystrokes, you can:
* Learn more about the code you're using
* Keep track of the parameters you're typing
* Add calls to properties and methods 
<!--
### Insert code snippets (preview)

Use **Ctrl+Space** to trigger IntelliSense code snippets.  Scroll through the suggestions or start typing to find the code you want to insert.  Once you insert code, tab through the arguments to customize the code for your own use.

:::image type="content" source="media/how-to-run-jupyter-notebooks/insert-snippet.gif" alt-text="Insert a code snippet":::

These same snippets are available when you open your notebook in VS Code. For a complete list of available snippets, see [Azure Machine Learning VS Code Snippets](https://github.com/Azure/azureml-snippets/blob/main/snippets/snippets.md).
