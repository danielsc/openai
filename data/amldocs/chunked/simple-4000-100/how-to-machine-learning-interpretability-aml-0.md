
# Use the Python interpretability package to explain ML models & predictions (preview)

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

In this how-to guide, you learn to use the interpretability package of the Azure Machine Learning Python SDK to perform the following tasks:


* Explain the entire model behavior or individual predictions on your personal machine locally.

* Enable interpretability techniques for engineered features.

* Explain the behavior for the entire model and individual predictions in Azure.

* Upload explanations to Azure Machine Learning Run History.

* Use a visualization dashboard to interact with your model explanations, both in a Jupyter Notebook and in the Azure Machine Learning studio.

* Deploy a scoring explainer alongside your model to observe explanations during inferencing.


For more information on the supported interpretability techniques and machine learning models, see [Model interpretability in Azure Machine Learning](how-to-machine-learning-interpretability.md) and [sample notebooks](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/explain-model).

For guidance on how to enable interpretability for models trained with automated machine learning see, [Interpretability: model explanations for automated machine learning models (preview)](how-to-machine-learning-interpretability-automl.md). 

## Generate feature importance value on your personal machine 
The following example shows how to use the interpretability package on your personal machine without contacting Azure services.

1. Install the `azureml-interpret` package.
    ```bash
    pip install azureml-interpret
    ```

2. Train a sample model in a local Jupyter Notebook.

    ```python
    # load breast cancer dataset, a well-known small dataset that comes with scikit-learn
    from sklearn.datasets import load_breast_cancer
    from sklearn import svm
    from sklearn.model_selection import train_test_split
    breast_cancer_data = load_breast_cancer()
    classes = breast_cancer_data.target_names.tolist()
    
    # split data into train and test
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(breast_cancer_data.data,            
                                                        breast_cancer_data.target,  
                                                        test_size=0.2,
                                                        random_state=0)
    clf = svm.SVC(gamma=0.001, C=100., probability=True)
    model = clf.fit(x_train, y_train)
    ```

3. Call the explainer locally.
   * To initialize an explainer object, pass your model and some training data to the explainer's constructor.
   * To make your explanations and visualizations more informative, you can choose to pass in feature names and output class names if doing classification.

   The following code blocks show how to instantiate an explainer object with `TabularExplainer`, `MimicExplainer`, and `PFIExplainer` locally.
   * `TabularExplainer` calls one of the three SHAP explainers underneath (`TreeExplainer`, `DeepExplainer`, or `KernelExplainer`).
   * `TabularExplainer` automatically selects the most appropriate one for your use case, but you can call each of its three underlying explainers directly.

    ```python
    from interpret.ext.blackbox import TabularExplainer

    # "features" and "classes" fields are optional
    explainer = TabularExplainer(model, 
                                 x_train, 
                                 features=breast_cancer_data.feature_names, 
                                 classes=classes)
    ```

    or

    ```python

    from interpret.ext.blackbox import MimicExplainer
    
    # you can use one of the following four interpretable models as a global surrogate to the black box model
    
    from interpret.ext.glassbox import LGBMExplainableModel
    from interpret.ext.glassbox import LinearExplainableModel
    from interpret.ext.glassbox import SGDExplainableModel
    from interpret.ext.glassbox import DecisionTreeExplainableModel

    # "features" and "classes" fields are optional
    # augment_data is optional and if true, oversamples the initialization examples to improve surrogate model accuracy to fit original model.  Useful for high-dimensional data where the number of rows is less than the number of columns.
    # max_num_of_augmentations is optional and defines max number of times we can increase the input data size.
    # LGBMExplainableModel can be replaced with LinearExplainableModel, SGDExplainableModel, or DecisionTreeExplainableModel
    explainer = MimicExplainer(model, 
                               x_train, 
                               LGBMExplainableModel, 
                               augment_data=True, 
                               max_num_of_augmentations=10, 
                               features=breast_cancer_data.feature_names, 
                               classes=classes)
    ```
