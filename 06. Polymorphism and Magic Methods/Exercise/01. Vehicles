from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    _CONSUMPTION_PER_KM = 0.9

    def get_fuel_needed(self, distance):
        return (self.fuel_consumption + Car._CONSUMPTION_PER_KM) * distance

    def drive(self, distance):
        fuel_needed = self.get_fuel_needed(distance)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    _CONSUMPTION_PER_KM = 1.6
    _KEPT_FUEL_PERCENTAGE = 0.95

    def get_fuel_needed(self, distance):
        return (self.fuel_consumption + Truck._CONSUMPTION_PER_KM) * distance

    def drive(self, distance):
        fuel_needed = self.get_fuel_needed(distance)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck._KEPT_FUEL_PERCENTAGE


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
