
# Use the Responsible AI dashboard in Azure Machine Learning studio

Responsible AI dashboards are linked to your registered models. To view your Responsible AI dashboard, go into your model registry and select the registered model you've generated a Responsible AI dashboard for. Then, select the **Responsible AI** tab to view a list of generated dashboards.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/view-responsible-ai-model-page.png" alt-text="Screenshot of the model details pane in Azure Machine Learning studio, with the 'Responsible AI' tab highlighted." lightbox= "./media/how-to-responsible-ai-dashboard/view-responsible-ai-model-page.png":::

You can configure multiple dashboards and attach them to your registered model. Various combinations of components (interpretability, error analysis, causal analysis, and so on) can be attached to each Responsible AI dashboard. The following image displays a dashboard's customization and the components that were generated within it. In each dashboard, you can view or hide various components within the dashboard UI itself.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/view-responsible-ai-dashboard.png" alt-text="Screenshot of Responsible AI tab with a dashboard name highlighted." lightbox = "./media/how-to-responsible-ai-dashboard/view-responsible-ai-dashboard.png":::

Select the name of the dashboard to open it into a full view in your browser. To return to your list of dashboards, you can select **Back to models details** at any time.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/dashboard-full-view.png" alt-text="Screenshot of a Responsible AI dashboard with the 'Back to model details' button highlighted." lightbox = "./media/how-to-responsible-ai-dashboard/dashboard-full-view.png":::

## Full functionality with integrated compute resource

Some features of the Responsible AI dashboard require dynamic, on-the-fly, and real-time computation (for example, what-if analysis). Unless you connect a compute resource to the dashboard, you might find some functionality missing. When you connect to a compute resource, you enable full functionality of your Responsible AI dashboard for the following components:

- **Error analysis**
    - Setting your global data cohort to any cohort of interest will update the error tree instead of disabling it.
    - Selecting other error or performance metrics is supported.
    - Selecting any subset of features for training the error tree map is supported.
    - Changing the minimum number of samples required per leaf node and error tree depth is supported.
    - Dynamically updating the heat map for up to two features is supported.
- **Feature importance**
    - An individual conditional expectation (ICE) plot in the individual feature importance tab is supported.
- **Counterfactual what-if**
    - Generating a new what-if counterfactual data point to understand the minimum change required for a desired outcome is supported.
- **Causal analysis**
    - Selecting any individual data point, perturbing its treatment features, and seeing the expected causal outcome of causal what-if is supported (only for regression machine learning scenarios).

You can also find this information on the Responsible AI dashboard page by selecting the **Information** icon, as shown in the following image:

:::image type="content" source="./media/how-to-responsible-ai-dashboard/compute-view-full-functionality.png" alt-text="Screenshot of the 'Information' icon on the Responsible AI dashboard.":::

### Enable full functionality of the Responsible AI dashboard

1. Select a running compute instance in the **Compute** dropdown list at the top of the dashboard. If you don’t have a running compute, create a new compute instance by selecting the plus sign (**+**) next to the dropdown. Or you can select the **Start compute** button to start a stopped compute instance. Creating or starting a compute instance might take few minutes.
