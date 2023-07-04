import pandas as pd
import numpy as np
from src.utils import validate_data

class PlantData:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.load_csv()

    def load_csv(self):
        try:
            data = pd.read_csv(self.csv_file)
            validate_data(data)
            return data
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None

    def process_plant_data(self):
        try:
            self.data['x'] = self.data['x'].apply(np.float64)
            self.data['y'] = self.data['y'].apply(np.float64)
            self.data['z'] = self.data['z'].apply(np.float64)
            return self.data
        except Exception as e:
            print(f"Error processing plant data: {e}")
            return None