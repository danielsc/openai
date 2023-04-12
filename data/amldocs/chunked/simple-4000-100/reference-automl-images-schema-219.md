
![Image example for instance segmentation.](media/reference-automl-images-schema/instance-segmentation-predictions.jpg)

## Data schema for online scoring

In this section, we document the input data format required to make predictions using a deployed model.

### Input format

The following JSON is the input format needed to generate predictions on any task using task-specific model endpoint.

```json
{
   "input_data": {
      "columns": [
         "image"
      ],
      "data": [
         "image_in_base64_string_format"
      ]
   }
}
```

This json is a dictionary with outer key `input_data` and inner keys `columns`, `data` as described in the following table. The endpoint accepts a json string in the above format and converts it into a dataframe of samples required by the scoring script. Each input image in the `request_json["input_data"]["data"]` section of the json is a [base64 encoded string](https://docs.python.org/3/library/base64.html#base64.encodebytes).


| Key       | Description  |
| -------- |----------|
| `input_data`<br> (outer key) | It's an outer key in json request. `input_data` is a dictionary that accepts input image samples <br>`Required, Dictionary` |
| `columns`<br> (inner key) | Column names to use to create dataframe. It accepts only one column with `image` as column name.<br>`Required, List` |
| `data`<br> (inner key) | List of base64 encoded images <br>`Required, List`|


After we [deploy the mlflow model](how-to-auto-train-image-models.md#register-and-deploy-model), we can use the following code snippet to get predictions for all tasks.

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=create_inference_request)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=dump_inference_request)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=invoke_inference)]

### Output format

Predictions made on model endpoints follow different structure depending on the task type. This section explores the output data formats for multi-class, multi-label image classification, object detection, and instance segmentation tasks.

The following schemas are applicable when the input request contains one image.

#### Image classification (binary/multi-class)

Endpoint for image classification returns all the labels in the dataset and their probability scores for the input image in the following format.  `visualizations` and `attributions` are related to explainability and when the request is only for scoring, values for these keys will always be None. For more information on explainability input and output schema for image classification, see the [explainability for image classification section](#image-classification-binarymulti-class-2).

```json
[
   {
      "filename": "/tmp/tmppjr4et28",
      "probs": [
         2.098e-06,
         4.783e-08,
         0.999,
         8.637e-06
      ],
      "labels": [
         "can",
         "carton",
         "milk_bottle",
         "water_bottle"
      ],
      "visualizations": None,
      "attributions": None
   }
]
```

#### Image classification multi-label

For image classification multi-label, model endpoint returns labels and their probabilities. `visualizations` and `attributions` are related to explainability and when the request is only for scoring, values for these keys will always be None. For more information on explainability input and output schema for multi-label classification, see the [explainability for image classification multi-label section](#image-classification-multi-label-2).

```json
[
   {
      "filename": "/tmp/tmpsdzxlmlm",
      "probs": [
         0.997,
         0.960,
         0.982,
         0.025
      ],
      "labels": [
         "can",
         "carton",
         "milk_bottle",
         "water_bottle"
      ],
      "visualizations": None,
      "attributions": None
   }
]
```
