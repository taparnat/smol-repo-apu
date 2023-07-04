import csv
import pandas as pd
from src.utils import handle_error

def load_csv(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        handle_error(e)

def write_csv(filename, data):
    try:
        data.to_csv(filename, index=False)
    except Exception as e:
        handle_error(e)