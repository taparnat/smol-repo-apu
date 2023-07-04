import pytest
import mock
from src import csv_handler

def test_load_csv():
    with mock.patch('pandas.read_csv', return_value='mocked_data'):
        result = csv_handler.load_csv('mocked_file.csv')
        assert result == 'mocked_data'

def test_save_csv():
    with mock.patch('pandas.DataFrame.to_csv') as mocked_to_csv:
        csv_handler.save_csv('mocked_data', 'mocked_file.csv')
        mocked_to_csv.assert_called_once_with('mocked_file.csv', index=False)