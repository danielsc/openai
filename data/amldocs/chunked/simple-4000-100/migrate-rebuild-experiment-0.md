
# Rebuild a Studio (classic) experiment in Azure Machine Learning

[!INCLUDE [ML Studio (classic) retirement](../../includes/machine-learning-studio-classic-deprecation.md)]

In this article, you learn how to rebuild an ML Studio (classic) experiment in Azure Machine Learning. For more information on migrating from Studio (classic), see [the migration overview article](migrate-overview.md).

Studio (classic) **experiments** are similar to **pipelines** in Azure Machine Learning. However, in Azure Machine Learning pipelines are built on the same back-end that powers the SDK. This means that you have two options for machine learning development: the drag-and-drop designer or code-first SDKs.

For more information on building pipelines with the SDK, see [What are Azure Machine Learning pipelines](concept-ml-pipelines.md).


## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- An Azure Machine Learning workspace. [Create workspace resources](quickstart-create-resources.md).
- A Studio (classic) experiment to migrate.
- [Upload your dataset](migrate-register-dataset.md) to Azure Machine Learning.

## Rebuild the pipeline

After you [migrate your dataset to Azure Machine Learning](migrate-register-dataset.md), you're ready to recreate your experiment.

In Azure Machine Learning, the visual graph is called a **pipeline draft**. In this section, you recreate your classic experiment as a pipeline draft.

1. Go to Azure Machine Learning studio ([ml.azure.com](https://ml.azure.com))
1. In the left navigation pane, select **Designer** > **Easy-to-use prebuilt modules**
    ![Screenshot showing how to create a new pipeline draft.](./media/tutorial-designer-automobile-price-train-score/launch-designer.png)

1. Manually rebuild your experiment with designer components.
    
    Consult the [module-mapping table](migrate-overview.md#studio-classic-and-designer-component-mapping) to find replacement modules. Many of Studio (classic)'s most popular modules have identical versions in the designer.

    > [!Important]
    > If your experiment uses the Execute R Script module, you need to perform additional steps to migrate your experiment. For more information, see [Migrate R Script modules](migrate-execute-r-script.md).

1. Adjust parameters.
    
    Select each module and adjust the parameters in the module settings panel to the right. Use the parameters to recreate the functionality of your Studio (classic) experiment. For more information on each module, see the [module reference](./component-reference/component-reference.md).

## Submit a job and check results

After you recreate your Studio (classic) experiment, it's time to submit a **pipeline job**.

A pipeline job executes on a **compute target** attached to your workspace. You can set a default compute target for the entire pipeline, or you can specify compute targets on a per-module basis.

Once you submit a job from a pipeline draft, it turns into a **pipeline job**. Each pipeline job is recorded and logged in Azure Machine Learning.

To set a default compute target for the entire pipeline:
1. Select the **Gear icon** ![Gear icon in the designer](./media/tutorial-designer-automobile-price-train-score/gear-icon.png) next to the pipeline name.
1. Select **Select compute target**.
1. Select an existing compute, or create a new compute by following the on-screen instructions.

Now that your compute target is set, you can submit a pipeline job:

1. At the top of the canvas, select **Submit**.
1. Select **Create new** to create a new experiment.
    
    Experiments organize similar pipeline jobs together. If you run a pipeline multiple times, you can select the same experiment for successive jobs. This is useful for logging and tracking.
1. Enter an experiment name. Then, select **Submit**.

    The first job may take up to 20 minutes. Since the default compute settings have a minimum node size of 0, the designer must allocate resources after being idle. Successive jobs take less time, since the nodes are already allocated. To speed up the running time, you can create a compute resources with a minimum node size of 1 or greater.
