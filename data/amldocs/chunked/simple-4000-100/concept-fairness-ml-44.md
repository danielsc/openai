After you understand your model's fairness issues, you can use the mitigation algorithms in the [Fairlearn](https://fairlearn.org/) open-source package to mitigate those issues. These algorithms support a set of constraints on the predictor's behavior called *parity constraints* or criteria. 

Parity constraints require some aspects of the predictor's behavior to be comparable across the groups that sensitive features define (for example, different races). The mitigation algorithms in the Fairlearn open-source package use such parity constraints to mitigate the observed fairness issues.

>[!NOTE]
> The unfairness mitigation algorithms in the Fairlearn open-source package can provide suggested mitigation strategies to reduce unfairness in a machine learning model, but those strategies don't eliminate unfairness. Developers might need to consider other parity constraints or criteria for their machine learning models. Developers who use Azure Machine Learning must determine for themselves if the mitigation sufficiently reduces unfairness in their intended use and deployment of machine learning models.  

The Fairlearn package supports the following types of parity constraints:

|Parity constraint  | Purpose  |Machine learning task  |
|---------|---------|---------|
|Demographic parity     |  Mitigate allocation harms | Binary classification, regression |
|Equalized odds  | Diagnose allocation and quality-of-service harms | Binary classification        |
|Equal opportunity | Diagnose allocation and quality-of-service harms | Binary classification        |
|Bounded group loss     |  Mitigate quality-of-service harms | Regression |

## Mitigation algorithms

The Fairlearn open-source package provides two types of unfairness mitigation algorithms:

- **Reduction**: These algorithms take a standard black-box machine learning estimator (for example, a LightGBM model) and generate a set of retrained models by using a sequence of reweighted training datasets. 

  For example, applicants of a certain gender might be upweighted or downweighted to retrain models and reduce disparities across gender groups. Users can then pick a model that provides the best trade-off between accuracy (or another performance metric) and disparity, based on their business rules and cost calculations.  
- **Post-processing**: These algorithms take an existing classifier and a sensitive feature as input. They then derive a transformation of the classifier's prediction to enforce the specified fairness constraints. The biggest advantage of one post-processing algorithm, threshold optimization, is its simplicity and flexibility because it doesn't need to retrain the model.

| Algorithm | Description | Machine learning task | Sensitive features | Supported parity constraints | Algorithm type |
| --- | --- | --- | --- | --- | --- |
| `ExponentiatedGradient` | Black-box approach to fair classification described in [A Reductions Approach to Fair Classification](https://arxiv.org/abs/1803.02453). | Binary classification | Categorical | Demographic parity, equalized odds| Reduction |
| `GridSearch` | Black-box approach described in [A Reductions Approach to Fair Classification](https://arxiv.org/abs/1803.02453).| Binary classification | Binary | Demographic parity, equalized odds | Reduction |
| `GridSearch` | Black-box approach that implements a grid-search variant of fair regression with the algorithm for bounded group loss described in [Fair Regression: Quantitative Definitions and Reduction-based Algorithms](https://arxiv.org/abs/1905.12843). | Regression | Binary | Bounded group loss| Reduction |
| `ThresholdOptimizer` | Postprocessing algorithm based on the paper [Equality of Opportunity in Supervised Learning](https://arxiv.org/abs/1610.02413). This technique takes as input an existing classifier and a sensitive feature. Then, it derives a monotone transformation of the classifier's prediction to enforce the specified parity constraints. | Binary classification | Categorical | Demographic parity, equalized odds| Post-processing |
