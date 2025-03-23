import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def simple_linear_regression(df, predictor, target):
    """
    Perform a simple linear regression.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        predictor (str): The independent variable (education level).
        target (str): The dependent variable (wages).

    Returns:
        statsmodels.regression.linear_model.RegressionResultsWrapper: Regression results.
    """
    X = df[[predictor]]
    X = sm.add_constant(X)  # Ajouter une constante
    Y = df[target]

    model = sm.OLS(Y, X).fit()
    return model

def multiple_linear_regression(df, predictors, target):
    """
    Perform a multiple linear regression.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        predictors (list): List of independent variables.
        target (str): The dependent variable (wages).

    Returns:
        dict: Model results including MSE and coefficients.
    """
    X = df[predictors]
    Y = df[target]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)
    mse = mean_squared_error(Y_test, Y_pred)

    return {"model": model, "mse": mse, "coefficients": model.coef_, "intercept": model.intercept_}