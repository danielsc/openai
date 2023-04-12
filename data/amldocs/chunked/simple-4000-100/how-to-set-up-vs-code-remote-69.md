1. Authorization. Some checks are performed to make sure the user attempting to make a connection is authorized to use the compute instance.
1. VS Code Remote Server is installed on the compute instance.
1. A WebSocket connection is established for real-time interaction.

Once the connection is established, it's persisted. A token is issued at the start of the session which gets refreshed automatically to maintain the connection with your compute instance.

After you connect to your remote compute instance, use the editor to:

* [Author and manage files on your remote compute instance or file share](https://code.visualstudio.com/docs/editor/codebasics).
* Use the [VS Code integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal) to [run commands and applications on your remote compute instance](how-to-access-terminal.md).
* [Debug your scripts and applications](https://code.visualstudio.com/Docs/editor/debugging)
* [Use VS Code to manage your Git repositories](concept-train-model-git-integration.md)

## Configure compute instance as remote notebook server

In order to configure a compute instance as a remote Jupyter Notebook server you'll need a few prerequisites:

* Azure Machine Learning Visual Studio Code extension. For more information, see the [Azure Machine Learning Visual Studio Code Extension setup guide](how-to-setup-vs-code.md).
* Azure Machine Learning workspace. [Use the Azure Machine Learning Visual Studio Code extension to create a new workspace](how-to-manage-resources-vscode.md#create-a-workspace) if you don't already have one.

To connect to a compute instance:

1. Open a Jupyter Notebook in Visual Studio Code.
1. When the integrated notebook experience loads, select **Jupyter Server**.

    > [!div class="mx-imgBorder"]
    > ![Launch Azure Machine Learning remote Jupyter Notebook server dropdown](media/how-to-set-up-vs-code-remote/launch-server-selection-dropdown.png)

    Alternatively, you also use the command palette:

    1. Open the command palette by selecting **View > Command Palette** from the menu bar.
    1. Enter into the text box `Azure ML: Connect to Compute instance Jupyter server`.

1. Choose `Azure ML Compute Instances` from the list of Jupyter server options.
1. Select your subscription from the list of subscriptions. If you have have previously configured your default Azure Machine Learning workspace, this step is skipped.
1. Select your workspace.
1. Select your compute instance from the list. If you don't have one, select **Create new Azure ML Compute Instance** and follow the prompts to create one.
1. For the changes to take effect, you have to reload Visual Studio Code.
1. Open a Jupyter Notebook and run a cell.

> [!IMPORTANT]
> You **MUST** run a cell in order to establish the connection.

At this point, you can continue to run cells in your Jupyter Notebook.

> [!TIP]
> You can also work with Python script files (.py) containing Jupyter-like code cells. For more information, see the [Visual Studio Code Python interactive documentation](https://code.visualstudio.com/docs/python/jupyter-support-py).

## Next steps

Now that you've set up Visual Studio Code Remote, you can use a compute instance as remote compute from Visual Studio Code to [interactively debug your code](how-to-debug-visual-studio-code.md).

[Tutorial: Train your first ML model](tutorial-1st-experiment-sdk-train.md) shows how to use a compute instance with an integrated notebook.
