import pytest
from car_management import CarManager

def test_id_iterator():
    CarManager()
    CarManager()
    assert CarManager.total_cars == 2