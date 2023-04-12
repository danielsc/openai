To set quotas at the workspace level, start in the [Azure portal](https://portal.azure.com).  Select any workspace in your subscription, and select **Usages + quotas** in the left pane. Then select the **Configure quotas** tab to view the quotas. You need privileges at the subscription scope to set the quota, since it's a setting that affects multiple workspaces.

## Set job autotermination policies 

In some cases, you should configure your training runs to limit their duration or terminate them early. For example, when you are using Azure Machine Learning's built-in hyperparameter tuning or automated machine learning.

Here are a few options that you have:
* Define a parameter called `max_run_duration_seconds` in your RunConfiguration to control the maximum duration a run can extend to on the compute you choose (either local or remote cloud compute).
* For [hyperparameter tuning](how-to-tune-hyperparameters.md#early-termination), define an early termination policy from a Bandit policy, a Median stopping policy, or a Truncation selection policy. To further control hyperparameter sweeps, use parameters such as `max_total_runs` or `max_duration_minutes`.
* For [automated machine learning](how-to-configure-auto-train.md#exit), set similar termination policies using the  `enable_early_stopping` flag. Also use properties such as `iteration_timeout_minutes` and `experiment_timeout_minutes` to control the maximum duration of a job or for the entire experiment.

## <a id="low-pri-vm"></a> Use low-priority VMs

Azure allows you to use excess unutilized capacity as Low-Priority VMs across virtual machine scale sets, Batch, and the Machine Learning service. These allocations are pre-emptible but come at a reduced price compared to dedicated VMs. In general, we recommend using Low-Priority VMs for Batch workloads. You should also use them where interruptions are recoverable either through resubmits (for Batch Inferencing) or through restarts (for deep learning training with checkpointing).

Low-Priority VMs have a single quota separate from the dedicated quota value, which is by VM family. Learn [more about AmlCompute quotas](how-to-manage-quotas.md).

 Low-Priority VMs don't work for compute instances, since they need to support interactive notebook experiences.

## Schedule compute instances

When you create a [compute instance](concept-compute-instance.md), the VM stays on so it is available for your work.  
* [Enable idle shutdown (preview)](how-to-create-manage-compute-instance.md#enable-idle-shutdown-preview) to save on cost when the VM has been idle for a specified time period.
* Or [set up a schedule](how-to-create-manage-compute-instance.md#schedule-automatic-start-and-stop) to automatically start and stop the compute instance (preview) to save cost when you aren't planning to use it.

## Use reserved instances

Another way to save money on compute resources is Azure Reserved VM Instance. With this offering, you commit to one-year or three-year terms. These discounts range up to 72% of the pay-as-you-go prices and are applied directly to your monthly Azure bill.

Azure Machine Learning Compute supports reserved instances inherently. If you purchase a one-year or three-year reserved instance, we will automatically apply discount against your Azure Machine Learning managed compute.

## Train locally

When prototyping and running training jobs that are small enough to run on your local computer, consider training locally. Using the Python SDK, setting your compute target to `local` executes your script locally. 

Visual Studio Code provides a full-featured environment for developing your machine learning applications. Using the Azure Machine Learning visual Visual Studio Code extension and Docker, you can run and debug locally. For more information, see [interactive debugging with Visual Studio Code](how-to-debug-visual-studio-code.md).

## Parallelize training

One of the key methods of optimizing cost and performance is by parallelizing the workload with the help of a parallel run step in Azure Machine Learning. This step allows you to use many smaller nodes to execute the task in parallel, hence allowing you to scale horizontally. There is an overhead for parallelization. Depending on the workload and the degree of parallelism that can be achieved, this may or may not be an option. For further information, see the [ParallelRunStep](xref:azureml.contrib.pipeline.steps.ParallelRunStep) documentation.
