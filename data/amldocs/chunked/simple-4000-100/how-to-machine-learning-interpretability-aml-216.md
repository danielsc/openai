
## Generate feature importance values via remote runs

The following example shows how you can use the `ExplanationClient` class to enable model interpretability for remote runs. It’s conceptually similar to the local process, except you:

* Use the `ExplanationClient` in the remote run to upload the interpretability context.
* Download the context later in a local environment.

1. Install the `azureml-interpret` package.
    ```bash
    pip install azureml-interpret
    ```
1. Create a training script in a local Jupyter Notebook. For example, `train_explain.py`.

    ```python
    from azureml.interpret import ExplanationClient
    from azureml.core.run import Run
    from interpret.ext.blackbox import TabularExplainer

    run = Run.get_context()
    client = ExplanationClient.from_run(run)

    # write code to get and split your data into train and test sets here
    # write code to train your model here 

    # explain predictions on your local machine
    # "features" and "classes" fields are optional
    explainer = TabularExplainer(model, 
                                 x_train, 
                                 features=feature_names, 
                                 classes=classes)

    # explain overall model predictions (global explanation)
    global_explanation = explainer.explain_global(x_test)
    
    # uploading global model explanation data for storage or visualization in webUX
    # the explanation can then be downloaded on any compute
    # multiple explanations can be uploaded
    client.upload_model_explanation(global_explanation, comment='global explanation: all features')
    # or you can only upload the explanation object with the top k feature info
    #client.upload_model_explanation(global_explanation, top_k=2, comment='global explanation: Only top 2 features')
    ```

1. Set up an Azure Machine Learning Compute as your compute target and submit your training run. See [Create and manage Azure Machine Learning compute clusters](how-to-create-attach-compute-cluster.md) for instructions. You might also find the [example notebooks](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/explain-model/azure-integration/remote-explanation) helpful.

1. Download the explanation in your local Jupyter Notebook.

    ```python
    from azureml.interpret import ExplanationClient
    
    client = ExplanationClient.from_run(run)
    
    # get model explanation data
    explanation = client.download_model_explanation()
    # or only get the top k (e.g., 4) most important features with their importance values
    explanation = client.download_model_explanation(top_k=4)
    
    global_importance_values = explanation.get_ranked_global_values()
    global_importance_names = explanation.get_ranked_global_names()
    print('global importance values: {}'.format(global_importance_values))
    print('global importance names: {}'.format(global_importance_names))
    ```


## Visualizations

After you download the explanations in your local Jupyter Notebook, you can use the visualizations in the explanations dashboard to understand and interpret your model. To load the explanations dashboard widget in your Jupyter Notebook, use the following code:

```python
from raiwidgets import ExplanationDashboard

ExplanationDashboard(global_explanation, model, datasetX=x_test)
```

The visualizations support explanations on both engineered and raw features. Raw explanations are based on the features from the original dataset and engineered explanations are based on the features from the dataset with feature engineering applied.

When attempting to interpret a model with respect to the original dataset, it’s recommended to use raw explanations as each feature importance will correspond to a column from the original dataset. One scenario where engineered explanations might be useful is when examining the impact of individual categories from a categorical feature. If a one-hot encoding is applied to a categorical feature, then the resulting engineered explanations will include a different importance value per category, one per one-hot engineered feature. This encoding can be useful when narrowing down which part of the dataset is most informative to the model.
