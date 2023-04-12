    In the Gantt chart, the length of each bar shows how long the step takes, steps with a longer bar length take more time. You can also filter the table below by "total duration". When you select a row in the table, it will show you the node in the Gantt chart too. When you select a bar on the Gantt chart it will also highlight it in the table.

    In the table, reuse is denoted with the recycling icon.

    If you select the log icon next the node name it will open the detail page, which shows parameter, code, outputs, logs etc.

    :::image type="content" source="./media/how-to-use-pipeline-ui/detail-page-from-log-icon.png" alt-text="Screenshot highlighting the log icon and showing the detail page." lightbox= "./media/how-to-use-pipeline-ui/detail-page-from-log-icon.png":::

    If you're trying to make the queue time shorter for a node, you can change the compute node number and modify job priority to get more compute resources on this one.

### How to find the node that runs the longest in each status

Besides the total duration, you can also sort by durations for each status. For example, you can sort by *Preparing* duration to see which step spends the most time on image building. Then you can open the detail page to find that image building fails because of timeout issue.

#### What do I do if a duration issue identified

Status and definitions:

| Status | What does it mean? | Time estimation | Next step |
|------|--------------|-------------|----------|
| Not started | Job is submitted from client side and accepted in Azure ML services. Time spent in this stage is mainly in Azure ML service scheduling and preprocessing. | If there's no backend service issue, this time should be very short.| Open support case via Azure portal. |
|Preparing | In this status, job is pending for some preparation on job dependencies, for example, environment image building.| If you're using curated or registered custom environment, this time should be very short. | Check image building log. |
|Inqueue | Job is pending for compute resource allocation. Time spent in this stage is mainly depending on the status of your compute cluster.| If you're using a cluster with enough compute resource, this time should be short. | Check with workspace admin whether to increase the max nodes of the target compute or change the job to another less busy compute. |
|Running | Job is executing on remote compute. Time spent in this stage is mainly in two parts: <br> Runtime preparation: image pulling, docker starting and data preparation (mount or download). <br> User script execution. | This status is expected to be most time consuming one.	| 1. Go to the source code check if there's any user error. <br>  2. View the monitoring tab of compute metrics (CPU, memory, networking etc.) to identify the bottleneck. <br> 3. Try online debug with [interactive endpoints](how-to-interactive-jobs.md) if the job is running or locally debug of your code. |
| Finalizing | Job is in post processing after execution complete. Time spent in this stage is mainly for some post processes like: output uploading, metric/logs uploading and resources clean up.| It will be short for command job. However, might be very long for PRS/MPI job because for a distributed job, the finalizing status is from the first node starting finalizing to the last node done finalizing. | Change your step job output mode from upload to mount if you find unexpected long finalizing time, or open support case via Azure portal. |

### Different view of Gantt chart

- Critical path
  - You'll see only the step jobs in the pipeline's critical path (jobs that have a dependency).
  - By default the critical path of the pipeline job is shown.
- Flatten view
  - You'll see all step jobs.
  - In this view, you'll see more nodes than in critical path.
- Compact view
  - You'll only see step jobs that are longer than 30 seconds.
- Hierarchical view.
  - You'll see all jobs including pipeline component jobs and step jobs.
