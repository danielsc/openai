Mitigation steps are available via standalone tools such as [Fairlearn](https://fairlearn.org/). For more information, see the [unfairness mitigation algorithms](https://fairlearn.org/v0.7.0/user_guide/mitigation.html).

### Responsible decision-making

Decision-making is one of the biggest promises of machine learning. The Responsible AI dashboard can help you make informed business decisions through:

- Data-driven insights, to further understand causal treatment effects on an outcome by using historical data only. For example:

  "How would a medicine affect a patient's blood pressure?"
  
  "How would providing promotional values to certain customers affect revenue?"
  
  These insights are provided through the [causal inference](concept-causal-inference.md) component of the dashboard.
- Model-driven insights, to answer users' questions (such as "What can I do to get a different outcome from your AI next time?") so they can take action. These insights are provided to data scientists through the [counterfactual what-if](concept-counterfactual-analysis.md) component.

:::image type="content" source="./media/concept-responsible-ai-dashboard/decision-making.png" alt-text="Diagram that shows responsible AI dashboard capabilities for responsible business decision-making.":::

Exploratory data analysis, causal inference, and counterfactual analysis capabilities can help you make informed model-driven and data-driven decisions responsibly.

These components of the Responsible AI dashboard support responsible decision-making:

- **Data analysis**: You can reuse the data analysis component here to understand data distributions and to identify overrepresentation and underrepresentation. Data exploration is a critical part of decision making, because it isn't feasible to make informed decisions about a cohort that's underrepresented in the data.
- **Causal inference**: The causal inference component estimates how a real-world outcome changes in the presence of an intervention. It also helps construct promising interventions by simulating feature responses to various interventions and creating rules to determine which population cohorts would benefit from a particular intervention. Collectively, these functionalities allow you to apply new policies and effect real-world change.
  
  The capabilities of this component come from the [EconML](https://github.com/Microsoft/EconML) package, which estimates heterogeneous treatment effects from observational data via machine learning.
- **Counterfactual analysis**: You can reuse the counterfactual analysis component here to generate minimum changes applied to a data point's features that lead to opposite model predictions. For example: Taylor would have obtained the loan approval from the AI if they earned $10,000 more in annual income and had two fewer credit cards open. 

  Providing this information to users informs their perspective. It educates them on how they can take action to get the desired outcome from the AI in the future.
  
  The capabilities of this component come from the [DiCE](https://github.com/interpretml/DiCE) package.

## Reasons for using the Responsible AI dashboard

Although progress has been made on individual tools for specific areas of Responsible AI, data scientists often need to use various tools to holistically evaluate their models and data. For example: they might have to use model interpretability and fairness assessment together. 

If data scientists discover a fairness issue with one tool, they then need to jump to a different tool to understand what data or model factors lie at the root of the issue before taking any steps on mitigation. The following factors further complicate this challenging process:

- There's no central location to discover and learn about the tools, extending the time it takes to research and learn new techniques. 
- The different tools don't communicate with each other. Data scientists must wrangle the datasets, models, and other metadata as they pass them between the tools. 
