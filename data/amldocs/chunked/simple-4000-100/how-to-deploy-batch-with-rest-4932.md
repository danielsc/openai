
#### Invoke the batch endpoint with different input options

It's time to invoke the batch endpoint to start a batch scoring job. If your data is a folder (potentially with multiple files) publicly available from the web, you can use the following snippet:

```rest-api
response=$(curl --location --request POST $SCORING_URI \
--header "Authorization: Bearer $SCORING_TOKEN" \
--header "Content-Type: application/json" \
--data-raw "{
    \"properties\": {
    	\"InputData\": {
    		\"mnistinput\": {
    			\"JobInputType\" : \"UriFolder\",
    			\"Uri\":  \"https://pipelinedata.blob.core.windows.net/sampledata/mnist\"
    		}
        }
    }
}")

JOB_ID=$(echo $response | jq -r '.id')
JOB_ID_SUFFIX=$(echo ${JOB_ID##/*/})
```

Now, let's look at other options for invoking the batch endpoint. When it comes to input data, there are multiple scenarios you can choose from, depending on the input type (whether you are specifying a folder or a single file), and the URI type (whether you are using a path on Azure Machine Learning registered datastore, a reference to Azure Machine Learning registered V2 data asset, or a public URI).

- An `InputData` property has `JobInputType` and `Uri` keys. When you are specifying a single file, use `"JobInputType": "UriFile"`, and when you are specifying a folder, use `'JobInputType": "UriFolder"`.

- When the file or folder is on Azure ML registered datastore, the syntax for the `Uri` is  `azureml://datastores/<datastore-name>/paths/<path-on-datastore>` for folder, and `azureml://datastores/<datastore-name>/paths/<path-on-datastore>/<file-name>` for a specific file. You can also use the longer form to represent the same path, such as `azureml://subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/workspaces/<workspace-name>/datastores/<datastore-name>/paths/<path-on-datastore>/`.

- When the file or folder is registered as V2 data asset as `uri_folder` or `uri_file`, the syntax for the `Uri` is `\"azureml://locations/<location-name>/workspaces/<workspace-name>/data/<data-name>/versions/<data-version>"` (Asset ID form) or `\"/subscriptions/<subscription-id>/resourcegroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>/data/<data-name>/versions/<data-version>\"` (ARM ID form).

- When the file or folder is a publicly accessible path, the syntax for the URI is `https://<public-path>` for folder, `https://<public-path>/<file-name>` for a specific file.

> [!NOTE]
> For more information about data URI, see [Azure Machine Learning data reference URI](reference-yaml-core-syntax.md#azure-ml-data-reference-uri).

Below are some examples using different types of input data.

- If your data is a folder on the Azure ML registered datastore, you can either:

    - Use the short form to represent the URI:

    ```rest-api
    response=$(curl --location --request POST $SCORING_URI \
    --header "Authorization: Bearer $SCORING_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw "{
        \"properties\": {
            \"InputData\": {
                \"mnistInput\": {
                    \"JobInputType\" : \"UriFolder\",
                    \"Uri": \"azureml://datastores/workspaceblobstore/paths/$ENDPOINT_NAME/mnist\"
                }
            }
        }
    }")
    
    JOB_ID=$(echo $response | jq -r '.id')
    JOB_ID_SUFFIX=$(echo ${JOB_ID##/*/})
    ```

    - Or use the long form for the same URI:

    ```rest-api
    response=$(curl --location --request POST $SCORING_URI \
    --header "Authorization: Bearer $SCORING_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw "{
        \"properties\": {
        	\"InputData\": {
        		\"mnistinput\": {
        			\"JobInputType\" : \"UriFolder\",
        			\"Uri\": \"azureml://subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/workspaces/$WORKSPACE/datastores/workspaceblobstore/paths/$ENDPOINT_NAME/mnist\"
        		}
            }
        }
    }")
    
    JOB_ID=$(echo $response | jq -r '.id')
    JOB_ID_SUFFIX=$(echo ${JOB_ID##/*/})
    ```
