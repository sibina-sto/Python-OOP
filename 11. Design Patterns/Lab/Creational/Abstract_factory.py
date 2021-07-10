from abc import ABC, abstractmethod


class Car:
    pass


class BMW(Car):
    pass


class Mercedes(Car):
    pass


class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass


class BMWFactory(CarFactory):
    def produce_car(self):
        return BMW()


class MercedesFactory(CarFactory):
    def produce_car(self):
        return Mercedes()