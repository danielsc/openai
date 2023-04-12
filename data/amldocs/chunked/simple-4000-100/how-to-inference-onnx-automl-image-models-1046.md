The instance segmentation model predicts boxes, labels, scores, and masks. ONNX outputs a predicted mask per instance, along with corresponding bounding boxes and class confidence score. You might need to convert from binary mask to polygon if necessary.

```python

def get_predictions_from_ONNX(onnx_session, img_data):
    """Perform predictions with ONNX runtime
    
    :param onnx_session: onnx model session
    :type onnx_session: class InferenceSession
    :param img_data: pre-processed numpy image
    :type img_data: ndarray with shape 1xCxHxW
    :return: boxes, labels , scores , masks with shapes
            (No. of instances, 4) (No. of instances,) (No. of instances,)
            (No. of instances, 1, HEIGHT, WIDTH))  
    :rtype: tuple
    """
    
    sess_input = onnx_session.get_inputs()
    sess_output = onnx_session.get_outputs()
    # predict with ONNX Runtime
    output_names = [ output.name for output in sess_output]
    predictions = onnx_session.run(output_names=output_names,\
                                               input_feed={sess_input[0].name: img_data})
    return output_names, predictions

output_names, predictions = get_predictions_from_ONNX(session, img_data)
```


## Postprocessing

# [Multi-class image classification](#tab/multi-class)

Apply `softmax()` over predicted values to get classification confidence scores (probabilities) for each class. Then the prediction will be the class with the highest probability. 

### Without PyTorch

```python
def softmax(x):
    e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e_x / np.sum(e_x, axis=1, keepdims=True)

conf_scores = softmax(scores)
class_preds = np.argmax(conf_scores, axis=1)
print("predicted classes:", ([(class_idx, classes[class_idx]) for class_idx in class_preds]))
```

### With PyTorch

```python
conf_scores = torch.nn.functional.softmax(torch.from_numpy(scores), dim=1)
class_preds = torch.argmax(conf_scores, dim=1)
print("predicted classes:", ([(class_idx.item(), classes[class_idx]) for class_idx in class_preds]))
```

# [Multi-label image classification](#tab/multi-label)

This step differs from multi-class classification. You need to apply `sigmoid` to the logits (ONNX output) to get confidence scores for multi-label image classification.

### Without PyTorch

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# we apply a threshold of 0.5 on confidence scores
score_threshold = 0.5
conf_scores = sigmoid(scores)
image_wise_preds = np.where(conf_scores > score_threshold)
for image_idx, class_idx in zip(image_wise_preds[0], image_wise_preds[1]):
    print('image: {}, class_index: {}, class_name: {}'.format(image_files[image_idx], class_idx, classes[class_idx]))
```

### With PyTorch

```python
# we apply a threshold of 0.5 on confidence scores
score_threshold = 0.5
conf_scores = torch.sigmoid(torch.from_numpy(scores))
image_wise_preds = torch.where(conf_scores > score_threshold)
for image_idx, class_idx in zip(image_wise_preds[0], image_wise_preds[1]):
    print('image: {}, class_index: {}, class_name: {}'.format(image_files[image_idx], class_idx, classes[class_idx]))
```

For multi-class and multi-label classification, you can follow the same steps mentioned earlier for all the supported model architectures in AutoML.


# [Object detection with Faster R-CNN or RetinaNet](#tab/object-detect-cnn)

For object detection, predictions are automatically on the scale of `height_onnx`, `width_onnx`. To transform the predicted box coordinates to the original dimensions, you can implement the following calculations. 

- Xmin * original_width/width_onnx
- Ymin * original_height/height_onnx
- Xmax * original_width/width_onnx
- Ymax * original_height/height_onnx
  
Another option is to use the following code to scale the box dimensions to be in the range of [0, 1]. Doing so allows the box coordinates to be multiplied with original images height and width with respective coordinates (as described in [visualize predictions section](#visualize-predictions)) to get boxes in original image dimensions.
