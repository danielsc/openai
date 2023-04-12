

1. To sign in to the Azure CLI in the VM environment, use the following command:

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

1. To configure the defaults for the CLI, use the following commands:

```azurecli
### Part of automated testing: only required when this script is called via vm run-command invoke inorder to gather the parameters ###
set -e
for args in "$@"
do
    keyname=$(echo $args | cut -d ':' -f 1)
    result=$(echo $args | cut -d ':' -f 2)
    export $keyname=$result
done

# $USER is no set when used from az vm run-command
export USER=$(whoami)

# <setup_docker_az_cli> 
# setup docker
sudo apt-get update -y && sudo apt install docker.io -y && sudo snap install docker && docker --version && sudo usermod -aG docker $USER
# setup az cli and ml extension
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash && az extension add --upgrade -n ml -y
# </setup_docker_az_cli> 

# login using az cli. 
### NOTE to user: use `az login` - and do NOT use the below command (it requires setting up of user assigned identity). ###
az login --identity -u /subscriptions/$SUBSCRIPTION/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/$IDENTITY_NAME

# <configure_defaults> 
# configure cli defaults
az account set --subscription $SUBSCRIPTION
az configure --defaults group=$RESOURCE_GROUP workspace=$WORKSPACE location=$LOCATION
# </configure_defaults> 

# Clone the samples repo. This is needed to build the image and create the managed online deployment.
# Note: We will hardcode the below line in the docs (without GIT_BRANCH) so we don't need to explain the logic to the user.
sudo mkdir -p /home/samples; sudo git clone -b $GIT_BRANCH --depth 1 https://github.com/Azure/azureml-examples.git /home/samples/azureml-examples -q

```

1. To clone the example files for the deployment, use the following command:

    ```azurecli
    sudo mkdir -p /home/samples; sudo git clone -b main --depth 1 https://github.com/Azure/azureml-examples.git /home/samples/azureml-examples
    ```

1. To build a custom docker image to use with the deployment, use the following commands:

```azurecli
set -e
### Part of automated testing: only required when this script is called via vm run-command invoke inorder to gather the parameters ###
for args in "$@"
do
    keyname=$(echo $args | cut -d ':' -f 1)
    result=$(echo $args | cut -d ':' -f 2)
    export $keyname=$result
done

# login using the user assigned identity. 
az login --identity -u /subscriptions/$SUBSCRIPTION/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/$IDENTITY_NAME
az account set --subscription $SUBSCRIPTION
az configure --defaults group=$RESOURCE_GROUP workspace=$WORKSPACE location=$LOCATION

# <build_image> 
# Navigate to the samples
cd /home/samples/azureml-examples/cli/$ENV_DIR_PATH
# login to acr. Optionally, to avoid using sudo, complete the docker post install steps: https://docs.docker.com/engine/install/linux-postinstall/
sudo az acr login -n "$ACR_NAME"
# Build the docker image with the sample docker file
sudo docker build -t "$ACR_NAME.azurecr.io/repo/$IMAGE_NAME":v1 .
# push the image to the ACR
sudo docker push "$ACR_NAME.azurecr.io/repo/$IMAGE_NAME":v1
# check if the image exists in acr
az acr repository show -n "$ACR_NAME" --repository "repo/$IMAGE_NAME"
# </build_image> 
```
