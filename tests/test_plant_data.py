import pytest
import mock
from src import plant_data, utils

def test_process_plant_data():
    with mock.patch('src.plant_data.pandas') as mock_pandas:
        mock_pandas.read_csv.return_value = 'csv_data'
        assert plant_data.process_plant_data('test.csv') == 'csv_data'
        mock_pandas.read_csv.assert_called_once_with('test.csv')

def test_PlantData():
    plant = plant_data.PlantData('test.csv')
    assert plant.data == 'test.csv'

    with mock.patch.object(utils, 'load_csv', return_value='csv_data') as mock_load_csv:
        plant.load_data()
        mock_load_csv.assert_called_once_with('test.csv')
        assert plant.data == 'csv_data'

    with mock.patch.object(plant, 'process_plant_data', return_value='processed_data') as mock_process:
        plant.process_data()
        mock_process.assert_called_once_with()
        assert plant.data == 'processed_data'