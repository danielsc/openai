When you first submit a remote job using an environment, the Azure Machine Learning service invokes an [ACR Build Task](../container-registry/container-registry-tasks-overview.md) on the Azure Container Registry (ACR) associated with the Workspace. The built Docker image is then cached on the Workspace ACR. Curated environments are backed by Docker images that are cached in Global ACR. At the start of the job execution, the image is retrieved by the compute target from the relevant ACR.

For local jobs, a Docker or conda environment is created based on the environment definition. The scripts are then executed on the target compute - a local runtime environment or local Docker engine.

### Building environments as Docker images

If the image for a particular environment definition doesn't already exist in the workspace ACR, a new image will be built. The image build consists of two steps:

 1. Downloading a base image, and executing any Docker steps
 2. Building a conda environment according to conda dependencies specified in the environment definition.

The second step is optional, and the environment may instead come from the Docker build context or base image. In this case you're responsible for installing any Python packages, by including them in your base image, or specifying custom Docker steps. You're also responsible for specifying the correct location for the Python executable. It is also possible to use a [custom Docker base image](./how-to-deploy-custom-container.md).

### Image caching and reuse

If you use the same environment definition for another job, Azure Machine Learning reuses the cached image from the Workspace ACR to save time.

To view the details of a cached image, check the Environments page in Azure Machine Learning studio or use [`MLClient.environments`](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-environments) to get and inspect the environment.

To determine whether to reuse a cached image or build a new one, AzureML computes a [hash value](https://en.wikipedia.org/wiki/Hash_table) from the environment definition and compares it to the hashes of existing environments. The hash is based on the environment definition's:
 
 * Base image
 * Custom docker steps
 * Python packages
 * Spark packages

The hash isn't affected by the environment name or version. If you rename your environment or create a new one with the same settings and packages as another environment, then the hash value will remain the same. However, environment definition changes like adding or removing a Python package or changing a package version will result cause the resulting hash value to change. Changing the order of dependencies or channels in an environment will also change the hash and require a new image build. Similarly, any change to a curated environment will result in the creation of a new "non-curated" environment. 

> [!NOTE]
> You will not be able to submit any local changes to a curated environment without changing the name of the environment. The prefixes "AzureML-" and "Microsoft" are reserved exclusively for curated environments, and your job submission will fail if the name starts with either of them.

The environment's computed hash value is compared with those in the Workspace and global ACR, or on the compute target (local jobs only). If there is a match then the cached image is pulled and used, otherwise an image build is triggered.

The following diagram shows three environment definitions. Two of them have different names and versions but identical base images and Python packages, which results in the same hash and corresponding cached image. The third environment has different Python packages and versions, leading to a different hash and cached image.

![Diagram of environment caching and Docker images](./media/concept-environments/environment-caching.png)

Actual cached images in your workspace ACR will have names like `azureml/azureml_e9607b2514b066c851012848913ba19f` with the hash appearing at the end.
