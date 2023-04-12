
* Delete

    ```azurecli
    az ml compute delete --name instance --resource-group my-resource-group --workspace-name my-workspace
    ```

# [Studio](#tab/azure-studio)
<a name="schedule"></a>

In your workspace in Azure Machine Learning studio, select **Compute**, then select **compute instance** on the top.

![Manage a compute instance](./media/concept-compute-instance/manage-compute-instance.png)

You can perform the following actions:

* Create a new compute instance
* Refresh the compute instances tab.
* Start, stop, and restart a compute instance.  You do pay for the instance whenever it's running. Stop the compute instance when you aren't using it to reduce cost. Stopping a compute instance deallocates it. Then start it again when you need it. You can also schedule a time for the compute instance to start and stop.
* Delete a compute instance.
* Filter the list of compute instances to show only ones you've created.

For each compute instance in a workspace that you created (or that was created for you), you can:

* Access Jupyter, JupyterLab, RStudio on the compute instance.
* SSH into compute instance. SSH access is disabled by default but can be enabled at compute instance creation time. SSH access is through public/private key mechanism. The tab will give you details for SSH connection such as IP address, username, and port number. In a virtual network deployment, disabling SSH prevents SSH access from public internet, you can still SSH from within virtual network using private IP address of compute instance node and port 22.
* Select the compute name to:
    * View details about a specific compute instance such as IP address, and region.
    * Create or modify the schedule for starting and stopping the compute instance (preview).  Scroll down to the bottom of the page to edit the schedule.


[Azure RBAC](../role-based-access-control/overview.md) allows you to control which users in the workspace can create, delete, start, stop, restart a compute instance. All users in the workspace contributor and owner role can create, delete, start, stop, and restart compute instances across the workspace. However, only the creator of a specific compute instance, or the user assigned if it was created on their behalf, is allowed to access Jupyter, JupyterLab, and RStudio on that compute instance. A compute instance is dedicated to a single user who has root access.  That user has access to Jupyter/JupyterLab/RStudio running on the instance. Compute instance will have single-user sign-in and all actions will use that user’s identity for Azure RBAC and attribution of experiment jobs. SSH access is controlled through public/private key mechanism.

These actions can be controlled by Azure RBAC:
* *Microsoft.MachineLearningServices/workspaces/computes/read*
* *Microsoft.MachineLearningServices/workspaces/computes/write*
* *Microsoft.MachineLearningServices/workspaces/computes/delete*
* *Microsoft.MachineLearningServices/workspaces/computes/start/action*
* *Microsoft.MachineLearningServices/workspaces/computes/stop/action*
* *Microsoft.MachineLearningServices/workspaces/computes/restart/action*
* *Microsoft.MachineLearningServices/workspaces/computes/updateSchedules/action*

To create a compute instance, you'll need permissions for the following actions:
* *Microsoft.MachineLearningServices/workspaces/computes/write*
* *Microsoft.MachineLearningServices/workspaces/checkComputeNameAvailability/action*

### Audit and observe compute instance version (preview)

Once a compute instance is deployed, it does not get automatically updated. Microsoft [releases](azure-machine-learning-ci-image-release-notes.md) new VM images on a monthly basis. To understand options for keeping recent with the latest version, see [vulnerability management](concept-vulnerability-management.md#compute-instance). 

To keep track of whether an instance's operating system version is current, you could query its version using the Studio UI. In your workspace in Azure Machine Learning studio, select Compute, then select compute instance on the top. Select a compute instance's compute name to see its properties including the current operating system. Enable 'audit and observe compute instance os version' under the previews management panel to see these preview properties.
