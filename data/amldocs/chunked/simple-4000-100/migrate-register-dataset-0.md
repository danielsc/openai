
# Migrate a Studio (classic) dataset to Azure Machine Learning

[!INCLUDE [ML Studio (classic) retirement](../../includes/machine-learning-studio-classic-deprecation.md)]

In this article, you learn how to migrate a Studio (classic) dataset to Azure Machine Learning. For more information on migrating from Studio (classic), see [the migration overview article](migrate-overview.md).

You have three options to migrate a dataset to Azure Machine Learning. Read each section to determine which option is best for your scenario.


|Where is the data? | Migration option  |
|---------|---------|
|In Studio (classic)     |  Option 1: [Download the dataset from Studio (classic) and upload it to Azure Machine Learning](#download-the-dataset-from-studio-classic).      |
|Cloud storage     | Option 2: [Register a dataset from a cloud source](#import-data-from-cloud-sources). <br><br>  Option 3: [Use the Import Data module to get data from a cloud source](#import-data-from-cloud-sources).        |

> [!NOTE]
> Azure Machine Learning also supports [code-first workflows](./v1/how-to-create-register-datasets.md) for creating and managing datasets. 

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- An Azure Machine Learning workspace. [Create workspace resources](quickstart-create-resources.md).
- A Studio (classic) dataset to migrate.


## Download the dataset from Studio (classic)

The simplest way to migrate a  Studio (classic) dataset to Azure Machine Learning is to download your dataset and register it in Azure Machine Learning. This creates a new copy of your dataset and uploads it to an Azure Machine Learning datastore.

You can download the following Studio (classic) dataset types directly.

* Plain text (.txt)
* Comma-separated values (CSV) with a header (.csv) or without (.nh.csv)
* Tab-separated values (TSV) with a header (.tsv) or without (.nh.tsv)
* Excel file
* Zip file (.zip)

To download datasets directly:
1. Go to your Studio (classic) workspace ([https://studio.azureml.net](https://studio.azureml.net)).
1. In the left navigation bar, select the **Datasets** tab.
1. Select the dataset(s) you want to download.
1. In the bottom action bar, select **Download**.

    :::image type="content" source="./media/migrate-register-dataset/download-dataset.png" alt-text="AScreenshot showing how to download a dataset in Studio (classic)." lightbox = "./media/migrate-register-dataset/download-dataset.png":::

For the following data types, you must use the **Convert to CSV** module to download datasets.

* SVMLight data (.svmlight) 
* Attribute Relation File Format (ARFF) data (.arff) 
* R object or workspace file (.RData)
* Dataset type (.data). Dataset type is  Studio(classic) internal data type for module output.

To convert your dataset to a CSV and download the results:

1. Go to your Studio (classic) workspace ([https://studio.azureml.net](https://studio.azureml.net)).
1. Create a new experiment.
1. Drag and drop the dataset you want to download onto the canvas.
1. Add a **Convert to CSV** module.
1. Connect the **Convert to CSV** input port to the output port of your dataset.
1. Run the experiment.
1. Right-click the **Convert to CSV** module.
1. Select **Results dataset** > **Download**.

    :::image type="content" source="./media/migrate-register-dataset/csv-download-dataset.png" alt-text="Screenshot showing how to setup a convert to CSV pipeline." lightbox = "./media/migrate-register-dataset/csv-download-dataset.png":::

### Upload your dataset to Azure Machine Learning

After you download the data file, you can register it as a data asset in Azure Machine Learning:
1. Navigate to [Azure Machine Learning studio](https://ml.azure.com)

1. Under __Assets__ in the left navigation, select __Data__. On the Data assets tab, select Create
:::image type="content" source="./media/how-to-create-data-assets/data-assets-create.png" alt-text="Screenshot highlights Create in the Data assets tab.":::
