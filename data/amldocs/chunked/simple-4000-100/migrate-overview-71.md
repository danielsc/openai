1. Modify client applications that invoke Studio (classic) web services to use your new [Azure Machine Learning endpoints](migrate-rebuild-integrate-with-client-app.md).

## Step 5: Cleanup Studio (classic) assets

1. [Clean up Studio (classic) assets](./classic/export-delete-personal-data-dsr.md) to avoid extra charges. You may want to retain assets for fallback until you have validated Azure Machine Learning workloads.

## Step 6: Review and expand scenarios

1. Review the model migration for best practices and validate workloads.
1. Expand scenarios and migrate additional workloads to Azure Machine Learning.


## Studio (classic) and designer component-mapping

Consult the following table to see which modules to use while rebuilding Studio (classic) experiments in the designer.


> [!IMPORTANT]
> The designer implements modules through open-source Python packages rather than C# packages like Studio (classic). Because of this difference, the output of designer components may vary slightly from their Studio (classic) counterparts.


|Category|Studio (classic) module|Replacement designer component|
|--------------|----------------|--------------------------------------|
|Data input and output|- Enter Data Manually </br> - Export Data </br> - Import Data </br> - Load Trained Model </br> - Unpack Zipped Datasets|- Enter Data Manually </br> - Export Data </br> - Import Data|
|Data Format Conversions|- Convert to CSV </br> - Convert to Dataset </br> - Convert to ARFF </br> - Convert to SVMLight </br> - Convert to TSV|- Convert to CSV </br> - Convert to Dataset|
|Data Transformation - Manipulation|- Add Columns</br> - Add Rows </br> - Apply SQL Transformation </br> - Cleaning Missing Data </br> - Convert to Indicator Values </br> - Edit Metadata </br> - Join Data </br> - Remove Duplicate Rows </br> - Select Columns in Dataset </br> - Select Columns Transform </br> - SMOTE </br> - Group Categorical Values|- Add Columns</br> - Add Rows </br> - Apply SQL Transformation </br> - Cleaning Missing Data </br> - Convert to Indicator Values </br> - Edit Metadata </br> - Join Data </br> - Remove Duplicate Rows </br> - Select Columns in Dataset </br> - Select Columns Transform </br> - SMOTE|
|Data Transformation – Scale and Reduce |- Clip Values </br> - Group Data into Bins </br> - Normalize Data </br>- Principal Component Analysis |- Clip Values </br> - Group Data into Bins </br> - Normalize Data|
|Data Transformation – Sample and Split|- Partition and Sample </br> - Split Data|- Partition and Sample </br> - Split Data|
|Data Transformation – Filter |- Apply Filter </br> - FIR Filter </br> - IIR Filter </br> - Median Filter </br> - Moving Average Filter </br> - Threshold Filter </br> - User Defined Filter||
|Data Transformation – Learning with Counts |- Build Counting Transform </br> - Export Count Table </br> - Import Count Table </br> - Merge Count Transform</br>  - Modify Count Table Parameters||
|Feature Selection |- Filter Based Feature Selection </br> - Fisher Linear Discriminant Analysis  </br> - Permutation Feature Importance |- Filter Based Feature Selection </br>  - Permutation Feature Importance|
| Model - Classification| - Multiclass Decision Forest </br> - Multiclass Decision Jungle  </br> - Multiclass Logistic Regression  </br>- Multiclass Neural Network  </br>- One-vs-All Multiclass </br>- Two-Class Averaged Perceptron </br>- Two-Class Bayes Point Machine </br>- Two-Class Boosted Decision Tree  </br> - Two-Class Decision Forest  </br> - Two-Class Decision Jungle  </br> - Two-Class Locally-Deep SVM </br> - Two-Class Logistic Regression  </br> - Two-Class Neural Network </br> - Two-Class Support Vector Machine  | - Multiclass Decision Forest </br>  - Multiclass Boost Decision Tree  </br> - Multiclass Logistic Regression </br> - Multiclass Neural Network </br> - One-vs-All Multiclass  </br> - Two-Class Averaged Perceptron  </br> - Two-Class Boosted Decision Tree  </br> - Two-Class Decision Forest </br>-  Two-Class Logistic Regression </br> - Two-Class Neural Network </br>-   Two-Class Support Vector Machine  |
