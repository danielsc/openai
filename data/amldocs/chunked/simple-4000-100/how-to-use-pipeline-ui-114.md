During iterative model development, you may have a baseline pipeline, and then do some modifications such as changing a parameter, dataset or compute resource, etc. If your new pipeline failed, you can use pipeline comparison to identify what has changed by comparing it to the baseline pipeline, which could help with figuring out why it failed.

#### Compare a pipeline with its parent

The first thing you should check when debugging is to locate the failed node and check the logs.

For example, you may get an error message showing that your pipeline failed due to out-of-memory. If your pipeline is cloned from a completed parent pipeline, you can use pipeline comparison to see what has changed.

1. Select **Show lineage**.
1. Select the link under "Cloned From". This will open a new browser tab with the parent pipeline.

      :::image type="content" source="./media/how-to-use-pipeline-ui/cloned-from.png" alt-text="Screenshot showing the cloned from link, with the previous step, the lineage button highlighted." lightbox= "./media/how-to-use-pipeline-ui/cloned-from.png":::

1. Select **Add to compare** on the failed pipeline and the parent pipeline. This will add them in the comparison candidate list.

      :::image type="content" source="./media/how-to-use-pipeline-ui/comparison-list.png" alt-text="Screenshot showing the comparison list with a parent and child pipeline added." lightbox= "./media/how-to-use-pipeline-ui/comparison-list.png":::

### Compare topology

Once the two pipelines are added to the comparison list, you'll have two options: **Compare detail** and **Compare graph**. **Compare graph** allows you to compare pipeline topology.

**Compare graph** shows you the graph topology changes between pipeline A and B. The special nodes in pipeline A are highlighted in red and marked with "A only". The special nodes in pipeline B are in green and marked with "B only". The shared nodes are in gray. If there are differences on the shared nodes, what has been changed is shown on the top of node.

There are three categories of changes with summaries viewable in the detail page, parameter change, input source, pipeline component. When the pipeline component is changed this means that there's a topology change inside or an inner node parameter change, you can select the folder icon on the pipeline component node to dig down into the details. Other changes can be detected by viewing the colored nodes in the compare graph.

   :::image type="content" source="./media/how-to-use-pipeline-ui/parameter-changed.png" alt-text="Screenshot showing the parameter changed and the component information tab." lightbox= "./media/how-to-use-pipeline-ui/parameter-changed.png":::

### Compare pipeline meta info and properties

If you investigate the dataset difference and find that data or topology doesn't seem to be the root cause of failure, you can also check the pipeline details like pipeline parameter, output or run settings.

**Compare graph** is used to compare pipeline topology, **Compare detail** is used to compare pipeline properties link meta info or settings.

To access the detail comparison, go to the comparison list, select **Compare details** or select **Show compare details** on the pipeline comparison page.

You'll see *Pipeline properties* and *Run properties*.

- Pipeline properties include pipeline parameters, run and output setting, etc.
- Run properties include job status, submit time and duration, etc.

The following screenshot shows an example of using the detail comparison, where the default compute setting might have been the reason for failure.

:::image type="content" source="./media/how-to-use-pipeline-ui/compute.png" alt-text="Screenshot showing the comparison overview of the default compute." lightbox= "./media/how-to-use-pipeline-ui/compute.png":::

To quickly check the topology comparison, select the pipeline name and select **Compare graph**.

:::image type="content" source="./media/how-to-use-pipeline-ui/compare-graph.png" alt-text="Screenshot of detail comparison with compare graph highlighted." lightbox= "./media/how-to-use-pipeline-ui/compare-graph.png":::
