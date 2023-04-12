
# Overview of forecasting methods in AutoML
This article focuses on the methods that AutoML uses to prepare time series data and build forecasting models. Instructions and examples for training forecasting models in AutoML can be found in our [set up AutoML for time series forecasting](./how-to-auto-train-forecast.md) article.

AutoML uses several methods to forecast time series values. These methods can be roughly assigned to two categories:

1. Time series models that use historical values of the target quantity to make predictions into the future.
2. Regression, or explanatory, models that use predictor variables to forecast values of the target.

As an example, consider the problem of forecasting daily demand for a particular brand of orange juice from a grocery store. Let $y_t$ represent the demand for this brand on day $t$. A **time series model** predicts demand at $t+1$ using some function of historical demand,

$y_{t+1} = f(y_t, y_{t-1}, \ldots, y_{t-s})$. 

The function $f$ often has parameters that we tune using observed demand from the past. The amount of history that $f$ uses to make predictions, $s$, can also be considered a parameter of the model.

The time series model in the orange juice demand example may not be accurate enough since it only uses information about past demand. There are many other factors that likely influence future demand such as price, day of the week, and whether it's a holiday or not. Consider a **regression model** that uses these predictor variables,

$y = g(\text{price}, \text{day of week}, \text{holiday})$.

Again, $g$ generally has a set of parameters, including those governing regularization, that AutoML tunes using past values of the demand and the predictors. We omit $t$ from the expression to emphasize that the regression model uses correlational patterns between _contemporaneously_ defined variables to make predictions. That is, to predict $y_{t+1}$ from $g$, we must know which day of the week $t+1$ falls on, whether it's a holiday, and the orange juice price on day $t+1$. The first two pieces of information are always easily found by consulting a calendar. A retail price is usually set in advance, so the price of orange juice is likely also known one day ahead. However, the price may not be known 10 days into the future! It's important to understand that the utility of this regression is limited by how far into the future we need forecasts, also called the **forecast horizon**, and to what degree we know the future values of the predictors.

> [!IMPORTANT]
> AutoML's forecasting regression models assume that all features provided by the user are known into the future, at least up to the forecast horizon.  

AutoML's forecasting regression models can also be augmented to use historical values of the target and predictors. The result is a hybrid model with characteristics of a time series model and a pure regression model. Historical quantities are additional predictor variables in the regression and we refer to them as **lagged quantities**. The _order_ of the lag refers to how far back the value is known. For example, the current value of an order-two lag of the target for our orange juice demand example is the observed juice demand from two days ago.

Another notable difference between the time series models and the regression models is in the way they generate forecasts. Time series models are generally defined by recursion relations and produce forecasts one-at-a-time. To forecast many periods into the future, they iterate up-to the forecast horizon, feeding previous forecasts back into the model to generate the next one-period-ahead forecast as needed. In contrast, the regression models are so-called **direct forecasters** that generate _all_ forecasts up to the horizon in one go. Direct forecasters can be preferable to recursive ones because recursive models compound prediction error when they feed previous forecasts back into the model. When lag features are included, AutoML makes some important modifications to the training data so that the regression models can function as direct forecasters. See the [lag features article](./concept-automl-forecasting-lags.md) for more details. 
