A crucial part of transparency is *interpretability*: the useful explanation of the behavior of AI systems and their components. Improving interpretability requires stakeholders to comprehend how and why AI systems function the way they do. The stakeholders can then identify potential performance issues, fairness issues, exclusionary practices, or unintended outcomes.  

**Transparency in Azure Machine Learning**: The [model interpretability](how-to-machine-learning-interpretability.md) and [counterfactual what-if](./concept-counterfactual-analysis.md) components of the [Responsible AI dashboard](concept-responsible-ai-dashboard.md) enable data scientists and developers to generate human-understandable descriptions of the predictions of a model. 

The model interpretability component provides multiple views into a model's behavior: 

- *Global explanations*. For example, what features affect the overall behavior of a loan allocation model?
- *Local explanations*. For example, why was a customer's loan application approved or rejected? 
- *Model explanations for a selected cohort of data points*. For example, what features affect the overall behavior of a loan allocation model for low-income applicants?

The counterfactual what-if component enables understanding and debugging a machine learning model in terms of how it reacts to feature changes and perturbations.

Azure Machine Learning also supports a [Responsible AI scorecard](./how-to-responsible-ai-scorecard.md). The scorecard is a customizable PDF report that developers can easily configure, generate, download, and share with their technical and non-technical stakeholders to educate them about their datasets and models health, achieve compliance, and build trust. This scorecard can also be used in audit reviews to uncover the characteristics of machine learning models.

## Privacy and security

As AI becomes more prevalent, protecting privacy and securing personal and business information are becoming more important and complex. With AI, privacy and data security require close attention because access to data is essential for AI systems to make accurate and informed predictions and decisions about people. AI systems must comply with privacy laws that:

- Require transparency about the collection, use, and storage of data.
- Mandate that consumers have appropriate controls to choose how their data is used.  

**Privacy and security in Azure Machine Learning**: Azure Machine Learning enables administrators and developers to [create a secure configuration that complies](concept-enterprise-security.md) with their companies' policies. With Azure Machine Learning and the Azure platform, users can:

- Restrict access to resources and operations by user account or group.
- Restrict incoming and outgoing network communications.
- Encrypt data in transit and at rest.
- Scan for vulnerabilities.
- Apply and audit configuration policies.

Microsoft has also created two open-source packages that can enable further implementation of privacy and security principles:

- [SmartNoise](https://github.com/opendifferentialprivacy/smartnoise-core): Differential privacy is a set of systems and practices that help keep the data of individuals safe and private. In machine learning solutions, differential privacy might be required for regulatory compliance. SmartNoise is an open-source project (co-developed by Microsoft) that contains components for building differentially private systems that are global.

- [Counterfit](https://github.com/Azure/counterfit/): Counterfit is an open-source project that comprises a command-line tool and generic automation layer to allow developers to simulate cyberattacks against AI systems. Anyone can download the tool and deploy it through Azure Cloud Shell to run in a browser, or deploy it locally in an Anaconda Python environment. It can assess AI models hosted in various cloud environments, on-premises, or in the edge. The tool is agnostic to AI models and supports various data types, including text, images, or generic input.
