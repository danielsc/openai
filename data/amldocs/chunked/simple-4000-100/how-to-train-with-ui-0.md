
# Create a training job with the job creation UI (preview)

There are many ways to create a training job with Azure Machine Learning. You can use the CLI (see [Train models (create jobs)](how-to-train-model.md)), the REST API (see [Train models with REST (preview)](how-to-train-with-rest.md)), or you can use the UI to directly create a training job. In this article, you'll learn how to use your own data and code to train a machine learning model with the job creation UI in Azure Machine Learning studio.

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/machine-learning/search/) today.

* An Azure Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md). 

* Understanding of what a job is in Azure Machine Learning. See [how to train models]how-to-train-model.md).

## Get started

1. Sign in to [Azure Machine Learning studio](https://ml.azure.com). 

1. Select your subscription and workspace.
 
* You may enter the job creation UI from the homepage. Click **Create new** and select **Job**. 
[![Azure Machine Learning studio homepage](media/how-to-train-with-ui/home-entry.png)](media/how-to-train-with-ui/home-entry.png)

* Or, you may enter the job creation from the left pane. Click **+New** and select **Job**. 
[![Azure Machine Learning studio left navigation](media/how-to-train-with-ui/left-nav-entry.png)](media/how-to-train-with-ui/left-nav-entry.png)


These options will all take you to the job creation panel, which has a wizard for configuring and creating a training job. 

## Select compute resources

The first step in the job creation UI is to select the compute target on which you'd like your job to run. The job creation UI supports several compute types:

| Compute Type | Introduction | 
| --- | --- | 
| Compute instance | [What is an Azure Machine Learning compute instance?](concept-compute-instance.md) | 
| Compute cluster | [What is a compute cluster?](how-to-create-attach-compute-cluster.md#what-is-a-compute-cluster) | 
| Attached Compute (Kubernetes cluster) | [Configure and attach Kubernetes cluster anywhere (preview)](how-to-attach-kubernetes-anywhere.md). | 

1. Select a compute type
1. Select an existing compute resource. The dropdown shows the node information and SKU type to help your choice.
1. For a compute cluster or a Kubernetes cluster, you may also specify how many nodes you want for the job in **Instance count**. The default number of instances is 1. 
1. When you're satisfied with your choices, choose **Next**. 
 [![Select a compute cluster](media/how-to-train-with-ui/compute-cluster.png)](media/how-to-train-with-ui/compute-cluster.png)

If you're using Azure Machine Learning for the first time, you'll see an empty list and a link to create a new compute. 

 [![Create a new compute instance](media/how-to-train-with-ui/create-new-compute.png)](media/how-to-train-with-ui/create-new-compute.png)

For more information on creating the various types, see:

| Compute Type | How to | 
| --- | --- | 
| Compute instance | [Create and manage an Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md) | 
| Compute cluster | [Create an Azure Machine Learning compute cluster](how-to-create-attach-compute-cluster.md) | 
| Attached Kubernetes cluster | [Attach an Azure Arc-enabled Kubernetes cluster](how-to-attach-kubernetes-anywhere.md) | 

## Specify the necessary environment

After selecting a compute target, you need to specify the runtime environment for your job. The job creation UI supports three types of environment:

* Curated environments
* Custom environments
* Container registry image 

### Curated environments

Curated environments are Azure-defined collections of Python packages used in common ML workloads. Curated environments are available in your workspace by default. These environments are backed by cached Docker images, which reduce the job preparation overhead. The cards displayed in the "Curated environments" page show details of each environment. To learn more, see [curated environments in Azure Machine Learning](resource-curated-environments.md).
