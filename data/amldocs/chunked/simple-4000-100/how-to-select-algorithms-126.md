Parameters are the knobs a data scientist gets to turn when setting up an algorithm. They are numbers that affect the algorithm’s behavior, such as error tolerance or number of iterations, or options between variants of how the algorithm behaves. The training time and accuracy of the algorithm can sometimes be sensitive to getting just the right settings. Typically, algorithms with large numbers of parameters require the most trial and error to find a good combination.

Alternatively, there is the [Tune Model Hyperparameters component](./algorithm-module-reference/tune-model-hyperparameters.md?WT.mc_id=docs-article-lazzeri) in Machine Learning designer: The goal of this component is to determine the optimum hyperparameters for a machine learning model. The component builds and tests multiple models by using different combinations of settings. It compares metrics over all models to get the combinations of settings. 

While this is a great way to make sure you’ve spanned the parameter space, the time required to train a model increases exponentially with the number of parameters. The upside is that having many parameters typically indicates that an algorithm has greater flexibility. It can often achieve very good accuracy, provided you can find the right combination of parameter settings.

## Number of features

In machine learning, a feature is a quantifiable variable of the phenomenon you are trying to analyze. For certain types of data, the number of features can be very large compared to the number of data points. This is often the case with genetics or textual data. 

A large number of features can bog down some learning algorithms, making training time unfeasibly long. [Support vector machines](./algorithm-module-reference/two-class-support-vector-machine.md?WT.mc_id=docs-article-lazzeri) are particularly well suited to scenarios with a high number of features. For this reason, they have been used in many applications from information retrieval to text and image classification. Support vector machines can be used for both classification and regression tasks.

Feature selection refers to the process of applying statistical tests to inputs, given a specified output. The goal is to determine which columns are more predictive of the output. The [Filter Based Feature Selection component](./algorithm-module-reference/filter-based-feature-selection.md?WT.mc_id=docs-article-lazzeri) in Machine Learning designer provides multiple feature selection algorithms to choose from. The component includes correlation methods such as Pearson correlation and chi-squared values.

You can also use the [Permutation Feature Importance component](./algorithm-module-reference/permutation-feature-importance.md?WT.mc_id=docs-article-lazzeri) to compute a set of feature importance scores for your dataset. You can then leverage these scores to help you determine the best features to use in a model.

## Next steps

 - [Learn more about Azure Machine Learning designer](./concept-designer.md?WT.mc_id=docs-article-lazzeri)
 - For descriptions of all the machine learning algorithms available in Azure Machine Learning designer, see [Machine Learning designer algorithm and component reference](./component-reference/component-reference.md?WT.mc_id=docs-article-lazzeri)
 - To explore the relationship between deep learning, machine learning, and AI, see [Deep Learning vs. Machine Learning](./concept-deep-learning-vs-machine-learning.md?WT.mc_id=docs-article-lazzeri)
