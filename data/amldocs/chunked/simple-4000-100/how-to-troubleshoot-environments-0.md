
# Troubleshooting environment image builds using troubleshooting log error messages

In this article, learn how to troubleshoot common problems you may encounter with environment image builds.

## Azure Machine Learning environments

Azure Machine Learning environments are an encapsulation of the environment where your machine learning training happens.
They specify the base docker image, Python packages, and software settings around your training and scoring scripts.
Environments are managed and versioned assets within your Machine Learning workspace that enable reproducible, auditable, and portable machine learning workflows across various compute targets.

### Types of environments

Environments can broadly be divided into three categories: curated, user-managed, and system-managed.

Curated environments are pre-created environments that are managed by Azure Machine Learning (AzureML) and are available by default in every workspace.

Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks.
These pre-created environments also allow for faster deployment time.

In user-managed environments, you're responsible for setting up your environment and installing every package that your training script needs on the compute target.
Also be sure to include any dependencies needed for model deployment.
These types of environments are represented by two subtypes. For the first type, BYOC (bring your own container), you bring an existing Docker image to AzureML. For the second type, Docker build context based environments, AzureML materializes the image from the context that you provide.

System-managed environments are used when you want conda to manage the Python environment for you.
A new isolated conda environment is materialized from your conda specification on top of a base Docker image. By default, common properties are added to the derived image.
Note that environment isolation implies that Python dependencies installed in the base image won't be available in the derived image.

### Create and manage environments

You can create and manage environments from clients like AzureML Python SDK, AzureML CLI, AzureML Studio UI, VS code extension. 

"Anonymous" environments are automatically registered in your workspace when you submit an experiment without registering or referencing an already existing environment.
They won't be listed but may be retrieved by version or label.

AzureML builds environment definitions into Docker images.
It also caches the environments in the Azure Container Registry associated with your AzureML Workspace so they can be reused in subsequent training jobs and service endpoint deployments.
Multiple environments with the same definition may result the same image, so the cached image will be reused.
Running a training script remotely requires the creation of a Docker image.

### Reproducibility and vulnerabilities

#### *Vulnerabilities*

Vulnerabilities can be addressed by upgrading to a newer version of a dependency or migrating to a different dependency that satisfies security
requirements. Mitigating vulnerabilities is time consuming and costly since it can require refactoring of code and infrastructure. With the prevalence
of open source software and the use of complicated nested dependencies, it's important to manage and keep track of vulnerabilities.

There are some ways to decrease the impact of vulnerabilities:

- Reduce your number of dependencies - use the minimal set of the dependencies for each scenario.
- Compartmentalize your environment so issues can be scoped and fixed in one place.
- Understand flagged vulnerabilities and their relevance to your scenario.

#### *Vulnerabilities vs Reproducibility*

Reproducibility is one of the foundations of software development. While developing production code, a repeated operation must guarantee the same
result. Mitigating vulnerabilities can disrupt reproducibility by changing dependencies.
