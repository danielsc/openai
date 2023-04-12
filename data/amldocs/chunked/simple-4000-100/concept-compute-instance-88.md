Don't store training data on the notebooks file share. You can use the `/tmp` directory on the compute instance for your temporary data.  However, don't write large files of data on the OS disk of the compute instance. OS disk on compute instance has 128-GB capacity. You can also store temporary training data on temporary disk mounted on /mnt. Temporary disk size is based on the VM size chosen and can store larger amounts of data if a higher size VM is chosen. You can also mount [datastores and datasets](v1/concept-azure-machine-learning-architecture.md#datasets-and-datastores). Any software packages you install are saved on the OS disk of compute instance. Note customer managed key encryption is currently not supported for OS disk. The OS disk for compute instance is encrypted with Microsoft-managed keys. 

## Create

Follow the steps in the [Quickstart: Create workspace resources you need to get started with Azure Machine Learning](quickstart-create-resources.md) to create a basic compute instance.  

For more options, see [create a new compute instance](how-to-create-manage-compute-instance.md?tabs=azure-studio#create).

As an administrator, you can **[create a compute instance for others in the workspace (preview)](how-to-create-manage-compute-instance.md#create-on-behalf-of-preview)**.

You can also **[use a setup script (preview)](how-to-customize-compute-instance.md)** for an automated way to customize and configure the compute instance.

Other ways to create a compute instance:
* Directly from the integrated notebooks experience.
* From Azure Resource Manager template. For an example template, see the [create an Azure Machine Learning compute instance template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-compute-create-computeinstance).
* With [Azure Machine Learning SDK](how-to-create-manage-compute-instance.md?tabs=python#create)
* From the [CLI extension for Azure Machine Learning](how-to-create-manage-compute-instance.md?tabs=azure-cli#create)

The dedicated cores per region per VM family quota and total regional quota, which applies to compute instance creation, is unified and shared with Azure Machine Learning training compute cluster quota. Stopping the compute instance doesn't release quota to ensure you'll be able to restart the compute instance. Don't stop the compute instance through the OS terminal by doing a sudo shutdown.

Compute instance comes with P10 OS disk. Temp disk type depends on the VM size chosen. Currently, it isn't possible to change the OS disk type.


## Compute target

Compute instances can be used as a [training compute target](concept-compute-target.md#training-compute-targets) similar to Azure Machine Learning [compute training clusters](how-to-create-attach-compute-cluster.md).  But a compute instance has only a single node, while a compute cluster can have more nodes.

A compute instance:

* Has a job queue.
* Runs jobs securely in a virtual network environment, without requiring enterprises to open up SSH port. The job executes in a containerized environment and packages your model dependencies in a Docker container.
* Can run multiple small jobs in parallel (preview).  One job per core can run in parallel while the rest of the jobs are queued.
* Supports single-node multi-GPU [distributed training](how-to-train-distributed-gpu.md) jobs

You can use compute instance as a local inferencing deployment target for test/debug scenarios.

> [!TIP]
> The compute instance has 120GB OS disk. If you run out of disk space and get into an unusable state, please clear at least 5 GB disk space on OS disk (mounted on /) through the compute instance terminal by removing files/folders and then do `sudo reboot`. Temporary disk will be freed after restart; you do not need to clear space on temp disk manually. To access the terminal go to compute list page or compute instance details page and click on **Terminal** link. You can check available disk space by running `df -h` on the terminal. Clear at least 5 GB space before doing `sudo reboot`. Please do not stop or restart the compute instance through the Studio until 5 GB disk space has been cleared. Auto shutdowns, including scheduled start or stop as well as idle shutdowns(preview), will not work if the CI disk is full.
