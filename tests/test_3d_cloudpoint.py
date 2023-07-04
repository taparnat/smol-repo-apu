import pytest
import mock
import numpy as np
from src import 3d_cloudpoint, utils

def test_plot_3d_cloud():
    with mock.patch('matplotlib.pyplot.show') as mock_show:
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        3d_cloudpoint.plot_3d_cloud(data)
        mock_show.assert_called_once()

def test_transform_to_3d():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    transformed_data = 3d_cloudpoint.transform_to_3d(data)
    assert transformed_data.shape == (3, 3)

def test_load_cloudpoint_data():
    with mock.patch('src.csv_handler.load_csv') as mock_load_csv:
        mock_load_csv.return_value = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        data = 3d_cloudpoint.load_cloudpoint_data('test.csv')
        np.testing.assert_array_equal(data, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        mock_load_csv.assert_called_once_with('test.csv')

def test_save_cloudpoint_data():
    with mock.patch('src.csv_handler.save_csv') as mock_save_csv:
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        3d_cloudpoint.save_cloudpoint_data('test.csv', data)
        mock_save_csv.assert_called_once_with('test.csv', data)