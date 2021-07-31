from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class SoundMakingAnimal(Animal):
    def __init__(self, sound):
        self.animal_sound = sound

    def make_sound(self):
        return self.animal_sound


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [SoundMakingAnimal("meow"), SoundMakingAnimal("woof-woof"), SoundMakingAnimal("cluck")]
animal_sound(animals)
