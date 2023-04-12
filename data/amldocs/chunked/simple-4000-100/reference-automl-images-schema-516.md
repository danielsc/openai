### Output format (XAI)

Predictions made on model endpoints follow different schema depending on the task type. This section describes the output data formats for multi-class, multi-label image classification tasks.

The following schemas are defined for the case of two input images.

#### Image classification (binary/multi-class)
Output schema is [same as described above](#data-schema-for-online-scoring) except that `visualizations` and `attributions` key values won't be `None`, if these keys were set to `True` in the request.

If `model_explainability`, `visualizations`, `attributions` are set to `True` in the input request, then the output will have `visualizations` and `attributions`. More details on these parameters are explained in the following table. Visualizations and attributions are generated against a class that has the highest probability score.  

| Output key | Description  |
|--------- |------------- |
|`visualizations` |Single image in base64 string format with type <br> `Optional, String` |
|`attributions` | multi-dimensional array with pixel wise attribution scores of shape `[3, valid_crop_size, valid_crop_size]` <br> `Optional, List`|



```json
[
    {
       "filename": "/tmp/tmp7lqqp4pt/tmp7xmop_j8",
       "probs": [
          0.006,
          9.345e-05,
          0.992,
          0.003
       ],
       "labels": [
          "can",
          "carton",
          "milk_bottle",
          "water_bottle"
       ],
       "visualizations": "iVBORw0KGgoAAAAN.....",
       "attributions": [[[-4.2969e-04, -1.3090e-03,  7.7791e-04,  ...,  2.6677e-04,
                          -5.5195e-03,  1.7989e-03],
                          .
                          .
                          .
                         [-5.8236e-03, -7.9108e-04, -2.6963e-03,  ...,  2.6517e-03,
                           1.2546e-03,  6.6507e-04]]]
    }
]
```

#### Image classification multi-label
The only difference in the output schema of **multi-label classification** compared to **multi-class classification** is that there can be multiple classes in each image for which explanations can be generated. So, `visualizations` is the list of base64 image strings and `attributions` is the list of attribution scores against each selected class based on the `confidence_score_threshold_multilabel` (default is 0.5).

If `model_explainability`, `visualizations`, `attributions` are set to `True` in the input request, then the output will have `visualizations` and `attributions`. More details on these parameters are explained in the following table. Visualizations and attributions are generated against all the classes that have the probability score greater than or equal to `confidence_score_threshold_multilabel`. 

| Output key | Description  |
|--------- |------------- |
|`visualizations` |List of images in base64 string format with type <br> `Optional, String` |
|`attributions` | List of multi-dimensional arrays with pixel wise attribution scores against each class, where each multi-dimensional array is of shape `[3, valid_crop_size, valid_crop_size]` <br> `Optional, List`|


> [!WARNING]
> While generating explanations on online endpoint, make sure to select only few classes based on confidence score in order to avoid timeout issues on the endpoint or use the endpoint with GPU instance type. To generate explanations for large number of classes in multi-label classification, refer to [batch scoring notebook](https://github.com/Azure/azureml-examples/tree/main/v1/python-sdk/tutorials/automl-with-azureml/image-classification-multiclass-batch-scoring).

```json
[
    {
       "filename": "/tmp/tmp_9zieom3/tmp6threa9_",
       "probs": [
          0.994,
          0.994,
          0.843,
          0.166
       ],
       "labels": [
          "can",
          "carton",
          "milk_bottle",
          "water_bottle"
       ],
       "visualizations": ["iVBORw0KGgoAAAAN.....", "iVBORw0KGgoAAAAN......", .....],
       "attributions": [
                        [[[-4.2969e-04, -1.3090e-03,  7.7791e-04,  ...,  2.6677e-04,
                           -5.5195e-03,  1.7989e-03],
                           .
                           .
                           .
                          [-5.8236e-03, -7.9108e-04, -2.6963e-03,  ...,  2.6517e-03,
                            1.2546e-03,  6.6507e-04]]],
                        .
                        .
                        .
                       ]
    }
]
```
