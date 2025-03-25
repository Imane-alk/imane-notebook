Impact of Education Level on Wages in the United States (1973–2022)
Project overview
This mini-project aims to analyze the relationship between education level and wages in the United States over the period 1973–2022. The goal is to explore how higher educational attainment correlates with higher wages and how this relationship has evolved over time. Framed within an econometric approach, the study seeks to empirically test a widely accepted hypothesis in labor economics: investment in education translates into higher income.
The dataset comes from Kaggle: “Wages by Education in the USA (1973–2022),” based on data from the Economic Policy Institute. It provides average hourly wages by the highest level of education attained, disaggregated by year, gender, and race. For this analysis, we focused solely on the relationship between education and wages, deliberately excluding race to concentrate on educational outcomes (a choice made to avoid ethically sensitive comparisons beyond the scope of this project).
The central research question is: To what extent does educational attainment influence income, and does this link hold when controlling for other factors?

Project structure
The project follows good software engineering practices and is organized into the following components:
* notebooks/ Contains Jupyter notebooks used for exploratory data analysis and presenting results. The main notebook, project.ipynb, includes the full econometric analysis (data loading, cleaning, visualizations, regression models, and interpretations). It serves as a reproducible and readable record of the project.
* src/ Source code modules for the project:
    * data_processing.py: functions for loading, cleaning, and transforming the dataset (e.g., formatting columns, encoding education levels).
    * models.py: implementation of both simple and multiple linear regression models, along with performance metrics.
    * visualization.py: functions to generate plots such as wage distributions and time-series trends.
* data/ Contains the raw dataset (wages_by_education.csv). No manual edits are made here; all processing is handled through data_processing.py.
* tests/ Includes unit tests (with pytest) to verify core functionality such as data loading and model consistency.
* main.py Main script to run the full analysis pipeline: data loading, preprocessing, modeling, and visualization.
* requirements.txt Lists all necessary Python packages to run the project, such as pandas, numpy, matplotlib, seaborn, statsmodels, and scikit-learn.

How to Run the Project
1. Prerequisites
* Python 3.x installed
* It is recommended to use a virtual environment (venv or conda)
2. Install Dependencies
From the root directory of the project, run:
bash
Copier
pip install -r requirements.txt
3. Run the Main Script
bash
Copier
python main.py
This script performs the entire workflow: data preprocessing, training regression models, and generating outputs (graphs, printed summaries, metrics).
4. Use the Jupyter Notebook (Optional)
To explore the analysis interactively, launch Jupyter from the root folder:
bash
Copier
jupyter notebook
Open the file notebooks/project.ipynb. This notebook includes step-by-step explanations, code cells, and visualizations that guide the reader through the analysis.
5. Run Unit Tests (Optional)
To ensure everything works as expected:
bash
Copier
pytest
This will run all test functions in the tests/ folder to validate data loading and model integrity.

Modeling approach
Code is divided into separate components for data processing, modeling, and visualization. This makes the project easier to read, maintain, and extend. Unit tests provide additional confidence in each component.
Tools used
* pandas, numpy for data handling
* matplotlib, seaborn for visualizations
* statsmodels for statistical analysis
* scikit-learn for machine learning-based regression and evaluation
Regression Models
* Simple Linear Regression Examines the effect of one predictor at a time (e.g., education level vs. wages). Education levels were encoded into numerical variables or dummies for modeling.
* Multiple Linear Regression Includes several predictors at once to account for additional factors (e.g., year, gender). The dataset was split into train/test sets to evaluate predictive performance using metrics such as Mean Squared Error (MSE). We found that including more variables improved model accuracy.

Key insights & limitations
* Results confirm that higher education levels are generally associated with higher wages.
* However, the dataset provides aggregate (not individual-level) data, which limits the granularity of analysis.
* Key explanatory variables such as work experience, region, or sector are missing from the dataset.
* We chose to exclude race from the analysis to keep the focus on education, acknowledging the ethical and analytical limitations this entails.
* Linear models were used for simplicity, but non-linear patterns may exist. Outliers and noise may slightly affect estimates, though residuals were checked for consistency.

Personal reflection
This project allowed me to put into practice the entire data science pipeline from raw data cleaning and modular coding to statistical modeling and final interpretation. I particularly appreciated the importance of reproducibility and structure, which I ensured by organizing code into modules and writing unit tests.
I also realized the limits of statistical models when applied to real-world, aggregated data. While the patterns confirmed economic intuition, I remained cautious not to overinterpret the results (correlation is not causation).
In short, this mini-project helped me solidify both my technical and analytical skills while working on a socially relevant topic. With better data (e.g., richer variables or micro-level observations), this analysis could be extended to offer even more robust insights.
