
import pandas as pd

def load_results(file_path):
    """Load CSV results for Streamlit dashboard."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Tool", "Status", "Time", "Details"])
