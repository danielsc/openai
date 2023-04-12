
# Debug jobs and monitor training progress (preview)

> [!IMPORTANT]
> Items marked (preview) in this article are currently in public preview.
> The preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

Machine learning model training is usually an iterative process and requires significant experimentation. With the Azure Machine Learning interactive job experience, data scientists can use the Azure Machine Learning Python SDKv2, Azure Machine Learning CLIv2 or the Azure Studio to access the container where their job is running.  Once the job container is accessed, users can iterate on training scripts, monitor training progress or debug the job remotely like they typically do on their local machines. Jobs can be interacted with via different training applications including **JupyterLab, TensorBoard, VS Code** or by connecting to the job container directly via **SSH**.  

Interactive training is supported on **Azure Machine Learning Compute Clusters** and **Azure Arc-enabled Kubernetes Cluster**.

## Prerequisites
- Review [getting started with training on Azure Machine Learning](./how-to-train-model.md).
- To use this feature in Azure Machine Learning Studio, enable the "Debug & monitor your training jobs" flight via the [preview panel](./how-to-enable-preview-features.md#how-do-i-enable-preview-features).
- To use **VS Code**, [follow this guide](how-to-setup-vs-code.md) to set up the Azure Machine Learning extension.
- Make sure your job environment has the `openssh-server` and `ipykernel ~=6.0` packages installed (all Azure Machine Learning curated training environments have these packages installed by default).
- Interactive applications can't be enabled on distributed training runs where the distribution type is anything other than Pytorch, Tensorflow or MPI. Custom distributed training setup (configuring multi-node training without using the above distribution frameworks) is not currently supported.


## Interact with your job container

By specifying interactive applications at job creation, you can connect directly to the container on the compute node where your job is running. Once you have access to the job container, you can test or debug your job in the exact same environment where it would run. You can also use VS Code to attach to the running process and debug as you would locally. 

### Enable during job submission
# [Azure Machine Learning Studio](#tab/ui)
1. Create a new job from the left navigation pane in the studio portal.


2. Choose `Compute cluster` or `Attached compute` (Kubernetes) as the compute type, choose the compute target, and specify how many nodes you need in `Instance count`. 
  
  :::image type="content" source="./media/interactive-jobs/select-compute.png" alt-text="Screenshot of selecting a compute location for a job.":::

3. Follow the wizard to choose the environment you want to start the job.
  

4. In `Job settings` step, add your training code (and input/output data) and reference it in your command to make sure it's mounted to your job.
  
  :::image type="content" source="./media/interactive-jobs/sleep-command.png" alt-text="Screenshot of reviewing a drafted job and completing the creation.":::

  You can put `sleep <specific time>` at the end of your command to specify the amount of time you want to reserve the compute resource. The format follows: 
      * sleep 1s
      * sleep 1m
      * sleep 1h
      * sleep 1d

  You can also use the ```sleep infinity``` command that would keep the job alive indefinitely. 
    
  > [!NOTE]
  > If you use `sleep infinity`, you will need to manually [cancel the job](./how-to-interactive-jobs.md#end-job) to let go of the compute resource (and stop billing). 
