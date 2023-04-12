Getting the most accurate answer possible isn’t always necessary. Sometimes an approximation is adequate, depending on what you want to use it for. If that is the case, you may be able to cut your processing time dramatically by sticking with more approximate methods. Approximate methods also naturally tend to avoid overfitting.

There are three ways to use the Evaluate Model component:

- Generate scores over your training data in order to evaluate the model
- Generate scores on the model, but compare those scores to scores on a reserved testing set
- Compare scores for two different but related models, using the same set of data

For a complete list of metrics and approaches you can use to evaluate the accuracy of machine learning models, see [Evaluate Model component](./algorithm-module-reference/evaluate-model.md?WT.mc_id=docs-article-lazzeri).

## Training time

In supervised learning, training means using historical data to build a machine learning model that minimizes errors. The number of minutes or hours necessary to train a model varies a great deal between algorithms. Training time is often closely tied to accuracy; one typically accompanies the other. 

In addition, some algorithms are more sensitive to the number of data points than others. You might choose a specific algorithm because you have a time limitation, especially when the data set is large.

In Machine Learning designer, creating and using a machine learning model is typically a three-step process:

1.	Configure a model, by choosing a particular type of algorithm, and then defining its parameters or hyperparameters. 

2.	Provide a dataset that is labeled and has data compatible with the algorithm. Connect both the data and the model to [Train Model component](./algorithm-module-reference/train-model.md?WT.mc_id=docs-article-lazzeri).

3.	After training is completed, use the trained model with one of the [scoring components](./algorithm-module-reference/score-model.md?WT.mc_id=docs-article-lazzeri) to make predictions on new data.

## Linearity

Linearity in statistics and machine learning means that there is a linear relationship between a variable and a constant in your dataset. For example, linear classification algorithms assume that classes can be separated by a straight line (or its higher-dimensional analog).

Lots of machine learning algorithms make use of linearity. In Azure Machine Learning designer, they include: 

- [Multiclass logistic regression](./algorithm-module-reference/multiclass-logistic-regression.md?WT.mc_id=docs-article-lazzeri)
- [Two-class logistic regression](./algorithm-module-reference/two-class-logistic-regression.md?WT.mc_id=docs-article-lazzeri)
- [Support vector machines](./algorithm-module-reference/two-class-support-vector-machine.md?WT.mc_id=docs-article-lazzeri)  

Linear regression algorithms assume that data trends follow a straight line. This assumption isn't bad for some problems, but for others it reduces accuracy. Despite their drawbacks, linear algorithms are popular as a first strategy. They tend to be algorithmically simple and fast to train.

![Nonlinear class boundary](./media/how-to-select-algorithms/nonlinear-class-boundary.png)

***Nonlinear class boundary***: *Relying on a linear classification
algorithm would result in low accuracy.*

![Data with a nonlinear trend](./media/how-to-select-algorithms/nonlinear-trend.png)

***Data with a nonlinear trend***: *Using a linear regression method would
generate much larger errors than necessary.*

## Number of parameters

Parameters are the knobs a data scientist gets to turn when setting up an algorithm. They are numbers that affect the algorithm’s behavior, such as error tolerance or number of iterations, or options between variants of how the algorithm behaves. The training time and accuracy of the algorithm can sometimes be sensitive to getting just the right settings. Typically, algorithms with large numbers of parameters require the most trial and error to find a good combination.
