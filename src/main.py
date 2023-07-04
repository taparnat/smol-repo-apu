import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from distortion_equation import distort_data
from csv_handler import load_csv
from 3d_cloudpoint import plot_3d_cloud
from plant_data import process_plant_data
from utils import *

def main():
    # Load the CSV data
    data = load_csv('data.csv')

    # Process the plant data
    plant_data = process_plant_data(data)

    # Distort the 3D cloudpoint data
    distorted_data = distort_data(plant_data)

    # Plot the distorted 3D cloudpoint data
    plot_3d_cloud(distorted_data)

if __name__ == "__main__":
    main()