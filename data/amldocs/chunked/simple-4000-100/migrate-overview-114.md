| Computer Vision| | - Apply Image Transformation </br> - Convert to Image Directory </br> - Init Image Transformation </br> - Split Image Directory  </br> - DenseNet Image Classification   </br>- ResNet Image Classification |

For more information on how to use individual designer components, see the [designer component reference](./component-reference/component-reference.md).

### What if a designer component is missing?

Azure Machine Learning designer contains the most popular modules from Studio (classic). It also includes new modules that take advantage of the latest machine learning techniques. 

If your migration is blocked due to missing modules in the designer, contact us by [creating a support ticket](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest).

## Example migration

The following experiment migration highlights some of the differences between Studio (classic) and Azure Machine Learning.

### Datasets

In Studio (classic), **datasets** were saved in your workspace and could only be used by Studio (classic).

![automobile-price-classic-dataset](./media/migrate-overview/studio-classic-dataset.png)

In Azure Machine Learning, **datasets** are registered to the workspace and can be used across all of Azure Machine Learning. For more information on the benefits of Azure Machine Learning datasets, see [Secure data access](./v1/concept-data.md).


### Pipeline

In Studio (classic), **experiments** contained the processing logic for your work. You created experiments with drag-and-drop modules.

![automobile-price-classic-experiment](./media/migrate-overview/studio-classic-experiment.png)

In Azure Machine Learning, **pipelines** contain the processing logic for your work. You can create pipelines with either drag-and-drop modules or by writing code.

![automobile-price-aml-pipeline](./media/migrate-overview/aml-pipeline.png)

### Web service endpoint

Studio (classic) used **REQUEST/RESPOND API** for real-time prediction and **BATCH EXECUTION API** for batch prediction or retraining.

![automobile-price-classic-webservice](./media/migrate-overview/studio-classic-web-service.png)

Azure Machine Learning uses **real-time endpoints** (managed endpoints) for real-time prediction and **pipeline endpoints** for batch prediction or retraining.

![automobile-price-aml-endpoint](./media/migrate-overview/aml-endpoint.png)

## Next steps

In this article, you learned the high-level requirements for migrating to Azure Machine Learning. For detailed steps, see the other articles in the Studio (classic) migration series:

1. **Migration overview**.
1. [Migrate dataset](migrate-register-dataset.md).
1. [Rebuild a Studio (classic) training pipeline](migrate-rebuild-experiment.md).
1. [Rebuild a Studio (classic) web service](migrate-rebuild-web-service.md).
1. [Integrate an Azure Machine Learning web service with client apps](migrate-rebuild-integrate-with-client-app.md).
1. [Migrate Execute R Script](migrate-execute-r-script.md).

See the [Azure Machine Learning Adoption Framework](https://aka.ms/mlstudio-classic-migration-repo) for additional migration resources.
