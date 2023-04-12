You can use either the `invoke` command or a REST client of your choice to invoke the endpoint and score some data: 

```azurecli
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file cli/endpoints/online/model-1/sample-request.json
```


### (Optional) Update the deployment

# [Azure CLI](#tab/azure-cli)

If you want to update the code, model, or environment, update the YAML file, and then run the `az ml online-endpoint update` command. 

> [!NOTE]
> If you update instance count and along with other model settings (code, model, or environment) in a single `update` command: first the scaling operation will be performed, then the other updates will be applied. In production environment is a good practice to perform these operations separately.

To understand how `update` works:

1. Open the file *online/model-1/onlinescoring/score.py*.
1. Change the last line of the `init()` function: After `logging.info("Init complete")`, add `logging.info("Updated successfully")`. 
1. Save the file.
1. Run this command:

    ```azurecli
    az ml online-deployment update -n blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml
    ```

    > [!Note]
    > Updating by using YAML is declarative. That is, changes in the YAML are reflected in the underlying Azure Resource Manager resources (endpoints and deployments). A declarative approach facilitates [GitOps](https://www.atlassian.com/git/tutorials/gitops): *All* changes to endpoints and deployments (even `instance_count`) go through the YAML.

    > [!TIP]
    > With the `update` command, you can use the [`--set` parameter in the Azure CLI](/cli/azure/use-cli-effectively#generic-update-parameters) to override attributes in your YAML *or* to set specific attributes without passing the YAML file. Using `--set` for single attributes is especially valuable in development and test scenarios. For example, to scale up the `instance_count` value for the first deployment, you could use the `--set instance_count=2` flag. However, because the YAML isn't updated, this technique doesn't facilitate [GitOps](https://www.atlassian.com/git/tutorials/gitops).

1. Because you modified the `init()` function (`init()` runs when the endpoint is created or updated), the message `Updated successfully` will be in the logs. Retrieve the logs by running:

```azurecli
set -e

# <set_endpoint_name> 
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

export ENDPOINT_NAME=endpt-moe-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --name $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml --all-traffic
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

# <test_endpoint>
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
# </test_endpoint>

# supress printing secret
set +x

# <test_endpoint_using_curl_get_key>
ENDPOINT_KEY=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME -o tsv --query primaryKey)
# </test_endpoint_using_curl_get_key>

set -x

# <test_endpoint_using_curl>
SCORING_URI=$(az ml online-endpoint show -n $ENDPOINT_NAME -o tsv --query scoring_uri)

curl --request POST "$SCORING_URI" --header "Authorization: Bearer $ENDPOINT_KEY" --header 'Content-Type: application/json' --data @endpoints/online/model-1/sample-request.json
# </test_endpoint_using_curl>

# <get_logs>
az ml online-deployment get-logs --name blue --endpoint $ENDPOINT_NAME
# </get_logs>

# <delete_endpoint>
az ml online-endpoint delete --name $ENDPOINT_NAME --yes --no-wait
# </delete_endpoint>
```
