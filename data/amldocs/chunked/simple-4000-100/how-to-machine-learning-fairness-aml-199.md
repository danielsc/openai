    1. Select a particular experiment to view all the runs in that experiment.
    1. Select a run, and then the **Fairness** tab to the explanation visualization dashboard.
    1. Once landing on the **Fairness** tab, click on a **fairness id** from the menu on the right.
    1. Configure your dashboard by selecting your sensitive attribute, performance metric, and fairness metric of interest to land on the fairness assessment page.
    1. Switch chart type from one to another to observe both **allocation** harms and **quality of service** harms.



    [![Fairness Dashboard Allocation](./media/how-to-machine-learning-fairness-aml/dashboard-1.png)](./media/how-to-machine-learning-fairness-aml/dashboard-1.png#lightbox)
    
    [![Fairness Dashboard Quality of Service](./media/how-to-machine-learning-fairness-aml/dashboard-2.png)](./media/how-to-machine-learning-fairness-aml/dashboard-2.png#lightbox)
    * **Models pane**
    1. If you registered your original model by following the previous steps, you can select **Models** in the left pane to view it.
    1. Select a model, and then the **Fairness** tab to view the explanation visualization dashboard.

    To learn more about the visualization dashboard and what it contains, check out Fairlearn's [user guide](https://fairlearn.org/main/user_guide/assessment/index.html#fairlearn-dashboard).

## Upload fairness insights for multiple models

To compare multiple models and see how their fairness assessments differ, you can pass more than one model to the visualization dashboard and compare their performance-fairness trade-offs.

1. Train your models:
    
    We now create a second classifier, based on a Support Vector Machine estimator, and upload a fairness dashboard dictionary using Fairlearn's `metrics` package. We assume that the previously trained model is still available.


    ```python
    # Put an SVM predictor onto the preprocessing pipeline
    from sklearn import svm
    svm_predictor = Pipeline(
        steps=[
            ("preprocessor", copy.deepcopy(preprocessor)),
            (
                "classifier",
                svm.SVC(),
            ),
        ]
    )

    # Train your second classification model
    svm_predictor.fit(X_train, y_train)
    ```

2. Register your models

    Next register both models within Azure Machine Learning. For convenience, store the results in a dictionary, which maps the `id` of the registered model (a string in `name:version` format) to the predictor itself:

    ```python
    model_dict = {}

    lr_reg_id = register_model("fairness_logistic_regression", lr_predictor)
    model_dict[lr_reg_id] = lr_predictor

    svm_reg_id = register_model("fairness_svm", svm_predictor)
    model_dict[svm_reg_id] = svm_predictor
    ```

3. Load the Fairness dashboard locally

    Before uploading the fairness insights into Azure Machine Learning, you can examine these predictions in a locally invoked Fairness dashboard. 



    ```python
    #  Generate models' predictions and load the fairness dashboard locally 
    ys_pred = {}
    for n, p in model_dict.items():
        ys_pred[n] = p.predict(X_test)

    from raiwidgets import FairnessDashboard

    FairnessDashboard(sensitive_features=A_test,
                      y_true=y_test.tolist(),
                      y_pred=ys_pred)
    ```

3. Precompute fairness metrics.

    Create a dashboard dictionary using Fairlearn's `metrics` package.

    ```python
    sf = { 'Race': A_test.race, 'Sex': A_test.sex }

    from fairlearn.metrics._group_metric_set import _create_group_metric_set

    dash_dict = _create_group_metric_set(y_true=Y_test,
                                        predictions=ys_pred,
                                        sensitive_features=sf,
                                        prediction_type='binary_classification')
    ```
4. Upload the precomputed fairness metrics.
    
    Now, import `azureml.contrib.fairness` package to perform the upload:

    ```python
    from azureml.contrib.fairness import upload_dashboard_dictionary, download_dashboard_by_upload_id
    ```
