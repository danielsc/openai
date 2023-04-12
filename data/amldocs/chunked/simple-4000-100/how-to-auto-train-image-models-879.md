Using Explainable AI in AutoML for Images on the deployed endpoint, users can get **visualizations** of explanations (attributions overlaid on an input image) and/or **attributions** (multi-dimensional array of size `[3, valid_crop_size, valid_crop_size]`) for each image. Apart from visualizations, users can also get attribution matrices to gain more control over the explanations (like generating custom visualizations using attributions or scrutinizing segments of attributions). All the explanation algorithms will use cropped square images with size `valid_crop_size` for generating attributions.


Explanations can be generated either from **online endpoint** or **batch endpoint**. Once the deployment is done, this endpoint can be utilized to generate the explanations for predictions. In case of online deployment, make sure to pass `request_settings = OnlineRequestSettings(request_timeout_ms=90000)` parameter to `ManagedOnlineDeployment` and set `request_timeout_ms` to its maximum value to avoid **timeout issues** while generating explanations (refer to [register and deploy model section](#register-and-deploy-model)). Some of the explainability (XAI) methods like `xrai` consume more time (specially for multi-label classification as we need to generate attributions and/or visualizations against each predicted label). So, we recommend any GPU instance for faster explanations. For more information on input and output schema for generating explanations, see the [schema docs](reference-automl-images-schema.md#data-format-for-online-scoring-and-explainability-xai).


We support following state-of-the-art explainability algorithms in AutoML for images:
   - [XRAI](https://arxiv.org/abs/1906.02825) (xrai)
   - [Integrated Gradients](https://arxiv.org/abs/1703.01365) (integrated_gradients)
   - [Guided GradCAM](https://arxiv.org/abs/1610.02391v4) (guided_gradcam)
   - [Guided BackPropagation](https://arxiv.org/abs/1412.6806) (guided_backprop)

Following table describes the explainability algorithm specific tuning parameters for XRAI and Integrated Gradients. Guided backpropagation and guided gradcam don't require any tuning parameters.

| XAI algorithm | Algorithm specific parameters  | Default Values |
|--------- |------------- | --------- |
| `xrai` | 1. `n_steps`: The number of steps used by the approximation method. Larger number of steps lead to better approximations of attributions (explanations). Range of n_steps is [2, inf), but the performance of attributions starts to converge after 50 steps. <br> `Optional, Int` <br><br> 2. `xrai_fast`: Whether to use faster version of XRAI. if `True`, then computation time for explanations is faster but leads to less accurate explanations (attributions) <br>`Optional, Bool` <br> | `n_steps = 50` <br> `xrai_fast = True` |
| `integrated_gradients` | 1. `n_steps`: The number of steps used by the approximation method. Larger number of steps lead to better attributions (explanations). Range of n_steps is [2, inf), but the performance of attributions starts to converge after 50 steps.<br> `Optional, Int` <br><br> 2. `approximation_method`: Method for approximating the integral. Available approximation methods are `riemann_middle` and `gausslegendre`.<br> `Optional, String` | `n_steps = 50` <br> `approximation_method = riemann_middle` |


Internally XRAI algorithm uses integrated gradients. So, `n_steps` parameter is required by both integrated gradients and XRAI algorithms. Larger number of steps consume more time for approximating the explanations and it may result in timeout issues on the online endpoint.

We recommend using XRAI > Guided GradCAM > Integrated Gradients > Guided BackPropagation algorithms for better explanations, whereas Guided BackPropagation > Guided GradCAM > Integrated Gradients > XRAI are recommended for faster explanations in the specified order.

A sample request to the online endpoint looks like the following. This request generates explanations when `model_explainability` is set to `True`. Following request will generate visualizations and attributions using faster version of XRAI algorithm with 50 steps.
