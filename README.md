# Eduard Bateiko Portfolio

# Project 1: [Bitcoin prediction for 1 day](https://bateikoed.github.io/dipl_program/bitcoin%20predicton/)

Predict stock value of Bitcoin price and highlight the most important words from Google Search which influentce on Bitcoin. I used Yahoo API for gathering stock value and Google Trends API. 

**Feature engeneering**: got from each time series lags, moving average, exponential moving average, moving standart deviation, exponential standart deviation. Prepared data like regression task. <br>
**Research**: Compared result using Box-Cox transformation and not. Using 180 and 30 days for test set and comparing metrics. Worked with not stationary time series. <br>
**Libraries**: scikit-learn, Pandas, Numpy, Featuretools, SciPy, Matplotlib, Pandas-Profiling, yahoofinance, pytrends, statsmodels, MLFlow.<br>
**Models** : RandomForest, XGBoost, LinearRegression, Extra Trees, Decision Tree, Elastic Net.

![](images/project1/2021-05-07_22-00.png)
