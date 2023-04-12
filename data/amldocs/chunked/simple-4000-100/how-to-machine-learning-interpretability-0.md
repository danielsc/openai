
# Model interpretability

This article describes methods you can use for model interpretability in Azure Machine Learning.

> [!IMPORTANT]
> With the release of the Responsible AI dashboard, which includes model interpretability, we recommend that you migrate to the new experience, because the older SDK v1 preview model interpretability dashboard will no longer be actively maintained.

## Why model interpretability is important to model debugging

When you're using machine learning models in ways that affect people’s lives, it's critically important to understand what influences the behavior of models. Interpretability helps answer questions in scenarios such as:
* Model debugging: Why did my model make this mistake? How can I improve my model?
* Human-AI collaboration: How can I understand and trust the model’s decisions?
* Regulatory compliance: Does my model satisfy legal requirements?  

The interpretability component of the [Responsible AI dashboard](concept-responsible-ai-dashboard.md) contributes to the “diagnose” stage of the model lifecycle workflow by generating human-understandable descriptions of the predictions of a machine learning model. It provides multiple views into a model’s behavior: 
* Global explanations: For example, what features affect the overall behavior of a loan allocation model?
* Local explanations: For example, why was a customer’s loan application approved or rejected? 

You can also observe model explanations for a selected cohort as a subgroup of data points. This approach is valuable when, for example, you're assessing fairness in model predictions for individuals in a particular demographic group. The **Local explanation** tab of this component also represents a full data visualization, which is great for general eyeballing of the data and looking at differences between correct and incorrect predictions of each cohort.

The capabilities of this component are founded by the [InterpretML](https://interpret.ml/) package, which generates model explanations.

Use interpretability when you need to:

* Determine how trustworthy your AI system’s predictions are by understanding what features are most important for the predictions.
* Approach the debugging of your model by understanding it first and identifying whether the model is using healthy features or merely false correlations.
* Uncover potential sources of unfairness by understanding whether the model is basing predictions on sensitive features or on features that are highly correlated with them.
* Build user trust in your model’s decisions by generating local explanations to illustrate their outcomes.
* Complete a regulatory audit of an AI system to validate models and monitor the impact of model decisions on humans.

## How to interpret your model

In machine learning, *features* are the data fields you use to predict a target data point. For example, to predict credit risk, you might use data fields for age, account size, and account age. Here, age, account size, and account age are features. Feature importance tells you how each data field affects the model's predictions. For example, although you might use age heavily in the prediction, account size and account age might not affect the prediction values significantly. Through this process, data scientists can explain resulting predictions in ways that give stakeholders visibility into the model's most important features.

By using the classes and methods in the Responsible AI dashboard and by using SDK v2 and CLI v2, you can:

* Explain model prediction by generating feature-importance values for the entire model (global explanation) or individual data points (local explanation).
* Achieve model interpretability on real-world datasets at scale.
* Use an interactive visualization dashboard to discover patterns in your data and its explanations at training time.

By using the classes and methods in the SDK v1, you can:

* Explain model prediction by generating feature-importance values for the entire model or individual data points.
