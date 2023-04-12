The function `generate_data_transformation_config()` specifies the featurization step in the final scikit-learn pipeline. The featurizers from the original experiment are reproduced here, along with their parameters.

For example, possible data transformation that can happen in this function can be based on imputers like, `SimpleImputer()` and `CatImputer()`, or transformers such as `StringCastTransformer()` and `LabelEncoderTransformer()`. 

The following is a transformer of type `StringCastTransformer()` that can be used to transform a set of columns. In this case, the set indicated by `column_names`.

```python    
def get_mapper_0(column_names):
    # ... Multiple imports to package dependencies, removed for simplicity ...
    
    definition = gen_features(
        columns=column_names,
        classes=[
            {
                'class': StringCastTransformer,
            },
            {
                'class': CountVectorizer,
                'analyzer': 'word',
                'binary': True,
                'decode_error': 'strict',
                'dtype': numpy.uint8,
                'encoding': 'utf-8',
                'input': 'content',
                'lowercase': True,
                'max_df': 1.0,
                'max_features': None,
                'min_df': 1,
                'ngram_range': (1, 1),
                'preprocessor': None,
                'stop_words': None,
                'strip_accents': None,
                'token_pattern': '(?u)\\b\\w\\w+\\b',
                'tokenizer': wrap_in_lst,
                'vocabulary': None,
            },
        ]
    )
    mapper = DataFrameMapper(features=definition, input_df=True, sparse=True)
    
    return mapper
```

Be aware that if you have many columns that need to have the same featurization/transformation applied (for example, 50 columns in several column groups), these columns are handled by grouping based on type. 

In the following example, notice that each group has a unique mapper applied. This mapper is then applied to each of the columns of that group.

```python
def generate_data_transformation_config():
    from sklearn.pipeline import FeatureUnion
    
    column_group_1 = [['id'], ['ps_reg_01'], ['ps_reg_02'], ['ps_reg_03'], ['ps_car_11_cat'], ['ps_car_12'], ['ps_car_13'], ['ps_car_14'], ['ps_car_15'], ['ps_calc_01'], ['ps_calc_02'], ['ps_calc_03']]
    
    column_group_2 = ['ps_ind_06_bin', 'ps_ind_07_bin', 'ps_ind_08_bin', 'ps_ind_09_bin', 'ps_ind_10_bin', 'ps_ind_11_bin', 'ps_ind_12_bin', 'ps_ind_13_bin', 'ps_ind_16_bin', 'ps_ind_17_bin', 'ps_ind_18_bin', 'ps_car_08_cat', 'ps_calc_15_bin', 'ps_calc_16_bin', 'ps_calc_17_bin', 'ps_calc_18_bin', 'ps_calc_19_bin', 'ps_calc_20_bin']
    
    column_group_3 = ['ps_ind_01', 'ps_ind_02_cat', 'ps_ind_03', 'ps_ind_04_cat', 'ps_ind_05_cat', 'ps_ind_14', 'ps_ind_15', 'ps_car_01_cat', 'ps_car_02_cat', 'ps_car_03_cat', 'ps_car_04_cat', 'ps_car_05_cat', 'ps_car_06_cat', 'ps_car_07_cat', 'ps_car_09_cat', 'ps_car_10_cat', 'ps_car_11', 'ps_calc_04', 'ps_calc_05', 'ps_calc_06', 'ps_calc_07', 'ps_calc_08', 'ps_calc_09', 'ps_calc_10', 'ps_calc_11', 'ps_calc_12', 'ps_calc_13', 'ps_calc_14']
    
    feature_union = FeatureUnion([
        ('mapper_0', get_mapper_0(column_group_1)),
        ('mapper_1', get_mapper_1(column_group_3)),
        ('mapper_2', get_mapper_2(column_group_2)),
    ])
    return feature_union
```

This approach allows you to have a more streamlined code, by not having a transformer's code-block for each column, which can be especially cumbersome even when you have tens or hundreds of columns in your dataset.

With classification and regression tasks, [`FeatureUnion`] is used for featurizers.
For time-series forecasting models, multiple time series-aware featurizers are collected into a scikit-learn pipeline, then wrapped in the `TimeSeriesTransformer`.
Any user provided featurizations for time series forecasting models happens before the ones provided by automated ML. 

### Preprocessor specification code
