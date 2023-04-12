
# From artifacts to models in MLflow

The following article explains the differences between an artifact and a model in MLflow and how to transition from one to the other. It also explains how Azure Machine Learning uses the MLflow model's concept to enabled streamlined deployment workflows.

## What's the difference between an artifact and a model?

If you are not familiar with MLflow, you may not be aware of the difference between logging artifacts or files vs. logging MLflow models. There are some fundamental differences between the two:

### Artifacts

Any file generated (and captured) from an experiment's run or job is an artifact. It may represent a model serialized as a Pickle file, the weights of a PyTorch or TensorFlow model, or even a text file containing the coefficients of a linear regression. Other artifacts can have nothing to do with the model itself, but they can contain configuration to run the model, pre-processing information, sample data, etc. As you can see, an artifact can come in any format. 

You may have been logging artifacts already:

```python
filename = 'model.pkl'
with open(filename, 'wb') as f:
  pickle.dump(model, f)

mlflow.log_artifact(filename)
```

### Models

A model in MLflow is also an artifact. However, we make stronger assumptions about this type of artifacts. Such assumptions provide a clear contract between the saved files and what they mean. When you log your models as artifacts (simple files), you need to know what the model builder meant for each of them in order to know how to load the model for inference. On the contrary, MLflow models can be loaded using the contract specified in the [The MLModel format](concept-mlflow-models.md#the-mlmodel-format).

In Azure Machine Learning, logging models has the following advantages:
> [!div class="checklist"]
> * You can deploy them on real-time or batch endpoints without providing an scoring script nor an environment.
> * When deployed, Model's deployments have a Swagger generated automatically and the __Test__ feature can be used in Azure ML studio.
> * Models can be used as pipelines inputs directly.
> * You can use the [Responsible AI dashbord (preview)](how-to-responsible-ai-dashboard.md).

Models can get logged by using MLflow SDK:

```python
import mlflow
mlflow.sklearn.log_model(sklearn_estimator, "classifier")
```


## The MLmodel format

MLflow adopts the MLmodel format as a way to create a contract between the artifacts and what they represent. The MLmodel format stores assets in a folder. Among them, there is a particular file named MLmodel. This file is the single source of truth about how a model can be loaded and used.

![a sample MLflow model in MLmodel format](media/concept-mlflow-models/mlflow-mlmodel.png)

The following example shows how the `MLmodel` file for a computer version model trained with `fastai` may look like:

__MLmodel__

```yaml
artifact_path: classifier
flavors:
  fastai:
    data: model.fastai
    fastai_version: 2.4.1
  python_function:
    data: model.fastai
    env: conda.yaml
    loader_module: mlflow.fastai
    python_version: 3.8.12
model_uuid: e694c68eba484299976b06ab9058f636
run_id: e13da8ac-b1e6-45d4-a9b2-6a0a5cfac537
signature:
  inputs: '[{"type": "tensor",
             "tensor-spec": 
                 {"dtype": "uint8", "shape": [-1, 300, 300, 3]}
           }]'
  outputs: '[{"type": "tensor", 
              "tensor-spec": 
                 {"dtype": "float32", "shape": [-1,2]}
            }]'
```

### The model's flavors

Considering the variety of machine learning frameworks available to use, MLflow introduced the concept of flavor as a way to provide a unique contract to work across all of them. A flavor indicates what to expect for a given model created with a specific framework. For instance, TensorFlow has its own flavor, which specifies how a TensorFlow model should be persisted and loaded. Because each model flavor indicates how they want to persist and load models, the MLModel format doesn't enforce a single serialization mechanism that all the models need to support. Such decision allows each flavor to use the methods that provide the best performance or best support according to their best practices - without compromising compatibility with the MLModel standard.
