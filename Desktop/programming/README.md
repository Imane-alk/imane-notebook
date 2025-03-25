<<<<<<< HEAD
# Impact of Education Level on Wages in the United States (1973–2022)

## Project overview

=======
##Impact of Education Level on Wages in the United States (1973–2022)
#Project overview
>>>>>>> cbc1f42d3ae6dc4a874cec766e9c738a437ce1a7
This mini-project aims to analyze the relationship between education level and wages in the United States over the period 1973–2022. The goal is to explore how higher educational attainment correlates with higher wages and how this relationship has evolved over time. Framed within an econometric approach, the study seeks to empirically test a widely accepted hypothesis in labor economics: investment in education translates into higher income.

<<<<<<< HEAD
The dataset comes from Kaggle: **"Wages by Education in the USA (1973–2022)"**, based on data from the **Economic Policy Institute**. It provides average hourly wages by the highest level of education attained, disaggregated by year, gender, and race. For this analysis, we focused solely on the relationship between education and wages, deliberately excluding race to concentrate on educational outcomes. This choice was made to avoid ethically sensitive comparisons that are outside the scope of the project.

**Research question:**  
To what extent does educational attainment influence income, and does this link hold when controlling for other factors?


## Project structure

The project follows good software engineering practices and is organized as follows:

- `notebooks/`  
  Contains Jupyter notebooks for exploratory data analysis and presentation of results. The main notebook `project.ipynb` includes the full econometric analysis: data loading, visualizations, linear regressions, and result interpretation.

- `src/`  
  Source code organized into modules:
  - `data_processing.py`: loading and preprocessing functions (reading the raw CSV file, cleaning, encoding, etc.).
  - `models.py`: implementations of simple and multiple linear regressions, along with metrics (e.g. MSE, R²).
  - `visualization.py`: plotting functions (trends over time, regression scatter plots, etc.).

- `data/`  
  Contains the raw dataset (`wages_by_education.csv`). No manual modifications are made to this file.

- `tests/`  
  Unit tests using `pytest` to validate the correctness of core functions (data loading, preprocessing, model fitting).

- `main.py`  
  Main script to run the full pipeline: load data, clean, train models, and generate outputs (metrics and visualizations).

- `requirements.txt`  
  Cleaned and updated list of Python dependencies used in the project. Includes standard libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, and `scikit-learn`.


## How to run the project

### 1. Prerequisites

- Python 3.x installed  
- It is recommended to use a virtual environment (`venv` or `conda`)

### 2. Install dependencies

=======
#Project structure
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

#How to Run the Project
1. Prerequisites
* Python 3.x installed
* It is recommended to use a virtual environment (venv or conda)
2. Install Dependencies
>>>>>>> cbc1f42d3ae6dc4a874cec766e9c738a437ce1a7
From the root directory of the project, run:

```bash
pip install -r requirements.txt
```

### 3. Run the main script

```bash
python main.py
```

This will load the data, clean it, fit regression models, and generate key outputs (graphs and summaries).

### 4. Run the Jupyter Notebook (Optional)

```bash
jupyter notebook
```

Then open `notebooks/project.ipynb` to interactively explore the analysis, step-by-step explanations, and visualizations.

### 5. Run unit tests 

```bash
pytest
```

<<<<<<< HEAD
This will execute the test suite located in the `tests/` directory.


## Modeling approach

The analysis uses two types of regression models:

### Simple Linear Regression

Analyzes the relationship between wages and a single predictor (e.g. one education level). Education levels were encoded into numeric or dummy variables.

### Multiple Linear Regression

Incorporates multiple predictors simultaneously (e.g. year, other education levels) to control for additional effects. The dataset is split into training and testing sets to evaluate performance using Mean Squared Error (MSE). The multiple regression model showed improved accuracy over the simple models.


## Key insights and limitations

- Higher education levels are generally associated with higher wages.
- The dataset provides aggregated (not individual-level) data, limiting granularity.
- Important variables like experience, industry, or region are not included.
- Race was excluded from this analysis for ethical and methodological clarity.
- Linear models were used for simplicity; more complex patterns may exist.
- Some outliers may have affected the regression results.


## Personal reflection

This project allowed me to implement a complete data science pipeline: from cleaning raw data and modularizing the code to running regression models and interpreting real-world results. I became especially aware of the importance of reproducibility and structure in analytical work.

While the linear regression models confirmed basic economic intuitions, I also realized their limitations, particularly in the absence of richer, micro-level data. The ability to isolate and measure the effect of education would be improved with additional variables (like experience or sector). Nonetheless, this mini-project served as an important exercise in both programming and applied econometrics, and highlighted the importance of thoughtful design and documentation.
=======
#Modeling approach
Code is divided into separate components for data processing, modeling, and visualization. This makes the project easier to read, maintain, and extend. Unit tests provide additional confidence in each component.
#Tools used
* pandas, numpy for data handling
* matplotlib, seaborn for visualizations
* statsmodels for statistical analysis
* scikit-learn for machine learning-based regression and evaluation
#Regression Models
* Simple Linear Regression Examines the effect of one predictor at a time (e.g., education level vs. wages). Education levels were encoded into numerical variables or dummies for modeling.
* Multiple Linear Regression Includes several predictors at once to account for additional factors (e.g., year, gender). The dataset was split into train/test sets to evaluate predictive performance using metrics such as Mean Squared Error (MSE). We found that including more variables improved model accuracy.

#Key insights & limitations
* Results confirm that higher education levels are generally associated with higher wages.
* However, the dataset provides aggregate (not individual-level) data, which limits the granularity of analysis.
* Key explanatory variables such as work experience, region, or sector are missing from the dataset.
* We chose to exclude race from the analysis to keep the focus on education, acknowledging the ethical and analytical limitations this entails.
* Linear models were used for simplicity, but non-linear patterns may exist. Outliers and noise may slightly affect estimates, though residuals were checked for consistency.

#Personal reflection
This project allowed me to put into practice the entire data science pipeline from raw data cleaning and modular coding to statistical modeling and final interpretation. I particularly appreciated the importance of reproducibility and structure, which I ensured by organizing code into modules and writing unit tests.
I also realized the limits of statistical models when applied to real-world, aggregated data. While the patterns confirmed economic intuition, I remained cautious not to overinterpret the results (correlation is not causation).
In short, this mini-project helped me solidify both my technical and analytical skills while working on a socially relevant topic. With better data (e.g., richer variables or micro-level observations), this analysis could be extended to offer even more robust insights.
>>>>>>> cbc1f42d3ae6dc4a874cec766e9c738a437ce1a7
