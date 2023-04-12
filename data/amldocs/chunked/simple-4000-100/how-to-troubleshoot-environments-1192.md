* A container registry behind a virtual network is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)
* The image you're trying to reference doesn't exist in the container registry you specified 
* You haven't provided credentials for a private registry you're trying to pull the image from, or the provided credentials are incorrect

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

If you suspect that the path name to your container registry is incorrect
* For a registry `my-registry.io` and image `test/image` with tag `3.2`, a valid image path would be `my-registry.io/test/image:3.2`
* See [registry path documentation](https://aka.ms/azureml/environment/docker-registries)

If your container registry is behind a virtual network or is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)
* Configure the container registry by using the service endpoint (public access) from the portal and retry
* After you put the container registry behind a virtual network, run the [Azure Resource Manager template](https://aka.ms/azureml/environment/secure-resources-using-vnet) so the workspace can communicate with the container registry instance

If the image you're trying to reference doesn't exist in the container registry you specified
* Check that the correct tag is used and that `user_managed_dependencies` is set to `True`. Setting [user_managed_dependencies](https://aka.ms/azureml/environment/environment-python-section) to `True` disables conda and uses the user's installed packages

If you haven't provided credentials for a private registry you're trying to pull from, or the provided credentials are incorrect
* Set [workspace connections](https://aka.ms/azureml/environment/set-connection-v1) for the container registry if needed

### I/O Error
<!--issueDescription-->
This issue can happen when a Docker image pull fails due to a network issue.  

**Potential causes:**
* Network connection issue, which could be temporary
* Firewall is blocking the connection
* ACR is unreachable and there's network isolation. For more details, see [ACR unreachable](#acr-unreachable). 

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**  

Add the host to the firewall rules  
* See [configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md) to learn how to use Azure Firewall for your workspace and resources behind a VNet

Assess your workspace set-up. Are you using a virtual network, or are any of the resources you're trying to access during your image build behind a virtual network?
* Ensure that you've followed the steps in this article on [securing a workspace with virtual networks](https://aka.ms/azureml/environment/acr-private-endpoint)
* Azure Machine Learning requires both inbound and outbound access to the public internet. If there's a problem with your virtual network setup, there might be an issue with accessing certain repositories required during your image build  

If you aren't using a virtual network, or if you've configured it correctly
* Try rebuilding your image. If the timeout was due to a network issue, the problem might be transient, and a rebuild could fix the problem

## *Conda issues during build*
### Bad spec
<!--issueDescription-->
This issue can happen when a package listed in your conda specification is invalid or when a conda command is executed incorrectly.

**Potential causes:**
* The syntax you used in your conda specification is incorrect
* You're executing a conda command incorrectly

**Affected areas (symptoms):**
