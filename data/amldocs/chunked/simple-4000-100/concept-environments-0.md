
# What are Azure Machine Learning environments?

Azure Machine Learning environments are an encapsulation of the environment where your machine learning training happens. They specify the Python packages, environment variables, and software settings around your training and scoring scripts. They also specify runtimes (Python, Spark, or Docker). The environments are managed and versioned entities within your Machine Learning workspace that enable reproducible, auditable, and portable machine learning workflows across a variety of compute targets.

You can use an `Environment` object on your local compute to:
* Develop your training script.
* Reuse the same environment on Azure Machine Learning Compute for model training at scale.
* Deploy your model with that same environment.
* Revisit the environment in which an existing model was trained.

The following diagram illustrates how you can use a single `Environment` object in both your job configuration (for training) and your inference and deployment configuration (for web service deployments).

![Diagram of an environment in machine learning workflow](./media/concept-environments/ml-environment.png)

The environment, compute target and training script together form the job configuration: the full specification of a training job.

## Types of environments

Environments can broadly be divided into three categories: *curated*, *user-managed*, and *system-managed*.

Curated environments are provided by Azure Machine Learning and are available in your workspace by default. Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks. These pre-created environments also allow for faster deployment time. For a full list, see the [curated environments article](resource-curated-environments.md).

In user-managed environments, you're responsible for setting up your environment and installing every package that your training script needs on the compute target. Also be sure to include any dependencies needed for model deployment.

You use system-managed environments when you want [conda](https://conda.io/docs/) to manage the Python environment for you. A new conda environment is materialized from your conda specification on top of a base docker image.

## Create and manage environments

You can create environments from clients like the AzureML Python SDK, Azure Machine Learning CLI, Environments page in Azure Machine Learning studio, and [VS Code extension](how-to-manage-resources-vscode.md#create-environment). Every client allows you to customize the base image, Dockerfile, and Python layer if needed.

For specific code samples, see the "Create an environment" section of [How to use environments](how-to-manage-environments-v2.md#create-an-environment). 

Environments are also easily managed through your workspace, which allows you to:

* Register environments.
* Fetch environments from your workspace to use for training or deployment.
* Create a new instance of an environment by editing an existing one.
* View changes to your environments over time, which ensures reproducibility.
* Build Docker images automatically from your environments.

"Anonymous" environments are automatically registered in your workspace when you submit an experiment. They will not be listed but may be retrieved by version.

For code samples, see the "Manage environments" section of [How to use environments](how-to-manage-environments-v2.md#manage-environments).

## Environment building, caching, and reuse

Azure Machine Learning builds environment definitions into Docker images and conda environments. It also caches the environments so they can be reused in subsequent training jobs and service endpoint deployments. Running a training script remotely requires the creation of a Docker image, but a local job can use a conda environment directly. 

### Submitting a job using an environment

When you first submit a remote job using an environment, the Azure Machine Learning service invokes an [ACR Build Task](../container-registry/container-registry-tasks-overview.md) on the Azure Container Registry (ACR) associated with the Workspace. The built Docker image is then cached on the Workspace ACR. Curated environments are backed by Docker images that are cached in Global ACR. At the start of the job execution, the image is retrieved by the compute target from the relevant ACR.
