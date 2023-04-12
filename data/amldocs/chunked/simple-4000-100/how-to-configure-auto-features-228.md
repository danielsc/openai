To understand the scaling/normalization and the selected algorithm with its hyperparameter values, use `fitted_model.steps`. 

The following sample output is from running `fitted_model.steps` for a chosen run:

```
[('RobustScaler', 
  RobustScaler(copy=True, 
  quantile_range=[10, 90], 
  with_centering=True, 
  with_scaling=True)), 

  ('LogisticRegression', 
  LogisticRegression(C=0.18420699693267145, class_weight='balanced', 
  dual=False, 
  fit_intercept=True, 
  intercept_scaling=1, 
  max_iter=100, 
  multi_class='multinomial', 
  n_jobs=1, penalty='l2', 
  random_state=None, 
  solver='newton-cg', 
  tol=0.0001, 
  verbose=0, 
  warm_start=False))
```

To get more details, use this helper function: 

```python
from pprint import pprint

def print_model(model, prefix=""):
    for step in model.steps:
        print(prefix + step[0])
        if hasattr(step[1], 'estimators') and hasattr(step[1], 'weights'):
            pprint({'estimators': list(e[0] for e in step[1].estimators), 'weights': step[1].weights})
            print()
            for estimator in step[1].estimators:
                print_model(estimator[1], estimator[0]+ ' - ')
        elif hasattr(step[1], '_base_learners') and hasattr(step[1], '_meta_learner'):
            print("\nMeta Learner")
            pprint(step[1]._meta_learner)
            print()
            for estimator in step[1]._base_learners:
                print_model(estimator[1], estimator[0]+ ' - ')
        else:
            pprint(step[1].get_params())
            print()   
```

This helper function returns the following output for a particular run using `LogisticRegression with RobustScalar` as the specific algorithm.

```
RobustScaler
{'copy': True,
'quantile_range': [10, 90],
'with_centering': True,
'with_scaling': True}

LogisticRegression
{'C': 0.18420699693267145,
'class_weight': 'balanced',
'dual': False,
'fit_intercept': True,
'intercept_scaling': 1,
'max_iter': 100,
'multi_class': 'multinomial',
'n_jobs': 1,
'penalty': 'l2',
'random_state': None,
'solver': 'newton-cg',
'tol': 0.0001,
'verbose': 0,
'warm_start': False}
```

### Predict class probability

Models produced using automated ML all have wrapper objects that mirror functionality from their open-source origin class. Most classification model wrapper objects returned by automated ML implement the `predict_proba()` function, which accepts an array-like or sparse matrix data sample of your features (X values), and returns an n-dimensional array of each sample and its respective class probability.

Assuming you have retrieved the best run and fitted model using the same calls from above, you can call `predict_proba()` directly from the fitted model, supplying an `X_test` sample in the appropriate format depending on the model type.

```python
best_run, fitted_model = automl_run.get_output()
class_prob = fitted_model.predict_proba(X_test)
```

If the underlying model does not support the `predict_proba()` function or the format is incorrect, a model class-specific exception will be thrown. See the [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.predict_proba) and [XGBoost](https://xgboost.readthedocs.io/en/latest/python/python_api.html) reference docs for examples of how this function is implemented for different model types.

<a name="bert-integration"></a>

## BERT integration in automated ML

[BERT](https://techcommunity.microsoft.com/t5/azure-ai/how-bert-is-integrated-into-azure-automated-machine-learning/ba-p/1194657) is used in the featurization layer of automated ML. In this layer, if a column contains free text or other types of data like timestamps or simple numbers, then featurization is applied accordingly.

For BERT, the model is fine-tuned and trained utilizing the user-provided labels. From here, document embeddings are output as features alongside others, like timestamp-based features, day of week. 
