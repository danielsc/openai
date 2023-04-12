    * Provision with a setup script (preview) - for more information about how to create and use a setup script, see [Customize the compute instance with a script](how-to-customize-compute-instance.md).
  
You can also create a compute instance with an [Azure Resource Manager template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-compute-create-computeinstance).

### Enable SSH access

SSH access is disabled by default.  SSH access can't be changed after creation. Make sure to enable access if you plan to debug interactively with [VS Code Remote](how-to-set-up-vs-code-remote.md).  

[!INCLUDE [amlinclude-info](../../includes/machine-learning-enable-ssh.md)]

### Connect with SSH

[!INCLUDE [ssh-access](../../includes/machine-learning-ssh-access.md)]



## Create on behalf of (preview)

> [!IMPORTANT]
> Items marked (preview) below are currently in public preview.
> The preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

As an administrator, you can create a compute instance on behalf of a data scientist and assign the instance to them with:

* Studio, using the [Advanced settings](?tabs=azure-studio#advanced-settings)

* [Azure Resource Manager template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-compute-create-computeinstance).  For details on how to find the TenantID and ObjectID needed in this template, see [Find identity object IDs for authentication configuration](../healthcare-apis/azure-api-for-fhir/find-identity-object-ids.md).  You can also find these values in the Azure Active Directory portal.

* REST API

The data scientist you create the compute instance for needs the following be [Azure role-based access control (Azure RBAC)](../role-based-access-control/overview.md) permissions:

* *Microsoft.MachineLearningServices/workspaces/computes/start/action*
* *Microsoft.MachineLearningServices/workspaces/computes/stop/action*
* *Microsoft.MachineLearningServices/workspaces/computes/restart/action*
* *Microsoft.MachineLearningServices/workspaces/computes/applicationaccess/action*
* *Microsoft.MachineLearningServices/workspaces/computes/updateSchedules/action*

The data scientist can start, stop, and restart the compute instance. They can use the compute instance for:
* Jupyter
* JupyterLab
* RStudio
* Posit Workbench (formerly RStudio Workbench)
* Integrated notebooks

## Enable idle shutdown (preview)

> [!IMPORTANT]
> Items marked (preview) below are currently in public preview.
> The preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

To avoid getting charged for a compute instance that is switched on but inactive, you can configure when to shut down your compute instance due to inactivity.

A compute instance is considered inactive if the below conditions are met:
* No active Jupyter Kernel sessions (which translates to no Notebooks usage via Jupyter, JupyterLab or Interactive notebooks)
* No active Jupyter terminal sessions
* No active AzureML runs or experiments
* No SSH connections
* No VS code connections; you must close your VS Code connection for your compute instance to be considered inactive. Sessions are auto-terminated if VS code detects no activity for 3 hours. 

Activity on custom applications installed on the compute instance isn't considered. There are also some basic bounds around inactivity time periods; compute instance must be inactive for a minimum of 15 mins and a maximum of three days. 
