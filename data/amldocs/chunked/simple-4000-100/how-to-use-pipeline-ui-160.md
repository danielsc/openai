:::image type="content" source="./media/how-to-use-pipeline-ui/compare-graph.png" alt-text="Screenshot of detail comparison with compare graph highlighted." lightbox= "./media/how-to-use-pipeline-ui/compare-graph.png":::

### How to debug your failed node in a pipeline by comparing to similar completed node

If you only updated node properties and changed nothing in the pipeline, then you can debug the node by comparing it with the jobs that are submitted from the same component.

#### Find the job to compare with

1. Find a successful job to compare with by viewing all runs submitted from the same component.
    1. Right select the failed node and select *View Jobs*. This will give you a list of all the jobs.
  
        :::image type="content" source="./media/how-to-use-pipeline-ui/view-jobs.png" alt-text="Screenshot that shows a failed node with view jobs highlighted." lightbox= "./media/how-to-use-pipeline-ui/view-jobs.png":::

    1. Choose a completed job as a comparison target.
1. After you found a failed and completed job to compare with, add the two jobs to the comparison candidate list.
    1. For the failed node, right select and select *Add to compare*.
    1. For the completed job, go to its parent pipeline and located the completed job. Then select *Add to compare*.
1. Once the two jobs are in the comparison list, select **Compare detail** to show the differences.

### Share the comparison results

To share your comparison results select **Share** and copying the link. For example, you might find out that the dataset difference might of lead to the failure but you aren't a dataset specialist, you can share the comparison result with a data engineer on your team.

:::image type="content" source="./media/how-to-use-pipeline-ui/share.png" alt-text="Screenshot showing the share button and the link you should copy." lightbox= "./media/how-to-use-pipeline-ui/share.png":::

## View profiling to debug pipeline performance issues (preview)

Profiling (preview) can help you debug pipeline performance issues such as hang, long pole etc. Profiling will list the duration information of each step in a pipeline and provide a Gantt chart for visualization.

Profiling enables you to:

- Quickly find which node takes longer time than expected.
- Identify the time spent of job on each status

To enable this feature:

1. Navigate to Azure Machine Learning studio UI.
2. Select **Manage preview features** (megaphone icon) among the icons on the top right side of the screen.
3. In **Managed preview feature** panel, toggle on **View profiling to debug pipeline performance issues** feature.

### How to find the node that runs totally the longest

1. On the Jobs page, select the job name and enter the job detail page.
1. In the action bar, select **View profiling**. Profiling only works for root level pipeline. It will take a few minutes to load the next page.

    :::image type="content" source="./media/how-to-use-pipeline-ui/view-profiling.png" alt-text="Screenshot showing the pipeline at root level with the view profiling button highlighted." lightbox= "./media/how-to-use-pipeline-ui/view-profiling.png":::

1. After the profiler loads, you'll see a Gantt chart. By Default the critical path of a pipeline is shown. A critical path is a subsequence of steps that determine a pipeline job's total duration.

    :::image type="content" source="./media/how-to-use-pipeline-ui/critical-path.png" alt-text="Screenshot showing the Gantt chart and the critical path." lightbox= "./media/how-to-use-pipeline-ui/critical-path.png":::

1. To find the step that takes the longest, you can either view the Gantt chart or the table below it.

    In the Gantt chart, the length of each bar shows how long the step takes, steps with a longer bar length take more time. You can also filter the table below by "total duration". When you select a row in the table, it will show you the node in the Gantt chart too. When you select a bar on the Gantt chart it will also highlight it in the table.
