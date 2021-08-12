# Time Series Forecasting With ARIMA
# (Autoregressive Integrated Moving Average)

- [Time Series Forecasting With ARIMA](#time-series-forecasting-with-arima)
- [(Autoregressive Integrated Moving Average)](#autoregressive-integrated-moving-average)
  - [Introduction](#introduction)
  - [Basic](#basic)
    - [Part 1: Data Exploration](#part-1-data-exploration)
  - [Advanced](#advanced)
    - [Part 2: Box-Jenkins Method](#part-2-box-jenkins-method)
  - [Extra Credit](#extra-credit)
    - [Part 3: LAPD Calls For Service](#part-3-lapd-calls-for-service)

## Introduction
Using New York City Uber pickups data, we will forecast future trip volume.

## Basic
### Part 1: Data Exploration

1. Load the data from `data/uber.zip` and store it as a pandas Series called `rides`. The data
consists of timestamps for when customers are picked up, so set the appropriate arguments to
convert these values into a datetime format like so (what do the arguments do?):

    ```python
    import pandas as pd
    rides = pd.read_csv(
        'data/uber-aprsep-14.csv.zip', squeeze=True, parse_dates=['date'])
    ```

2. Create a pandas Series where the values are all 1 and the index are the timestamps that you
loaded using the following code:  

    ```python
    rides = pd.Series(1, index=rides)
    ```

    Your series should now look like this (where the left column is your index):

    ```
    >>> rides.head()
    date
    2014-04-01 00:11:00    1
    2014-04-01 00:17:00    1
    2014-04-01 00:21:00    1
    2014-04-01 00:28:00    1
    2014-04-01 00:33:00    1
    dtype: int64
    ```

3. Convert the data to hourly ride counts. (Look at the [documentation][1] for the `resample`
method, particularly the Notes and Examples sections.)  

    Your hourly data should look like this:

    ```
    >>> rides_hourly.head()
    date
    2014-04-01 00:00:00    138
    2014-04-01 01:00:00     66
    2014-04-01 02:00:00     53
    2014-04-01 03:00:00     93
    2014-04-01 04:00:00    166
    Freq: H, dtype: int64
    ```

<!-- Links -->
[1]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html

4. Plot the hourly ride counts. Comment on the presence of trends, seasonality and cycles. You can
zoom in on smaller time periods if the data is too dense like so (set your own start and end dates):

  ```python
  rides_hourly['2014-04-01':'2014-09-30']
  ```

5. Seasonal subseries plots are another way to visualize time series data, where the data for each
'season' are plotted as their own series. It can help detect seasonality in data for a selected
periodicity. Below are seasonal subseries plots for hourly and daily rides. Comment on the presence
of trends, seasonality and cycles.

    <div align='center'>
        <img src='images/hourly-subseries.png'/>
    </div>

    <div align='center'>
        <img src='images/daily-subseries.png'/>
    </div>

## Advanced
### Part 2: Box-Jenkins Method
We will follow the Box-Jenkins method to identify ARIMA models, starting with a non-seasonal ARIMA
model before tackling more complex seasonal ARIMA models (SARIMA).

<div align='center'>
    <img src='images/box-jenkins-method.png' width=500/>
</div>

6.  Create a Series for **weekly** rides and plot it. Discard the final observation because it is
only a partial week. We can only use the Box-Jenkins method to identify patterns in stationary
data. Do you think this time series is stationary? Comment on the presence of trends, seasonality
and cycles, and on how the data varies with time.

7. When the series appears to have nonconstant variance (amount of variation depends on the level
of the series or particular periods of time), we can apply a mathematical transformation to try to
make the variance more constant.  

    A useful family of transformations is the Box-Cox transformations ([Box & Cox, 1964][2]), which
    transforms data using a parameter $\lambda$ as follows:

    <div align='center'>
        <img src='images/box-cox-1.png'>
    </div>

    <!-- $$
        y^{\left( \lambda \right)} = 
        \begin{cases}
            \frac{y^{\lambda} - 1}{\lambda} &(\lambda \neq 0)\\
            \log y &(\lambda = 0)
        \end{cases}
        $$ -->

        This is conceptually equivalent (**but not equivalent in implementation**) to:

    <div align='center'>
        <img src='images/box-cox-2.png'>
    </div>

    <!-- $$
        y^{\left( \lambda \right)} = 
        \begin{cases}
            y^{\lambda} &(\lambda \neq 0)\\
            \log y &(\lambda = 0)
        \end{cases}
        $$ -->

    So $\lambda$ can be interpreted as transforming the data by raising it to the power $\lambda$,
    or taking the natural log if $\lambda$ = 0.

    A Box-Cox transformation makes the distribution of the data more normal-like, which is the
    basis for determining confidence intervals for $\lambda$. Use the following code to find a 95%
    confidence interval for $\lambda$ using [scipy.stats.boxcox][3]. If 1 is in the confidence
    interval, the data does not need to be transformed. Why?

    ```python
    from scipy.stats import boxcox
    transformed, lmbda, ci = boxcox(rides_weekly, alpha=0.05)
    print(ci)
    ```

<!-- Links -->
[2]: http://www.econ.uiuc.edu/~econ536/Papers/boxcox64.pdf
[3]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boxcox.html

8. In addition to visually inspecting the data, we can inspect the ACF plot of the data.
Non-stationary time series will have ACF plots that decrease slowly (exponential decay). However,
if the autocorrelation values decrease quickly, it does not necessarily mean the data is
stationary. Use the code below to create an ACF (autocorrelation function) plot of the data. Is the
data stationary?

    ```python
    import statsmodels.api as sm
    rides_weekly = rides.resample('W').count()[:-1]
    _ = sm.graphics.tsa.plot_acf(rides_weekly)
    ```

9. We can also use statistical hypothesis tests to determine whether data are stationary. Two
popular tests are the augmented Dickey-Fuller (ADF) test and the Kwiatowski-Phillips-Schmidt-Shin
(KPSS) test. Be careful interpreting the results of the tests as the null hypothesis of the ADF
test is that a series is non-stationary but the null hypothesis of the KPSS test is the opposite,
that a series is stationary.  

    The ADF test is more widely known, but the KPSS test is the default in the R programming language's
`auto.arima` function of the `forecast` package, due to its [better real-world performance.][4]  

    Contrary to what you may see online, there is no reason to perform both tests on the same data.
They test for the same aspect of non-stationarity (presence of a unit root) and in practice,
[using the ADF test will lead to more differencing of the data than using the KPSS test.][4] Also,
performing both tests sometimes leads to contradictory results.  

    You can import the tests using the code below:

    ```python
    from statsmodels.tsa.stattools import adfuller, kpss
    ```

    Perform both tests on the data and interpret the results (remember to use only one of these
    tests in the future when you do your own forecasting projects.)

<!-- Links -->
[4]: https://robjhyndman.com/hyndsight/unit-root-tests/

10. Hopefully you have concluded that the data is not stationary because the mean is not constant
over time (there is an increasing trend.) We can either detrend or difference the data to remove trends.

    Detrending involves fitting a model to the data where the predictor is time, and then
    subtracting the predicted values from the observed data values.

    Differencing involves taking the difference between consecutive observations, and should not be
    done more than 2 times in practice for nonseasonal models. Additionally, differencing data when
    it is not necessary (overdifferencing) can introduce new structure into the data and result in
    unnecessarily complicated models.

    Difference the non-stationary data and then investigate whether it is still non-stationary:

    ```python
    rides_weekly.diff().dropna()  # Drop NaNs to avoid exceptions during investigations.
    ```

11. We can now identify potential ARIMA(p, d, q) models for our data, where p represents the AR
(autoregressive) order, d represents the difference order and q represents the MA (moving average)
order.

    Inspecting ACF plots can suggest an MA order and inspecting PACF plots can suggest an AR order.

    The ACF of an MA(q) process will truncate after the qth lag. The PACF of an AR(p) process will
    truncate after the pth lag.

    Use the following code to generate plots:

    ```python
    import matplotlib.pyplot as plt
    import statmodels.api as sm
    fig, axs = plt.subplots(2, sharex=True, figsize=(16, 4.5))
    sm.graphics.tsa.plot_acf(rides_diff, ax=axs[0])
    sm.graphics.tsa.plot_pacf(rides_diff, ax=axs[1], lags=11, method='ywmle')
    plt.show()
    ```

    Propose p and q based on ACF and PACF plots. Propose d (how many times was the data
    differenced?)

12. In converting the data to weekly rides, we lost a lot of information. We were forced to do so
because ARIMA cannot model seasonal patterns. Let's extend the ARIMA framework to model seasonal
patterns (seasonal ARIMA aka SARIMA). Instead of forecasting weekly rides, we will forecast daily rides.

    *Note: The raw data has weekly and hourly seasonality, but SARIMA can only handle one season.
    Multiple seasonality is beyond the scope of this immersive.*

    Assess the daily rides data for nonconstant variance and apply transformations as appropriate.

13. Is the transformed data stationary? Try a stationarity test.

14. Plot the transformed data. Is it stationary?

    *Note: Stationarity tests cannot detect violations of stationarity due to seasonality.*

15. Use plots, differencing and stationarity tests to make the data stationary. Use this code to
get started:

    ```python
    rides_daily = rides.resample('D').count()
    transformed, _ = boxcox(rides_daily)
    transformed = pd.Series(transformed, index=rides_daily.index)
    # Remove seasonal patterns that occur within 7 day periods.
    transformed.diff(periods=7).dropna()
    ```

    *Note: You may also detrend the data by fitting a model where the data is the target and values
    of time are the predictor. Stick to differencing for this assignment.*

16. Make ACF and PACF plots of the stationary data.

17. The seasonal ARIMA(p, d, q)x(P, D, Q)$_m$ indicates ARIMA orders of *p*, *d* and *q*, and
season-level AR, differencing and MA orders of *P*, *D* and *Q*, respectively.  
    *m* represents the seasonal period (e.g. Monthly data across years may have a season of 12.
    Daily data may have a weekly season, or *m*=7. Hourly data may have a daily season, or *m*=24.)  
    We identified AR and MA orders *p* and *q* in ARIMA by looking for the lag where values
    abruptly drop-off.
    Similarly in SARIMA, we can identify *P*, the seasonal MA order, and *Q*, the seasonal AR order,
    by looking at lags which correspond to multiples of the period *m*, and examining the pattern
    of decay.

    Propose *P* and *Q* for a seasonal ARIMA model that fits the data. What is the value of *D*?
    What is the value of *m*?

    Also propose *p*, *d* and *q* based on the ACF and PACF plots.

18. A few more potential SARIMA models were identified by following [this guide][5]. The
non-seasonal and seasonal orders of the model are show below in the format
`(p, d, q), (P, D, Q, m)`.

    ```python
    models = [[(0, 0, 1), (3, 1, 1, 7)],
              [(0, 0, 1), (0, 1, 1, 7)],
              [(0, 1, 1), (0, 1, 1, 7)],
              [(0, 1, 2), (0, 1, 1, 7)],
              [(1, 0, 1), (0, 1, 1, 7)],
              [(2, 0, 1), (0, 1, 1, 7)],
              [(3, 0, 1), (0, 1, 1, 7)]]
    ```

    What follows is a demonstration of how to compare various SARIMA models.

    <!-- Links -->
    [5]: https://people.duke.edu/~rnau/Slides_on_ARIMA_models--Robert_Nau.pdf


    ```python
    import numpy as np
    # Print dictionaries in a nicer format.
    import pprint
    # Common model metric for forecasting.
    from sklearn.metrics import mean_absolute_percentage_error
    # Time series cross-validation.
    from sklearn.model_selection import TimeSeriesSplit, train_test_split

    # ARIMA(p, d, q)x(P, D, Q)m orders + trend.
    models = [[(0, 0, 1), (3, 1, 1, 7), 'n'],
              [(0, 0, 1), (0, 1, 1, 7), 'n'],
              [(0, 1, 1), (0, 1, 1, 7), 'n'],
              [(0, 1, 2), (0, 1, 1, 7), 'n'],
              [(1, 0, 1), (0, 1, 1, 7), 'c'],
              [(2, 0, 1), (0, 1, 1, 7), 'c'],
              [(3, 0, 1), (0, 1, 1, 7), 'c']]  # Evaluate AutoARIMA model from exercise 19.
    # Record model scores.
    model_scores = dict()
    # `shuffle=False` splits the time series into two periods. Otherwise
    # observations would be randomly selected from across the series to
    # produce a test set.
    # The test set is 2 weeks long because that is the forecast horizon we
    # are interested in.
    y_train, y_test = train_test_split(
        rides_daily, test_size=0.075, shuffle=False)
    # Optimize model for forecasting the next 2 weeks (14 days).
    tscv = TimeSeriesSplit(test_size=14)

    for (p, d, q), (P, D, Q, m), trend in models:
        # Identify which models are producing warnings.
        # print(f'{(p, d, q)}x{(P, D, Q)}{m}')
        scores = []
        for cvtrain_i, cvtest_i in tscv.split(y_train):
            # Fit model. Powell optimizer converges better than other
            # methods.
            res = sm.tsa.statespace.SARIMAX(
                y_train[cvtrain_i], order=(p, d, q),
                seasonal_order=(P, D, Q, m),
                trend=trend).fit(method='powell', disp=False)
            # Score model.
            y_true = y_train[cvtest_i]
            mape = mean_absolute_percentage_error(
                y_true, res.predict(y_true.index[0], y_true.index[-1]))
            scores.append(mape)
        # Average and standard deviation of cross-validation scores.
        scores = np.asarray(scores)
        model_scores[f'{(p, d, q)}x{(P, D, Q)}{m}'] = [scores.mean().round(4),
                                                       scores.std().round(4)]

    pprint.pprint(model_scores)
    ```

        {'(0, 0, 1)x(0, 1, 1)7': [0.1512, 0.0939],
         '(0, 0, 1)x(3, 1, 1)7': [0.1552, 0.0914],
         '(0, 1, 1)x(0, 1, 1)7': [0.1081, 0.0552],
         '(0, 1, 2)x(0, 1, 1)7': [0.1235, 0.0579],
         '(1, 0, 1)x(0, 1, 1)7': [0.111, 0.0377],
         '(2, 0, 1)x(0, 1, 1)7': [0.1118, 0.0377],
         '(3, 0, 1)x(0, 1, 1)7': [0.1097, 0.0362]}


    *The ARIMA(0, 1, 1)x(0, 1, 1)7 appears to be the best predictive model out of the potential models
    based on MAPE. The model equation can be written explicitly as follows:*  

    <div align='center'>
        <img src='images/sarima-model-equation.png'>
    </div>

    <!-- *$B$ is the backshift operator, defined as: $B y_t = y_{t-1}$*    

    $$
    \begin{align*}
    (1 - B)(1 - B^{7})y_t &= (1 - \theta_1 B)(1 - \Theta_1 B^7)e_t \\
    (1 - B - B^7 + B^8)y_t &= (1 - \theta_1 B - \Theta_1 B^7 
    + \theta_1 \Theta_1 B^8)e_t \\
    y_t - y_{t-1} - y_{t-7} + y_{t-8} &= e_t - \theta_1 e_{t-1}
    - \Theta_1 e_{t-7} + \theta_1 \Theta_1 e_{t-8} \\
    y_t &= y_{t-1} + y_{t-7} - y_{t-8} + e_t - \theta_1 e_{t-1}
    - \Theta_1 e_{t-7} + \theta_1 \Theta_1 e_{t-8} \\
    y_t &= y_{t-1} + y_{t-7} - y_{t-8} + e_t - 0.3306 e_{t-1}
    - 0.8842 e_{t-7} + (-0.3306)*(-0.8842) e_{t-8}
    \end{align*}
    $$

    $$
    y_t = y_{t-1} + y_{t-7} - y_{t-8} + e_t - 0.3306 e_{t-1}
    - 0.8842 e_{t-7} + 0.2923 e_{t-8}
    $$ -->

    *We can investigate the model diagnostics to evaluate the quality of forecast intervals.*  
    *The Ljung-Box p-value=0.63, so there is not enough evidence to conclude that the model residuals
    are correlated. The residuals appear uncorrelated (lower right plot) so there is no leftover
    structure to add to our model.*  

    *The heteroskedascity test p-value=0.06, so there is not enough evidence to conclude that the
    variation of the residuals is different between the beginning and end of the data series (upper
    left plot). This is good for our forecast interval.*  

    *The Jarque-Bera test p-value=0.00, so there is evidence that the residuals do not follow a Normal
    distribution (top right and bottom left plot). This is bad for our forecast interval.*  

    *These statistical test results suggest that automatically generated forecast intervals and
    the default statistical significance tests of the model coefficients will not be accurate, but the
    model will still be useful for predicting mean trends.*  
    *You can use bootstrapping to generate intervals, but you will have to implement it on your own.*


    ```python
    # Investigate diagnostics of selected model.

    from IPython.display import display

    res = sm.tsa.statespace.SARIMAX(
        y_train, order=(0, 1, 1),
        seasonal_order=(0, 1, 1, 7)).fit(method='powell', disp=False)
    display(res.summary())

    fig, ax = plt.subplots(figsize=(16, 9), tight_layout=True)
    res.plot_diagnostics(fig=fig)
    plt.show()
    ```


    <table class="simpletable">
    <caption>SARIMAX Results</caption>
    <tr>
      <th>Dep. Variable:</th>                 <td>y</td>               <th>  No. Observations:  </th>    <td>169</td>   
    </tr>
    <tr>
      <th>Model:</th>           <td>SARIMAX(0, 1, 1)x(0, 1, 1, 7)</td> <th>  Log Likelihood     </th> <td>-1527.969</td>
    </tr>
    <tr>
      <th>Date:</th>                  <td>Sun, 28 Mar 2021</td>        <th>  AIC                </th> <td>3061.938</td> 
    </tr>
    <tr>
      <th>Time:</th>                      <td>06:03:58</td>            <th>  BIC                </th> <td>3071.183</td> 
    </tr>
    <tr>
      <th>Sample:</th>                   <td>04-01-2014</td>           <th>  HQIC               </th> <td>3065.692</td> 
    </tr>
    <tr>
      <th></th>                         <td>- 09-16-2014</td>          <th>                     </th>     <td> </td>    
    </tr>
    <tr>
      <th>Covariance Type:</th>              <td>opg</td>              <th>                     </th>     <td> </td>    
    </tr>
    </table>
    <table class="simpletable">
    <tr>
         <td></td>        <th>coef</th>     <th>std err</th>      <th>z</th>      <th>P>|z|</th>  <th>[0.025</th>    <th>0.975]</th>  
    </tr>
    <tr>
      <th>ma.L1</th>   <td>   -0.3306</td> <td>    0.051</td> <td>   -6.516</td> <td> 0.000</td> <td>   -0.430</td> <td>   -0.231</td>
    </tr>
    <tr>
      <th>ma.S.L7</th> <td>   -0.8842</td> <td>    0.072</td> <td>  -12.214</td> <td> 0.000</td> <td>   -1.026</td> <td>   -0.742</td>
    </tr>
    <tr>
      <th>sigma2</th>  <td> 9.828e+06</td> <td> 7.89e+05</td> <td>   12.458</td> <td> 0.000</td> <td> 8.28e+06</td> <td> 1.14e+07</td>
    </tr>
    </table>
    <table class="simpletable">
    <tr>
      <th>Ljung-Box (L1) (Q):</th>     <td>0.23</td> <th>  Jarque-Bera (JB):  </th> <td>35.03</td>
    </tr>
    <tr>
      <th>Prob(Q):</th>                <td>0.63</td> <th>  Prob(JB):          </th> <td>0.00</td> 
    </tr>
    <tr>
      <th>Heteroskedasticity (H):</th> <td>0.59</td> <th>  Skew:              </th> <td>0.15</td> 
    </tr>
    <tr>
      <th>Prob(H) (two-sided):</th>    <td>0.06</td> <th>  Kurtosis:          </th> <td>5.27</td> 
    </tr>
    </table><br/><br/>Warnings:<br/>[1] Covariance matrix calculated using the outer product of gradients (complex-step).




    ![png](images/output_57_1.png)



    *The model predicts the end of September well.*  
    *If you investigate other models, you will find that this model has relatively large confidence
    intervals, so there is a lot of uncertainty in the forecast.*  
    *The model achieves an MAPE of 10.2% on the test set, which is similar to the cross-validation
    performance of 10.8%.*


    ```python
    # Plot prediction performance on test set.
    # The confidence intervals are inaccurate because the assumptions
    # underlying their equations were not satisfied.
    # You can use bootstrapping to generate intervals, but you will have to
    # implement it on your own.
    predict = res.get_prediction(y_test.index[0], y_test.index[-1])
    predict_ci = predict.conf_int()
    mape = mean_absolute_percentage_error(y_test, predict.predicted_mean)

    fig, ax = plt.subplots(figsize=(16, 4.5))
    ax.plot(y_train, 'k')
    ax.plot(y_test, 'k')
    ax.plot(predict.predicted_mean, 'b',
            label='ARIMA(0, 1, 1)x(0, 1, 1)$_7$')
    ax.fill_between(
        predict_ci.index, predict_ci['lower y'], predict_ci['upper y'],
        alpha=0.5, color='b', label='95% CI')
    ax.fill_between(
        predict_ci.index, predict.predicted_mean, y_test,
        alpha=0.5, color='r', label=f'MAPE: {mape:.3f}')
    ax.set(title='Daily Rides', xlabel='Date', ylabel='Rides')
    ax.legend(loc='upper left', fontsize='x-large')
    plt.show()
    ```



    ![png](images/output_59_0.png)
    


19. R users will be familiar with the `auto.arima` function in the R `forecast` package, which searches for a combination of ARIMA parameters that produces good predictive models based on a stepwise-algorithm ([Hyndman & Khandakar, 2008][6]).

    The Python `pmdarima` library ([installation instructions][7]) is actively maintained* (as of 2021) and emulates the functionality of `auto.arima`.  What follows is a demonstration of the library.

    *Warning: Become dependent on small open-source projects at [your own risk][8].

    <!-- Links -->
    [6]: https://cran.r-project.org/web/packages/forecast/vignettes/JSS2008.pdf
    [7]: http://alkaline-ml.com/pmdarima/setup.html#setup
    [8]: https://xkcd.com/2347/

    *The ARIMA(1, 1, 2)x(1, 0, 1)7 model has the lowest AIC (Akaike information criterion, a common
    model metric for statistical regression models) of the models explored by the AutoARIMA algorithm.*  

    ***AutoARIMA allows us to quickly evaluate a large number of models, but we may be able to produce a
    better model using our expertise if we spend more time on the problem. This is the trade-off of
    using automatic methods.***

    *The model equation can be written explicitly and if you go through the long algebra, you may find
    that this model is very similar to the one we manually crafted, with additional lagged terms that
    have negligible coefficients. Different combinations of order values can yield models with similar point predictions that differ in their forecast intervals.*  

    *We can investigate the model diagnostics to evaluate the quality of forecast intervals.*  
    *The Ljung-Box p-value=0.53, so there is not enough evidence to conclude that the model residuals
    are correlated. The residuals appear uncorrelated (lower right plot) so there is no leftover
    structure to add to our model.*  

    *The heteroskedascity test p-value=0.01, so there is evidence that the variation of the residuals
    is different between the beginning and end of the data series (upper left plot). This is bad for
    our forecast interval.*  

    *The Jarque-Bera test p-value=0.00, so there is evidence that the residuals do not follow a Normal
    distribution (top right and bottom left plot). This is bad for our forecast interval.*  

    *The highest order nonseasonal MA coefficient is not statistically significant with a p-value=0.98.
    The p-value is inaccurate as indicated by the results of the tests above but ignoring that,
    including non-significant terms is not a problem for prediction, but we may want to remove such
    terms as part of the process of improving the forecast interval (distributional forecast.)*  

    *These statistical test results suggest that automatically generated forecast intervals and
    the default statistical significance tests of the model coefficients will not be accurate, but the
    model will still be useful for predicting mean trends.*  
    *You can use bootstrapping to generate intervals, but you will have to implement it on your own.*


    ```python
    from IPython.display import display
    import matplotlib.pyplot as plt
    import pmdarima as pm
    from pmdarima.model_selection import train_test_split

    y_train, y_test = train_test_split(rides_daily, test_size=0.075)
    # We observed strong seasonality in the data, but the `AutoARIMA`
    # algorithm does not select a model with seasonal differencing.
    # However, different combinations of ARIMA orders can lead to similar
    # models when the model formula are written out and simplified.
    res = pm.AutoARIMA(m=7, seasonal=True).fit(y_train)
    display(res.summary())

    # AutoARIMA does not have a plot_diagnostics method, so we fit the same
    # final model using ARIMA. lbfgs optimization method does not converge
    # so we use powell's method.
    res = pm.ARIMA(order=(1, 1, 2), seasonal_order=(1, 0, 1, 7),
                   method='powell').fit(y_train)

    fig, ax = plt.subplots(figsize=(16, 9), tight_layout=True)
    res.plot_diagnostics(fig=fig)
    plt.show()
    ```


    <table class="simpletable">
    <caption>SARIMAX Results</caption>
    <tr>
      <th>Dep. Variable:</th>                  <td>y</td>                <th>  No. Observations:  </th>    <td>169</td>   
    </tr>
    <tr>
      <th>Model:</th>           <td>SARIMAX(1, 1, 2)x(1, 0, [1], 7)</td> <th>  Log Likelihood     </th> <td>-1593.942</td>
    </tr>
    <tr>
      <th>Date:</th>                   <td>Sun, 28 Mar 2021</td>         <th>  AIC                </th> <td>3199.883</td> 
    </tr>
    <tr>
      <th>Time:</th>                       <td>06:04:38</td>             <th>  BIC                </th> <td>3218.627</td> 
    </tr>
    <tr>
      <th>Sample:</th>                         <td>0</td>                <th>  HQIC               </th> <td>3207.490</td> 
    </tr>
    <tr>
      <th></th>                             <td> - 169</td>              <th>                     </th>     <td> </td>    
    </tr>
    <tr>
      <th>Covariance Type:</th>               <td>opg</td>               <th>                     </th>     <td> </td>    
    </tr>
    </table>
    <table class="simpletable">
    <tr>
         <td></td>        <th>coef</th>     <th>std err</th>      <th>z</th>      <th>P>|z|</th>  <th>[0.025</th>    <th>0.975]</th>  
    </tr>
    <tr>
      <th>ar.L1</th>   <td>    0.6584</td> <td>    0.135</td> <td>    4.888</td> <td> 0.000</td> <td>    0.394</td> <td>    0.922</td>
    </tr>
    <tr>
      <th>ma.L1</th>   <td>   -0.9651</td> <td>    0.168</td> <td>   -5.730</td> <td> 0.000</td> <td>   -1.295</td> <td>   -0.635</td>
    </tr>
    <tr>
      <th>ma.L2</th>   <td>   -0.0024</td> <td>    0.159</td> <td>   -0.015</td> <td> 0.988</td> <td>   -0.314</td> <td>    0.309</td>
    </tr>
    <tr>
      <th>ar.S.L7</th> <td>    0.9965</td> <td>    0.007</td> <td>  142.092</td> <td> 0.000</td> <td>    0.983</td> <td>    1.010</td>
    </tr>
    <tr>
      <th>ma.S.L7</th> <td>   -0.9296</td> <td>    0.073</td> <td>  -12.802</td> <td> 0.000</td> <td>   -1.072</td> <td>   -0.787</td>
    </tr>
    <tr>
      <th>sigma2</th>  <td>  9.44e+06</td> <td> 1.48e-08</td> <td> 6.39e+14</td> <td> 0.000</td> <td> 9.44e+06</td> <td> 9.44e+06</td>
    </tr>
    </table>
    <table class="simpletable">
    <tr>
      <th>Ljung-Box (L1) (Q):</th>     <td>0.39</td> <th>  Jarque-Bera (JB):  </th> <td>48.57</td>
    </tr>
    <tr>
      <th>Prob(Q):</th>                <td>0.53</td> <th>  Prob(JB):          </th> <td>0.00</td> 
    </tr>
    <tr>
      <th>Heteroskedasticity (H):</th> <td>0.51</td> <th>  Skew:              </th> <td>0.23</td> 
    </tr>
    <tr>
      <th>Prob(H) (two-sided):</th>    <td>0.01</td> <th>  Kurtosis:          </th> <td>5.59</td> 
    </tr>
    </table><br/><br/>Warnings:<br/>[1] Covariance matrix calculated using the outer product of gradients (complex-step).<br/>[2] Covariance matrix is singular or near-singular, with condition number 1.74e+30. Standard errors may be unstable.


        C:\Users\K\miniconda3\lib\site-packages\statsmodels\tsa\statespace\sarimax.py:978: UserWarning: Non-invertible starting MA parameters found. Using zeros as starting parameters.
          warn('Non-invertible starting MA parameters found.'




    ![png](images/output_62_2.png)



    *The model predicts the end of September better than our manually crafted model, with less
    uncertainty (narrower forecast intervals.)*  
    *The model achieves an MAPE of 9.1% on the test set.*


    ```python
    # Plot prediction performance on test set.
    # The confidence intervals are inaccurate because the assumptions
    # underlying their equations were not satisfied.
    # You can use bootstrapping to generate intervals, but you will have to
    # implement it on your own.
    preds, conf_int = res.predict(len(y_test), return_conf_int=True)
    mape = mean_absolute_percentage_error(y_test, preds)

    fig, ax = plt.subplots(figsize=(16, 4.5))
    ax.plot(y_train, 'k')
    ax.plot(y_test, 'k')
    ax.plot(y_test.index, preds, 'b',
            label='ARIMA(1, 1, 2)x(1, 0, 1)$_7$')
    ax.fill_between(y_test.index, conf_int[:, 0], conf_int[:, 1],
                    alpha=0.5, color='b', label='95% CI')
    ax.fill_between(y_test.index, preds, y_test, alpha=0.5, color='r',
                    label=f'MAPE: {mape:.3f}')
    ax.set(title='Daily Rides', xlabel='Date', ylabel='Rides')
    ax.legend(fontsize='x-large')
    plt.show()
    ```



  ![png](images/output_64_0.png)



## Extra Credit
### Part 3: LAPD Calls For Service

20. Using data about LAPD calls for service between 2010-2020, use ARIMA models to predict the total
number of calls for the following periods:
    - First 2 weeks of July 2020 (July 1 - 14)
    - Month of July 2020

    Identify at least two prediction models before choosing a final model, and plot your fitted
    model with predictions overlaid on the raw data.

    You can run the `make_lapd.py` script in `src/` to clean and concatenate the yearly calls
    files. Here are a few ways to do so:
    ```console
    # 1. Navigate to time-series-arima/src and run the following from
    # the console.
    python make_lapd.py --dir_data ../data/raw/lapd --dir_out ../data

    # Or
    # 2. Navigate to time-series-arima/data and run the following from
    # the console.
    python ../src/make_lapd.py --dir_data raw/lapd

    # etc.
    ```

    If the resulting file is too large to work with, just work with 2020 data in `data/raw/lapd`.
