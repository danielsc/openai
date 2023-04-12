1. Expand the **Experiments** node inside your workspace.
1. Right-click the experiment you want to view and select **View Experiment in Studio**.
1. A prompt appears asking you to open the experiment URL in Azure Machine Learning studio. Select **Open**.

Alternatively, use the `> Azure ML: View Experiment in Studio` command respectively in the command palette.

### Track job progress

As you're running your job, you may want to see its progress. To track the progress of a job in Azure Machine Learning studio from the extension:

1. Expand the subscription node that contains your workspace.
1. Expand the **Experiments** node inside your workspace.
1. Expand the job node you want to track progress for.
1. Right-click the job and select **View Job in Studio**.
1. A prompt appears asking you to open the job URL in Azure Machine Learning studio. Select **Open**.

### Download job logs & outputs

Once a job is complete, you may want to download the logs and assets such as the model generated as part of a job.

1. Expand the subscription node that contains your workspace.
1. Expand the **Experiments** node inside your workspace.
1. Expand the job node you want to download logs and outputs for.
1. Right-click the job:
    - To download the outputs, select **Download outputs**.
    - To download the logs, select **Download logs**.

Alternatively, use the `> Azure ML: Download Outputs` and `> Azure ML: Download Logs` commands respectively in the command palette.

## Compute instances

For more information, see [compute instances](concept-compute-instance.md).

### Create compute instance

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Compute** node.
1. Right-click the **Compute instances** node in your workspace and select **Create Compute**.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Compute` command in the command palette.

### Connect to compute instance

To use a compute instance as a development environment or remote Jupyter server, see [Connect to a compute instance](how-to-set-up-vs-code-remote.md?tabs=extension).

### Stop or restart compute instance

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Compute instances** node inside your **Compute** node.
1. Right-click the compute instance you want to stop or restart and select **Stop Compute instance** or **Restart Compute instance** respectively.

Alternatively, use the `> Azure ML: Stop Compute instance` and `Restart Compute instance` commands respectively in the command palette.

### View compute instance configuration

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Compute instances** node inside your **Compute** node.
1. Right-click the compute instance you want to inspect and select **View Compute instance Properties**.

Alternatively, use the `Azure ML: View Compute instance Properties` command in the command palette.

### Delete compute instance

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Compute instances** node inside your **Compute** node.
1. Right-click the compute instance you want to delete and select **Delete Compute instance**.

Alternatively, use the `Azure ML: Delete Compute instance` command in the command palette.

## Compute clusters

For more information, see [training compute targets](concept-compute-target.md#training-compute-targets).

### Create compute cluster

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Expand the **Compute** node.
1. Right-click the **Compute clusters** node in your workspace and select **Create Compute**.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.
