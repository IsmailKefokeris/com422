from pytest import *
from week1_tasks.Car import Car


class TestCarHappy:

    def test_car_creation_model(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.model == "Audi"

    def test_car_creation_colour(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.colour == "Red"

    def test_car_creation_curr_speed(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.currentSpeed == 50

    def test_car_creation_max_speed(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.maxSpeed == 150

    def test_car_creation_fuel_level(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.fuelLevel == 90

    def test_accelerate_car_curr_speed_change_increase_not_max(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.accelerate(90)
        assert c1.currentSpeed == (50+90)

    def test_accelerate_car_fuel_level_change(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.accelerate(50)
        assert c1.fuelLevel == (90-(50/2))

    def test_accelerate_car_curr_speed_increase_to_max_speed(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.accelerate(150)
        assert c1.currentSpeed == c1.maxSpeed

    def test_accelerate_car_curr_speed_increase_to_max_speed_fuel_level_decreased(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.accelerate(150)
        assert c1.fuelLevel == 15

    def test_car_brake_return_true(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.brake(50) is True

    def test_car_brake_curr_speed_decrease(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.brake(50)
        assert c1.currentSpeed == 0

    def test_car_fuel_level_increase(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.refuel(5)
        assert c1.fuelLevel == (90 + 5)

    def test_car_fuel_level_increase_return_true(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.refuel(5) is True


class TestCarSad:

    def test_accelerate_car_not_enough_fuel_curr_speed_reduced(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.accelerate(190)
        assert c1.currentSpeed == 0

    def test_accelerate_car_not_enough_fuel_return_false(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.accelerate(190) is False

    def test_car_brake_return_true(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.brake(500) is False

    def test_car_fuel_level_max_or_full(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        c1.refuel(50)
        assert c1.fuelLevel == 100

    def test_car_fuel_level_max_or_full_return_true(self):
        c1 = Car("Audi", "Red", 50, 150, 90)
        assert c1.refuel(50) is True

