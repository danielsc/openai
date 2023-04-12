1. Go to Environments page, select Custom environment, and select + Create option to create an environment for your deployment. Use the downloaded conda yaml to create a custom environment

1. Select the model, and from the Deploy drop-down option, select Deploy to real-time endpoint

1. Complete all the steps in wizard to create an online endpoint and deployment

 
# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

## Configure the CLI 

To create a deployment from the CLI, you'll need the Azure CLI with the ML v2 extension. Run the following command to confirm that you've both:

```azurecli
### TESTED

# <az_extension_list>
az extension list 
# </az_extension_list>

# <az_ml_install>
az extension add -n ml
# </az_ml_install>

# <list_defaults>
az configure -l -o table
# </list_defaults>

apt-get install sudo
# <az_extension_install_linux>
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash 
az extension add -n ml -y 
# </az_extension_install_linux>

# <az_ml_update>
az extension update -n ml
# </az_ml_update>

# <az_ml_verify>
az ml -h
# </az_ml_verify>

# <az_extension_remove>
az extension remove -n azure-cli-ml
az extension remove -n ml
# </az_extension_remove>

# <git_clone>
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples/cli
# </git_clone>

# <az_version>
az version
# </az_version>

### UNTESTED
exit

# <az_account_set>
az account set -s "<YOUR_SUBSCRIPTION_NAME_OR_ID>"
# </az_account_set>

# <az_login>
az login
# </az_login>

```

If you receive an error message or you don't see `Extensions: ml` in the response, follow the steps at [Install and set up the CLI (v2)](how-to-configure-cli.md).

Sign in:

```azurecli
### TESTED

# <az_extension_list>
az extension list 
# </az_extension_list>

# <az_ml_install>
az extension add -n ml
# </az_ml_install>

# <list_defaults>
az configure -l -o table
# </list_defaults>

apt-get install sudo
# <az_extension_install_linux>
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash 
az extension add -n ml -y 
# </az_extension_install_linux>

# <az_ml_update>
az extension update -n ml
# </az_ml_update>

# <az_ml_verify>
az ml -h
# </az_ml_verify>

# <az_extension_remove>
az extension remove -n azure-cli-ml
az extension remove -n ml
# </az_extension_remove>

# <git_clone>
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples/cli
# </git_clone>

# <az_version>
az version
# </az_version>

### UNTESTED
exit

# <az_account_set>
az account set -s "<YOUR_SUBSCRIPTION_NAME_OR_ID>"
# </az_account_set>

# <az_login>
az login
# </az_login>

```

If you've access to multiple Azure subscriptions, you can set your active subscription:

```azurecli
### TESTED

# <az_extension_list>
az extension list 
# </az_extension_list>

# <az_ml_install>
az extension add -n ml
# </az_ml_install>

# <list_defaults>
az configure -l -o table
# </list_defaults>

apt-get install sudo
# <az_extension_install_linux>
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash 
az extension add -n ml -y 
# </az_extension_install_linux>

# <az_ml_update>
az extension update -n ml
# </az_ml_update>

# <az_ml_verify>
az ml -h
# </az_ml_verify>

# <az_extension_remove>
az extension remove -n azure-cli-ml
az extension remove -n ml
# </az_extension_remove>

# <git_clone>
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples/cli
# </git_clone>

# <az_version>
az version
# </az_version>

### UNTESTED
exit

# <az_account_set>
az account set -s "<YOUR_SUBSCRIPTION_NAME_OR_ID>"
# </az_account_set>

# <az_login>
az login
# </az_login>

```

Set the default resource group and workspace to where you wish to create the deployment:

```azurecli
#!/bin/bash
# rc install - uncomment and adjust below to run all tests on a CLI release candidate
# az extension remove -n ml

# <az_ml_install>
az extension add -n ml -y
# </az_ml_install>

# Use a daily build
# az extension add --source https://azuremlsdktestpypi.blob.core.windows.net/wheels/sdk-cli-v2-public/ml-2.9.0-py3-none-any.whl --yes
# remove ml extension if it is installed
# if az extension show -n ml &>/dev/null; then
#     echo -n 'Removing ml extension...'
#     if ! az extension remove -n ml -o none --only-show-errors &>/dev/null; then
#         echo 'Error failed to remove ml extension' >&2
#     fi
#     echo -n 'Re-installing ml...'
# fi

# if ! az extension add --yes --source "https://azuremlsdktestpypi.blob.core.windows.net/wheels/sdk-cli-v2-public/ml-2.10.0-py3-none-any.whl" -o none --only-show-errors &>/dev/null; then
#     echo 'Error failed to install ml azure-cli extension' >&2
#     exit 1
# fi

# az version

## For backward compatibility - running on old subscription
# <set_variables>
GROUP="azureml-examples"
LOCATION="eastus"
WORKSPACE="main"
# </set_variables>

# If RESOURCE_GROUP_NAME is empty, the az configure is pending.
RESOURCE_GROUP_NAME=${RESOURCE_GROUP_NAME:-}
if [[ -z "$RESOURCE_GROUP_NAME" ]]
then
    echo "No resource group name [RESOURCE_GROUP_NAME] specified, defaulting to ${GROUP}."
    # Installing extension temporarily assuming the run is on old subscription
    # without bootstrap script.

    # <az_configure_defaults>
    az configure --defaults group=$GROUP workspace=$WORKSPACE location=$LOCATION
    # </az_configure_defaults>
    echo "Default resource group set to $GROUP"
else
    echo "Workflows are using the new subscription."
fi
```
