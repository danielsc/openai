### Create the virtual machine jump box

To create an Azure Virtual Machine that can be used to connect to the VNet, use the following command. Replace `<your-new-password>` with the password you want to use when connecting to this VM:

```azurecli
# create vm
az vm create --name test-vm --vnet-name vnet-$SUFFIX --subnet snet-scoring --image UbuntuLTS --admin-username azureuser --admin-password <your-new-password> --resource-group <my-resource-group>
```

> [!IMPORTANT]
> The VM created by these commands has a public endpoint that you can connect to over the public network.

The response from this command is similar to the following JSON document:

```json
{
  "fqdns": "",
  "id": "/subscriptions/<GUID>/resourceGroups/<my-resource-group>/providers/Microsoft.Compute/virtualMachines/test-vm",
  "location": "westus",
  "macAddress": "00-0D-3A-ED-D8-E8",
  "powerState": "VM running",
  "privateIpAddress": "192.168.0.12",
  "publicIpAddress": "20.114.122.77",
  "resourceGroup": "<my-resource-group>",
  "zones": ""
}
```

Use the following command to connect to the VM using SSH. Replace `publicIpAddress` with the value of the public IP address in the response from the previous command:

```azurecli
ssh azureusere@publicIpAddress
```

When prompted, enter the password you used when creating the VM.

### Configure the VM

1. Use the following commands from the SSH session to install the CLI and Docker:

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

1. To create the environment variables used by this example, run the following commands. Replace `<YOUR_SUBSCRIPTION_ID>` with your Azure subscription ID. Replace `<YOUR_RESOURCE_GROUP>` with the resource group that contains your workspace. Replace `<SUFFIX_USED_IN_SETUP>` with the suffix you provided earlier. Replace `<LOCATION>` with the location of your Azure workspace. Replace `<YOUR_ENDPOINT_NAME>` with the name to use for the endpoint.

    > [!TIP]
    > Use the tabs to select whether you want to perform a deployment using an MLflow model or generic ML model.

    # [Generic model](#tab/model)

```azurecli
#!/bin/bash

set -e

# This is the instructions for docs.User has to execute this from a test VM - that is why user cannot use defaults from their local setup


# <set_env_vars> 
export SUBSCRIPTION="<YOUR_SUBSCRIPTION_ID>"
export RESOURCE_GROUP="<YOUR_RESOURCE_GROUP>"
export LOCATION="<LOCATION>"

# SUFFIX that was used when creating the workspace resources. Alternatively the resource names can be looked up from the resource group after the vnet setup script has completed.
export SUFFIX="<SUFFIX_USED_IN_SETUP>"

# SUFFIX used during the initial setup. Alternatively the resource names can be looked up from the resource group after the  setup script has completed.
export WORKSPACE=mlw-$SUFFIX
export ACR_NAME=cr$SUFFIX

# provide a unique name for the endpoint
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"

# name of the image that will be built for this sample and pushed into acr - no need to change this
export IMAGE_NAME="img"

# Yaml files that will be used to create endpoint and deployment. These are relative to azureml-examples/cli/ directory. Do not change these
export ENDPOINT_FILE_PATH="endpoints/online/managed/vnet/sample/endpoint.yml"
export DEPLOYMENT_FILE_PATH="endpoints/online/managed/vnet/sample/blue-deployment-vnet.yml"
export SAMPLE_REQUEST_PATH="endpoints/online/managed/vnet/sample/sample-request.json"
export ENV_DIR_PATH="endpoints/online/managed/vnet/sample/environment"
# </set_env_vars>

export SUFFIX="mevnet" # used during setup of secure vnet workspace: setup/setup-repo/azure-github.sh
export SUBSCRIPTION=$(az account show --query "id" -o tsv)
export RESOURCE_GROUP=$(az configure -l --query "[?name=='group'].value" -o tsv)
export LOCATION=$(az configure -l --query "[?name=='location'].value" -o tsv)
# remove all whitespace from location
export LOCATION="$(echo -e "${LOCATION}" | tr -d '[:space:]')"
export IDENTITY_NAME=uai$SUFFIX
# export ACR_NAME=cr$SUFFIX
export WORKSPACE=mlw-$SUFFIX
export ENDPOINT_NAME=$ENDPOINT_NAME
# VM name used during creation: endpoints/online/managed/vnet/setup_vm/vm-main.bicep
export VM_NAME="moevnet-vm"
# VNET name and subnet name used during vnet worskapce setup: endpoints/online/managed/vnet/setup_ws/main.bicep
export VNET_NAME=vnet-$SUFFIX
export SUBNET_NAME="snet-scoring"
export ENDPOINT_NAME=endpt-vnet-`echo $RANDOM`

# Get the current branch name of the azureml-examples. Useful in PR scenario. Since the sample code is cloned and executed from a VM, we need to pass the branch name when running az vm run-command
# If running from local machine, change it to your branch name
export GIT_BRANCH=$GITHUB_HEAD_REF
# need to set branch name manually if executed from main
if [ "$GIT_BRANCH" == "" ];
then
   GIT_BRANCH="main"
fi

# We use a different workspace for managed vnet endpoints
az configure --defaults workspace=$WORKSPACE

export ACR_NAME=$(az ml workspace show -n $WORKSPACE --query container_registry -o tsv | cut -d'/' -f9-)
if [[ -z "$ACRNAME" ]]
then
    export ACR_NAME=$(az acr list --query '[].{Name:name}' --output tsv)
fi

### setup VM & deploy/test ###
# if vm exists, wait for 15 mins before trying to delete
export VM_EXISTS=$(az vm list -o tsv --query "[?name=='$VM_NAME'].name")
if [ "$VM_EXISTS" != "" ];
then
   echo "VM already exists from previous run. Waiting for 15 mins before deleting."
   sleep 15m
   az vm delete -n $VM_NAME -y
fi

# Create the VM. In the docs we will provide instructions to create a VM using az vm create -n $VM_NAME
az deployment group create --name $VM_NAME-$ENDPOINT_NAME --template-file endpoints/online/managed/vnet/setup_vm/vm-main.bicep --parameters vmName=$VM_NAME identityName=$IDENTITY_NAME vnetName=$VNET_NAME subnetName=$SUBNET_NAME

az vm run-command invoke -n $VM_NAME --command-id RunShellScript --scripts @endpoints/online/managed/vnet/setup_vm/scripts/vmsetup.sh --parameters "SUBSCRIPTION:$SUBSCRIPTION" "RESOURCE_GROUP:$RESOURCE_GROUP" "LOCATION:$LOCATION" "IDENTITY_NAME:$IDENTITY_NAME" "GIT_BRANCH:$GIT_BRANCH"

# build image
az vm run-command invoke -n $VM_NAME --command-id RunShellScript --scripts @endpoints/online/managed/vnet/setup_vm/scripts/build_image.sh --parameters "SUBSCRIPTION:$SUBSCRIPTION" "RESOURCE_GROUP:$RESOURCE_GROUP" "LOCATION:$LOCATION" "IDENTITY_NAME:$IDENTITY_NAME" "ACR_NAME=$ACR_NAME" "IMAGE_NAME:$IMAGE_NAME" "ENV_DIR_PATH:$ENV_DIR_PATH"

# create endpoint/deployment inside managed vnet
az vm run-command invoke -n $VM_NAME --command-id RunShellScript --scripts @endpoints/online/managed/vnet/setup_vm/scripts/create_moe.sh --parameters "SUBSCRIPTION:$SUBSCRIPTION" "RESOURCE_GROUP:$RESOURCE_GROUP" "LOCATION:$LOCATION" "IDENTITY_NAME:$IDENTITY_NAME" "WORKSPACE:$WORKSPACE" "ENDPOINT_NAME:$ENDPOINT_NAME" "ACR_NAME=$ACR_NAME" "IMAGE_NAME:$IMAGE_NAME" "ENDPOINT_FILE_PATH:$ENDPOINT_FILE_PATH" "DEPLOYMENT_FILE_PATH:$DEPLOYMENT_FILE_PATH" "SAMPLE_REQUEST_PATH:$SAMPLE_REQUEST_PATH"

# test the endpoint by scoring it
export CMD_OUTPUT=$(az vm run-command invoke -n $VM_NAME --command-id RunShellScript --scripts @endpoints/online/managed/vnet/setup_vm/scripts/score_endpoint.sh --parameters "SUBSCRIPTION:$SUBSCRIPTION" "RESOURCE_GROUP:$RESOURCE_GROUP" "LOCATION:$LOCATION" "IDENTITY_NAME:$IDENTITY_NAME" "WORKSPACE:$WORKSPACE" "ENDPOINT_NAME:$ENDPOINT_NAME" "SAMPLE_REQUEST_PATH:$SAMPLE_REQUEST_PATH")

# the scoring output for sample request should be [11055.977245525679, 4503.079536107787]. We are validating if part of the number is available in the output (not comparing all the decimals to accomodate rounding discrepencies)
if [[ $CMD_OUTPUT =~ "11055" ]]; then
   echo "Scoring works!"
else
   echo "Error in scoring"
   # delete the VM before exiting with error
   az vm delete -n $VM_NAME -y --no-wait
   # exit with error
   exit 1
fi


### Cleanup
# <delete_endpoint>
az ml online-endpoint delete --name $ENDPOINT_NAME --yes --no-wait
# </delete_endpoint>
# <delete_vm> 
az vm delete -n $VM_NAME -y --no-wait
# </delete_vm> 
```
