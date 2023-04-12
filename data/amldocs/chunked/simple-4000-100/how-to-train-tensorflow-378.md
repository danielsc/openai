
Once you've created the endpoint, you can retrieve it as follows:

```python
endpoint = ml_client.online_endpoints.get(name=online_endpoint_name)

print(
    f'Endpint "{endpoint.name}" with provisioning state "{endpoint.provisioning_state}" is retrieved'
)
```

### Deploy the model to the endpoint

After you've created the endpoint, you can deploy the model with the entry script. An endpoint can have multiple deployments. Using rules, the endpoint can then direct traffic to these deployments.

In the following code, you'll create a single deployment that handles 100% of the incoming traffic. We've specified an arbitrary color name (*tff-blue*) for the deployment. You could also use any other name such as *tff-green* or *tff-red* for the deployment.
The code to deploy the model to the endpoint does the following:

- deploys the best version of the model that you registered earlier;
- scores the model, using the `score.py` file; and
- uses the same curated environment (that you declared earlier) to perform inferencing.

```python
model = registered_model

from azure.ai.ml.entities import CodeConfiguration

# create an online deployment.
blue_deployment = ManagedOnlineDeployment(
    name="tff-blue",
    endpoint_name=online_endpoint_name,
    model=model,
    code_configuration=CodeConfiguration(code="./src", scoring_script="score.py"),
    environment=curated_env_name,
    instance_type="Standard_DS3_v2",
    instance_count=1,
)

blue_deployment = ml_client.begin_create_or_update(blue_deployment).result()
```

> [!NOTE]
> Expect this deployment to take a bit of time to finish.

### Test the deployment with a sample query

Now that you've deployed the model to the endpoint, you can predict the output of the deployed model, using the `invoke` method on the endpoint. To run the inference, use the sample request file `sample-request.json` from the *request* folder.

```python
# # predict using the deployed model
result = ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    request_file="./request/sample-request.json",
    deployment_name="tff-blue",
)
```

You can then print the returned predictions and plot them along with the input images. Use red font color and inverted image (white on black) to highlight the misclassified samples.

```python
# compare actual value vs. the predicted values:
import matplotlib.pyplot as plt

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

In this article, you trained and registered a TensorFlow model. You also deployed the model to an online endpoint. See these other articles to learn more about Azure Machine Learning.

- [Track run metrics during training](how-to-log-view-metrics.md)
- [Tune hyperparameters](how-to-tune-hyperparameters.md)
- [Reference architecture for distributed deep learning training in Azure](/azure/architecture/reference-architectures/ai/training-deep-learning)