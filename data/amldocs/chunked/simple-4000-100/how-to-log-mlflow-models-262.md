
# [Using a model loader](#tab/loader)

Sometimes your model logic is complex and there are several source files that your model loads on inference time. This would be the case when you have a Python library for your model for instance. In this scenario, you want to package the library all along with your model so it can move as a single piece. 

Use this method when:
> [!div class="checklist"]
> * Your model can't be serialized in Pickle format or there is a better format available for that.
> * Your model artifacts can be stored in a folder where all the requiered artifacts are placed.
> * Your model source code is complex and it requires multiple Python files. Potentially, there is a library that supports your model.
> * You want to customize the way the model is loaded and how the `predict` function works.

MLflow supports this kind of models too by allowing you to specify any arbitrary source code to package along with the model as long as it has a *loader module*. Loader modules can be specified in the `log_model()` instruction using the argument `loader_module` which indicates the Python namespace where the loader is implemented. The argument `code_path` is also required, where you indicate the source files where the `loader_module` is defined. You are required to implement in this namespace a function called `_load_pyfunc(data_path: str)` that received the path of the artifacts and returns an object with a method predict (at least).

```python
model_path = 'xgb.model'
model.save_model(model_path)

mlflow.pyfunc.log_model("classifier", 
                        data_path=model_path,
                        code_path=['src'],
                        loader_module='loader_module'
                        signature=signature)
```

> [!NOTE]
> * The model was saved using the save method of the framework used (it's not saved as a pickle).
> * A new parameter, `data_path`, was added pointing to the folder where the model's artifacts are located. This can be a folder or a file. Whatever is on that folder or file, it will be packaged with the model.
> * A new parameter, `code_path`, was added pointing to the location where the source code is placed. This can be a path or a single file. Whatever is on that folder or file, it will be packaged with the model.
> * `loader_module` is the Python module where the function `_load_pyfunc` is defined.

The folder `src` contains a file called `loader_module.py` (which is the loader module):

__src/loader_module.py__

```python
class MyModel():
    def __init__(self, model):
        self._model = model

    def predict(self, data):
        return self._model.predict_proba(data)

def _load_pyfunc(data_path: str):
    import os

    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.load_model(os.path.abspath(data_path))

    return MyModel(model)
```

> [!NOTE]
> * The class `MyModel` doesn't inherits from `PythonModel` as we did before, but it has a `predict` function.
> * The model's source code is on a file. This can be any source code you want. If your project has a folder src, it is a great candidate.
> * We added a function `_load_pyfunc` which returns an instance of the model's class.

The complete training code would look as follows:

```python
import mlflow
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from mlflow.models import infer_signature

mlflow.xgboost.autolog(log_models=False)

model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
y_probs = model.predict_proba(X_test)

accuracy = accuracy_score(y_test, y_probs.argmax(axis=1))
mlflow.log_metric("accuracy", accuracy)

model_path = "xgb.model"
model.save_model(model_path)

signature = infer_signature(X_test, y_probs)
mlflow.pyfunc.log_model("classifier",
                        data_path=model_path,
                        code_path=["loader_module.py"],
                        loader_module="loader_module",
                        signature=signature)
```
