
# Migrate to Azure Machine Learning from ML Studio (classic)

> [!IMPORTANT]
> Support for Machine Learning Studio (classic) will end on 31 August 2024. We recommend you transition to [Azure Machine Learning](./overview-what-is-azure-machine-learning.md) by that date.
>
> Beginning 1 December 2021, you will not be able to create new Machine Learning Studio (classic) resources. Through 31 August 2024, you can continue to use the existing Machine Learning Studio (classic) resources.  
>
> ML Studio (classic) documentation is being retired and may not be updated in the future.

Learn how to migrate from Studio (classic) to Azure Machine Learning. Azure Machine Learning provides a modernized data science platform that combines no-code and code-first approaches.

This is a guide for a basic "lift and shift" migration. If you want to optimize an existing machine learning workflow, or modernize a machine learning platform, see the [Azure Machine Learning adoption framework](https://aka.ms/mlstudio-classic-migration-repo) for additional resources including digital survey tools, worksheets, and planning templates.

Please work with your Cloud Solution Architect on the migration. 

![Azure ML adoption framework](./media/migrate-overview/aml-adoption-framework.png)

## Recommended approach

To migrate to Azure Machine Learning, we recommend the following approach:

> [!div class="checklist"]
> * Step 1: Assess Azure Machine Learning
> * Step 2: Define a strategy and plan
> * Step 3: Rebuild experiments and web services
> * Step 4: Integrate client apps
> * Step 5: Clean up Studio (classic) assets
> * Step 6: Review and expand scenarios


## Step 1: Assess Azure Machine Learning
1. Learn about [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/); its benefits, costs, and architecture.

1. Compare the capabilities of Azure Machine Learning and Studio (classic).

    >[!NOTE]
    > The **designer** feature in Azure Machine Learning provides a similar drag-and-drop experience to Studio (classic). However, Azure Machine Learning also provides robust [code-first workflows](concept-model-management-and-deployment.md) as an alternative. This migration series focuses on the designer, since it's most similar to the Studio (classic) experience.

    [!INCLUDE [aml-compare-classic](../../includes/machine-learning-compare-classic-aml.md)]

3. Verify that your critical Studio (classic) modules are supported in Azure Machine Learning designer. For more information, see the [Studio (classic) and designer component-mapping](#studio-classic-and-designer-component-mapping) table below.

4. [Create an Azure Machine Learning workspace](quickstart-create-resources.md).

## Step 2: Define a strategy and plan

1. Define business justifications and expected outcomes.
1. Align an actionable Azure Machine Learning adoption plan to business outcomes.
1. Prepare people, processes, and environments for change.

Please work with your Cloud Solution Architect to define your strategy. 

See the [Azure Machine Learning Adoption Framework](https://aka.ms/mlstudio-classic-migration-repo) for planning resources including a planning doc template. 

## Step 3: Rebuild your first model

After you've defined a strategy, migrate your first model.

1. [Migrate datasets to Azure Machine Learning](migrate-register-dataset.md).
1. Use the designer to [rebuild experiments](migrate-rebuild-experiment.md).
1. Use the designer to [redeploy web services](migrate-rebuild-web-service.md).

    >[!NOTE]
    > Above guidance are built on top of AzureML v1 concepts and features. AzureML has CLI v2 and Python SDK v2. We suggest to rebuild your ML Studio(classic) models using v2 instead of v1. Start with AzureML v2 [here](./concept-v2.md)  

## Step 4: Integrate client apps

1. Modify client applications that invoke Studio (classic) web services to use your new [Azure Machine Learning endpoints](migrate-rebuild-integrate-with-client-app.md).

## Step 5: Cleanup Studio (classic) assets
