
For more, see [Install the Azure CLI for Linux](/cli/azure/install-azure-cli-linux).

## Set up

Login:

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

If you have access to multiple Azure subscriptions, you can set your active subscription:

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

Optionally, setup common variables in your shell for usage in subsequent commands:

```azurecli
echo "Setting variables..."

# <set_variables>

GROUP="azureml-examples"

LOCATION="eastus"

WORKSPACE="main"

# </set_variables>



# additional variables

SUBSCRIPTION=$(az account show --query id -o tsv)

SECRET_NAME="AZ_CREDS"



echo "Installing Azure CLI extension for Azure Machine Learning..."

# <az_ml_install>

az extension add -n ml -y

# </az_ml_install>



echo "Creating resource group..."

# <az_group_create>

az group create -n $GROUP -l $LOCATION

# </az_group_create>



echo "Creating service principal and setting repository secret..."

# <set_repo_secret>

az ad sp create-for-rbac --name $GROUP --role owner --scopes /subscriptions/$SUBSCRIPTION/resourceGroups/$GROUP --sdk-auth | gh secret set $SECRET_NAME

# </set_repo_secret>



echo "Creating Azure Machine Learning workspace..."

# <az_ml_workspace_create>

az ml workspace create -n $WORKSPACE -g $GROUP -l $LOCATION

# </az_ml_workspace_create>



echo "Configuring Azure CLI defaults..."

# <az_configure_defaults>

az configure --defaults group=$GROUP workspace=$WORKSPACE location=$LOCATION

# </az_configure_defaults>



echo "Setting up workspace..."

bash -x setup-workspace.sh

echo "Setting up managed vnet workspace"
# Managed online endpoint vnet setup: Create via bicep: vnet, workspace, storage, acr, kv, nsg, PEs + UAI
# <managed_vnet_workspace_suffix>
# SUFFIX will be used as resource name suffix in created workspace and related resources
export SUFFIX="<UNIQUE_SUFFIX>"
# </managed_vnet_workspace_suffix>
export SUFFIX="mevnet"
# <managed_vnet_workspace_create>
az deployment group create --template-file endpoints/online/managed/vnet/setup_ws/main.bicep --parameters suffix=$SUFFIX
# Note: if you get an error that appinsights is not available in your current location, use optional parameter to the above script: appinsightsLocation=<location> (e.g. westus2)
# </managed_vnet_workspace_create>

# create the user assigned identity used in the vnet egress testing
az deployment group create --template-file endpoints/online/managed/vnet/setup_ws/uai.bicep --parameters suffix=$SUFFIX

echo "Setting up internal workspaces..."

bash -x create-workspace-internal.sh



echo "Setting up extra workspaces..."

bash -x create-workspace-extras.sh


```
