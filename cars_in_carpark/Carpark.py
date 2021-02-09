from Car import Car


class Carpark:

    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.spaces = []

    def add_car(self, car):
        if len(self.spaces) < self.max_limit:
            if self.check_reg_num_exist(car.reg_num):
                self.spaces.append(car)
                return True
        return False

    def remove_car(self, reg):
        for num in range(len(self.spaces)):
            if self.spaces[num].reg_num == reg:
                del self.spaces[num]
                return True
        return False

    def check_reg_num_exist(self, reg):
        for car in self.spaces:
            if car.reg_num == reg:
                return True
        return False

    def __str__(self):
        return f"There are {len(self.spaces)} cars parked in the car park..They are {self.spaces}"


c1 = Car(15234)
c2 = Car(155634)

carspark = Carpark(10)

carspark.add_car(c1)

print(carspark)
