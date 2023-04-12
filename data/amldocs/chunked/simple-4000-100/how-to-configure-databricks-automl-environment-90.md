### AutoML config settings

In AutoML config, when using Azure Databricks add the following parameters:

- ```max_concurrent_iterations``` is based on number of worker nodes in your cluster.
- ```spark_context=sc``` is based on the default spark context.

## ML notebooks that work with Azure Databricks

Try it out:
+ While many sample notebooks are available, **only [these sample notebooks](https://github.com/Azure/azureml-examples/tree/main/v1/python-sdk/tutorials/automl-with-databricks) work with Azure Databricks.**

+ Import these samples directly from your workspace. See below:
![Select Import](./media/how-to-configure-environment/azure-db-screenshot.png)
![Import Panel](./media/how-to-configure-environment/azure-db-import.png)

+ Learn how to [create a pipeline with Databricks as the training compute](v1/how-to-create-machine-learning-pipelines.md).

## Troubleshooting

* **Databricks cancel an automated machine learning run**: When you use automated machine learning capabilities on Azure Databricks, to cancel a run and start a new experiment run, restart your Azure Databricks cluster.

* **Databricks >10 iterations for automated machine learning**: In automated machine learning settings, if you have more than 10 iterations, set `show_output` to `False` when you submit the run.

* **Databricks widget for the Azure Machine Learning SDK and automated machine learning**: The Azure Machine Learning SDK widget isn't supported in a Databricks notebook because the notebooks can't parse HTML widgets. You can view the widget in the portal by using this Python code in your Azure Databricks notebook cell:

    ```
    displayHTML("<a href={} target='_blank'>Azure Portal: {}</a>".format(local_run.get_portal_url(), local_run.id))
    ```

* **Failure when installing packages**

    Azure Machine Learning SDK installation fails on Azure Databricks when more packages are installed. Some packages, such as `psutil`, can cause conflicts. To avoid installation errors, install packages by freezing the library version. This issue is related to Databricks and not to the Azure Machine Learning SDK. You might experience this issue with other libraries, too. Example:
    
    ```python
    psutil cryptography==1.5 pyopenssl==16.0.0 ipython==2.2.0
    ```

    Alternatively, you can use init scripts if you keep facing install issues with Python libraries. This approach isn't officially supported. For more information, see [Cluster-scoped init scripts](/azure/databricks/clusters/init-scripts#cluster-scoped-init-scripts).

* **Import error: cannot import name `Timedelta` from `pandas._libs.tslibs`**: If you see this error when you use automated machine learning, run the two following lines in your notebook:
    ```
    %sh rm -rf /databricks/python/lib/python3.7/site-packages/pandas-0.23.4.dist-info /databricks/python/lib/python3.7/site-packages/pandas
    %sh /databricks/python/bin/pip install pandas==0.23.4
    ```

* **Import error: No module named 'pandas.core.indexes'**: If you see this error when you use automated machine learning:

    1. Run this command to install two packages in your Azure Databricks cluster:
    
       ```bash
       scikit-learn==0.19.1
       pandas==0.22.0
       ```
    
    1. Detach and then reattach the cluster to your notebook.
    
    If these steps don't solve the issue, try restarting the cluster.

* **FailToSendFeather**: If you see a `FailToSendFeather` error when reading data on Azure Databricks cluster, refer to the following solutions:
    
    * Upgrade `azureml-sdk[automl]` package to the latest version.
    * Add `azureml-dataprep` version 1.1.8 or above.
    * Add `pyarrow` version 0.11 or above.
  

## Next steps

- [Train and deploy a model](tutorial-train-deploy-notebook.md) on Azure Machine Learning with the MNIST dataset.
- See the [Azure Machine Learning SDK for Python reference](/python/api/overview/azure/ml/intro).
