 You can either use the steps mentioned for Faster R-CNN (in case of Mask R-CNN, each sample has four elements boxes, labels, scores, masks) or refer to the [visualize predictions](#visualize-predictions) section for instance segmentation.


<a id='visualize_section'></a>
## Visualize predictions


# [Multi-class image classification](#tab/multi-class)

Visualize an input image with labels

```python
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
%matplotlib inline

sample_image_index = 0 # change this for an image of interest from image_files list
IMAGE_SIZE = (18, 12)
plt.figure(figsize=IMAGE_SIZE)
img_np = mpimg.imread(image_files[sample_image_index])

img = Image.fromarray(img_np.astype('uint8'), 'RGB')
x, y = img.size

fig,ax = plt.subplots(1, figsize=(15, 15))
# Display the image
ax.imshow(img_np)

label = class_preds[sample_image_index]
if torch.is_tensor(label):
    label = label.item()
    
conf_score = conf_scores[sample_image_index]
if torch.is_tensor(conf_score):
    conf_score = np.max(conf_score.tolist())
else:
    conf_score = np.max(conf_score)

display_text = '{} ({})'.format(label, round(conf_score, 3))
print(display_text)

color = 'red'
plt.text(30, 30, display_text, color=color, fontsize=30)

plt.show()
```

# [Multi-label image classification](#tab/multi-label)

Visualize an input image with labels

```python
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
%matplotlib inline

sample_image_index = 0 # change this for an image of interest from image_files list
IMAGE_SIZE = (18, 12)
plt.figure(figsize=IMAGE_SIZE)
img_np = mpimg.imread(image_files[sample_image_index])
img = Image.fromarray(img_np.astype('uint8'), 'RGB')
x, y = img.size

fig,ax = plt.subplots(1, figsize=(15, 15))
# Display the image
ax.imshow(img_np)
# we apply a threshold of 0.5 on confidence scores
score_threshold = 0.5
label_offset_x = 30
label_offset_y = 30
if torch.is_tensor(conf_scores):
    sample_image_scores = conf_scores[sample_image_index].tolist()
else:
    sample_image_scores = conf_scores[sample_image_index]
    
for index, score in enumerate(sample_image_scores):
    if score > score_threshold:
        label = classes[index]
        display_text = '{} ({})'.format(label, round(score, 3))
        print(display_text)

        color = 'red'
        plt.text(label_offset_x, label_offset_y, display_text, color=color, fontsize=30)
        label_offset_y += 30

plt.show()
```

# [Object detection with Faster R-CNN or RetinaNet](#tab/object-detect-cnn)

Visualize an input image with boxes and labels

```python
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.pyplot as plt
%matplotlib inline

img_np = mpimg.imread(image_files[1])  # replace with desired image index
image_boxes = filtered_boxes_batch[1]  # replace with desired image index

IMAGE_SIZE = (18, 12)
plt.figure(figsize=IMAGE_SIZE)
img = Image.fromarray(img_np.astype('uint8'), 'RGB')
x, y = img.size
print(img.size)

fig,ax = plt.subplots(1)
# Display the image
ax.imshow(img_np)

# Draw box and label for each detection 
for detect in image_boxes:
    label = detect['label']
    box = detect['box']
    ymin, xmin, ymax, xmax =  box['topY'], box['topX'], box['bottomY'], box['bottomX']
    topleft_x, topleft_y = x * xmin, y * ymin
    width, height = x * (xmax - xmin), y * (ymax - ymin)
    print('{}: {}, {}, {}, {}'.format(detect['label'], topleft_x, topleft_y, width, height))
    rect = patches.Rectangle((topleft_x, topleft_y), width, height, 
                             linewidth=1, edgecolor='green', facecolor='none')

    ax.add_patch(rect)
    color = 'green'
    plt.text(topleft_x, topleft_y, label, color=color)

plt.show()
```

# [Object detection with YOLO](#tab/object-detect-yolo)

Visualize an input image with boxes and labels

```python
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.pyplot as plt
%matplotlib inline

img_np = mpimg.imread(image_files[1])  # replace with desired image index
image_boxes = bounding_boxes_batch[1]  # replace with desired image index

IMAGE_SIZE = (18, 12)
plt.figure(figsize=IMAGE_SIZE)
img = Image.fromarray(img_np.astype('uint8'), 'RGB')
x, y = img.size
print(img.size)

fig,ax = plt.subplots(1)
# Display the image
ax.imshow(img_np)

# Draw box and label for each detection 
for detect in image_boxes:
    label = detect['label']
    box = detect['box']
    ymin, xmin, ymax, xmax =  box['topY'], box['topX'], box['bottomY'], box['bottomX']
    topleft_x, topleft_y = x * xmin, y * ymin
    width, height = x * (xmax - xmin), y * (ymax - ymin)
    print('{}: {}, {}, {}, {}'.format(detect['label'], topleft_x, topleft_y, width, height))
    rect = patches.Rectangle((topleft_x, topleft_y), width, height, 
                             linewidth=1, edgecolor='green', facecolor='none')

    ax.add_patch(rect)
    color = 'green'
    plt.text(topleft_x, topleft_y, label, color=color)

plt.show()
```
