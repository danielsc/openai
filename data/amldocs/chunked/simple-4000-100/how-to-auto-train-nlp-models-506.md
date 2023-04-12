

## Known Issues

Dealing with very low scores, or higher loss values: 

For certain datasets, regardless of the NLP task, the scores produced may be very low, sometimes even zero. This would be accompanied by higher loss values implying that the neural network failed to converge. This can happen more frequently on certain GPU SKUs.

While such cases are uncommon, they're possible and the best way to handle it is to leverage hyperparameter tuning and provide a wider range of values, especially for hyperparameters like learning rates. Until our hyperparameter tuning capability is available in production we recommend users, who face such issues, to leverage the NC6 or ND6 compute clusters, where we've found training outcomes to be fairly stable.

## Next steps

+ [Deploy AutoML models to an online (real-time inference) endpoint](how-to-deploy-automl-endpoint.md)
+ [Troubleshoot automated ML experiments](how-to-troubleshoot-auto-ml.md)
