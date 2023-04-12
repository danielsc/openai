For automated ML jobs, you need to ensure the file datastore that connects to your AzureFile storage has the appropriate authentication credentials. Otherwise, the following message results. Learn how to [update your data access authentication credentials](v1/how-to-train-with-datasets.md#azurefile-storage).

Error message: 
`Could not create a connection to the AzureFileService due to missing credentials. Either an Account Key or SAS token needs to be linked the default workspace blob store.`

## Data schema

When you try to create a new automated ML experiment via the **Edit and submit** button in the Azure Machine Learning studio, the data schema for the new experiment must match the schema of the data that was used in the original experiment. Otherwise, an error message similar to the following results. Learn more about how to [edit and submit experiments from the studio UI](how-to-use-automated-ml-for-ml-models.md#edit-and-submit-jobs-preview).

Error message non-vision experiments: ` Schema mismatch error: (an) additional column(s): "Column1: String, Column2: String, Column3: String", (a) missing column(s)`

Error message for vision datasets: `Schema mismatch error: (an) additional column(s): "dataType: String, dataSubtype: String, dateTime: Date, category: String, subcategory: String, status: String, address: String, latitude: Decimal, longitude: Decimal, source: String, extendedProperties: String", (a) missing column(s): "image_url: Stream, image_details: DataRow, label: List" Vision dataset error(s): Vision dataset should have a target column with name 'label'. Vision dataset should have labelingProjectType tag with value as 'Object Identification (Bounding Box)'.`

## Databricks
See [How to configure an automated ML experiment with Databricks](how-to-configure-databricks-automl-environment.md#troubleshooting).


## Forecasting R2 score is always zero

 This issue arises if the training data provided has time series that contains the same value for the last `n_cv_splits` + `forecasting_horizon` data points.

If this pattern is expected in your time series, you can switch your primary metric to **normalized root mean squared error**.

## Failed deployment

 For versions <= 1.18.0 of the SDK, the base image created for deployment may fail with the following error: `ImportError: cannot import name cached_property from werkzeug`.

  The following steps can work around the issue:

  1. Download the model package
  1. Unzip the package
  1. Deploy using the unzipped assets

## Azure Functions application
  
  Automated ML does not currently support Azure Functions applications. 

## Sample notebook failures

 If a sample notebook fails with an error that property, method, or library does not exist:

* Ensure that the correct kernel has been selected in the Jupyter Notebook. The kernel is displayed in the top right of the notebook page. The default is *azure_automl*. The kernel is saved as part of the notebook. If you switch to a new conda environment, you need to select the new kernel in the notebook.

  * For Azure Notebooks, it should be Python 3.6.
  * For local conda environments, it should be the conda environment name that you specified in automl_setup.

* To ensure the notebook is for the SDK version that you are using,
  * Check the SDK version by executing `azureml.core.VERSION` in a Jupyter Notebook cell.
  * You can download previous version of the sample notebooks from GitHub with these steps:
    1. Select the `Branch` button
    1. Navigate to the `Tags` tab
    1. Select the version
    
## Experiment throttling

If you have over 100 automated ML experiments, this may cause new automated ML experiments to have long run times. 

## VNet Firewall Setting Download Failure

If you are under virtual networks (VNets), you may run into model download failures when using AutoML NLP. This is because network traffic is blocked from downloading the models and tokenizers from Azure CDN. To unblock this, please allow list the below URLs in the “Application rules” setting of the VNet firewall policy:
