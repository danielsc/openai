## Findings
- Hyperparameter tuning for fine-tuning is useful. Outof 83 runs, the best model was 20 percentage points better than the median model.
![](images/f1_score.png)

| stat | value |
| --- | --- |
| count |   83.000000 |
| mean    |  0.265154 |
| min     | 0.008580|
| 50%    |   0.307420|
| max      | 0.506950|

- Even if we drop all runs that have an f1 score below 0.1, the best model is still >17 percentage points better than the median (and the mean) model.

| stat | value |
| --- | --- |
| count   | 65.000000
| mean |     0.335467 
|min|       0.219880
|50% |      0.332230
|max |     0.506950


## Issues:

- AOAI: Having only accuracy and f1_score as metrics to evaluate is quite limiting. In the case of a Yelp 1-5 rating, it seems that MSE might be a better metric to optimize for. Not sure if modeling this as a regression task would be feasible or advised with OpenAI. 

- AzureML: To enable early stopping, we need to allow the job to react to cancellation by hyperdrive, such that the fine_tune operation on the AOAI side get's cancelled, too (https://msdata.visualstudio.com/Vienna/_workitems/edit/1351560)

- AzureML: cannot see other than primary metric in the table of trials

- AOAI: Where is the reference documentation for the AOAI Python SDK? 

- AOAI: Where is the documenation for the Azure-specific extensions to the AOAI service, for instance hyperparameters to control **LORA**?
