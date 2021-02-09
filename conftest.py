import pytest
from week1_tasks.Car import Car
from test_driven_development_example.table import Table
from test_driven_development_example.restaurant import Restaurant


@pytest.fixture
def default_car():
    print("\n---------- Start ----------")
    yield Car("Audi", "Red", 50, 150, 90)
    print("\n---------- Stop ----------")

@pytest.fixture
def default_table():
    yield Table(502, 4, True)

@pytest.fixture
def large_table():
    yield Table(523, 10, True)

@pytest.fixture
def empty_restaurant():
    yield Restaurant()

