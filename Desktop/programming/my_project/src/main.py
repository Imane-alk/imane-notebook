import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import load_data, preprocess_data
from src.visualization import plot_distribution, plot_wage_trends
from src.models import simple_linear_regression, multiple_linear_regression

# Charger et préparer les données
file_path = "data/wages_by_education.csv"
df = load_data(file_path)
df = preprocess_data(df)

# Liste des niveaux d'éducation
education_levels = ["less_than_hs", "high_school", "some_college", "bachelors_degree", "advanced_degree"]

# Afficher les distributions et tendances
plot_distribution(df, education_levels)
plot_wage_trends(df, education_levels)

# Effectuer une régression linéaire simple
target_variable = "advanced_degree"
model = simple_linear_regression(df, "bachelors_degree", target_variable)
print(model.summary())

# Effectuer une régression multiple
predictors = ["bachelors_degree", "some_college", "high_school", "less_than_hs"]
mlr_results = multiple_linear_regression(df, predictors, target_variable)
print(f"Mean Squared Error: {mlr_results['mse']}")
print(f"Model Coefficients: {mlr_results['coefficients']}")
print(f"Intercept: {mlr_results['intercept']}")
