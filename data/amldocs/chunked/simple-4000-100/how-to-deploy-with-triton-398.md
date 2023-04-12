

1. To create the deployment using the YAML configuration, use the following command:

```azurecli
set -e

BASE_PATH=endpoints/online/triton/single-model

# <installing-requirements>
pip install numpy
pip install tritonclient[http]
pip install pillow
pip install gevent
# </installing-requirements>

# <set_endpoint_name>
export ENDPOINT_NAME=triton-single-endpt-`echo $RANDOM`
# </set_endpoint_name>

# <create_endpoint>
az ml online-endpoint create -n $ENDPOINT_NAME -f $BASE_PATH/create-managed-endpoint.yaml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f $BASE_PATH/create-managed-deployment.yaml --all-traffic
# </create_deployment>

# <get_status>
az ml online-endpoint show -n $ENDPOINT_NAME
# </get_status>

# check if create was successful
endpoint_status=`az ml online-endpoint show --name $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $endpoint_status
if [[ $endpoint_status == "Succeeded" ]]
then
  echo "Endpoint created successfully"
else
  echo "Endpoint creation failed"
  exit 1
fi

deploy_status=`az ml online-deployment show --name blue --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <get_scoring_uri>
scoring_uri=$(az ml online-endpoint show -n $ENDPOINT_NAME --query scoring_uri -o tsv)
scoring_uri=${scoring_uri%/*}
# </get_scoring_uri>

# <get_token>
auth_token=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME --query accessToken -o tsv)
# </get_token>

# <check_scoring_of_model>
python $BASE_PATH/triton_densenet_scoring.py --base_url=$scoring_uri --token=$auth_token --image_path $BASE_PATH/data/peacock.jpg
# </check_scoring_of_model>

# <delete_endpoint>
az ml online-endpoint delete -n $ENDPOINT_NAME --yes
# </delete_endpoint>


```


# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

1. To create a new endpoint using the `ManagedOnlineEndpoint` object, use the following command:

    ```python 
    endpoint = ml_client.online_endpoints.begin_create_or_update(endpoint)
    ``` 

1. To create the deployment using the `ManagedOnlineDeployment` object, use the following command:

    ```python 
    ml_client.online_deployments.begin_create_or_update(deployment)
    ```

1. Once the deployment completes, its traffic value will be set to `0%`. Update the traffic to 100%. 

    ```python 
    endpoint.traffic = {"blue": 100}
    ml_client.online_endpoints.begin_create_or_update(endpoint)
    ```


# [Studio](#tab/azure-studio)
1. Complete the wizard to deploy to the endpoint.

    :::image type="content" source="media/how-to-deploy-with-triton/review-screen-triton.png" lightbox="media/how-to-deploy-with-triton/review-screen-triton.png" alt-text="Screenshot showing NCD review screen":::

1. Once the deployment completes, its traffic value will be set to `0%`. Update the traffic to 100% from the Endpoint page by clicking `Update Traffic` on the second menu row. 


## Test the endpoint

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Once your deployment completes, use the following command to make a scoring request to the deployed endpoint. 

> [!TIP]
> The file `/cli/endpoints/online/triton/single-model/triton_densenet_scoring.py` in the azureml-examples repo is used for scoring. The image passed to the endpoint needs pre-processing to meet the size, type, and format requirements, and post-processing to show the predicted label. The `triton_densenet_scoring.py` uses the `tritonclient.http` library to communicate with the Triton inference server.

1. To get the endpoint scoring uri, use the following command:

```azurecli
set -e

BASE_PATH=endpoints/online/triton/single-model

# <installing-requirements>
pip install numpy
pip install tritonclient[http]
pip install pillow
pip install gevent
# </installing-requirements>

# <set_endpoint_name>
export ENDPOINT_NAME=triton-single-endpt-`echo $RANDOM`
# </set_endpoint_name>

# <create_endpoint>
az ml online-endpoint create -n $ENDPOINT_NAME -f $BASE_PATH/create-managed-endpoint.yaml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f $BASE_PATH/create-managed-deployment.yaml --all-traffic
# </create_deployment>

# <get_status>
az ml online-endpoint show -n $ENDPOINT_NAME
# </get_status>

# check if create was successful
endpoint_status=`az ml online-endpoint show --name $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $endpoint_status
if [[ $endpoint_status == "Succeeded" ]]
then
  echo "Endpoint created successfully"
else
  echo "Endpoint creation failed"
  exit 1
fi

deploy_status=`az ml online-deployment show --name blue --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <get_scoring_uri>
scoring_uri=$(az ml online-endpoint show -n $ENDPOINT_NAME --query scoring_uri -o tsv)
scoring_uri=${scoring_uri%/*}
# </get_scoring_uri>

# <get_token>
auth_token=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME --query accessToken -o tsv)
# </get_token>

# <check_scoring_of_model>
python $BASE_PATH/triton_densenet_scoring.py --base_url=$scoring_uri --token=$auth_token --image_path $BASE_PATH/data/peacock.jpg
# </check_scoring_of_model>

# <delete_endpoint>
az ml online-endpoint delete -n $ENDPOINT_NAME --yes
# </delete_endpoint>


```
