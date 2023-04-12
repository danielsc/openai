
# Model performance and fairness

This article describes methods that you can use to understand your model performance and fairness in Azure Machine Learning.

## What is machine learning fairness?

Artificial intelligence and machine learning systems can display unfair behavior. One way to define unfair behavior is by its harm, or its impact on people. AI systems can give rise to many types of harm. To learn more, see the [NeurIPS 2017 keynote by Kate Crawford](https://www.youtube.com/watch?v=fMym_BKWQzk).

Two common types of AI-caused harms are:

- **Harm of allocation**: An AI system extends or withholds opportunities, resources, or information for certain groups. Examples include hiring, school admissions, and lending, where a model might be better at picking good candidates among a specific group of people than among other groups.

- **Harm of quality-of-service**: An AI system doesn't work as well for one group of people as it does for another. For example, a voice recognition system might fail to work as well for women as it does for men.

To reduce unfair behavior in AI systems, you have to assess and mitigate these harms. The *model overview* component of the [Responsible AI dashboard](concept-responsible-ai-dashboard.md) contributes to the identification stage of the model lifecycle by generating model performance metrics for your entire dataset and your identified cohorts of data. It generates these metrics across subgroups identified in terms of sensitive features or sensitive attributes.

>[!NOTE]
> Fairness is a socio-technical challenge. Quantitative fairness metrics don't capture many aspects of fairness, such as justice and due process. Also, many quantitative fairness metrics can't all be satisfied simultaneously. 
>
> The goal of the Fairlearn open-source package is to enable humans to assess the impact and mitigation strategies. Ultimately, it's up to the humans who build AI and machine learning models to make trade-offs that are appropriate for their scenarios.

In this component of the Responsible AI dashboard, fairness is conceptualized through an approach known as *group fairness*. This approach asks: "Which groups of individuals are at risk for experiencing harm?" The term *sensitive features* suggests that the system designer should be sensitive to these features when assessing group fairness. 

During the assessment phase, fairness is quantified through *disparity metrics*. These metrics can evaluate and compare model behavior across groups either as ratios or as differences. The Responsible AI dashboard supports two classes of disparity metrics:

- **Disparity in model performance**: These sets of metrics calculate the disparity (difference) in the values of the selected performance metric across subgroups of data. Here are a few examples:

  - Disparity in accuracy rate
  - Disparity in error rate
  - Disparity in precision
  - Disparity in recall
  - Disparity in mean absolute error (MAE)  

- **Disparity in selection rate**: This metric contains the difference in selection rate (favorable prediction) among subgroups. An example of this is disparity in loan approval rate. Selection rate means the fraction of data points in each class classified as 1 (in binary classification) or distribution of prediction values (in regression).

The fairness assessment capabilities of this component come from the [Fairlearn](https://fairlearn.org/) package. Fairlearn provides a collection of model fairness assessment metrics and unfairness mitigation algorithms.

>[!NOTE]
> A fairness assessment is not a purely technical exercise. The Fairlearn open-source package can identify quantitative metrics to help you assess the fairness of a model, but it won't perform the assessment for you.  You must perform a qualitative analysis to evaluate the fairness of your own models. The sensitive features noted earlier are an example of this kind of qualitative analysis.

## Parity constraints for mitigating unfairness

After you understand your model's fairness issues, you can use the mitigation algorithms in the [Fairlearn](https://fairlearn.org/) open-source package to mitigate those issues. These algorithms support a set of constraints on the predictor's behavior called *parity constraints* or criteria. 
