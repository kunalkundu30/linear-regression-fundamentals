# linear-regression-fundamentals

The notebook 'linear regression.ipynb' visualizes key assumptions of linear regression and how to check if they are valid.

**Assumptions for equalisation of MSE minimisation to MLE maximisation**:

1. **Linearity**:<br>
    There is linear relationship between features and target. This can be checked using:<br>
    i. **Scatter plot of features with target** - There should be linear relationship.<br>
    ii. **Residual vs fitted plot** - This is a scatter plot of errors with predicted values. The errors should be randomly distributed in this plot. If there is a pattern in the errors plot, it might indicate non-linearity or unequal error variances (violation of homoscedasticity).<br>
2. **Normality**:<br>
    The errors are normally distributed with mean 0. This can be checked using:<br>
    i. **Histogram of errors** - Errors should be normally distributed. This is not a good way to check because the number of bins is input by user.<br>
    ii. **Q-Q plot** - This is a plot of error quantiles on y axis and quaniltes of standard normal distribution on x axis. Ideally, the points should lie on y=x line on graph.<br>
    iii. Check mean of errors to be 0.<br>
3. **Homoscedasticity**:<br>
    The standard deviation of errors is same for error distribution for all samples. This can be checked using:<br>
    i. **Scatter plot of errors with feature** - Errors should be randomly distributed around mean 0. This is not a good way to use when linear rgression is used with more than 1 feature.<br>
    ii. **Scale-location plot** - This is a scatter plot of sqrt(|Standardised erros|) vs predicted values. The points should be randomly distributed.<br>
4. **Independence of samples and errors**:<br>
    The samples and errors are drawn independent to each other.<br>
    i. **Autocorrelation plot** - It is a plot of auto-correlation of errors. Ideally, the autocorrelation should be low and there should not be a pattern in the graph. If there is a pattern, it could mean that the errors are not independent of each other. This can be a useful thing to check in time series data.<br>

**Assumption for robustness of results**:<br>
1. **Multi-collinearity**:<br>
    The features are not correlated with each other. This can be checked using:<br>
    i. **Heatmap of correlation plot** - Columns having correlation higher than a threshold can be removed. This can only be used to detect bivariate relationship only.<br>
    ii. **Variable Inflation Factor (VIF)** - It shows correlation of a variable with group of variables. Higher the VIF, more the correlation. VIF is calculated by measuring how well each variable is defined by other variables. It is given by: VIF = 1/(1-R^2). If VIF for a variable is greater than 5, it means that variable can be explained by other variables and multicollinearity is high.<br>


**Other graphs**:
1. **Residual vs leverage plot**
2. **Cook's distance plot**

These plots are used to visualise points that have high influence on the output of the model. If a few points have a very high influence, these points should be further investigated. This could help in identifying non-linearity, heteroskedasticity and outliers. Generally, points that have cook's distance less than 0.5 are not considered very influential.


**Confounding:**<br>
It occurs when a variable affects the relationship between another dependent variable and independent variable. If there is a correlation between a dependent and independent variable, it does not necessarily mean causation.This can occur because of following reasons:<br>
1. **Multicollinearity** - It is the extreme case of confounding.<br>
2. **Selection bias** - It occurs when the data is biased because of the way in which it is collected. (Eg. group imbalance)<br>
3. **Omitted Variable Bias** - It occurs when any variable is omitted from the linear regression.<br>

It can be handled using:<br>
1. **Stratification** - It involves creating multiple categories or subgroups of data in which the confounding variable does not vary much and then test significance and strenth of association using Chi-squared test.

