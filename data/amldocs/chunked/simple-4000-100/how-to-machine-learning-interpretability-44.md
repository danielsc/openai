* Explain model prediction by generating feature-importance values for the entire model or individual data points.
* Achieve model interpretability on real-world datasets at scale during training and inference.
* Use an interactive visualization dashboard to discover patterns in your data and its explanations at training time.

> [!NOTE]
> Model interpretability classes are made available through the SDK v1 package. For more information, see [Install SDK packages for Azure Machine Learning](/python/api/overview/azure/ml/install) and [azureml.interpret](/python/api/azureml-interpret/azureml.interpret).

## Supported model interpretability techniques

The Responsible AI dashboard and `azureml-interpret` use the interpretability techniques that were developed in [Interpret-Community](https://github.com/interpretml/interpret-community/), an open-source Python package for training interpretable models and helping to explain opaque-box AI systems. Opaque-box models are those for which we have no information about their internal workings. 

Interpret-Community serves as the host for the following supported explainers, and currently supports the interpretability techniques presented in the next sections.

### Supported in Responsible AI dashboard in Python SDK v2 and CLI v2
|Interpretability technique|Description|Type|
|--|--|--|
|Mimic Explainer (Global Surrogate) + SHAP tree|Mimic Explainer is based on the idea of training global surrogate models to mimic opaque-box models. A global surrogate model is an intrinsically interpretable model that's trained to approximate the predictions of any opaque-box model as accurately as possible.<br><br> Data scientists can interpret the surrogate model to draw conclusions about the opaque-box model. The Responsible AI dashboard uses LightGBM (LGBMExplainableModel), paired with the SHAP (SHapley Additive exPlanations) Tree Explainer, which is a specific explainer to trees and ensembles of trees. The combination of LightGBM and SHAP tree provides model-agnostic global and local explanations of your machine learning models.|Model-agnostic|

### Supported in Python SDK v1
|Interpretability technique|Description|Type|
|--|--|--|
|SHAP Tree Explainer| The [SHAP](https://github.com/slundberg/shap) Tree Explainer, which focuses on a polynomial, time-fast, SHAP value-estimation algorithm that's specific to *trees and ensembles of trees*.|Model-specific|
|SHAP Deep Explainer| Based on the explanation from SHAP, Deep Explainer is a "high-speed approximation algorithm for SHAP values in deep learning models that builds on a connection with DeepLIFT described in the [SHAP NIPS paper](https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions). *TensorFlow* models and *Keras* models using the TensorFlow back end are supported (there's also preliminary support for PyTorch)."|Model-specific|
|SHAP Linear Explainer| The SHAP Linear Explainer computes SHAP values for a *linear model*, optionally accounting for inter-feature correlations.|Model-specific|
|SHAP Kernel Explainer| The SHAP Kernel Explainer uses a specially weighted local linear regression to estimate SHAP values for *any model*.|Model-agnostic|
|Mimic Explainer (Global Surrogate)| Mimic Explainer is based on the idea of training [global surrogate models](https://christophm.github.io/interpretable-ml-book/global.html) to mimic opaque-box models. A global surrogate model is an intrinsically interpretable model that's trained to approximate the predictions of *any opaque-box model* as accurately as possible. Data scientists can interpret the surrogate model to draw conclusions about the opaque-box model. You can use one of the following interpretable models as your surrogate model: LightGBM (LGBMExplainableModel), Linear Regression (LinearExplainableModel), Stochastic Gradient Descent explainable model (SGDExplainableModel), or Decision Tree (DecisionTreeExplainableModel).|Model-agnostic|
|Permutation Feature Importance Explainer| Permutation Feature Importance (PFI) is a technique used to explain classification and regression models that's inspired by [Breiman's Random Forests paper](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf) (see section 10). At a high level, the way it works is by randomly shuffling data one feature at a time for the entire dataset and calculating how much the performance metric of interest changes. The larger the change, the more important that feature is. PFI can explain the overall behavior of *any underlying model* but doesn't explain individual predictions. |Model-agnostic|
