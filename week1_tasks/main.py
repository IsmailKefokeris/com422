from Car import *

if __name__ == '__main__':
    car1 = Car("Audi", "Black", 50, 150, 65)
    car2 = Car("Mercedes", "Red", 35, 120, 65)

    print(f"The {car1.model} is {car1.colour} going at around {car1.currentSpeed}mph with a "
          f"fuel level of {car1.fuelLevel}...")
    print(f"The {car2.model} is {car2.colour} going at around {car2.currentSpeed}mph with a"
          f"fuel level of {car2.fuelLevel}%...")

    print("----------------------------------------------------------------")

    if car1.accelerate(100):
        print(f"The {car1.model} speed increased to {car1.currentSpeed}mph but its fuel has been reduced to"
              f" {car1.fuelLevel}%")
    else:
        print("Unable to Accelerate...")

    if car2.brake(15):
        print(f"The {car2.model} speed reduced to {car2.currentSpeed}mph")
    else:
        print("Unable to break if not moving")

    if car2.refuel(15):
        print(f"Fuel level increased to {car2.fuelLevel}%")
    else:
        print("Unable to refill that amount")

    if car2.accelerate(15):
        print(f"The {car2.model} speed increased to {car2.currentSpeed}mph but its fuel has been reduced to"
              f" {car2.fuelLevel}%")
    else:
        print("Unable to Accelerate...")

    print("----------------------------------------------------------------")

    print(f"The {car1.model} is {car1.colour} going at around {car1.currentSpeed}mph with a "
          f"fuel level of {car1.fuelLevel}%...")

    print(f"The {car2.model} is {car2.colour} going at around {car2.currentSpeed}mph with a"
          f"fuel level of {car2.fuelLevel}%...")
