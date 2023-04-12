* `prepare_data_node` loads the image and labels from Fashion MNIST data set into `mnist_train.csv` and `mnist_test.csv`.
* `train_node` trains a CNN model with Keras, using the `mnist_train.csv` training data.
* `score_node` scores the model using `mnist_test.csv` test data.

```python
# define a pipeline containing 3 nodes: Prepare data node, train node, and score node
@pipeline(
    default_compute=cpu_compute_target,
)
def image_classification_keras_minist_convnet(pipeline_input_data):
    """E2E image classification pipeline with keras using python sdk."""
    prepare_data_node = prepare_data_component(input_data=pipeline_input_data)

    train_node = keras_train_component(
        input_data=prepare_data_node.outputs.training_data
    )
    train_node.compute = gpu_compute_target

    score_node = keras_score_component(
        input_data=prepare_data_node.outputs.test_data,
        input_model=train_node.outputs.output_model,
    )


# create a pipeline
pipeline_job = image_classification_keras_minist_convnet(pipeline_input_data=fashion_ds)
```

## Next steps

* [Train models](how-to-train-model.md)
* [Tutorial: Create production ML pipelines with Python SDK v2](tutorial-pipeline-python-sdk.md)
* Learn more about [Data in Azure Machine Learning](concept-data.md)