1. Select a running compute instance in the **Compute** dropdown list at the top of the dashboard. If you don’t have a running compute, create a new compute instance by selecting the plus sign (**+**) next to the dropdown. Or you can select the **Start compute** button to start a stopped compute instance. Creating or starting a compute instance might take few minutes.

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/select-compute.png" alt-text="Screenshot of the 'Compute' dropdown box for selecting a running compute instance." lightbox = "./media/how-to-responsible-ai-dashboard/select-compute.png":::
    
2. When a compute is in a *Running* state, your Responsible AI dashboard starts to connect to the compute instance. To achieve this, a terminal process is created on the selected compute instance, and a Responsible AI endpoint is started on the terminal. Select **View terminal outputs** to view the current terminal process.

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/compute-connect-terminal.png" alt-text="Screenshot showing that the responsible AI dashboard is connecting to a compute resource." lightbox = "./media/how-to-responsible-ai-dashboard/compute-connect-terminal.png":::

3. When your Responsible AI dashboard is connected to the compute instance, you'll see a green message bar, and the dashboard is now fully functional.

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/compute-terminal-connected.png" alt-text="Screenshot showing that the dashboard is connected to the compute instance." lightbox= "./media/how-to-responsible-ai-dashboard/compute-terminal-connected.png":::

4. If the process takes a while and your Responsible AI dashboard is still not connected to the compute instance, or a red error message bar is displayed, it means there are issues with starting your Responsible AI endpoint. Select **View terminal outputs** and scroll down to the bottom to view the error message.

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/compute-terminal-error.png" alt-text="Screenshot of an error connecting to a compute." lightbox ="./media/how-to-responsible-ai-dashboard/compute-terminal-error.png":::

    If you're having difficulty figuring out how to resolve the "failed to connect to compute instance" issue, select the **Smile** icon at the upper right. Submit feedback to us about any error or issue you encounter. You can include a screenshot and your email address in the feedback form.

## UI overview of the Responsible AI dashboard

The Responsible AI dashboard includes a robust, rich set of visualizations and functionality to help you analyze your machine learning model or make data-driven business decisions:

- [Global controls](#global-controls)
- [Error analysis](#error-analysis)
- [Model overview and fairness metrics](#model-overview-and-fairness-metrics)
- [Data analysis](#data-analysis)
- [Feature importance (model explanations)](#feature-importances-model-explanations)
- [Counterfactual what-if](#counterfactual-what-if)
- [Causal analysis](#causal-analysis)

### Global controls

At the top of the dashboard, you can create cohorts (subgroups of data points that share specified characteristics) to focus your analysis of each component. The name of the cohort that's currently applied to the dashboard is always shown at the top left of your dashboard. The default view in your dashboard is your whole dataset, titled **All data (default)**.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/view-dashboard-global-controls.png" alt-text="Screenshot of a responsible AI dashboard showing all data." lightbox = "./media/how-to-responsible-ai-dashboard/view-dashboard-global-controls.png":::

1. **Cohort settings**: Allows you to view and modify the details of each cohort in a side panel.
2. **Dashboard configuration**: Allows you to view and modify the layout of the overall dashboard in a side panel.
