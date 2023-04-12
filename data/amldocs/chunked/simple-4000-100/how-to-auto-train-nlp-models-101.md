> For example, if your label is `"cs.AI"`, it's read as `"cs"` and `"AI"`. Whereas with the Python list format, the label would be `"['cs.AI']"`, which is read as `"cs.AI"` .


Example data for multi-label in plain text format. 

```
text,labels
"I love watching Chicago Bulls games.","basketball"
"The four most popular leagues are NFL, MLB, NBA and NHL","football,baseball,basketball,hockey"
"I like drinking beer.",""
```

Example data for multi-label in Python list with quotes format. 

``` python
text,labels
"I love watching Chicago Bulls games.","['basketball']"
"The four most popular leagues are NFL, MLB, NBA and NHL","['football','baseball','basketball','hockey']"
"I like drinking beer.","[]"
```

### Named entity recognition (NER)

Unlike multi-class or multi-label, which takes `.csv` format datasets, named entity recognition requires CoNLL format. The file must contain exactly two columns and in each row, the token and the label is separated by a single space. 

For example,

``` 
Hudson B-loc
Square I-loc
is O
a O
famous O
place O
in O
New B-loc
York I-loc
City I-loc

Stephen B-per
Curry I-per
got O
three O
championship O
rings O
```

### Data validation

Before training, automated ML applies data validation checks on the input data to ensure that the data can be preprocessed correctly. If any of these checks fail, the run fails with the relevant error message. The following are the requirements to pass data validation checks for each task.

> [!Note]
> Some data validation checks are applicable to both the training and the validation set, whereas others are applicable only to the training set. If the test dataset could not pass the data validation, that means that automated ML couldn't capture it and there is a possibility of model inference failure, or a decline in model performance.

Task | Data validation check
---|---
All tasks | At least 50 training samples are required 
Multi-class and Multi-label | The training data and validation data must have <br> - The same set of columns <br>- The same order of columns from left to right <br>- The same data type for columns with the same name <br>- At least two unique labels <br>  - Unique column names within each dataset (For example, the training set can't have multiple columns named **Age**)
Multi-class only | None
Multi-label only | - The label column format must be in [accepted format](#multi-label) <br> - At least one sample should have 0 or 2+ labels, otherwise it should be a `multiclass` task <br> - All labels should be in `str` or `int` format, with no overlapping. You should not have both label `1` and label `'1'`
NER only | - The file should not start with an empty line <br> - Each line must be an empty line, or follow format `{token} {label}`, where there is exactly one space between the token and the label and no white space after the label <br> - All labels must start with `I-`, `B-`, or be exactly `O`. Case sensitive <br> -  Exactly one empty line between two samples <br> - Exactly one empty line at the end of the file
   
## Configure experiment

Automated ML's NLP capability is triggered through task specific `automl` type jobs, which is the same workflow for submitting automated ML experiments for classification, regression and forecasting tasks. You would set parameters as you would for those experiments, such as `experiment_name`, `compute_name` and data inputs. 

However, there are key differences: 
* You can ignore `primary_metric`, as it is only for reporting purposes. Currently, automated ML only trains one model per run for NLP and there is no model selection.
* The `label_column_name` parameter is only required for multi-class and multi-label text classification tasks.
* If more than 10% of the samples in your dataset contain more than 128 tokens, it's considered long range. 
   * In order to use the long range text feature, you should use a NC6 or higher/better SKUs for GPU such as: [NCv3](../virtual-machines/ncv3-series.md) series or [ND](../virtual-machines/nd-series.md) series.
