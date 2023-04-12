1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Compute` command in the command palette.

### View compute configuration

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Compute clusters** node inside your **Compute** node.
1. Right-click the compute you want to view and select **View Compute Properties**.

Alternatively, use the `> Azure ML: View Compute Properties` command in the command palette.

### Delete compute cluster

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Compute clusters** node inside your **Compute** node.
1. Right-click the compute you want to delete and select **Remove Compute**.

Alternatively, use the `> Azure ML: Remove Compute` command in the command palette.

## Inference Clusters

For more information, see [compute targets for inference](concept-compute-target.md#compute-targets-for-inference).

### Manage inference clusters

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Inference clusters** node inside your **Compute** node.
1. Right-click the compute you want to:
    - **View Compute Properties**. Displays read-only configuration data about your attached compute.
    - **Detach compute**. Detaches the compute from your workspace.

Alternatively, use the `> Azure ML: View Compute Properties` and `> Azure ML: Detach Compute` commands respectively in the command palette.

### Delete inference clusters

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Attached computes** node inside your **Compute** node.
1. Right-click the compute you want to delete and select **Remove Compute**.

Alternatively, use the `> Azure ML: Remove Compute` command in the command palette.

## Attached Compute

For more information, see [unmanaged compute](concept-compute-target.md#unmanaged-compute).

### Manage attached compute

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Attached computes** node inside your **Compute** node.
1. Right-click the compute you want to:
    - **View Compute Properties**. Displays read-only configuration data about your attached compute.
    - **Detach compute**. Detaches the compute from your workspace.

Alternatively, use the `> Azure ML: View Compute Properties` and `> Azure ML: Detach Compute` commands respectively in the command palette.

## Models

For more information, see [models](v1/concept-azure-machine-learning-architecture.md#models)

### Create model

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Right-click the **Models** node in your workspace and select **Create Model**.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Model` command in the command palette.

### View model properties

1. Expand the subscription node that contains your workspace.
1. Expand the **Models** node inside your workspace.
1. Right-click the model whose properties you want to see and select **View Model Properties**. A file opens in the editor containing your model properties.

Alternatively, use the `> Azure ML: View Model Properties` command in the command palette.

### Download model

1. Expand the subscription node that contains your workspace.
1. Expand the **Models** node inside your workspace.
1. Right-click the model you want to download and select **Download Model File**.

Alternatively, use the `> Azure ML: Download Model File` command in the command palette.

### Delete a model

1. Expand the subscription node that contains your workspace.
1. Expand the **Models** node inside your workspace.
