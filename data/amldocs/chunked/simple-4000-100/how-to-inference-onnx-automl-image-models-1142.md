Another option is to use the following code to scale the box dimensions to be in the range of [0, 1]. Doing so allows the box coordinates to be multiplied with original images height and width with respective coordinates (as described in [visualize predictions section](#visualize-predictions)) to get boxes in original image dimensions.

```python
def _get_box_dims(image_shape, box):
    box_keys = ['topX', 'topY', 'bottomX', 'bottomY']
    height, width = image_shape[0], image_shape[1]

    box_dims = dict(zip(box_keys, [coordinate.item() for coordinate in box]))

    box_dims['topX'] = box_dims['topX'] * 1.0 / width
    box_dims['bottomX'] = box_dims['bottomX'] * 1.0 / width
    box_dims['topY'] = box_dims['topY'] * 1.0 / height
    box_dims['bottomY'] = box_dims['bottomY'] * 1.0 / height

    return box_dims

def _get_prediction(boxes, labels, scores, image_shape, classes):
    bounding_boxes = []
    for box, label_index, score in zip(boxes, labels, scores):
        box_dims = _get_box_dims(image_shape, box)

        box_record = {'box': box_dims,
                      'label': classes[label_index],
                      'score': score.item()}

        bounding_boxes.append(box_record)

    return bounding_boxes

# Filter the results with threshold.
# Please replace the threshold for your test scenario.
score_threshold = 0.8
filtered_boxes_batch = []
for batch_sample in range(0, batch_size*3, 3):
    # in case of retinanet change the order of boxes, labels, scores to boxes, scores, labels
    # confirm the same from order of boxes, labels, scores output_names 
    boxes, labels, scores = predictions[batch_sample], predictions[batch_sample + 1], predictions[batch_sample + 2]
    bounding_boxes = _get_prediction(boxes, labels, scores, (height_onnx, width_onnx), classes)
    filtered_bounding_boxes = [box for box in bounding_boxes if box['score'] >= score_threshold]
    filtered_boxes_batch.append(filtered_bounding_boxes)
```

# [Object detection with YOLO](#tab/object-detect-yolo)

The following code creates boxes, labels, and scores. Use these bounding box details to perform the same postprocessing steps as you did for the Faster R-CNN model. 

```python
from yolo_onnx_preprocessing_utils import non_max_suppression, _convert_to_rcnn_output

result_final = non_max_suppression(
    torch.from_numpy(result),
    conf_thres=0.1,
    iou_thres=0.5)

def _get_box_dims(image_shape, box):
    box_keys = ['topX', 'topY', 'bottomX', 'bottomY']
    height, width = image_shape[0], image_shape[1]

    box_dims = dict(zip(box_keys, [coordinate.item() for coordinate in box]))

    box_dims['topX'] = box_dims['topX'] * 1.0 / width
    box_dims['bottomX'] = box_dims['bottomX'] * 1.0 / width
    box_dims['topY'] = box_dims['topY'] * 1.0 / height
    box_dims['bottomY'] = box_dims['bottomY'] * 1.0 / height

    return box_dims

def _get_prediction(label, image_shape, classes):
    
    boxes = np.array(label["boxes"])
    labels = np.array(label["labels"])
    labels = [label[0] for label in labels]
    scores = np.array(label["scores"])
    scores = [score[0] for score in scores]

    bounding_boxes = []
    for box, label_index, score in zip(boxes, labels, scores):
        box_dims = _get_box_dims(image_shape, box)

        box_record = {'box': box_dims,
                      'label': classes[label_index],
                      'score': score.item()}

        bounding_boxes.append(box_record)

    return bounding_boxes

bounding_boxes_batch = []
for result_i, pad in zip(result_final, pad_list):
    label, image_shape = _convert_to_rcnn_output(result_i, height_onnx, width_onnx, pad)
    bounding_boxes_batch.append(_get_prediction(label, image_shape, classes))
print(json.dumps(bounding_boxes_batch, indent=1))
```

# [Instance segmentation](#tab/instance-segmentation)

 You can either use the steps mentioned for Faster R-CNN (in case of Mask R-CNN, each sample has four elements boxes, labels, scores, masks) or refer to the [visualize predictions](#visualize-predictions) section for instance segmentation.
