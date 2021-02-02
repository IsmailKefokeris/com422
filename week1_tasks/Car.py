class Car:

    def __init__(self, model, colour, currentSpeed, maxSpeed, fuelLevel):

        if fuelLevel < 0 or fuelLevel > 100:
            raise Exception("Fuel Level Can only be out of 100% (from 0 to 100)")
        self.model = model
        self.colour = colour
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self, accel):
        fuelChange = accel / 2

        if self.fuelLevel - fuelChange <= 0:
            self.currentSpeed = 0
            return False
        elif self.currentSpeed + accel <= self.maxSpeed and self.fuelLevel - fuelChange >= 5:
            self.currentSpeed += accel
            self.fuelLevel -= fuelChange
            return True
        elif self.currentSpeed + accel >= self.maxSpeed and self.fuelLevel - fuelChange >= 5:
            self.currentSpeed = self.maxSpeed
            self.fuelLevel -= fuelChange
            return True

    def brake(self, deccel):

        if self.currentSpeed - deccel >= 0:
            self.currentSpeed -= deccel
            return True
        return False

    def refuel(self, fuel):

        if self.fuelLevel + fuel <= 100:
            self.fuelLevel += fuel
            return True
        else:
            self.fuelLevel = 100
            return True

