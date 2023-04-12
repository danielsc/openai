For more information on workspaces, see [how to manage resources in VS Code](how-to-manage-resources-vscode.md).

## Create a GPU cluster for training

A compute target is the computing resource or environment where you run training jobs. For more information, see the [Azure Machine Learning compute targets documentation](./concept-compute-target.md).

1. In the Azure Machine Learning view, expand your workspace node.
1. Right-click the **Compute clusters** node inside your workspace's **Compute** node and select **Create Compute**

    > [!div class="mx-imgBorder"]
    > ![Create training compute cluster](./media/tutorial-train-deploy-image-classification-model-vscode/create-compute.png)

1. A specification file appears. Configure the specification file with the following options.

    ```yml
    $schema: https://azuremlschemas.azureedge.net/latest/compute.schema.json
    name: gpu-cluster
    type: amlcompute
    size: Standard_NC12
    
    min_instances: 0
    max_instances: 3
    idle_time_before_scale_down: 120
    ```

    The specification file creates a GPU cluster called `gpu-cluster` with at most 3 Standard_NC12 VM nodes that automatically scales down to 0 nodes after 120 seconds of inactivity.

    For more information on VM sizes, see [sizes for Linux virtual machines in Azure](../virtual-machines/sizes.md).

1. Right-click the specification file and select **Azure ML: Execute YAML**.

After a few minutes, the new compute target appears in the *Compute > Compute clusters* node of your workspace.

## <a name="train-the-model"></a> Train image classification model

During the training process, a TensorFlow model is trained by processing the training data and learning patterns embedded within it for each of the respective digits being classified.

Like workspaces and compute targets, training jobs are defined using resource templates. For this sample, the specification is defined in the *job.yml* file which looks like the following:

```yml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
code: src
command: >
    python train.py
environment: azureml:AzureML-tensorflow-2.4-ubuntu18.04-py37-cuda11-gpu:48
compute: azureml:gpu-cluster
experiment_name: tensorflow-mnist-example
description: Train a basic neural network with TensorFlow on the MNIST dataset.
```

This specification file submits a training job called `tensorflow-mnist-example` to the recently created `gpu-cluster` computer target that runs the code in the *train.py* Python script. The environment used is one of the curated environments provided by Azure Machine Learning which contains TensorFlow and other software dependencies required to run the training script. For more information on curated environments, see [Azure Machine Learning curated environments](resource-curated-environments.md).

To submit the training job:

1. Open the *job.yml* file.
1. Right-click the file in the text editor and select **Azure ML: Execute YAML**.

At this point, a request is sent to Azure to run your experiment on the selected compute target in your workspace. This process takes several minutes. The amount of time to run the training job is impacted by several factors like the compute type and training data size. To track the progress of your experiment, right-click the current run node and select **View Job in Azure portal**.

When the dialog requesting to open an external website appears, select **Open**.

> [!div class="mx-imgBorder"]
> ![Track experiment progress](./media/tutorial-train-deploy-image-classification-model-vscode/track-experiment-progress.png)

When the model is done training, the status label next to the run node updates to "Completed".

## Next steps

In this tutorial, you learn the following tasks:

> [!div class="checklist"]
> * Understand the code
> * Create a workspace
> * Create a GPU cluster for training
> * Train a model

For next steps, see:

* [Create and manage Azure Machine Learning resources using Visual Studio Code](how-to-set-up-vs-code-remote.md).
