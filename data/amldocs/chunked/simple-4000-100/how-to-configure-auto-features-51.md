The following table summarizes techniques that are automatically applied to your data. These techniques are applied for experiments that are configured by using the SDK or the studio UI. To disable this behavior, set `"featurization": 'off'` in your `AutoMLConfig` object.

> [!NOTE]
> If you plan to export your AutoML-created models to an [ONNX model](concept-onnx.md), only the featurization options indicated with an asterisk ("*") are supported in the ONNX format. Learn more about [converting models to ONNX](how-to-use-automl-onnx-model-dotnet.md).

|Featurization&nbsp;steps| Description |
| ------------- | ------------- |
|**Drop high cardinality or no variance features*** |Drop these features from training and validation sets. Applies to features with all values missing, with the same value across all rows, or with high cardinality (for example, hashes, IDs, or GUIDs).|
|**Impute missing values*** |For numeric features, impute with the average of values in the column.<br/><br/>For categorical features, impute with the most frequent value.|
|**Generate more features*** |For DateTime features: Year, Month, Day, Day of week, Day of year, Quarter, Week of the year, Hour, Minute, Second.<br><br> *For forecasting tasks,* these additional DateTime features are created: ISO year, Half - half-year, Calendar month as string, Week, Day of week as string, Day of quarter, Day of year, AM/PM (0 if hour is before noon (12 pm), 1 otherwise), AM/PM as string, Hour of day (12-hr basis)<br/><br/>For Text features: Term frequency based on unigrams, bigrams, and trigrams. Learn more about [how this is done with BERT.](#bert-integration)|
|**Transform and encode***|Transform numeric features that have few unique values into categorical features.<br/><br/>One-hot encoding is used for low-cardinality categorical features. One-hot-hash encoding is used for high-cardinality categorical features.|
|**Word embeddings**|A text featurizer converts vectors of text tokens into sentence vectors by using a pre-trained model. Each word's embedding vector in a document is aggregated with the rest to produce a document feature vector.|
|**Cluster Distance**|Trains a k-means clustering model on all numeric columns. Produces *k* new features (one new numeric feature per cluster) that contain the distance of each sample to the centroid of each cluster.|

In every automated machine learning experiment, your data is automatically scaled or normalized to help algorithms perform well. During model training, one of the following scaling or normalization techniques are applied to each model. 

|Scaling&nbsp;&&nbsp;processing| Description |
| ------------- | ------------- |
| [StandardScaleWrapper](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)  | Standardize features by removing the mean and scaling to unit variance  |
| [MinMaxScalar](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)  | Transforms features by scaling each feature by that column's minimum and maximum  |
| [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler) |Scale each feature by its maximum absolute value |
| [RobustScalar](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html) | Scales features by their quantile range |
| [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) |Linear dimensionality reduction using Singular Value Decomposition of the data to project it to a lower dimensional space |
| [TruncatedSVDWrapper](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html) |This transformer performs linear dimensionality reduction by means of truncated singular value decomposition (SVD). Contrary to PCA, this estimator does not center the data before computing the singular value decomposition, which means it can work with scipy.sparse matrices efficiently |
