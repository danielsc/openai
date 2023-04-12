
*Applies to: all scenarios*

If you're using a YAML for your conda specification, specify a version for pip

```yaml
name: project_environment
dependencies:
  - python=3.8
  - pip=22.3.1
  - pip:
      - numpy=1.24.1
channels:
  - anaconda
  - conda-forge
```

**Resources**
* See [conda package pinning](https://aka.ms/azureml/environment/how-to-pin-conda-packages)

## *Miscellaneous environment issues*
### R section is deprecated
<!--issueDescription-->
**Potential causes:**
* You specified an R section in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

The AzureML SDK for R was deprecated at the end of 2021 to make way for an improved R training and deployment experience using the Azure CLI v2

*Applies to: Python SDK v1*

Remove the R section from your environment definition

```python
env.r = None
```

*Applies to: all scenarios*

See the [samples repository](https://aka.ms/azureml/environment/train-r-models-cli-v2) to get started training R models using the Azure CLI v2

### No definition exists for environment
<!--issueDescription-->
**Potential causes:**
* You specified an environment that doesn't exist or hasn't been registered
* There was a misspelling or syntactical error in the way you specified your environment name or environment version

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Ensure that you are specifying your environment name correctly, along with the correct version
* `path-to-resource:version-number`

The 'latest' version of your environment is specified in a slightly different way
* `path-to-resource@latest`

## **Image build problems**

## *ACR issues*
### ACR unreachable
<!--issueDescription-->
This issue can happen by failing to access a workspace's associated Azure Container Registry (ACR) resource.

**Potential causes:**
* Workspace's ACR is behind a virtual network (VNet) (private endpoint or service endpoint), and no compute cluster is used to build images.
* Workspace's ACR is behind a virtual network (private endpoint or service endpoint), and the compute cluster used for building images have no access to the workspace's ACR.

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
* Pipeline job failures.
* Model deployment failures.
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Update the workspace image build compute property using SDK:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
ws.update(image_build_compute = 'mycomputecluster')
```

*Applies to: Azure CLI extensions v1 & v2*

Update the workspace image build compute property using Azure CLI:

```
az ml workspace update --name myworkspace --resource-group myresourcegroup --image-build-compute mycomputecluster
```

> [!NOTE]
> * Only Azure Machine Learning compute clusters are supported. Compute, Azure Kubernetes Service (AKS), or other instance types are not supported for image build compute.
> * Make sure the compute cluster's VNet that's used for the image build compute has access to the workspace's ACR.
> * Make sure the compute cluster is CPU based.

**Resources**
* [Enable Azure Container Registry (ACR)](https://aka.ms/azureml/environment/acr-private-endpoint)
* [How To Use Environments](https://aka.ms/azureml/environment/how-to-use-environments)

## *Docker pull issues*
### Failed to pull Docker image
<!--issueDescription-->
This issue can happen when a Docker image pull fails during an image build.

**Potential causes:**
* The path name to the container registry is incorrect
* A container registry behind a virtual network is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)
* The image you're trying to reference doesn't exist in the container registry you specified 
