import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.plant_data import PlantData

class CloudPoint:
    def __init__(self, plant_data):
        self.plant_data = plant_data

    def load_csv(self, filename):
        self.plant_data = pd.read_csv(filename)
        return self.plant_data

    def plot_3d_cloud(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.plant_data['x'], self.plant_data['y'], self.plant_data['z'])
        plt.show()