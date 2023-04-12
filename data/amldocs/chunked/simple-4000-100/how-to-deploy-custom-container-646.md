
### Stop the image

Now that you've tested locally, stop the image:

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

## Deploy your online endpoint to Azure
Next, deploy your online endpoint to Azure.

# [Azure CLI](#tab/cli)

### Create a YAML file for your endpoint and deployment

You can configure your cloud deployment using YAML. Take a look at the sample YAML for this example:

__tfserving-endpoint.yml__

```yaml
$schema: https://azuremlsdk2.blob.core.windows.net/latest/managedOnlineEndpoint.schema.json
name: tfserving-endpoint
auth_mode: aml_token
```

__tfserving-deployment.yml__

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: tfserving-deployment
endpoint_name: tfserving-endpoint
model:
  name: tfserving-mounted
  version: {{MODEL_VERSION}}
  path: ./half_plus_two
environment_variables:
  MODEL_BASE_PATH: /var/azureml-app/azureml-models/tfserving-mounted/{{MODEL_VERSION}}
  MODEL_NAME: half_plus_two
environment:
  #name: tfserving
  #version: 1
  image: docker.io/tensorflow/serving:latest
  inference_config:
    liveness_route:
      port: 8501
      path: /v1/models/half_plus_two
    readiness_route:
      port: 8501
      path: /v1/models/half_plus_two
    scoring_route:
      port: 8501
      path: /v1/models/half_plus_two:predict
instance_type: Standard_DS3_v2
instance_count: 1
```
