 
# Azure Machine Learning glossary

The Azure Machine Learning glossary is a short dictionary of terminology for the Azure Machine Learning platform. For the general Azure terminology, see also:

* [Microsoft Azure glossary: A dictionary of cloud terminology on the Azure platform](../azure-glossary-cloud-terminology.md)
* [Cloud computing terms](https://azure.microsoft.com/overview/cloud-computing-dictionary/) - General industry cloud terms.
* [Azure fundamental concepts](/azure/cloud-adoption-framework/ready/considerations/fundamental-concepts) - Microsoft Cloud Adoption Framework for Azure.

## Component

An Azure Machine Learning [component](concept-component.md) is a self-contained piece of code that does one step in a machine learning pipeline. Components are the building blocks of advanced machine learning pipelines. Components can do tasks such as data processing, model training, model scoring, and so on. A component is analogous to a function - it has a name, parameters, expects input, and returns output. 


## Compute

A compute is a designated compute resource where you run your job or host your endpoint. Azure Machine learning supports the following types of compute:

* **Compute cluster** - a managed-compute infrastructure that allows you to easily create a cluster of CPU or GPU compute nodes in the cloud.
* **Compute instance** - a fully configured and managed development environment in the cloud. You can use the instance as a training or inference compute for development and testing. It's similar to a virtual machine on the cloud.
* **Kubernetes cluster** - used to deploy trained machine learning models to Azure Kubernetes Service. You can create an Azure Kubernetes Service (AKS) cluster from your Azure ML workspace, or attach an existing AKS cluster.
* **Attached compute** - You can attach your own compute resources to your workspace and use them for training and inference.

## Data

Azure Machine Learning allows you to work with different types of data:

* URIs (a location in local/cloud storage)
  * `uri_folder`
  * `uri_file`
* Tables (a tabular data abstraction)
  * `mltable`
* Primitives
  * `string`
  * `boolean`
  * `number`

For most scenarios, you'll use URIs (`uri_folder` and `uri_file`) - a location in storage that can be easily mapped to the filesystem of a compute node in a job by either mounting or downloading the storage to the node.

`mltable` is an abstraction for tabular data that is to be used for AutoML Jobs, Parallel Jobs, and some advanced scenarios. If you're just starting to use Azure Machine Learning and aren't using AutoML, we strongly encourage you to begin with URIs.


## Datastore

Azure Machine Learning datastores securely keep the connection information to your data storage on Azure, so you don't have to code it in your scripts. You can register and create a datastore to easily connect to your storage account, and access the data in your underlying storage service. The CLI v2 and SDK v2 support the following types of cloud-based storage services:

* Azure Blob Container
* Azure File Share
* Azure Data Lake
* Azure Data Lake Gen2

## Environment

Azure Machine Learning environments are an encapsulation of the environment where your machine learning task happens. They specify the software packages, environment variables, and software settings around your training and scoring scripts. The environments are managed and versioned entities within your Machine Learning workspace. Environments enable reproducible, auditable, and portable machine learning workflows across various computes.

### Types of environment

Azure ML supports two types of environments: curated and custom.

Curated environments are provided by Azure Machine Learning and are available in your workspace by default. Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks. These pre-created environments also allow for faster deployment time. For a full list, see the [curated environments article](resource-curated-environments.md).
