import subprocess

def test_main_runs():
    result = subprocess.run(["python", "main.py"], capture_output=True)
    assert result.returncode == 0


