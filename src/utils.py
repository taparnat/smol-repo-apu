import numpy as np

def normalize_data(data):
    """
    Function to normalize data
    """
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)

def calculate_distance(point1, point2):
    """
    Function to calculate Euclidean distance between two points
    """
    return np.sqrt(np.sum((point1 - point2) ** 2))

def save_to_csv(data, filename):
    """
    Function to save data to a CSV file
    """
    np.savetxt(filename, data, delimiter=",")