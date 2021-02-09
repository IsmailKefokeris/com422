import pytest
from week1_tasks.Car import Car
from test_driven_development_example import bus_ticket


@pytest.fixture
def default_car():
    print("\n---------- Start ----------")
    yield Car("Audi", "Red", 50, 150, 90)
    print("\n---------- Stop ----------")

