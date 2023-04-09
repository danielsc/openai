---
title: 'CLI (v2) Automated ML Image Instance Segmentation job YAML schema'
titleSuffix: Azure Machine Learning
description: Reference documentation for the CLI (v2) Automated ML Image Instance Segmentation job YAML schema.
services: machine-learning
ms.service: machine-learning
ms.subservice: core
ms.topic: reference
ms.custom: cliv2, event-tier1-ignite-2022

ms.author: shoja
author: shouryaj
ms.date: 10/11/2022
ms.reviewer: ssalgado
---

# CLI (v2) Automated ML image instance segmentation job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLImageInstanceSegmentationJob.schema.json.


[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

For information on all the keys in Yaml syntax, see [Yaml syntax](./reference-automl-images-cli-classification.md#yaml-syntax) of image classification task. Here we only describe the keys that have different values as compared to what's specified for image classification task.

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `task` | const | **Required.** The type of AutoML task. | `image_instance_segmentation` | `image_instance_segmentation` |
| `primary_metric` | string |  The metric that AutoML will optimize for model selection. |`mean_average_precision` | `mean_average_precision` |
| `training_parameters` | object | Dictionary containing training parameters for the job. Provide an object that has keys as listed in following sections. <br> - [Model specific hyperparameters](./reference-automl-images-hyperparameters.md#model-specific-hyperparameters) for maskrcnn_* (if you're using maskrcnn_* for instance segmentation) <br> - [Model agnostic hyperparameters](./reference-automl-images-hyperparameters.md#model-agnostic-hyperparameters) <br> - [Object detection and instance segmentation task specific hyperparameters](./reference-automl-images-hyperparameters.md#object-detection-and-instance-segmentation-task-specific-hyperparameters). <br> <br> For an example, see [Supported model architectures](./how-to-auto-train-image-models.md?tabs=cli#supported-model-architectures) section.| | |

## Remarks

The `az ml job` command can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Examples relevant to image instance segmentation job are shown below.

## YAML: AutoML image instance segmentation job

:::code language="yaml" source="~/azureml-examples-main/cli/jobs/automl-standalone-jobs/cli-automl-image-instance-segmentation-task-fridge-items/cli-automl-image-instance-segmentation-task-fridge-items.yml":::

## YAML: AutoML image instance segmentation pipeline job

:::code language="yaml" source="~/azureml-examples-main/cli/jobs/pipelines/automl/image-instance-segmentation-task-fridge-items-pipeline/pipeline.yml":::

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
