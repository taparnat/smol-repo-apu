import pytest
import numpy as np
from mock import patch
from src.distortion_equation import distort_data
from src.utils import CloudPoint

def test_distort_data():
    # Mocking the CloudPoint object
    with patch('src.utils.CloudPoint') as MockCloudPoint:
        # Creating a mock instance
        instance = MockCloudPoint.return_value

        # Setting the return value of the x, y, z attributes
        instance.x, instance.y, instance.z = 1.0, 2.0, 3.0

        # Distorting the data
        distorted_data = distort_data(instance)

        # Asserting the distorted data
        assert isinstance(distorted_data, CloudPoint)
        assert np.isclose(distorted_data.x, 1.0, atol=1e-5)
        assert np.isclose(distorted_data.y, 2.0, atol=1e-5)
        assert np.isclose(distorted_data.z, 3.0, atol=1e-5)

    # Testing with actual CloudPoint object
    cloud_point = CloudPoint(1.0, 2.0, 3.0)
    distorted_data = distort_data(cloud_point)

    # Asserting the distorted data
    assert isinstance(distorted_data, CloudPoint)
    assert np.isclose(distorted_data.x, 1.0, atol=1e-5)
    assert np.isclose(distorted_data.y, 2.0, atol=1e-5)
    assert np.isclose(distorted_data.z, 3.0, atol=1e-5)