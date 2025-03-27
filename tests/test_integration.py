import sys
import os
import subprocess

# Ajouter le chemin vers src pour que les imports fonctionnent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_main_runs():
    script_path = os.path.join(os.path.dirname(__file__), "..", "src", "main.py")
    result = subprocess.run(["python", script_path], capture_output=True)
    assert result.returncode == 0, f"Le script main.py a échoué avec le code de retour {result.returncode}"


