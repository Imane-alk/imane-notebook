import pandas as pd
import os

def load_data(file_path):
    """
    Load the dataset and return a DataFrame.

    Parameters:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("The dataset is empty.")

    return df


def preprocess_data(df):
    """
    Preprocess the dataset by cleaning and converting types.

    Steps:
    - Drop missing values
    - Convert 'year' to int
    - Convert wage columns to float

    Parameters:
        df (pd.DataFrame): Raw dataframe

    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    df = df.dropna()
    df['year'] = df['year'].astype(int)
    wage_columns = [col for col in df.columns if col != "year"]
    df[wage_columns] = df[wage_columns].astype(float)

    return df
