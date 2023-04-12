Reproducibility is one of the foundations of software development. While developing production code, a repeated operation must guarantee the same
result. Mitigating vulnerabilities can disrupt reproducibility by changing dependencies.

AzureML's primary focus is to guarantee reproducibility. Environments can broadly be divided into three categories: curated,
user-managed, and system-managed.

**Curated environments** are pre-created environments that are managed by Azure Machine Learning (AzureML) and are available by default in every AzureML workspace provisioned.

Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks.
These pre-created environments also allow for faster deployment time.

In **user-managed environments**, you're responsible for setting up your environment and installing every package that your training script needs on the
compute target and for model deployment. These types of environments are represented by two subtypes:

- BYOC (bring your own container): the user provides a Docker image to AzureML
- Docker build context: AzureML materializes the image from the user provided content

Once you install more dependencies on top of a Microsoft-provided image, or bring your own base image, vulnerability
management becomes your responsibility.

You use **system-managed environments** when you want conda to manage the Python environment for you. A new isolated conda environment is materialized
from your conda specification on top of a base Docker image. While Azure Machine Learning patches base images with each release, whether you use the
latest image may be a tradeoff between reproducibility and vulnerability management. So, it's your responsibility to choose the environment version used
for your jobs or model deployments while using system-managed environments.

Associated to your Azure Machine Learning workspace is an Azure Container Registry instance that's used as a cache for container images. Any image
materialized is pushed to the container registry and used if experimentation or deployment is triggered for the corresponding environment. Azure
Machine Learning doesn't delete images from your container registry, and it's your responsibility to evaluate which images you need to maintain over time. You
can monitor and maintain environment hygiene with [Microsoft Defender for Container Registry](../defender-for-cloud/defender-for-containers-vulnerability-assessment-azure.md)
to help scan images for vulnerabilities. To
automate this process based on triggers from Microsoft Defender, see [Automate responses to Microsoft Defender for Cloud triggers](../defender-for-cloud/workflow-automation.md).

## **Environment definition problems**

## *Environment name issues*
### Curated prefix not allowed
<!--issueDescription-->
This issue can happen when the name of your custom environment uses terms reserved only for curated environments. *Curated* environments are environments that Microsoft maintains. *Custom* environments are environments that you create and maintain.
 
**Potential causes:**
* Your environment name starts with *Microsoft* or *AzureML*
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

 Update your environment name to exclude the reserved prefix you're currently using
 
**Resources**
* [Create and manage reusable environments](https://aka.ms/azureml/environment/create-and-manage-reusable-environments)

### Environment name is too long
<!--issueDescription-->
 
**Potential causes:**
* Your environment name is longer than 255 characters
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

 Update your environment name to be 255 characters or less

## *Docker issues*

*Applies to: Azure CLI & Python SDK v1*

To create a new environment, you must use one of the following approaches (see [DockerSection](https://aka.ms/azureml/environment/environment-docker-section)):
