import pytest

from .car import Car


@pytest.fixture
def my_car():
    return Car(50)


def test_car_accelerate(my_car):
    my_car.accelerate()
    assert my_car.speed == 55


def test_car_brake(my_car):
    my_car.brake()
    assert my_car.speed == 45