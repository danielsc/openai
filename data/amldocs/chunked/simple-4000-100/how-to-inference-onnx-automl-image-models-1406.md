
# [Instance segmentation](#tab/instance-segmentation)

Visualize a sample input image with masks and labels

```python
import matplotlib.patches as patches
import matplotlib.pyplot as plt
%matplotlib inline

def display_detections(image, boxes, labels, scores, masks, resize_height, 
                       resize_width, classes, score_threshold):
    """Visualize boxes and masks
    
    :param image: raw image
    :type image: PIL image
    :param boxes: box with shape (No. of instances, 4) 
    :type boxes: ndarray 
    :param labels: classes with shape (No. of instances,) 
    :type labels: ndarray
    :param scores: scores with shape (No. of instances,)
    :type scores: ndarray
    :param masks: masks with shape (No. of instances, 1, HEIGHT, WIDTH) 
    :type masks:  ndarray
    :param resize_height: expected height of an input image in onnx model
    :type resize_height: Int
    :param resize_width: expected width of an input image in onnx model
    :type resize_width: Int
    :param classes: classes with shape (No. of classes) 
    :type classes:  list
    :param score_threshold: threshold on scores in the range of 0-1
    :type score_threshold: float
    :return: None
    """

    _, ax = plt.subplots(1, figsize=(12,9))

    image = np.array(image)
    original_height = image.shape[0]
    original_width = image.shape[1]

    for mask, box, label, score in zip(masks, boxes, labels, scores):        
        if score <= score_threshold:
            continue
        mask = mask[0, :, :, None]        
        # resize boxes to original raw input size
        box = [box[0]*original_width/resize_width, 
               box[1]*original_height/resize_height, 
               box[2]*original_width/resize_width, 
               box[3]*original_height/resize_height]
        
        mask = cv2.resize(mask, (image.shape[1], image.shape[0]), 0, 0, interpolation = cv2.INTER_NEAREST)
        # mask is a matrix with values in the range of [0,1]
        # higher values indicate presence of object and vice versa
        # select threshold or cut-off value to get objects present       
        mask = mask > score_threshold
        image_masked = image.copy()
        image_masked[mask] = (0, 255, 255)
        alpha = 0.5  # alpha blending with range 0 to 1
        cv2.addWeighted(image_masked, alpha, image, 1 - alpha,0, image)
        rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1],\
                                 linewidth=1, edgecolor='b', facecolor='none')
        ax.annotate(classes[label] + ':' + str(np.round(score, 2)), (box[0], box[1]),\
                    color='w', fontsize=12)
        ax.add_patch(rect)
        
    ax.imshow(image)
    plt.show()

score_threshold = 0.5
img = Image.open(image_files[1])  # replace with desired image index
image_boxes = filtered_boxes_batch[1]  # replace with desired image index
boxes, labels, scores, masks = predictions[4:8]  # replace with desired image index
display_detections(img, boxes.copy(), labels, scores, masks.copy(), 
                   height_onnx, width_onnx, classes, score_threshold)
```


## Next steps
* [Learn more about computer vision tasks in AutoML](how-to-auto-train-image-models.md)
* [Troubleshoot AutoML experiments](how-to-troubleshoot-auto-ml.md)
