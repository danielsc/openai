
Load these into a test dataset.

```python
from src.utils import load_data

X_test = load_data(os.path.join(data_folder, "t10k-images-idx3-ubyte.gz"), False)
y_test = load_data(
    os.path.join(data_folder, "t10k-labels-idx1-ubyte.gz"), True
).reshape(-1)
```

Pick 30 random samples from the test set and write them to a JSON file.

```python
import json
import numpy as np

# find 30 random samples from test set
n = 30
sample_indices = np.random.permutation(X_test.shape[0])[0:n]

test_samples = json.dumps({"input_data": X_test[sample_indices].tolist()})
# test_samples = bytes(test_samples, encoding='utf8')

with open("request.json", "w") as outfile:
    outfile.write(test_samples)
```

You can then invoke the endpoint, print the returned predictions, and plot them along with the input images. Use red font color and inverted image (white on black) to highlight the misclassified samples.

```python
import matplotlib.pyplot as plt

# predict using the deployed model
result = ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    request_file="./request.json",
    deployment_name="keras-blue-deployment",
)

# compare actual value vs. the predicted values:
i = 0
plt.figure(figsize=(20, 1))

for s in sample_indices:
    plt.subplot(1, n, i + 1)
    plt.axhline("")
    plt.axvline("")

    # use different color for misclassified sample
    font_color = "red" if y_test[s] != result[i] else "black"
    clr_map = plt.cm.gray if y_test[s] != result[i] else plt.cm.Greys

    plt.text(x=10, y=-10, s=result[i], fontsize=18, color=font_color)
    plt.imshow(X_test[s].reshape(28, 28), cmap=clr_map)

    i = i + 1
plt.show()
```


> [!NOTE]
> Because the model accuracy is high, you might have to run the cell a few times before seeing a misclassified sample.

### Clean up resources

If you won't be using the endpoint, delete it to stop using the resource. Make sure no other deployments are using the endpoint before you delete it.

```python
ml_client.online_endpoints.begin_delete(name=online_endpoint_name)
```

> [!NOTE]
> Expect this cleanup to take a bit of time to finish.


## Next steps

In this article, you trained and registered a Keras model. You also deployed the model to an online endpoint. See these other articles to learn more about Azure Machine Learning.

- [Track run metrics during training](how-to-log-view-metrics.md)
- [Tune hyperparameters](how-to-tune-hyperparameters.md)
- [Reference architecture for distributed deep learning training in Azure](/azure/architecture/reference-architectures/ai/training-deep-learning)