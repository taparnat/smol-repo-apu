import pytest
import mock
from src import utils

def test_check_file_exists():
    with mock.patch('os.path') as mock_path:
        mock_path.isfile.return_value = True
        assert utils.check_file_exists("test.csv") == True

def test_check_file_not_exists():
    with mock.patch('os.path') as mock_path:
        mock_path.isfile.return_value = False
        assert utils.check_file_exists("test.csv") == False

def test_convert_to_float():
    assert utils.convert_to_float("1.23") == 1.23
    assert utils.convert_to_float("0.0") == 0.0
    assert utils.convert_to_float("-1.23") == -1.23

def test_convert_to_float_invalid_input():
    with pytest.raises(ValueError):
        utils.convert_to_float("invalid")

def test_convert_to_int():
    assert utils.convert_to_int("123") == 123
    assert utils.convert_to_int("0") == 0
    assert utils.convert_to_int("-123") == -123

def test_convert_to_int_invalid_input():
    with pytest.raises(ValueError):
        utils.convert_to_int("invalid")