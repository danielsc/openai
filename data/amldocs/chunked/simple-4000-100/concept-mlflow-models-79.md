Considering the variety of machine learning frameworks available to use, MLflow introduced the concept of flavor as a way to provide a unique contract to work across all of them. A flavor indicates what to expect for a given model created with a specific framework. For instance, TensorFlow has its own flavor, which specifies how a TensorFlow model should be persisted and loaded. Because each model flavor indicates how they want to persist and load models, the MLModel format doesn't enforce a single serialization mechanism that all the models need to support. Such decision allows each flavor to use the methods that provide the best performance or best support according to their best practices - without compromising compatibility with the MLModel standard.

The following is an example of the `flavors` section for an `fastai` model.

```yaml
flavors:
  fastai:
    data: model.fastai
    fastai_version: 2.4.1
  python_function:
    data: model.fastai
    env: conda.yaml
    loader_module: mlflow.fastai
    python_version: 3.8.12
```

### Signatures

[Model signatures in MLflow](https://www.mlflow.org/docs/latest/models.html#model-signature) are an important part of the model specification, as they serve as a data contract between the model and the server running our models. They are also important for parsing and enforcing model's input's types at deployment time. [MLflow enforces types when data is submitted to your model if a signature is available](https://www.mlflow.org/docs/latest/models.html#signature-enforcement).

Signatures are indicated when the model gets logged and persisted in the `MLmodel` file, in the `signature` section. **Autolog's** feature in MLflow automatically infers signatures in a best effort way. However, it may be required to [log the models manually if the signatures inferred are not the ones you need](https://www.mlflow.org/docs/latest/models.html#how-to-log-models-with-signatures). 

There are two types of signatures:

* **Column-based signature** corresponding to signatures that operate to tabular data. For models with this signature, MLflow supplies `pandas.DataFrame` objects as inputs.
* **Tensor-based signature:** corresponding to signatures that operate with n-dimensional arrays or tensors. For models with this signature, MLflow supplies `numpy.ndarray` as inputs (or a dictionary of `numpy.ndarray` in the case of named-tensors).

The following example corresponds to a computer vision model trained with `fastai`. This model receives a batch of images represented as tensors of shape `(300, 300, 3)` with the RGB representation of them (unsigned integers). It outputs batches of predictions (probabilities) for two classes. 

__MLmodel__

```yaml
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

> [!TIP]
> Azure Machine Learning generates Swagger for model's deployment in MLflow format with a signature available. This makes easier to test deployed endpoints using the Azure ML studio.

### Model's environment

Requirements for the model to run are specified in the `conda.yaml` file. Dependencies can be automatically detected by MLflow or they can be manually indicated when you call `mlflow.<flavor>.log_model()` method. The latter can be needed in cases that the libraries included in your environment are not the ones you intended to use.

The following is an example of an environment used for a model created with `fastai` framework:

__conda.yaml__

```yaml
channels:
- conda-forge
dependencies:
- python=3.8.5
- pip
- pip:
  - mlflow
  - astunparse==1.6.3
  - cffi==1.15.0
  - configparser==3.7.4
  - defusedxml==0.7.1
  - fastai==2.4.1
  - google-api-core==2.7.1
  - ipython==8.2.0
  - psutil==5.9.0
name: mlflow-env
```

> [!NOTE]
> MLflow environments and Azure Machine Learning environments are different concepts. While the former opperates at the level of the model, the latter operates at the level of the workspace (for registered environments) or jobs/deployments (for annonymous environments). When you deploy MLflow models in Azure Machine Learning, the model's environment is built and used for deployment. Alternatively, you can override this behaviour with the [Azure ML CLI v2](concept-v2.md) and deploy MLflow models using a specific Azure Machine Learning environments.
