import pytest
from week1_tasks.Car import Car


class TestCarHappy:

    def test_car_creation_model(self, default_car):
        assert default_car.model == "Audi"

    def test_car_creation_colour(self, default_car):
        assert default_car.colour == "Red"

    def test_car_creation_curr_speed(self, default_car):
        assert default_car.currentSpeed == 50

    def test_car_creation_max_speed(self, default_car):
        assert default_car.maxSpeed == 150

    def test_car_creation_fuel_level(self, default_car):
        assert default_car.fuelLevel == 90

    def test_accelerate_car_curr_speed_change_increase_not_max(self, default_car):
        default_car.accelerate(90)
        assert default_car.currentSpeed == (50 + 90)

    def test_accelerate_car_fuel_level_change(self, default_car):
        default_car.accelerate(50)
        assert default_car.fuelLevel == (90 - (50 / 2))

    def test_accelerate_car_curr_speed_increase_to_max_speed(self, default_car):
        default_car.accelerate(150)
        assert default_car.currentSpeed == default_car.maxSpeed

    def test_accelerate_car_curr_speed_increase_to_max_speed_fuel_level_decreased(self, default_car):
        default_car.accelerate(150)
        assert default_car.fuelLevel == (90 - (150 / 2))

    def test_car_brake_return_true(self, default_car):
        assert default_car.brake(50) is True

    def test_car_brake_curr_speed_decrease(self, default_car):
        default_car.brake(50)
        assert default_car.currentSpeed == 0

    def test_car_fuel_level_increase(self, default_car):
        default_car.refuel(5)
        assert default_car.fuelLevel == (90 + 5)

    def test_car_fuel_level_increase_return_true(self, default_car):
        assert default_car.refuel(5) is True


class TestCarSad:

    def test_accelerate_car_not_enough_fuel_curr_speed_reduced(self, default_car):
        default_car.accelerate(190)
        assert default_car.currentSpeed == 0

    def test_accelerate_car_not_enough_fuel_return_false(self, default_car):
        assert default_car.accelerate(190) is False

    def test_car_brake_return_true(self, default_car):
        assert default_car.brake(500) is False

    def test_car_fuel_level_max_or_full(self, default_car):
        default_car.refuel(50)
        assert default_car.fuelLevel == 100

    def test_car_fuel_level_max_or_full_return_true(self, default_car):
        assert default_car.refuel(50) is True
