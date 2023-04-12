- [Counterfit](https://github.com/Azure/counterfit/): Counterfit is an open-source project that comprises a command-line tool and generic automation layer to allow developers to simulate cyberattacks against AI systems. Anyone can download the tool and deploy it through Azure Cloud Shell to run in a browser, or deploy it locally in an Anaconda Python environment. It can assess AI models hosted in various cloud environments, on-premises, or in the edge. The tool is agnostic to AI models and supports various data types, including text, images, or generic input.

## Accountability

The people who design and deploy AI systems must be accountable for how their systems operate. Organizations should draw upon industry standards to develop accountability norms. These norms can ensure that AI systems aren't the final authority on any decision that affects people's lives. They can also ensure that humans maintain meaningful control over otherwise highly autonomous AI systems.

**Accountability in Azure Machine Learning**: [Machine learning operations (MLOps)](concept-model-management-and-deployment.md) is based on DevOps principles and practices that increase the efficiency of AI workflows. Azure Machine Learning provides the following MLOps capabilities for better accountability of your AI systems:

- Register, package, and deploy models from anywhere. You can also track the associated metadata that's required to use the model.
- Capture the governance data for the end-to-end machine learning lifecycle. The logged lineage information can include who is publishing models, why changes were made, and when models were deployed or used in production.
- Notify and alert on events in the machine learning lifecycle. Examples include experiment completion, model registration, model deployment, and data drift detection.
- Monitor applications for operational issues and issues related to machine learning. Compare model inputs between training and inference, explore model-specific metrics, and provide monitoring and alerts on your machine learning infrastructure.

Besides the MLOps capabilities, the [Responsible AI scorecard](concept-responsible-ai-scorecard.md) in Azure Machine Learning creates accountability by enabling cross-stakeholder communications. The scorecard also creates accountability by empowering developers to configure, download, and share their model health insights with their technical and non-technical stakeholders about AI data and model health. Sharing these insights can help build trust.  

The machine learning platform also enables decision-making by informing business decisions through:

- Data-driven insights, to help stakeholders understand causal treatment effects on an outcome, by using historical data only. For example, "How would a medicine affect a patient's blood pressure?" These insights are provided through the [causal inference](concept-causal-inference.md) component of the [Responsible AI dashboard](concept-responsible-ai-dashboard.md).
- Model-driven insights, to answer users' questions (such as "What can I do to get a different outcome from your AI next time?") so they can take action. Such insights are provided to data scientists through the [counterfactual what-if](concept-counterfactual-analysis.md) component of the [Responsible AI dashboard](concept-responsible-ai-dashboard.md).

## Next steps

- For more information on how to implement Responsible AI in Azure Machine Learning, see [Responsible AI dashboard](concept-responsible-ai-dashboard.md).
- Learn how to generate the Responsible AI dashboard via [CLI and SDK](how-to-responsible-ai-dashboard-sdk-cli.md) or [Azure Machine Learning studio UI](how-to-responsible-ai-dashboard-ui.md).
- Learn how to generate a [Responsible AI scorecard](concept-responsible-ai-scorecard.md) based on the insights observed in your Responsible AI dashboard.
- Learn about the [Responsible AI Standard](https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf) for building AI systems according to six key principles.
