|Permutation Feature Importance Explainer| Permutation Feature Importance (PFI) is a technique used to explain classification and regression models that's inspired by [Breiman's Random Forests paper](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf) (see section 10). At a high level, the way it works is by randomly shuffling data one feature at a time for the entire dataset and calculating how much the performance metric of interest changes. The larger the change, the more important that feature is. PFI can explain the overall behavior of *any underlying model* but doesn't explain individual predictions. |Model-agnostic|

Besides the interpretability techniques described above, we support another SHAP-based explainer, called Tabular Explainer. Depending on the model, Tabular Explainer uses one of the supported SHAP explainers:

* Tree Explainer for all tree-based models
* Deep Explainer for deep neural network (DNN) models
* Linear Explainer for linear models
* Kernel Explainer for all other models

Tabular Explainer has also made significant feature and performance enhancements over the direct SHAP explainers:

* **Summarization of the initialization dataset**: When speed of explanation is most important, we summarize the initialization dataset and generate a small set of representative samples. This approach speeds up the generation of overall and individual feature importance values.
* **Sampling the evaluation data set**: If you pass in a large set of evaluation samples but don't actually need all of them to be evaluated, you can set the sampling parameter to `true` to speed up the calculation of overall model explanations.

The following diagram shows the current structure of supported explainers:

:::image type="content" source="./media/how-to-machine-learning-interpretability/interpretability-architecture.png" alt-text=" Diagram of Machine Learning Interpretability architecture." lightbox="./media/how-to-machine-learning-interpretability/interpretability-architecture.png":::

## Supported machine learning models

The `azureml.interpret` package of the SDK supports models that are trained with the following dataset formats:

* `numpy.array`
* `pandas.DataFrame`
* `iml.datatypes.DenseData`
* `scipy.sparse.csr_matrix`

The explanation functions accept both models and pipelines as input. If a model is provided, it must implement the prediction function `predict` or `predict_proba` that conforms to the Scikit convention. If your model doesn't support this, you can wrap it in a function that generates the same outcome as `predict` or `predict_proba` in Scikit and use that wrapper function with the selected explainer. 

If you provide a pipeline, the explanation function assumes that the running pipeline script returns a prediction. When you use this wrapping technique, `azureml.interpret` can support models that are trained via PyTorch, TensorFlow, and Keras deep learning frameworks as well as classic machine learning models.

## Local and remote compute target

The `azureml.interpret` package is designed to work with both local and remote compute targets. If you run the package locally, the SDK functions won't contact any Azure services. 

You can run the explanation remotely on Azure Machine Learning Compute and log the explanation info into the Azure Machine Learning Run History Service. After this information is logged, reports and visualizations from the explanation are readily available on Azure Machine Learning studio for analysis.

## Next steps

* Learn how to generate the Responsible AI dashboard via [CLI v2 and SDK v2](how-to-responsible-ai-dashboard-sdk-cli.md) or the [Azure Machine Learning studio UI](how-to-responsible-ai-dashboard-ui.md).
* Explore the [supported interpretability visualizations](how-to-responsible-ai-dashboard.md#feature-importances-model-explanations) of the Responsible AI dashboard.
* Learn how to generate a [Responsible AI scorecard](how-to-responsible-ai-scorecard.md) based on the insights observed in the Responsible AI dashboard.
