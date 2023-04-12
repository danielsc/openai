These same snippets are available when you open your notebook in VS Code. For a complete list of available snippets, see [Azure Machine Learning VS Code Snippets](https://github.com/Azure/azureml-snippets/blob/main/snippets/snippets.md).

You can browse and search the list of snippets by using the notebook toolbar to open the snippet panel.

:::image type="content" source="media/how-to-run-jupyter-notebooks/open-snippet-panel.png" alt-text="Open snippet panel tool in the notebook toolbar":::

From the snippets panel, you can also submit a request to add new snippets.

:::image type="content" source="media/how-to-run-jupyter-notebooks/propose-new-snippet.png" alt-text="Snippet panel allows you to propose a new snippet":::
-->
## Share a notebook

Your notebooks are stored in your workspace's storage account, and can be shared with others, depending on their [access level](how-to-assign-roles.md) to your workspace.  They can open and edit the notebook as long as they have the appropriate access. For example, a Contributor can edit the notebook, while a Reader could only view it.

Other users of your workspace can find your notebook in the **Notebooks**, **User files** section of Azure ML studio. By default, your notebooks are in a folder with your username, and others can access them there.

You can also copy the URL from your browser when you open a notebook, then send to others.  As long as they have appropriate access to your workspace, they can open the notebook.

Since you don't share compute instances, other users who run your notebook will do so on their own compute instance.  

## Collaborate with notebook comments (preview)

Use a notebook comment to collaborate with others who have access to your notebook.

Toggle the comments pane on and off with the **Notebook comments** tool at the top of the notebook.  If your screen isn't wide enough, find this tool by first selecting the **...** at the end of the set of tools.

:::image type="content" source="media/how-to-run-jupyter-notebooks/notebook-comments-tool.png" alt-text="Screenshot of notebook comments tool in the top toolbar.":::  

Whether the comments pane is visible or not, you can add a comment into any code cell:

1. Select some text in the code cell.  You can only comment on text in a code cell.
1. Use the **New comment thread** tool to create your comment.
    :::image type="content" source="media/how-to-run-jupyter-notebooks/comment-from-code.png" alt-text="Screenshot of add a comment to a code cell tool.":::
1. If the comments pane was previously hidden, it will now open.  
1. Type your comment and post it with the tool or use **Ctrl+Enter**.
1. Once a comment is posted, select **...** in the top right to:
    * Edit the comment
    * Resolve the thread
    * Delete the thread

Text that has been commented will appear with a purple highlight in the code. When you select a comment in the comments pane, your notebook will scroll to the cell that contains the highlighted text.

> [!NOTE]
> Comments are saved into the code cell's metadata.

## Clean your notebook (preview)

Over the course of creating a notebook, you typically end up with cells you used for data exploration or debugging. The *gather* feature will help you produce a clean notebook without these extraneous cells.

1. Run all of your notebook cells.
1. Select the cell containing the code you wish the new notebook to run. For example, the code that submits an experiment, or perhaps the code that registers a model.
1. Select the **Gather** icon that appears on the cell toolbar.
    :::image type="content" source="media/how-to-run-jupyter-notebooks/gather.png" alt-text="Screenshot: select the Gather icon":::
1. Enter the name for your new "gathered" notebook.  

The new notebook contains only code cells, with all cells required to produce the same results as the cell you selected for gathering.

## Save and checkpoint a notebook

Azure Machine Learning creates a checkpoint file when you create an *ipynb* file.
