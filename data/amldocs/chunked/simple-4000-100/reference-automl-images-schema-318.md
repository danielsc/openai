
#### Object detection

Object detection model returns multiple boxes with their scaled top-left and bottom-right coordinates along with box label and confidence score.

```json
[
   {
      "filename": "/tmp/tmpdkg2wkdy",
      "boxes": [
         {
            "box": {
               "topX": 0.224,
               "topY": 0.285,
               "bottomX": 0.399,
               "bottomY": 0.620
            },
            "label": "milk_bottle",
            "score": 0.937
         },
         {
            "box": {
               "topX": 0.664,
               "topY": 0.484,
               "bottomX": 0.959,
               "bottomY": 0.812
            },
            "label": "can",
            "score": 0.891
         },
         {
            "box": {
               "topX": 0.423,
               "topY": 0.253,
               "bottomX": 0.632,
               "bottomY": 0.725
            },
            "label": "water_bottle",
            "score": 0.876
         }
      ]
   }
]
```
#### Instance segmentation

In instance segmentation, output consists of multiple boxes with their scaled top-left and bottom-right coordinates, labels, confidence scores, and polygons (not masks). Here, the polygon values are in the same format that we discussed in the [schema section](#instance-segmentation).

```json
[
    {
       "filename": "/tmp/tmpi8604s0h",
       "boxes": [
          {
             "box": {
                "topX": 0.679,
                "topY": 0.491,
                "bottomX": 0.926,
                "bottomY": 0.810
             },
             "label": "can",
             "score": 0.992,
             "polygon": [
                [
                   0.82, 0.811, 0.771, 0.810, 0.758, 0.805, 0.741, 0.797, 0.735, 0.791, 0.718, 0.785, 0.715, 0.778, 0.706, 0.775, 0.696, 0.758, 0.695, 0.717, 0.698, 0.567, 0.705, 0.552, 0.706, 0.540, 0.725, 0.520, 0.735, 0.505, 0.745, 0.502, 0.755, 0.493
                ]
             ]
          },
          {
             "box": {
                "topX": 0.220,
                "topY": 0.298,
                "bottomX": 0.397,
                "bottomY": 0.601
             },
             "label": "milk_bottle",
             "score": 0.989,
             "polygon": [
                [
                   0.365, 0.602, 0.273, 0.602, 0.26, 0.595, 0.263, 0.588, 0.251, 0.546, 0.248, 0.501, 0.25, 0.485, 0.246, 0.478, 0.245, 0.463, 0.233, 0.442, 0.231, 0.43, 0.226, 0.423, 0.226, 0.408, 0.234, 0.385, 0.241, 0.371, 0.238, 0.345, 0.234, 0.335, 0.233, 0.325, 0.24, 0.305, 0.586, 0.38, 0.592, 0.375, 0.598, 0.365
                ]
             ]
          },
          {
             "box": {
                "topX": 0.433,
                "topY": 0.280,
                "bottomX": 0.621,
                "bottomY": 0.679
             },
             "label": "water_bottle",
             "score": 0.988,
             "polygon": [
                [
                   0.576, 0.680, 0.501, 0.680, 0.475, 0.675, 0.460, 0.625, 0.445, 0.630, 0.443, 0.572, 0.440, 0.560, 0.435, 0.515, 0.431, 0.501, 0.431, 0.433, 0.433, 0.426, 0.445, 0.417, 0.456, 0.407, 0.465, 0.381, 0.468, 0.327, 0.471, 0.318
                ]
             ]
          }
       ]
    }
]
```


## Data format for Online Scoring and Explainability (XAI)

> [!IMPORTANT]
> These settings are currently in public preview. They are provided without a service-level agreement. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

> [!WARNING]
>  **Explainability** is supported only for **multi-class classification** and **multi-label classification**. While generating explanations on online endpoint, if you encounter timeout issues, use [batch scoring notebook](https://github.com/Azure/azureml-examples/tree/main/v1/python-sdk/tutorials/automl-with-azureml/image-classification-multiclass-batch-scoring) to generate explanations.
