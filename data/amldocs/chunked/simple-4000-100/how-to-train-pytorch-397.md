
Create a function to format and resize the image.

```python
# install torch and torchvision if needed
%pip install torch
%pip install torchvision

import torch
from torchvision import transforms


def preprocess(image_file):
    """Preprocess the input image."""
    data_transforms = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )

    image = Image.open(image_file)
    image = data_transforms(image).float()
    image = torch.tensor(image)
    image = image.unsqueeze(0)
    return image.numpy()
```

Format the image and convert it to a JSON file.

```python
image_data = preprocess("test_img.jpg")
input_data = json.dumps({"data": image_data.tolist()})
with open("request.json", "w") as outfile:
    outfile.write(input_data)
```

You can then invoke the endpoint with this JSON and print the result.

```python
# test the blue deployment
result = ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    request_file="request.json",
    deployment_name=online_deployment_name,
)

print(result)
```

### Clean up resources

If you won't be using the endpoint, delete it to stop using the resource. Make sure no other deployments are using the endpoint before you delete it.

```python
ml_client.online_endpoints.begin_delete(name=online_endpoint_name)
```

> [!NOTE]
> Expect this cleanup to take a bit of time to finish.


## Next steps

In this article, you trained and registered a deep learning neural network using PyTorch on Azure Machine Learning. You also deployed the model to an online endpoint. See these other articles to learn more about Azure Machine Learning.

- [Track run metrics during training](how-to-log-view-metrics.md)
- [Tune hyperparameters](how-to-tune-hyperparameters.md)
- [Reference architecture for distributed deep learning training in Azure](/azure/architecture/reference-architectures/ai/training-deep-learning)
