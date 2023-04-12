
    > [!TIP]
    > In this example, we build the Docker image before pushing it to Azure Container Registry. Alternatively, you can build the image in your vnet by using an Azure Machine Learning compute cluster and environments. For more information, see [Secure Azure Machine Learning workspace](how-to-secure-workspace-vnet.md#enable-azure-container-registry-acr).

### Create a secured managed online endpoint

1. To create a managed online endpoint that is secured using a private endpoint for inbound and outbound communication, use the following commands:

    > [!TIP]
    > You can test or debug the Docker image locally by using the `--local` flag when creating the deployment. For more information, see the [Deploy and debug locally](how-to-deploy-online-endpoints.md#deploy-and-debug-locally-by-using-local-endpoints) article.

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

# <create_local_deployment> 
# navigate to the cli directory in the azurem-examples repo
cd /home/samples/azureml-examples/cli/

# create endpoint
az ml online-endpoint create --local --name $ENDPOINT_NAME -f $ENDPOINT_FILE_PATH --set public_network_access="disabled"
# create deployment in managed vnet
az ml online-deployment create --local --name blue --endpoint $ENDPOINT_NAME -f $DEPLOYMENT_FILE_PATH --all-traffic --set environment.image="$ACR_NAME.azurecr.io/repo/$IMAGE_NAME:v1" egress_public_network_access="disabled"
# check if scoring works
az ml online-endpoint invoke --local --name $ENDPOINT_NAME --request-file $SAMPLE_REQUEST_PATH
# </create_local_deployment> 

# <create_vnet_deployment> 
# navigate to the cli directory in the azurem-examples repo
cd /home/samples/azureml-examples/cli/

# create endpoint
az ml online-endpoint create --name $ENDPOINT_NAME -f $ENDPOINT_FILE_PATH --set public_network_access="disabled"
# create deployment in managed vnet
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f $DEPLOYMENT_FILE_PATH --all-traffic --set environment.image="$ACR_NAME.azurecr.io/repo/$IMAGE_NAME:v1" egress_public_network_access="disabled"
# </create_vnet_deployment> 

# <get_logs> 
az ml online-deployment get-logs -n blue --endpoint $ENDPOINT_NAME
# </get_logs>

# check if scoring works
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file $SAMPLE_REQUEST_PATH


```


1. To make a scoring request with the endpoint, use the following commands:

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


# navigate to the samples directory
cd /home/samples/azureml-examples/cli/

# <check_deployment> 
# Try scoring using the CLI
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file $SAMPLE_REQUEST_PATH

# Try scoring using curl
ENDPOINT_KEY=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME -o tsv --query primaryKey)
SCORING_URI=$(az ml online-endpoint show -n $ENDPOINT_NAME -o tsv --query scoring_uri)
curl --request POST "$SCORING_URI" --header "Authorization: Bearer $ENDPOINT_KEY" --header 'Content-Type: application/json' --data @$SAMPLE_REQUEST_PATH
# </check_deployment> 


```
