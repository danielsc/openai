Assessing and debugging machine learning models is critical for model reliability, interpretability, fairness, and compliance. It helps determine how and why AI systems behave the way they do. You can then use this knowledge to improve model performance. Conceptually, model debugging consists of three stages:

1. **Identify**, to understand and recognize model errors and/or fairness issues by addressing the following questions:
  
   "What kinds of errors does my model have?"
  
   "In what areas are errors most prevalent?"
1. **Diagnose**, to explore the reasons behind the identified errors by addressing:
  
   "What are the causes of these errors?"

   "Where should I focus my resources to improve my model?"
1. **Mitigate**, to use the identification and diagnosis insights from previous stages to take targeted mitigation steps and address questions such as:

   "How can I improve my model?"

   "What social or technical solutions exist for these issues?"

:::image type="content" source="./media/concept-responsible-ai-dashboard/model-debugging.png" alt-text="Diagram of model debugging via Responsible AI dashboard." lightbox= "./media/concept-responsible-ai-dashboard/model-debugging.png":::

The following table describes when to use Responsible AI dashboard components to support model debugging:

| Stage | Component | Description |
|-------|-----------|-------------|
| Identify | Error analysis | The error analysis component helps you get a deeper understanding of model failure distribution and quickly identify erroneous cohorts (subgroups) of data. <br><br> The capabilities of this component in the dashboard come from the [Error Analysis](https://erroranalysis.ai/) package.|
| Identify | Fairness analysis | The fairness component defines groups in terms of sensitive attributes such as sex, race, and age. It then assesses how your model predictions affect these groups and how you can mitigate disparities. It evaluates the performance of your model by exploring the distribution of your prediction values and the values of your model performance metrics across the groups. <br><br>The capabilities of this component in the dashboard come from the [Fairlearn](https://fairlearn.org/) package.  |
| Identify | Model overview | The model overview component aggregates model assessment metrics in a high-level view of model prediction distribution for better investigation of its performance. This component also enables group fairness assessment by highlighting the breakdown of model performance across sensitive groups. |
| Diagnose | Data analysis | Data analysis visualizes datasets based on predicted and actual outcomes, error groups, and specific features. You can then identify issues of overrepresentation and underrepresentation, along with seeing how data is clustered in the dataset.  |
| Diagnose | Model interpretability | The interpretability component generates human-understandable explanations of the predictions of a machine learning model. It provides multiple views into a model's behavior: <br> - Global explanations (for example, which features affect the overall behavior of a loan allocation model) <br> - Local explanations (for example, why an applicant's loan application was approved or rejected) <br><br> The capabilities of this component in the dashboard come from the [InterpretML](https://interpret.ml/) package. |
| Diagnose | Counterfactual analysis and what-if| This component consists of two functionalities for better error diagnosis: <br> - Generating a set of examples in which minimal changes to a particular point alter the model's prediction. That is, the examples show the closest data points with opposite model predictions. <br> - Enabling interactive and custom what-if perturbations for individual data points to understand how the model reacts to feature changes. <br> <br> The capabilities of this component in the dashboard come from the [DiCE](https://github.com/interpretml/DiCE) package.  |

Mitigation steps are available via standalone tools such as [Fairlearn](https://fairlearn.org/). For more information, see the [unfairness mitigation algorithms](https://fairlearn.org/v0.7.0/user_guide/mitigation.html).
