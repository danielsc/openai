
# Customize the compute instance with a script 

Use a setup script for an automated way to customize and configure a compute instance at provisioning time. 

Use a compute instance as your fully configured and managed development environment in the cloud. For development and testing, you can also use the instance as a [training compute target](concept-compute-target.md#training-compute-targets) or for an [inference target](concept-compute-target.md#compute-targets-for-inference).   A compute instance can run multiple jobs in parallel and has a job queue. As a development environment, a compute instance can't be shared with other users in your workspace.

As an administrator, you can write a customization script to be used to provision all compute instances in the workspace according to your requirements. You can configure your setup script as a Creation script, which will run once when the compute instance is created. Or you can configure it as a Startup script, which will run every time the compute instance is started (including initial creation).

Some examples of what you can do in a setup script:

* Install packages, tools, and software
* Mount data
* Create custom conda environment and Jupyter kernels
* Clone git repositories and set git config
* Set network proxies
* Set environment variables
* Install JupyterLab extensions

## Create the setup script

The setup script is a shell script, which runs as `rootuser`.  Create or upload the script into your **Notebooks** files:

1. Sign into the [studio](https://ml.azure.com) and select your workspace.
2. On the left, select **Notebooks**
3. Use the **Add files** tool to create or upload your setup shell script.  Make sure the script filename ends in ".sh".  When you create a new file, also change the **File type** to *bash(.sh)*.

:::image type="content" source="media/how-to-create-manage-compute-instance/create-or-upload-file.png" alt-text="Create or upload your setup script to Notebooks file in studio":::

When the script runs, the current working directory of the script is the directory where it was uploaded. For example, if you upload the script to **Users>admin**, the location of the script on the compute instance and current working directory when the script runs is */home/azureuser/cloudfiles/code/Users/admin*. This location enables you to use relative paths in the script.

Script arguments can be referred to in the script as $1, $2, etc.

If your script was doing something specific to azureuser such as installing conda environment or Jupyter kernel, you'll have to put it within `sudo -u azureuser` block like this

```bash
#!/bin/bash

set -e

# This script installs a pip package in compute instance azureml_py38 environment.

sudo -u azureuser -i <<'EOF'

PACKAGE=numpy
ENVIRONMENT=azureml_py38 
conda activate "$ENVIRONMENT"
pip install "$PACKAGE"
conda deactivate
EOF

```

The command `sudo -u azureuser` changes the current working directory to `/home/azureuser`. You also can't access the script arguments in this block.

For other example scripts, see [azureml-examples](https://github.com/Azure/azureml-examples/tree/main/setup/setup-ci).

You can also use the following environment variables in your script:

* `CI_RESOURCE_GROUP`
* `CI_WORKSPACE`
* `CI_NAME`
* `CI_LOCAL_UBUNTU_USER` - points to `azureuser`

Use a setup script in conjunction with **Azure Policy to either enforce or default a setup script for every compute instance creation**.
The default value for a setup script timeout is 15 minutes. The time can be changed in studio, or through ARM templates using the `DURATION` parameter.
`DURATION` is a floating point number with an optional suffix: `'s'` for seconds (the default), `'m'` for minutes, `'h'` for hours or `'d'` for days.

## Use the script in studio

Once you store the script, specify it during creation of your compute instance:

1. Sign into [studio](https://ml.azure.com/) and select your workspace.
1. On the left, select **Compute**.
1. Select **+New** to create a new compute instance.
