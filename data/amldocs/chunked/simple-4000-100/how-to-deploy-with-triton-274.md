
# [Studio](#tab/azure-studio)

This section shows how you can define a Triton deployment on a managed online endpoint using [Azure Machine Learning studio](https://ml.azure.com).

1. Register your model in Triton format using the following YAML and CLI command. The YAML uses a densenet-onnx model from [https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/triton/single-model](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/triton/single-model)

    __create-triton-model.yaml__

    ```yml
    name: densenet-onnx-model
    version: 1
    path: ./models
    type: triton_model​
    description: Registering my Triton format model.
    ```

    ```azurecli
    az ml model create -f create-triton-model.yaml
    ```

    The following screenshot shows how your registered model will look on the __Models page__ of Azure Machine Learning studio.

    :::image type="content" source="media/how-to-deploy-with-triton/triton-model-format.png" lightbox="media/how-to-deploy-with-triton/triton-model-format.png" alt-text="Screenshot showing Triton model format on Models page.":::

1. From [studio](https://ml.azure.com), select your workspace and then use either the __endpoints__ or __models__ page to create the endpoint deployment:

    # [Endpoints page](#tab/endpoint)

    1. From the __Endpoints__ page, select **Create**.

        :::image type="content" source="media/how-to-deploy-with-triton/create-option-from-endpoints-page.png" lightbox="media/how-to-deploy-with-triton/create-option-from-endpoints-page.png" alt-text="Screenshot showing create option on the Endpoints UI page.":::

    1. Provide a name and authentication type for the endpoint, and then select __Next__.
    1. When selecting a model, select the Triton model registered previously. Select __Next__ to continue.

    1. When you select a model registered in Triton format, in the Environment step of the wizard, you don't need scoring script and environment.

        :::image type="content" source="media/how-to-deploy-with-triton/ncd-triton.png" lightbox="media/how-to-deploy-with-triton/ncd-triton.png" alt-text="Screenshot showing no code and environment needed for Triton models":::

    # [Models page](#tab/models)

    1. Select the Triton model, and then select __Deploy__. When prompted, select __Deploy to real-time endpoint__.

        :::image type="content" source="media/how-to-deploy-with-triton/deploy-from-models-page.png" lightbox="media/how-to-deploy-with-triton/deploy-from-models-page.png" alt-text="Screenshot showing how to deploy model from Models UI.":::



## Deploy to Azure

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

1. To create a new endpoint using the YAML configuration, use the following command:

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
