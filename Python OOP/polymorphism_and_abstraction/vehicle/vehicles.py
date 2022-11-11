from abc import ABC, abstractmethod


class Vehicle(ABC):
#there is no need to define init in every child class - we can define in only in the abstract parent class
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

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, amount):
        self.fuel_quantity += amount


class Truck(Vehicle):

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + 1.6)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, amount):
        self.fuel_quantity += 0.95 * amount


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
