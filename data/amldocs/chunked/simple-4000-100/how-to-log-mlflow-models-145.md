
Then, a custom model can be logged in the run like this:

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

signature = infer_signature(X_test, y_probs)
mlflow.pyfunc.log_model("classifier", 
                        python_model=ModelWrapper(model),
                        signature=signature)
```

> [!TIP]
> Note how the `infer_signature` method now uses `y_probs` to infer the signature. Our target column has the target class, but our model now returns the two probabilities for each class.


# [Using artifacts](#tab/artifacts)

Wrapping your model may be simple, but sometimes your model is composed by multiple pieces that need to be loaded or it can't just be serialized as a Pickle file. In those cases, the `PythonModel` supports indicating an arbitrary list of **artifacts**. Each artifact will be packaged along with your model.

Use this method when:
> [!div class="checklist"]
> * Your model can't be serialized in Pickle format or there is a better format available for that.
> * Your model have one or many artifacts that need to be referenced in order to load the model.
> * You may want to persist some inference configuration properties (i.e. number of items to recommend).
> * You want to customize the way the model is loaded and how the `predict` function works.

To log a custom model using artifacts, you can do something as follows:

```python
encoder_path = 'encoder.pkl'
joblib.dump(encoder, encoder_path)

model_path = 'xgb.model'
model.save_model(model_path)

mlflow.pyfunc.log_model("classifier", 
                        python_model=ModelWrapper(),
                        artifacts={ 
                            'encoder': encoder_path,
                            'model': model_path 
                        },
                        signature=signature)
```

> [!NOTE]
> * The model was saved using the save method of the framework used (it's not saved as a pickle).
> * `ModelWrapper()` is the model wrapper, but the model is not passed as a parameter to the constructor.
> A new parameter is indicated, `artifacts`, that is a dictionary with keys as the name of the artifact and values as the path is the local file system where the artifact is stored.

The corresponding model wrapper then would look as follows:

```python
from mlflow.pyfunc import PythonModel, PythonModelContext

class ModelWrapper(PythonModel):
    def load_context(self, context: PythonModelContext):
        import pickle
        from xgboost import XGBClassifier
        from sklearn.preprocessing import OrdinalEncoder
        
        self._encoder = pickle.loads(context.artifacts["encoder"])
        self._model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
        self._model.load_model(context.artifacts["model"])

    def predict(self, context: PythonModelContext, data):
        return self._model.predict_proba(data)
```

The complete training routine would look as follows:

```python
import mlflow
from xgboost import XGBClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
from mlflow.models import infer_signature

mlflow.xgboost.autolog(log_models=False)

encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=np.nan)
X_train['thal'] = encoder.fit_transform(X_train['thal'].to_frame())
X_test['thal'] = encoder.transform(X_test['thal'].to_frame())

model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
y_probs = model.predict_proba(X_test)

accuracy = accuracy_score(y_test, y_probs.argmax(axis=1))
mlflow.log_metric("accuracy", accuracy)

encoder_path = 'encoder.pkl'
joblib.dump(encoder, encoder_path)
model_path = "xgb.model"
model.save_model(model_path)

signature = infer_signature(X, y_probs)
mlflow.pyfunc.log_model("classifier", 
                        python_model=ModelWrapper(),
                        artifacts={ 
                            'encoder': encoder_path,
                            'model': model_path 
                        },
                        signature=signature)
```
