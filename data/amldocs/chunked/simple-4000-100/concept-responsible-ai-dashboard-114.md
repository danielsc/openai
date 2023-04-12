- The different tools don't communicate with each other. Data scientists must wrangle the datasets, models, and other metadata as they pass them between the tools. 
- The metrics and visualizations aren't easily comparable, and the results are hard to share.

The Responsible AI dashboard challenges this status quo. It's a comprehensive yet customizable tool that brings together fragmented experiences in one place. It enables you to seamlessly onboard to a single customizable framework for model debugging and data-driven decision-making. 

By using the Responsible AI dashboard, you can create dataset cohorts, pass those cohorts to all of the supported components, and observe your model health for your identified cohorts. You can further compare insights from all supported components across a variety of prebuilt cohorts to perform disaggregated analysis and find the blind spots of your model.

When you're ready to share those insights with other stakeholders, you can extract them easily by using the [Responsible AI PDF scorecard](how-to-responsible-ai-scorecard.md). Attach the PDF report to your compliance reports, or share it with colleagues to build trust and get their approval.

## Ways to customize the Responsible AI dashboard

The Responsible AI dashboard's strength lies in its customizability. It empowers users to design tailored, end-to-end model debugging and decision-making workflows that address their particular needs. 

Need some inspiration? Here are some examples of how the dashboard's components can be put together to analyze scenarios in diverse ways:

| Responsible AI dashboard flow | Use case |
|-------------------------------|----------|
| Model overview > error analysis > data analysis | To identify model errors and diagnose them by understanding the underlying data distribution |
| Model overview > fairness assessment > data analysis | To identify model fairness issues and diagnose them by understanding the underlying data distribution |
| Model overview > error analysis > counterfactuals analysis and what-if  | To diagnose errors in individual instances with counterfactual analysis (minimum change to lead to a different model prediction) |
| Model overview > data analysis | To understand the root cause of errors and fairness issues introduced via data imbalances or lack of representation of a particular data cohort |
| Model overview > interpretability | To diagnose model errors through understanding how the model has made its predictions |
| Data analysis > causal inference  | To distinguish between correlations and causations in the data or decide the best treatments to apply to get a positive outcome |
| Interpretability > causal inference | To learn whether the factors that the model has used for prediction-making have any causal effect on the real-world outcome|
| Data analysis > counterfactuals analysis and what-if | To address customers' questions about what they can do next time to get a different outcome from an AI system|

## People who should use the Responsible AI dashboard

The following people can use the Responsible AI dashboard, and its corresponding [Responsible AI scorecard](concept-responsible-ai-scorecard.md), to build trust with AI systems:

- Machine learning professionals and data scientists who are interested in debugging and improving their machine learning models before deployment
- Machine learning professionals and data scientists who are interested in sharing their model health records with product managers and business stakeholders to build trust and receive deployment permissions
- Product managers and business stakeholders who are reviewing machine learning models before deployment
- Risk officers who are reviewing machine learning models to understand fairness and reliability issues
- Providers of AI solutions who want to explain model decisions to users or help them improve the outcome
- Professionals in heavily regulated spaces who need to review machine learning models with regulators and auditors
