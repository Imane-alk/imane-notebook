# Impact of Education Level on Wages in the United States (1973–2022)

## Project overview

This mini-project aims to analyze the relationship between education level and wages in the United States over the period 1973–2022. The goal is to explore how higher educational attainment correlates with higher wages and how this relationship has evolved over time. It is framed within an econometric approach, the study seeks to empirically test a widely accepted hypothesis in labor economics: investment in education translates into higher income.

The dataset comes from Kaggle: **"Wages by Education in the USA (1973–2022)"**, based on data from the **Economic Policy Institute**. It provides average hourly wages by the highest level of education attained, disaggregated by year, gender, and race. For this analysis, we focused solely on the relationship between education and wages, deliberately excluding race to concentrate on educational outcomes. This choice was made to avoid ethically sensitive comparisons that are outside the scope of the project.

**Research question**  
To what extent does educational attainment influence income, and does this link hold when controlling for other factors?

---

## Project structure

The project is organized as follows:

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

---

## How to run the project

### 1. Prerequisites

- Python 3.9.6 installed  
- It is recommended to use a virtual environment (`venv` or `conda`)

### 2. Install dependencies

From the root directory of the project, run:

```bash
pip install -r requirements.txt
```

### 3. Run the main script

```bash
python main.py
```

This will load the data, clean it, fit regression models, and generate key outputs (graphs and summaries).

### 4. Run the Jupyter Notebook 

```bash
jupyter notebook
```

Then open `notebooks/project.ipynb` to interactively explore the analysis, step-by-step explanations, and visualizations.

### 5. Run unit tests 

```bash
pytest
```

This will execute the test suite located in the `tests/` directory.

---

## Modeling approach

The analysis uses two types of regression models:

### Simple Linear Regression

Analyzes the relationship between wages and a single predictor (e.g. one education level). Education levels were encoded into numeric or dummy variables.

### Multiple Linear Regression

Incorporates multiple predictors simultaneously (e.g. year, other education levels) to control for additional effects. The dataset is split into training and testing sets to evaluate performance using Mean Squared Error (MSE). The multiple regression model showed improved accuracy over the simple models.

---

## Key insights and limitations

- Higher education levels are generally associated with higher wages.
- The dataset provides aggregated (not individual-level) data, limiting granularity.
- Important variables like experience, industry, or region are not included.
- Race was excluded from this analysis for ethical and methodological clarity.
- Linear models were used for simplicity; more complex patterns may exist.
- Some outliers may have affected the regression results.

---

## Personal reflection

This project allowed me to implement a complete data science project from cleaning raw data and modularizing the code to running regression models and interpreting real-world results. I became especially aware of the importance of reproducibility and structure in analytical work.

While the linear regression models confirmed basic economic intuitions, I also realized their limitations, particularly in the absence of richer, micro-level data. The ability to isolate and measure the effect of education would be improved with additional variables (like experience or sector). Nonetheless, this mini-project served as an important exercise in both programming and applied econometrics, and highlighted the importance of thoughtful design and documentation.


