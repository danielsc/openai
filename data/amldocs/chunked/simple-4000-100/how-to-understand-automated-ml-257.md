Classification report provides the class-level values for metrics like precision, recall, f1-score, support, auc and average_precision with  various level of averaging - micro, macro and weighted as shown below.
Please refer to the metrics definitions from the [classification metrics](#classification-metrics) section.

![Classification report for image classification](./media/how-to-understand-automated-ml/image-classification-report.png)

### Object detection and instance segmentation metrics

Every prediction from an image object detection or instance segmentation  model is associated with a confidence score.
The predictions with confidence score greater than score threshold are output as predictions and used in the metric calculation, the default value of which is model specific and can be referred from the [hyperparameter tuning](reference-automl-images-hyperparameters.md#model-specific-hyperparameters) page(`box_score_threshold` hyperparameter).

The metric computation of an image object detection and instance segmentation model is based on an overlap measurement defined by a metric called **IoU** ([Intersection over Union](https://en.wikipedia.org/wiki/Jaccard_index)) which is computed by dividing the area of overlap between the ground-truth and the predictions by the area of union of the ground-truth and the predictions. The IoU computed from every prediction is compared with an **overlap threshold** called an IoU threshold which determines how much a prediction should overlap with a user-annotated ground-truth in order to be considered as a positive prediction. If the IoU computed from the prediction is less than the overlap threshold the prediction would not be considered as a positive prediction for the associated class.

The primary metric for the evaluation of image object detection and instance segmentation models is the **mean average precision (mAP)**. The mAP is the average value of the average precision(AP) across all the classes. Automated ML object detection models support the computation of mAP using the below two popular methods.

**Pascal VOC metrics**: 

[Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/devkit_doc.html#SECTION00044000000000000000) mAP is the default way of mAP computation for object detection/instance segmentation models. Pascal VOC style mAP method calculates the area under a version of the precision-recall curve. First p(rᵢ), which is precision at recall i is computed for all unique recall values. p(rᵢ) is then replaced with maximum precision obtained for any recall r' >= rᵢ. The precision value is monotonically decreasing in this version of the curve. Pascal VOC mAP metric is by default evaluated with an IoU threshold of 0.5. A detailed explanation of this concept is available in this [blog](https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173).


**COCO metrics**: 

[COCO evaluation method](https://cocodataset.org/#detection-eval) uses a 101-point interpolated method for AP calculation along with averaging over ten IoU thresholds. AP@[.5:.95] corresponds to the average AP for IoU from 0.5 to 0.95 with a step size of 0.05. Automated ML logs all the twelve metrics defined by the COCO method including the AP and AR(average recall) at various scales in the application logs while the metrics user interface shows only the mAP  at an IoU threshold of 0.5. 

> [!TIP]
> The image object detection model evaluation can use coco metrics if the `validation_metric_type` hyperparameter is set to be 'coco' as explained in the [hyperparameter tuning](reference-automl-images-hyperparameters.md#object-detection-and-instance-segmentation-task-specific-hyperparameters) section.

#### Epoch-level metrics for object detection and instance segmentation
The mAP, precision and recall values are logged at an epoch-level for image object detection/instance segmentation models. The mAP, precision and recall metrics are also logged at a class level with the name 'per_label_metrics'. The 'per_label_metrics' should be viewed as a table. 
