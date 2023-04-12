
* Access to NCv3-series VMs for your Azure subscription.

    > [!IMPORTANT]
    > You may need to request a quota increase for your subscription before you can use this series of VMs. For more information, see [NCv3-series](../virtual-machines/ncv3-series.md).

The information in this article is based on the [online-endpoints-triton.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/triton/single-model/online-endpoints-triton.ipynb) notebook contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste files, clone the repo, and then change directories to the `sdk/endpoints/online/triton/single-model/` directory in the repo:

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/sdk/python/endpoints/online/triton/single-model/
```

# [Studio](#tab/azure-studio)

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

* An Azure Machine Learning workspace. If you don't have one, use the steps in [Manage Azure Machine Learning workspaces in the portal, or with the Python SDK](how-to-manage-workspace.md) to create one.


## Define the deployment configuration

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

This section shows how you can deploy to a managed online endpoint using the Azure CLI with the Machine Learning extension (v2).

> [!IMPORTANT]
> For Triton no-code-deployment, **[testing via local endpoints](how-to-deploy-online-endpoints.md#deploy-and-debug-locally-by-using-local-endpoints)** is currently not supported.

1. To avoid typing in a path for multiple commands, use the following command to set a `BASE_PATH` environment variable. This variable points to the directory where the model and associated YAML configuration files are located:

    ```azurecli
    BASE_PATH=endpoints/online/triton/single-model
    ```

1. Use the following command to set the name of the endpoint that will be created. In this example, a random name is created for the endpoint:

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
