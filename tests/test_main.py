import pytest
import mock
from src import main, utils

def test_distort_data():
    with mock.patch('src.distortion_equation.distort_data') as mock_distort:
        main.distort_data()
        mock_distort.assert_called_once()

def test_load_csv():
    with mock.patch('src.csv_handler.load_csv') as mock_load:
        main.load_csv('test.csv')
        mock_load.assert_called_once_with('test.csv')

def test_plot_3d_cloud():
    with mock.patch('src.3d_cloudpoint.plot_3d_cloud') as mock_plot:
        main.plot_3d_cloud()
        mock_plot.assert_called_once()

def test_process_plant_data():
    with mock.patch('src.plant_data.process_plant_data') as mock_process:
        main.process_plant_data()
        mock_process.assert_called_once()

def test_main():
    with mock.patch.object(utils, 'load_csv') as mock_load:
        with mock.patch.object(utils, 'distort_data') as mock_distort:
            with mock.patch.object(utils, 'plot_3d_cloud') as mock_plot:
                with mock.patch.object(utils, 'process_plant_data') as mock_process:
                    main.main()
                    mock_load.assert_called_once()
                    mock_distort.assert_called_once()
                    mock_plot.assert_called_once()
                    mock_process.assert_called_once()