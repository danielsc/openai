- Professionals in heavily regulated spaces who need to review machine learning models with regulators and auditors

## Supported scenarios and limitations

- The Responsible AI dashboard currently supports regression and classification (binary and multi-class) models trained on tabular structured data. 
- The Responsible AI dashboard currently supports MLflow models that are registered in Azure Machine Learning with a sklearn (scikit-learn) flavor only. The scikit-learn models should implement `predict()/predict_proba()` methods, or the model should be wrapped within a class that implements `predict()/predict_proba()` methods. The models must be loadable in the component environment and must be pickleable.
- The Responsible AI dashboard currently visualizes up to 5K of your data points on the dashboard UI. You should downsample your dataset to 5K or less before passing it to the dashboard.
- The dataset inputs to the Responsible AI dashboard must be pandas DataFrames in Parquet format. NumPy and SciPy sparse data is currently not supported. 
- The Responsible AI dashboard currently supports numeric or categorical features. For categorical features, the user has to explicitly specify the feature names.  
- The Responsible AI dashboard currently doesn't support datasets with more than 10K columns.


## Next steps

- Learn how to generate the Responsible AI dashboard via [CLI and SDK](how-to-responsible-ai-insights-sdk-cli.md) or [Azure Machine Learning studio UI](how-to-responsible-ai-insights-ui.md).
- Learn how to generate a [Responsible AI scorecard](concept-responsible-ai-scorecard.md) based on the insights observed on the Responsible AI dashboard.
