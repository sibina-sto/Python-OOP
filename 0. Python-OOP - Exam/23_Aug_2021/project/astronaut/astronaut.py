from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self._name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount