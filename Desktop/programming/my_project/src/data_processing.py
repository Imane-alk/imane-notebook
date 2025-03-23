import pandas as pd
import os

def load_data(file_path):
    """
    Load dataset and return a Pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    # Vérifier si le DataFrame est vide
    if df.empty:
        raise ValueError("The dataset is empty.")

    return df

def preprocess_data(df):
    """
    Clean the dataset (handle missing values, rename columns, etc.).
    
    Parameters:
        df (pd.DataFrame): The DataFrame to clean.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = df.dropna()  # Supprime les valeurs manquantes
    return df