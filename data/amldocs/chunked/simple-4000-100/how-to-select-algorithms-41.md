| **Algorithm** | **Accuracy** | **Training time** | **Linearity** | **Parameters** | **Notes** |
| --- |:---:|:---:|:---:|:---:| --- |
| **Classification family** | | | | | |
| [Two-Class logistic regression](./algorithm-module-reference/two-class-logistic-regression.md?WT.mc_id=docs-article-lazzeri) |Good  |Fast |Yes |4 | |
| [Two-class decision forest](./algorithm-module-reference/two-class-decision-forest.md?WT.mc_id=docs-article-lazzeri) |Excellent |Moderate |No |5 |Shows slower scoring times. Suggest not working with One-vs-All Multiclass, because of slower scoring times caused by tread locking in accumulating tree predictions |
| [Two-class boosted decision tree](./algorithm-module-reference/two-class-boosted-decision-tree.md?WT.mc_id=docs-article-lazzeri) |Excellent |Moderate |No |6 |Large memory footprint |
| [Two-class neural network](./algorithm-module-reference/two-class-neural-network.md?WT.mc_id=docs-article-lazzeri) |Good |Moderate |No |8 | |
| [Two-class averaged perceptron](./algorithm-module-reference/two-class-averaged-perceptron.md?WT.mc_id=docs-article-lazzeri) |Good |Moderate |Yes |4 | |
| [Two-class support vector machine](./algorithm-module-reference/two-class-support-vector-machine.md?WT.mc_id=docs-article-lazzeri) |Good |Fast |Yes |5 |Good for large feature sets |
| [Multiclass logistic regression](./algorithm-module-reference/multiclass-logistic-regression.md?WT.mc_id=docs-article-lazzeri) |Good |Fast |Yes |4 | |
| [Multiclass decision forest](./algorithm-module-reference/multiclass-decision-forest.md?WT.mc_id=docs-article-lazzeri) |Excellent |Moderate |No |5 |Shows slower scoring times |
| [Multiclass boosted decision tree](./algorithm-module-reference/multiclass-boosted-decision-tree.md?WT.mc_id=docs-article-lazzeri) |Excellent |Moderate |No |6 | Tends to improve accuracy with some small risk of less coverage |
| [Multiclass neural network](./algorithm-module-reference/multiclass-neural-network.md?WT.mc_id=docs-article-lazzeri) |Good |Moderate |No |8 | |
| [One-vs-all multiclass](./algorithm-module-reference/one-vs-all-multiclass.md?WT.mc_id=docs-article-lazzeri) | - | - | - | - |See properties of the two-class method selected |
| **Regression family** | | | | | |
| [Linear regression](./algorithm-module-reference/linear-regression.md?WT.mc_id=docs-article-lazzeri) |Good |Fast |Yes |4 | |
| [Decision forest regression](./algorithm-module-reference/decision-forest-regression.md?WT.mc_id=docs-article-lazzeri)|Excellent |Moderate |No |5 | |
| [Boosted decision tree regression](./algorithm-module-reference/boosted-decision-tree-regression.md?WT.mc_id=docs-article-lazzeri) |Excellent |Moderate |No |6 |Large memory footprint |
| [Neural network regression](./algorithm-module-reference/neural-network-regression.md?WT.mc_id=docs-article-lazzeri) |Good |Moderate |No |8 | |
| **Clustering family** | | | | | |
| [K-means clustering](./algorithm-module-reference/k-means-clustering.md?WT.mc_id=docs-article-lazzeri) |Excellent |Moderate |Yes |8 |A clustering algorithm |

## Requirements for a data science scenario

Once you know what you want to do with your data, you need to determine additional requirements for your solution. 

Make choices and possibly trade-offs for the following requirements:

- Accuracy
- Training time
- Linearity
- Number of parameters
- Number of features

## Accuracy

Accuracy in machine learning measures the effectiveness of a model as the proportion of true results to total cases. In Machine Learning designer, the [Evaluate Model component](./algorithm-module-reference/evaluate-model.md?WT.mc_id=docs-article-lazzeri) computes a set of industry-standard evaluation metrics. You can use this component to measure the accuracy of a trained model.

Getting the most accurate answer possible isn’t always necessary. Sometimes an approximation is adequate, depending on what you want to use it for. If that is the case, you may be able to cut your processing time dramatically by sticking with more approximate methods. Approximate methods also naturally tend to avoid overfitting.
