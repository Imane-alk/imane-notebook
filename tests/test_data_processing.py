import sys
import os
import pandas as pd

# Ajouter le chemin vers src pour que les imports fonctionnent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_processing import load_data, preprocess_data

def test_load_data():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "wages_by_education.csv")
    df = load_data(path)
    assert not df.empty, "Le dataset ne doit pas être vide"
    assert isinstance(df, pd.DataFrame), "Le dataset doit être un DataFrame"

def test_preprocess_data():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "wages_by_education.csv")
    df = load_data(path)
    df_clean = preprocess_data(df)
    
    assert "year" in df_clean.columns, "La colonne 'year' doit exister"
    assert df_clean["year"].dtype == int, "'year' doit être de type int"
    assert df_clean.isnull().sum().sum() == 0, "Il ne doit pas rester de valeurs manquantes"
    assert all(df_clean.dtypes[1:].apply(lambda x: x == float)), "Les colonnes numériques doivent être de type float"

