
# Manage Azure Machine Learning resources with the VS Code Extension (preview)

Learn how to manage Azure Machine Learning resources with the VS Code extension.

![Azure Machine Learning VS Code Extension](media/how-to-manage-resources-vscode/azure-machine-learning-vscode-extension.png)

## Prerequisites

- Azure subscription. If you don't have one, sign up to try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
- Visual Studio Code. If you don't have it, [install it](https://code.visualstudio.com/docs/setup/setup-overview).
- Azure Machine Learning extension. Follow the [Azure Machine Learning VS Code extension installation guide](how-to-setup-vs-code.md) to set up the extension.

## Create resources

The quickest way to create resources is using the extension's toolbar.

1. Open the Azure Machine Learning view.
1. Select **+** in the activity bar.
1. Choose your resource from the dropdown list.
1. Configure the specification file. The information required depends on the type of resource you want to create.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, you can create a resource by using the command palette:

1. Open the command palette **View > Command Palette**
1. Enter `> Azure ML: Create <RESOURCE-TYPE>` into the text box. Replace `RESOURCE-TYPE` with the type of resource you want to create.
1. Configure the specification file.
1. Open the command palette **View > Command Palette**
1. Enter `> Azure ML: Create Resource` into the text box.

## Version resources

Some resources like environments, datasets, and models allow you to make changes to a resource and store the different versions.

To version a resource:

1. Use the existing specification file that created the resource or follow the create resources process to create a new specification file.
1. Increment the version number in the template.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

As long as the name of the updated resource is the same as the previous version, Azure Machine Learning picks up the changes and creates a new version.

## Workspaces

For more information, see [workspaces](concept-workspace.md).

### Create a workspace

1. In the Azure Machine Learning view, right-click your subscription node and select **Create Workspace**.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Workspace` command in the command palette.

### Remove workspace

1. Expand the subscription node that contains your workspace.
1. Right-click the workspace you want to remove.
1. Select whether you want to remove:
    - *Only the workspace*: This option deletes **only** the workspace Azure resource. The resource group, storage accounts, and any other resources the workspace was attached to are still in Azure.
    - *With associated resources*: This option deletes the workspace **and** all resources associated with it.

Alternatively, use the `> Azure ML: Remove Workspace` command in the command palette.

## Datastores

The extension currently supports datastores of the following types:

- Azure Blob
- Azure Data Lake Gen 1
- Azure Data Lake Gen 2
- Azure File

For more information, see [datastore](concept-data.md#datastore).

### Create a datastore

1. Expand the subscription node that contains your workspace.
1. Expand the workspace node you want to create the datastore under.
1. Right-click the **Datastores** node and select **Create Datastore**.
1. Choose the datastore type.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Datastore` command in the command palette.

### Manage a datastore

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Datastores** node inside your workspace.
