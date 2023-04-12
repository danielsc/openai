For testing our endpoint, we are going to use a sample of 1000 images from the original ImageNet dataset. Batch endpoints can only process data that is located in the cloud and that is accessible from the Azure Machine Learning workspace. In this example, we are going to upload it to an Azure Machine Learning data store. Particularly, we are going to create a data asset that can be used to invoke the endpoint for scoring. However, notice that batch endpoints accept data that can be placed in multiple type of locations.

1. Let's download the associated sample data:

   # [Azure CLI](#tab/cli)
   
   ```bash
   wget https://azuremlexampledata.blob.core.windows.net/data/imagenet-1000.zip
   unzip imagenet-1000.zip -d /tmp/imagenet-1000
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   !wget https://azuremlexampledata.blob.core.windows.net/data/imagenet-1000.zip
   !unzip imagenet-1000.zip -d /tmp/imagenet-1000
   ```

2. Now, let's create the data asset from the data just downloaded

   # [Azure CLI](#tab/cli)
   
   Create a data asset definition in `YAML`:
   
   __imagenet-sample-unlabeled.yml__
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
   name: imagenet-sample-unlabeled
   description: A sample of 1000 images from the original ImageNet dataset.
   type: uri_folder
   path: /tmp/imagenet-1000
   ```
   
   Then, create the data asset:
   
   ```azurecli
   az ml data create -f imagenet-sample-unlabeled.yml
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   data_path = "/tmp/imagenet-1000"
   dataset_name = "imagenet-sample-unlabeled"

   imagenet_sample = Data(
       path=data_path,
       type=AssetTypes.URI_FOLDER,
       description="A sample of 1000 images from the original ImageNet dataset",
       name=dataset_name,
   )
   ```
   
   Then, create the data asset:
   
   ```python
   ml_client.data.create_or_update(imagenet_sample)
   ```
   
   To get the newly created data asset, use:
   
   ```python
   imagenet_sample = ml_client.data.get(dataset_name, label="latest")
   ```
   
3. Now that the data is uploaded and ready to be used, let's invoke the endpoint:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   JOB_NAME = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input azureml:imagenet-sample-unlabeled@latest | jq -r '.name')
   ```
   
   > [!NOTE]
   > The utility `jq` may not be installed on every installation. You can get instructions in [this link](https://stedolan.github.io/jq/download/).
   
   # [Python](#tab/sdk)
   
   ```python
   input = Input(type=AssetTypes.URI_FOLDER, path=imagenet_sample.id)
   job = ml_client.batch_endpoints.invoke(
      endpoint_name=endpoint.name,
      input=input,
   )
   ```
   
   > [!TIP]
   > Notice how we are not indicating the deployment name in the invoke operation. That's because the endpoint automatically routes the job to the default deployment. Since our endpoint only has one deployment, then that one is the default one. You can target an specific deployment by indicating the argument/parameter `deployment_name`.

4. A batch job is started as soon as the command returns. You can monitor the status of the job until it finishes:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   az ml job show --name $JOB_NAME
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   ml_client.jobs.get(job.name)
   ```

5. Once the deployment is finished, we can download the predictions:

   # [Azure CLI](#tab/cli)

   To download the predictions, use the following command:

   ```azurecli
   az ml job download --name $JOB_NAME --output-name score --download-path ./
   ```

   # [Python](#tab/sdk)

   ```python
   ml_client.jobs.download(name=job.name, output_name='score', download_path='./')
   ```

6. The output predictions will look like the following. Notice that the predictions have been combined with the labels for the convenience of the reader. To know more about how to achieve this see the associated notebook.

    ```python
    import pandas as pd
    score = pd.read_csv("named-outputs/score/predictions.csv", header=None,  names=['file', 'class', 'probabilities'], sep=' ')
    score['label'] = score['class'].apply(lambda pred: imagenet_labels[pred])
    score
    ```
