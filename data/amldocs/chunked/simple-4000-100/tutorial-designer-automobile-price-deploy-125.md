    In the **Deployment logs** tab, you can find the detailed deployment logs of your real-time endpoint.

1. To test your endpoint, go to the **Test** tab. From here, you can enter test data and select **Test** verify the output of your endpoint.

## Update the real-time endpoint

You can update the online endpoint with new model trained in the designer. On the online endpoint detail page, find your previous training pipeline job and inference pipeline job.

1. You can directly find and modify your training pipeline draft in the designer homepage.
    
    Or you can open the training pipeline job link and then clone it into a new pipeline draft to continue editing.

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/endpoint-train-job-link.png" alt-text="Screenshot showing training job link in endpoint detail page.":::

1. After you submit the modified training pipeline, go to the job detail page.

1. When the job completes, right click **Train Model** and select **Register data**.

     :::image type="content" source="./media/how-to-run-batch-predictions-designer/register-train-model-as-dataset.png" alt-text="Screenshot showing register trained model as dataset.":::

    Input name and select **File** type.

    :::image type="content" source="./media/how-to-run-batch-predictions-designer/register-train-model-as-dataset-2.png" alt-text="Screenshot of register as a data asset with new data asset selected.":::

1. After the dataset registers successfully, open your inference pipeline draft, or clone the previous inference pipeline job into a new draft. In the inference pipeline draft, replace the previous trained model shown as **MD-XXXX** node connected to the **Score Model** component with the newly registered dataset.

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/modify-inference-pipeline.png" alt-text="Screenshot showing how to modify inference pipeline.":::


1. If you need to update the data preprocessing part in your training pipeline, and would like to update that into the inference pipeline, the processing is similar as steps above.

    You just need to register the transformation output of the transformation component as dataset.

    Then manually replace the **TD-** component in inference pipeline with the registered dataset.

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/replace-td-module.png" alt-text="Screenshot showing how to replace transformation component.":::

1. After modifying your inference pipeline with the newly trained model or transformation, submit it. When the job is completed, deploy it to the existing online endpoint deployed previously.

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/deploy-to-existing-endpoint.png" alt-text="Screenshot showing how to replace existing real-time endpoint.":::

## Limitations

* Due to datastore access limitation, if your inference pipeline contains **Import Data** or **Export Data** component, they'll be auto-removed when deploy to real-time endpoint.

* If you have datasets in the real-time inference pipeline and want to deploy it to real-time endpoint, currently this flow only supports datasets registered from **Blob** datastore. If you want to use datasets from other type datastores, you can use Select Column to connect with your initial dataset with settings of selecting all columns, register the outputs of Select Column as File dataset and then replace the initial dataset in the real-time inference pipeline with this newly registered dataset.

* If your inference graph contains "Enter Data Manually" component which is not connected to the same port as “Web service Input” component, the "Enter Data Manually" component will not be executed during HTTP call processing. A workaround is to register the outputs of that "Enter Data Manually" component as dataset, then in the inference pipeline draft, replace the "Enter Data Manually" component with the registered dataset. 
