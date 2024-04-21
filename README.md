# linear-regression-fundamentals

The notebook 'linear regression.ipynb' visualizes key assumptions of linear regression.

Assumptions for equalisation of MSE minimisation to MLE maximisation:

1. Linearity:
    There is linear relationship between features and target. This can be checked using:
    i. Scatter plot of features with target - There should be linear relationship. 
    ii. Residual vs fitted plot - This is a scatter plot of errors with predicted values. The errors should be randomly distributed in this plot. If there is a pattern in the errors plot, it might indicate non-linearity or unequal error variances (violation of homoscedasticity).
2. Normality:
    The errors are normally distributed with mean 0. This can be checked using:
    i. Histogram of errors - Errors should be normally distributed. This is not a good way to check because the number of bins is input by user.
    ii. Q-Q plot - This is a plot of error quantiles on y axis and quaniltes of standard normal distribution on x axis. Ideally, the points should lie on y=x line on graph.
    iii. Check mean of erros to be 0.
3. Homoscedasticity:
    The standard deviation of errors is same for error distribution for all samples. This can be checked using:
    i. Scatter plot of errors with feature - Errors should be randomly distributed around mean 0. This is not a good way to use when linear rgression is used with more than 1 feature.
    ii. Scale-location plot - This is a scatter plot of sqrt(|Standardised erros|) vs predicted values. The points should be randomly distributed.
4. Independence of samples and errors:
    The samples and errors are drawn independent to each other.
    i. Autocorrelation plot - It is a plot of auto-correlation of errors. Ideally, the autocorrelation should be low and there should not be a pattern in the graph. If there is a pattern, it could mean that the errors are not independent of each other. This can be a useful thing to check in time series data.

Assumption for robustness:
1. Multi-collinearity
    The features are not correlated with each other.