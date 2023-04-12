
Machine learning subcommands require the `--workspace/-w` and `--resource-group/-g` parameters. To avoid typing these repeatedly, configure defaults:

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

> [!TIP]
> Most code examples assume you have set a default workspace and resource group. You can override these on the command line.

You can show your current defaults using `--list-defaults/-l`:

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

> [!TIP]
> Combining with `--output/-o` allows for more readable output formats.

## Secure communications

The `ml` CLI extension (sometimes called 'CLI v2') for Azure Machine Learning sends operational data (YAML parameters and metadata) over the public internet. All the `ml` CLI extension commands communicate with the Azure Resource Manager. This communication is secured using HTTPS/TLS 1.2.

Data in a data store that is secured in a virtual network is _not_ sent over the public internet. For example, if your training data is located in the default storage account for the workspace, and the storage account is in a virtual network.

> [!NOTE]
> With the previous extension (`azure-cli-ml`, sometimes called 'CLI v1'), only some of the commands communicate with the Azure Resource Manager. Specifically, commands that create, update, delete, list, or show Azure resources. Operations such as submitting a training job communicate directly with the Azure Machine Learning workspace. If your workspace is [secured with a private endpoint](how-to-configure-private-link.md), that is enough to secure commands provided by the `azure-cli-ml` extension.
