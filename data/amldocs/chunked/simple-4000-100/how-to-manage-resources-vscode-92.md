1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Datastores** node inside your workspace.
1. Right-click the datastore you want to:
    - *Unregister Datastore*. Removes datastore from your workspace.
    - *View Datastore*. Display read-only datastore settings

Alternatively, use the `> Azure ML: Unregister Datastore` and `> Azure ML: View Datastore` commands respectively in the command palette.

## Datasets

The extension currently supports the following dataset types:

- *Tabular*: Allows you to materialize data into a DataFrame.
- *File*: A file or collection of files. Allows you to download or mount files to your compute.

For more information, see [datasets](./v1/concept-data.md)

### Create dataset

1. Expand the subscription node that contains your workspace.
1. Expand the workspace node you want to create the dataset under.
1. Right-click the **Datasets** node and select **Create Dataset**.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Dataset` command in the command palette.

### Manage a dataset

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Datasets** node.
1. Right-click the dataset you want to:
    - **View Dataset Properties**. Lets you view metadata associated with a specific dataset. If you have multiple versions of a dataset, you can choose to only view the dataset properties of a specific version by expanding the dataset node and performing the same steps described in this section on the version of interest.
    - **Preview dataset**. View your dataset directly in the VS Code Data Viewer. Note that this option is only available for tabular datasets.
    - **Unregister dataset**. Removes a dataset and all versions of it from your workspace.

Alternatively, use the `> Azure ML: View Dataset Properties` and `> Azure ML: Unregister Dataset` commands respectively in the command palette.

## Environments

For more information, see [environments](concept-environments.md).

### Create environment

1. Expand the subscription node that contains your workspace.
1. Expand the workspace node you want to create the datastore under.
1. Right-click the **Environments** node and select **Create Environment**.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Environment` command in the command palette.

### View environment configurations

To view the dependencies and configurations for a specific environment in the extension:

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Environments** node.
1. Right-click the environment you want to view and select **View Environment**.

Alternatively, use the `> Azure ML: View Environment` command in the command palette.

## Experiments

For more information, see [experiments](v1/concept-azure-machine-learning-architecture.md#experiments).

### Create job

The quickest way to create a job is by clicking the **Create Job** icon in the extension's activity bar.

Using the resource nodes in the Azure Machine Learning view:

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Right-click the **Experiments** node in your workspace and select **Create Job**.
1. Choose your job type.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Job` command in the command palette.

### View job

To view your job in Azure Machine Learning studio:

1. Expand the subscription node that contains your workspace.
1. Expand the **Experiments** node inside your workspace.
1. Right-click the experiment you want to view and select **View Experiment in Studio**.
