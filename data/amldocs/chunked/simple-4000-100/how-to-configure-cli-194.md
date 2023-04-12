
Now, install the `ml` extension:

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

Run the help command to verify your installation and see available subcommands:

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

You can upgrade the extension to the latest version:

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

### Installation on Linux

If you're using Linux, the fastest way to install the necessary CLI version and the Machine Learning extension is:

```bash
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

For more, see [Install the Azure CLI for Linux](/cli/azure/install-azure-cli-linux).
