1. You'll see the values you need for **<SUBSCRIPTION_ID>**, **<RESOURCE_GROUP>**, and **<AML_WORKSPACE_NAME>**.
1. Copy a value, then close the window and paste that into your code.  Open the tool again to get the next value.

:::image type="content" source="media/tutorial-pipeline-python-sdk/find-info.png" alt-text="Screenshot shows how to find values needed for your code.":::

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=ml_client)]

The result is a handler to the workspace that you'll use to manage other resources and jobs.

> [!IMPORTANT]
> Creating MLClient will not connect to the workspace. The client initialization is lazy, it will wait for the first time it needs to make a call (in the notebook below, that will happen during dataset registration).

## Register data from an external url

The data you use for training is usually in one of the locations below:

* Local machine
* Web
* Big Data Storage services (for example, Azure Blob, Azure Data Lake Storage, SQL)
 
Azure ML uses a `Data` object to register a reusable definition of data, and consume data within a pipeline. In the section below, you'll consume some data from web url as one example. Data from other sources can be created as well. `Data` assets from other sources can be created as well.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=credit_data)]

This code just created a `Data` asset, ready to be consumed as an input by the pipeline that you'll define in the next sections. In addition, you can register the data to your workspace so it becomes reusable across pipelines.

Registering the data asset will enable you to:

* Reuse and share the data asset in future pipelines
* Use versions to track the modification to the data asset
* Use the data asset from Azure ML designer, which is Azure ML's GUI for pipeline authoring

Since this is the first time that you're making a call to the workspace, you may be asked to authenticate. Once the authentication is complete, you'll then see the dataset registration completion message.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=update-credit_data)]

In the future, you can fetch the same dataset from the workspace using `credit_dataset = ml_client.data.get("<DATA ASSET NAME>", version='<VERSION>')`.

## Create a compute resource to run your pipeline

Each step of an Azure ML pipeline can use a different compute resource for running the specific job of that step. It can be single or multi-node machines with Linux or Windows OS, or a specific compute fabric like Spark.

In this section, you'll provision a Linux [compute cluster](how-to-create-attach-compute-cluster.md?tabs=python). See the [full list on VM sizes and prices](https://azure.microsoft.com/pricing/details/machine-learning/) .

For this tutorial you only need a basic cluster, so we'll  use a Standard_DS3_v2 model with 2 vCPU cores, 7 GB RAM and create an Azure ML Compute.  

> [!TIP]
> If you already have a compute cluster, replace "cpu-cluster" in the code below with the name of your cluster.  This will keep you from creating another one.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=cpu_cluster)]

## Create a job environment for pipeline steps

So far, you've created a development environment on the compute instance, your development machine. You'll also need an environment to use for each step of the pipeline. Each step can have its own environment, or you can use some common environments for multiple steps.

In this example, you'll create a conda environment for your jobs, using a conda yaml file.
First, create a directory to store the file in.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=dependencies_dir)]

Now, create the file in the dependencies directory.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=conda.yml)]
