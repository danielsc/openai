In the previous step, we downloaded a file `mlflow-model/artifacts/settings.json` from the best model. which can be used to update the inference settings before registering the model. Although it's recommended to use the same parameters as training for best performance.

Each of the tasks (and some models) has a set of parameters. By default, we use the same values for the parameters that were used during the training and validation. Depending on the behavior that we need when using the model for inference, we can change these parameters. Below you can find a list of parameters for each task type and model.  

| Task | Parameter name | Default  |
|--------- |------------- | --------- |
|Image classification (multi-class and multi-label) | `valid_resize_size`<br>`valid_crop_size` | 256<br>224 |
|Object detection | `min_size`<br>`max_size`<br>`box_score_thresh`<br>`nms_iou_thresh`<br>`box_detections_per_img` | 600<br>1333<br>0.3<br>0.5<br>100 |
|Object detection using `yolov5`| `img_size`<br>`model_size`<br>`box_score_thresh`<br>`nms_iou_thresh` | 640<br>medium<br>0.1<br>0.5 |
|Instance segmentation| `min_size`<br>`max_size`<br>`box_score_thresh`<br>`nms_iou_thresh`<br>`box_detections_per_img`<br>`mask_pixel_score_threshold`<br>`max_number_of_polygon_points`<br>`export_as_image`<br>`image_type` | 600<br>1333<br>0.3<br>0.5<br>100<br>0.5<br>100<br>False<br>JPG|

For a detailed description on task specific hyperparameters, please refer to [Hyperparameters for computer vision tasks in automated machine learning](./reference-automl-images-hyperparameters.md).
    
If you want to use tiling, and want to control tiling behavior, the following parameters are available: `tile_grid_size`, `tile_overlap_ratio` and `tile_predictions_nms_thresh`. For more details on these parameters please check [Train a small object detection model using AutoML](./how-to-use-automl-small-object-detect.md).

###  Test the deployment
Please check this [Test the deployment](./tutorial-auto-train-image-models.md#test-the-deployment) section to test the deployment and visualize the detections from the model.

## Generate explanations for predictions

> [!IMPORTANT]
> These settings are currently in public preview. They are provided without a service-level agreement. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

> [!WARNING]
>  **Model Explainability** is supported only for **multi-class classification** and **multi-label classification**.

Some of the advantages of using Explainable AI (XAI) with AutoML for images:
- Improves the transparency in the complex vision model predictions
- Helps the users to understand the important features/pixels in the input image that are contributing to the model predictions
- Helps in troubleshooting the models
- Helps in discovering the bias

### Explanations
Explanations are **feature attributions** or weights given to each pixel in the input image based on its contribution to model's prediction. Each weight can be negative (negatively correlated with the prediction) or positive (positively correlated with the prediction). These attributions are calculated against the predicted class. For multi-class classification, exactly one attribution matrix of size `[3, valid_crop_size, valid_crop_size]` will be generated per sample, whereas for multi-label classification, attribution matrix of size `[3, valid_crop_size, valid_crop_size]` will be generated for each predicted label/class for each sample.

Using Explainable AI in AutoML for Images on the deployed endpoint, users can get **visualizations** of explanations (attributions overlaid on an input image) and/or **attributions** (multi-dimensional array of size `[3, valid_crop_size, valid_crop_size]`) for each image. Apart from visualizations, users can also get attribution matrices to gain more control over the explanations (like generating custom visualizations using attributions or scrutinizing segments of attributions). All the explanation algorithms will use cropped square images with size `valid_crop_size` for generating attributions.
