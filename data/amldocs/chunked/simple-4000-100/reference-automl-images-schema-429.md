>  **Explainability** is supported only for **multi-class classification** and **multi-label classification**. While generating explanations on online endpoint, if you encounter timeout issues, use [batch scoring notebook](https://github.com/Azure/azureml-examples/tree/main/v1/python-sdk/tutorials/automl-with-azureml/image-classification-multiclass-batch-scoring) to generate explanations.

In this section, we document the input data format required to make predictions and generate explanations for the predicted class/classes using a deployed model. There's no separate deployment needed for explainability. The same endpoint for online scoring can be utilized to generate explanations. We just need to pass some extra explainability related parameters in input schema and get either visualizations of explanations and/or attribution score matrices (pixel level explanations).

### Supported explainability methods:
   - [XRAI](https://arxiv.org/abs/1906.02825) (xrai)
   - [Integrated Gradients](https://arxiv.org/abs/1703.01365) (integrated_gradients)
   - [Guided GradCAM](https://arxiv.org/abs/1610.02391v4) (guided_gradcam)
   - [Guided BackPropagation](https://arxiv.org/abs/1412.6806) (guided_backprop)

### Input format (XAI)

The following input formats are supported to generate predictions and explanations on any classification task using task-specific model endpoint. After we [deploy the model](./how-to-auto-train-image-models.md#register-and-deploy-model), we can use the following schema to get predictions and explanations.

```json
{
   "input_data": {
      "columns": ["image"],
      "data": [json.dumps({"image_base64": "image_in_base64_string_format", 
                           "model_explainability": True,
                           "xai_parameters": {}
                         })
      ]
   }
}
```

Along with the image, there are two extra parameters (`model_explainability` and `xai_parameters`) required in the input schema to generate explanations.

| Key       | Description  | Default Value |
| -------- |----------|-----|
| `image_base64` | input image in base64 format<br>`Required, String` | - |
| `model_explainability` | Whether to generate explanations or just the scoring<br>`Optional, Bool` | `False` |
| `xai_parameters` | If `model_explainability` is True, then `xai_parameters` is a dictionary containing  explainability algorithm related parameters with `xai_algorithm`, `visualizations`, `attributions` ask keys. <br>`Optional, Dictionary` <br> If `xai_parameters` isn't passed, then the `xrai` explainability algorithm is used with its default value| `{"xai_algorithm": "xrai", "visualizations": True, "attributions": False}` |
| `xai_algorithm` | Name of the Explainability algorithm to be used. Supported XAI algorithms are {`xrai`, `integrated_gradients`, `guided_gradcam`, `guided_backprop`}<br>`Optional, String`| `xrai` |
| `visualizations` | Whether to return visualizations of explanations. <br>`Optional, Bool`| `True` |
| `attributions` | Whether to return feature attributions. <br>`Optional, Bool`| `False` |
| `confidence_score_threshold_multilabel` | Confidence score threshold to select top classes to generate explanations in **multi-label classification**. <br>`Optional, Float`| `0.5` |

Following table describes the supported schemas for explainability.

|Type | Schema |
|---|----|
|Inference on single image in base64 format | Dictionary with `image_base64` as key and value is base64 encoded image, <br> `model_explainability` key with True or False and `xai_parameters` dictionary with XAI algorithm specific parameters <br> `Required, Json String` <br> `Works for one or more images`  |

Each input image in the `request_json`, defined in the code below, is a base64 encoded string appended to the list `request_json["input_data"]["data"]`:

```python
import base64
import json
# Get the details for online endpoint
endpoint = ml_client.online_endpoints.get(name=online_endpoint_name)

sample_image = "./test_image.jpg"

# Define explainability (XAI) parameters
model_explainability = True
xai_parameters = {"xai_algorithm": "xrai",
                  "visualizations": True,
                  "attributions": False}

def read_image(image_path):
    with open(image_path, "rb") as f:
        return f.read()

# Create request json
request_json = {

    "input_data": {
        "columns": ["image"],
        "data": [json.dumps({"image_base64": base64.encodebytes(read_image(sample_image)).decode("utf-8"),
                             "model_explainability": model_explainability,
                             "xai_parameters": xai_parameters})],
    }
}

request_file_name = "sample_request_data.json"

with open(request_file_name, "w") as request_file:
    json.dump(request_json, request_file)

resp = ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name=deployment.name,
    request_file=request_file_name,
)
predictions = json.loads(resp)
```
