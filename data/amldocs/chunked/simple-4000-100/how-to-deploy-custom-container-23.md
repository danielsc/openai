|[torchserve/huggingface-textgen](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/torchserve/huggingface-textgen)|[deploy-custom-container-torchserve-huggingface-textgen](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-torchserve-huggingface-textgen.sh)|Deploy Hugging Face models to an online endpoint and follow along with the Hugging Face Transformers TorchServe example.| 
|[triton/single-model](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/triton/single-model)|[deploy-custom-container-triton-single-model](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-triton-single-model.sh)|Deploy a Triton model using a custom container|

This article focuses on serving a TensorFlow model with TensorFlow (TF) Serving. 

> [!WARNING]
> Microsoft may not be able to help troubleshoot problems caused by a custom image. If you encounter problems, you may be asked to use the default image or one of the images Microsoft provides to see if the problem is specific to your image.

## Prerequisites

[!INCLUDE [cli & sdk](../../includes/machine-learning-cli-sdk-v2-prereqs.md)]

* You, or the service principal you use, must have `Contributor` access to the Azure Resource Group that contains your workspace. You'll have such a resource group if you configured your workspace using the quickstart article.

* To deploy locally, you must have [Docker engine](https://docs.docker.com/engine/install/) running locally. This step is **highly recommended**. It will help you debug issues.

## Download source code

To follow along with this tutorial, download the source code below.

# [Azure CLI](#tab/cli)

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/cli
```

# [Python SDK](#tab/python)

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/sdk
```

See also [the example notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/custom-container/online-endpoints-custom-container.ipynb) but note that `3. Test locally` section in the notebook assumes to run under the `azureml-examples/sdk` directory.


## Initialize environment variables

Define environment variables:

```azurecli
#/bin/bash

set -e

# <initialize_variables>
BASE_PATH=endpoints/online/custom-container/tfserving/half-plus-two
AML_MODEL_NAME=tfserving-mounted
MODEL_NAME=half_plus_two
MODEL_BASE_PATH=/var/azureml-app/azureml-models/$AML_MODEL_NAME/1
# </initialize_variables>

# <download_and_unzip_model>
wget https://aka.ms/half_plus_two-model -O $BASE_PATH/half_plus_two.tar.gz
tar -xvf $BASE_PATH/half_plus_two.tar.gz -C $BASE_PATH
# </download_and_unzip_model>

# Clean up utility
cleanup(){
    rm $BASE_PATH/half_plus_two.tar.gz
    rm -r $BASE_PATH/half_plus_two
}

# <run_image_locally_for_testing>
docker run --rm -d -v $PWD/$BASE_PATH:$MODEL_BASE_PATH -p 8501:8501 \
 -e MODEL_BASE_PATH=$MODEL_BASE_PATH -e MODEL_NAME=$MODEL_NAME \
 --name="tfserving-test" docker.io/tensorflow/serving:latest
sleep 10
# </run_image_locally_for_testing>

# <check_liveness_locally>
curl -v http://localhost:8501/v1/models/$MODEL_NAME
# </check_liveness_locally>

# <check_scoring_locally>
curl --header "Content-Type: application/json" \
  --request POST \
  --data @$BASE_PATH/sample_request.json \
  http://localhost:8501/v1/models/$MODEL_NAME:predict
# </check_scoring_locally>

# <stop_image>
docker stop tfserving-test
# </stop_image>

# <set_endpoint_name> 
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

export ENDPOINT_NAME=endpt-tfserving-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --name $ENDPOINT_NAME -f $BASE_PATH/tfserving-endpoint.yml
# </create_endpoint>

MODEL_VERSION=$RANDOM
sed -e "s/{{MODEL_VERSION}}/$MODEL_VERSION/g" -i $BASE_PATH/tfserving-deployment.yml

# <create_deployment>
az ml online-deployment create --name tfserving-deployment --endpoint $ENDPOINT_NAME -f $BASE_PATH/tfserving-deployment.yml --all-traffic
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

deploy_status=`az ml online-deployment show --name tfserving-deployment --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  # <delete_endpoint_and_model>
  az ml online-endpoint delete -n $ENDPOINT_NAME -y
  echo "deleting model..."
  az ml model archive -n tfserving-mounted --version 1
  # </delete_endpoint_and_model>
  cleanup
  exit 1
fi

# Test remotely
echo "Testing endpoint"
for i in {1..10}
do
   # <invoke_endpoint>
   RESPONSE=$(az ml online-endpoint invoke -n $ENDPOINT_NAME --request-file $BASE_PATH/sample_request.json)
   # </invoke_endpoint>
done

echo "Tested successfully, response was $RESPONSE. Cleaning up..."

# <delete_endpoint_and_model>
az ml online-endpoint delete -n $ENDPOINT_NAME -y
echo "deleting model..."
az ml model archive -n tfserving-mounted --version 1
# </delete_endpoint_and_model>

cleanup

```
