import numpy as np

def distort_data(cloud_point, distortion_factor):
    """
    Function to distort a 3D cloud point data using a distortion equation
    :param cloud_point: 3D cloud point data
    :param distortion_factor: Factor by which to distort the data
    :return: Distorted 3D cloud point data
    """
    distorted_data = cloud_point * distortion_factor
    return distorted_data

def apply_distortion(cloud_points, distortion_factor):
    """
    Function to apply distortion to all cloud points
    :param cloud_points: List of 3D cloud point data
    :param distortion_factor: Factor by which to distort the data
    :return: List of distorted 3D cloud point data
    """
    return [distort_data(cloud_point, distortion_factor) for cloud_point in cloud_points]