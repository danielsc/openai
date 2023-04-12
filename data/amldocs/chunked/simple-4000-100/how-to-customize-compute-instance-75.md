1. Sign into [studio](https://ml.azure.com/) and select your workspace.
1. On the left, select **Compute**.
1. Select **+New** to create a new compute instance.
1. [Fill out the form](how-to-create-manage-compute-instance.md?tabs=azure-studio#create).
1. On the second page of the form, open **Show advanced settings**.
1. Turn on **Provision with setup script**.
1. Select either **Creation script** or **Startup script** tab.
1. Browse to the shell script you saved.  Or upload a script from your computer.
1. Add command arguments as needed.

:::image type="content" source="media/how-to-create-manage-compute-instance/setup-script.png" alt-text="Provision a compute instance with a setup script in the studio.":::

> [!TIP]
> If workspace storage is attached to a virtual network you might not be able to access the setup script file unless you are accessing the studio from within virtual network.

## Use the script in a Resource Manager template

In a Resource Manager [template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-compute-create-computeinstance), add `setupScripts` to invoke the setup script when the compute instance is provisioned. For example:

```json
"setupScripts":{
    "scripts":{
        "creationScript":{
        "scriptSource":"workspaceStorage",
        "scriptData":"[parameters('creationScript.location')]",
        "scriptArguments":"[parameters('creationScript.cmdArguments')]"
        }
    }
}
```

`scriptData` above specifies the location of the creation script in the notebooks file share such as `Users/admin/testscript.sh`.
`scriptArguments` is optional above and specifies the arguments for the creation script.

You could instead provide the script inline for a Resource Manager template.  The shell command can refer to any dependencies uploaded into the notebooks file share.  When you use an inline string, the working directory for the script is `/mnt/batch/tasks/shared/LS_root/mounts/clusters/**ciname**/code/Users`.

For example, specify a base64 encoded command string for `scriptData`:

```json
"setupScripts":{
    "scripts":{
        "creationScript":{
        "scriptSource":"inline",
        "scriptData":"[base64(parameters('inlineCommand'))]",
        "scriptArguments":"[parameters('creationScript.cmdArguments')]"
        }
    }
}
```

## Setup script logs

Logs from the setup script execution appear in the logs folder in the compute instance details page. Logs are stored back to your notebooks file share under the `Logs\<compute instance name>` folder. Script file and command arguments for a particular compute instance are shown in the details page.

## Next steps

* [Access the compute instance terminal](how-to-access-terminal.md)
* [Create and manage files](how-to-manage-files.md)
* [Update the compute instance to the latest VM image](concept-vulnerability-management.md#compute-instance)
