pip install --ignore-installed [package]
```

Try creating a separate environment using conda

## *Docker push issues*
### Failed to store Docker image
<!--issueDescription-->
This issue can happen when a Docker image fails to be stored (pushed) to a container registry.  

**Potential causes:**
* A transient issue has occurred with the ACR associated with the workspace
* A container registry behind a virtual network is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)

**Affected areas (symptoms):**
* Failure in building environments from the UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**  

Retry the environment build if you suspect this is a transient issue with the workspace's Azure Container Registry (ACR)  

If your container registry is behind a virtual network or is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)
* Configure the container registry by using the service endpoint (public access) from the portal and retry
* After you put the container registry behind a virtual network, run the [Azure Resource Manager template](https://aka.ms/azureml/environment/secure-resources-using-vnet) so the workspace can communicate with the container registry instance

If you aren't using a virtual network, or if you've configured it correctly, test that your credentials are correct for your ACR by attempting a simple local build
* Get credentials for your workspace ACR from the Azure portal
* Log in to your ACR using `docker login <myregistry.azurecr.io> -u "username" -p "password"`
* For an image "helloworld", test pushing to your ACR by running `docker push helloworld`
* See [Quickstart: Build and run a container image using Azure Container Registry Tasks](../container-registry/container-registry-quickstart-task-cli.md)

## *Miscellaneous build issues*
### Build log unavailable
<!--issueDescription-->
**Potential causes:**
* AzureML isn't authorized to store your build logs in your storage account
* A transient error occurred while saving your build logs
* A system error occurred before an image build was triggered

**Affected areas (symptoms):**
* A successful build, but no available logs.
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

A rebuild may fix the issue if it's transient
