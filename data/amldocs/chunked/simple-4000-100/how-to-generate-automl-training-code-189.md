Any user provided featurizations for time series forecasting models happens before the ones provided by automated ML. 

### Preprocessor specification code

The function `generate_preprocessor_config()`, if present, specifies a preprocessing step to be done after featurization in the final scikit-learn pipeline.

Normally, this preprocessing step only consists of data standardization/normalization that's accomplished with [`sklearn.preprocessing`](https://scikit-learn.org/stable/modules/preprocessing.html).

Automated ML only specifies a preprocessing step for non-ensemble classification and regression models.

Here's an example of a generated preprocessor code:

```python
def generate_preprocessor_config():
    from sklearn.preprocessing import MaxAbsScaler
    
    preproc = MaxAbsScaler(
        copy=True
    )
    
    return preproc
```

### Algorithm and hyperparameters specification code

The algorithm and hyperparameters specification code is likely what many ML professionals are most interested in. 

The `generate_algorithm_config()` function specifies the actual algorithm and hyperparameters for training the model as the last stage of the final scikit-learn pipeline. 

The following example uses an XGBoostClassifier algorithm with specific hyperparameters.

```python
def generate_algorithm_config():
    from xgboost.sklearn import XGBClassifier
    
    algorithm = XGBClassifier(
        base_score=0.5,
        booster='gbtree',
        colsample_bylevel=1,
        colsample_bynode=1,
        colsample_bytree=1,
        gamma=0,
        learning_rate=0.1,
        max_delta_step=0,
        max_depth=3,
        min_child_weight=1,
        missing=numpy.nan,
        n_estimators=100,
        n_jobs=-1,
        nthread=None,
        objective='binary:logistic',
        random_state=0,
        reg_alpha=0,
        reg_lambda=1,
        scale_pos_weight=1,
        seed=None,
        silent=None,
        subsample=1,
        verbosity=0,
        tree_method='auto',
        verbose=-10
    )
    
    return algorithm
```

The generated code in most cases uses open source software (OSS) packages and classes. There are instances where intermediate wrapper classes are used to simplify more complex code. For example, XGBoost classifier and other commonly used libraries like LightGBM or Scikit-Learn algorithms can be applied. 

As an ML Professional, you are able to customize that algorithm's configuration code by tweaking its hyperparameters as needed based on your skills and experience for that algorithm and your particular ML problem.

For ensemble models, `generate_preprocessor_config_N()` (if needed) and `generate_algorithm_config_N()` are defined for each learner in the ensemble model, where `N` represents the placement of each learner in the ensemble model's list. For stack ensemble models, the meta learner `generate_algorithm_config_meta()` is defined.

### End to end training code

Code generation emits `build_model_pipeline()` and `train_model()` for defining the scikit-learn pipeline and for calling `fit()` on it, respectively.

```python
def build_model_pipeline():
    from sklearn.pipeline import Pipeline
    
    logger.info("Running build_model_pipeline")
    pipeline = Pipeline(
        steps=[
            ('featurization', generate_data_transformation_config()),
            ('preproc', generate_preprocessor_config()),
            ('model', generate_algorithm_config()),
        ]
    )
    
    return pipeline
```

The scikit-learn pipeline includes the featurization step, a preprocessor (if used), and the algorithm or model.

For time-series forecasting models, the scikit-learn pipeline is wrapped in a `ForecastingPipelineWrapper`, which has some additional logic needed to properly handle time-series data depending on the applied algorithm.
For all task types, we use `PipelineWithYTransformer` in cases where the label column needs to be encoded.

Once you have the scikit-Learn pipeline, all that is left to call is the `fit()` method to train the model:
