## Inference with ONNX Runtime

Inferencing with ONNX Runtime differs for each computer vision task.

# [Multi-class image classification](#tab/multi-class)

```python
def get_predictions_from_ONNX(onnx_session, img_data):
    """Perform predictions with ONNX runtime
    
    :param onnx_session: onnx model session
    :type onnx_session: class InferenceSession
    :param img_data: pre-processed numpy image
    :type img_data: ndarray with shape 1xCxHxW
    :return: scores with shapes
            (1, No. of classes in training dataset) 
    :rtype: numpy array
    """

    sess_input = onnx_session.get_inputs()
    sess_output = onnx_session.get_outputs()
    print(f"No. of inputs : {len(sess_input)}, No. of outputs : {len(sess_output)}")    
    # predict with ONNX Runtime
    output_names = [ output.name for output in sess_output]
    scores = onnx_session.run(output_names=output_names,\
                                               input_feed={sess_input[0].name: img_data})
    
    return scores[0]

scores = get_predictions_from_ONNX(session, img_data)
```

# [Multi-label image classification](#tab/multi-label)

```python
def get_predictions_from_ONNX(onnx_session,img_data):
    """Perform predictions with ONNX runtime
    
    :param onnx_session: onnx model session
    :type onnx_session: class InferenceSession
    :param img_data: pre-processed numpy image
    :type img_data: ndarray with shape 1xCxHxW
    :return: scores with shapes
            (1, No. of classes in training dataset) 
    :rtype: numpy array
    """
    
    sess_input = onnx_session.get_inputs()
    sess_output = onnx_session.get_outputs()
    print(f"No. of inputs : {len(sess_input)}, No. of outputs : {len(sess_output)}")    
    # predict with ONNX Runtime
    output_names = [ output.name for output in sess_output]
    scores = onnx_session.run(output_names=output_names,\
                                               input_feed={sess_input[0].name: img_data})
    
    return scores[0]

scores = get_predictions_from_ONNX(session, img_data)
```

# [Object detection with Faster R-CNN or RetinaNet](#tab/object-detect-cnn)

```python
def get_predictions_from_ONNX(onnx_session, img_data):
    """perform predictions with ONNX runtime
    
    :param onnx_session: onnx model session
    :type onnx_session: class InferenceSession
    :param img_data: pre-processed numpy image
    :type img_data: ndarray with shape 1xCxHxW
    :return: boxes, labels , scores 
            (No. of boxes, 4) (No. of boxes,) (No. of boxes,)
    :rtype: tuple
    """

    sess_input = onnx_session.get_inputs()
    sess_output = onnx_session.get_outputs()
    
    # predict with ONNX Runtime
    output_names = [output.name for output in sess_output]
    predictions = onnx_session.run(output_names=output_names,\
                                               input_feed={sess_input[0].name: img_data})

    return output_names, predictions

output_names, predictions = get_predictions_from_ONNX(session, img_data)
```

# [Object detection with YOLO](#tab/object-detect-yolo)

```python
def get_predictions_from_ONNX(onnx_session,img_data):
    """perform predictions with ONNX Runtime
    
    :param onnx_session: onnx model session
    :type onnx_session: class InferenceSession
    :param img_data: pre-processed numpy image
    :type img_data: ndarray with shape 1xCxHxW
    :return: boxes, labels , scores 
    :rtype: list
    """
    sess_input = onnx_session.get_inputs()
    sess_output = onnx_session.get_outputs()
    # predict with ONNX Runtime
    output_names = [ output.name for output in sess_output]
    pred = onnx_session.run(output_names=output_names,\
                                               input_feed={sess_input[0].name: img_data})
    return pred[0]

result = get_predictions_from_ONNX(session, img_data)

```

# [Instance segmentation](#tab/instance-segmentation)

The instance segmentation model predicts boxes, labels, scores, and masks. ONNX outputs a predicted mask per instance, along with corresponding bounding boxes and class confidence score. You might need to convert from binary mask to polygon if necessary.
