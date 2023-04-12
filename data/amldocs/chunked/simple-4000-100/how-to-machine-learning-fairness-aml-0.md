
# Use Azure Machine Learning with the Fairlearn open-source package to assess the fairness of ML models (preview)

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

In this how-to guide, you will learn to use the [Fairlearn](https://fairlearn.github.io/) open-source Python package with Azure Machine Learning to perform the following tasks:

* Assess the fairness of your model predictions. To learn more about fairness in machine learning, see the [fairness in machine learning article](concept-fairness-ml.md).
* Upload, list and download fairness assessment insights to/from Azure Machine Learning studio.
* See a fairness assessment dashboard in Azure Machine Learning studio to interact with your model(s)' fairness insights.

>[!NOTE]
> Fairness assessment is not a purely technical exercise. **This package can help you assess the fairness of a machine learning model, but only you can configure and make decisions as to how the model performs.**  While this package helps to identify quantitative metrics to assess fairness, developers of machine learning models must also perform a qualitative analysis to evaluate the fairness of their own models.

## Azure Machine Learning Fairness SDK 

The Azure Machine Learning Fairness SDK, `azureml-contrib-fairness`, integrates the open-source Python package, [Fairlearn](http://fairlearn.github.io),
within Azure Machine Learning. To learn more about Fairlearn's integration within Azure Machine Learning, check out these [sample notebooks](https://github.com/Azure/MachineLearningNotebooks/tree/master/contrib/fairness). For more information on Fairlearn, see the [example guide](https://fairlearn.org/main/auto_examples/) and [sample notebooks](https://github.com/fairlearn/fairlearn/tree/master/notebooks). 

Use the following commands to install the `azureml-contrib-fairness` and `fairlearn` packages:
```bash
pip install azureml-contrib-fairness
pip install fairlearn==0.4.6
```
Later versions of Fairlearn should also work in the following example code.



## Upload fairness insights for a single model

The following example shows how to use the fairness package. We will upload model fairness insights into Azure Machine Learning and see the fairness assessment dashboard in Azure Machine Learning studio.

1. Train a sample model in Jupyter Notebook. 

    For the dataset, we use the well-known adult census dataset, which we fetch from OpenML. We pretend we have a loan decision problem with the label indicating whether an individual repaid a previous loan. We will train a model to predict if previously unseen individuals will repay a loan. Such a model might be used in making loan decisions.

    ```python
    import copy
    import numpy as np
    import pandas as pd

    from sklearn.compose import ColumnTransformer
    from sklearn.datasets import fetch_openml
    from sklearn.impute import SimpleImputer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import make_column_selector as selector
    from sklearn.pipeline import Pipeline
    
    from raiwidgets import FairnessDashboard

    # Load the census dataset
    data = fetch_openml(data_id=1590, as_frame=True)
    X_raw = data.data
    y = (data.target == ">50K") * 1
    
    # (Optional) Separate the "sex" and "race" sensitive features out and drop them from the main data prior to training your model
    X_raw = data.data
    y = (data.target == ">50K") * 1
    A = X_raw[["race", "sex"]]
    X = X_raw.drop(labels=['sex', 'race'],axis = 1)
    
    # Split the data in "train" and "test" sets
    (X_train, X_test, y_train, y_test, A_train, A_test) = train_test_split(
        X_raw, y, A, test_size=0.3, random_state=12345, stratify=y
    )

    # Ensure indices are aligned between X, y and A,
    # after all the slicing and splitting of DataFrames
    # and Series
    X_train = X_train.reset_index(drop=True)
    X_test = X_test.reset_index(drop=True)
    y_train = y_train.reset_index(drop=True)
    y_test = y_test.reset_index(drop=True)
    A_train = A_train.reset_index(drop=True)
    A_test = A_test.reset_index(drop=True)

    # Define a processing pipeline. This happens after the split to avoid data leakage
    numeric_transformer = Pipeline(
        steps=[
            ("impute", SimpleImputer()),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_transformer = Pipeline(
        [
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("ohe", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, selector(dtype_exclude="category")),
            ("cat", categorical_transformer, selector(dtype_include="category")),
        ]
    )

    # Put an estimator onto the end of the pipeline
    lr_predictor = Pipeline(
        steps=[
            ("preprocessor", copy.deepcopy(preprocessor)),
            (
                "classifier",
                LogisticRegression(solver="liblinear", fit_intercept=True),
            ),
        ]
    )

    # Train the model on the test data
    lr_predictor.fit(X_train, y_train)

    # (Optional) View this model in the fairness dashboard, and see the disparities which appear:
    from raiwidgets import FairnessDashboard
    FairnessDashboard(sensitive_features=A_test,
                      y_true=y_test,
                      y_pred={"lr_model": lr_predictor.predict(X_test)})
    ```
