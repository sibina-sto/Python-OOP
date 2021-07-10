from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class VictorianFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa('Victorian')

    def create_table(self):
        return Table('Victorian')


class ModernFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa('Modern')

    def create_table(self):
        return Table('Modern')


class Sofa:
    def __init__(self, name):
        self.name = name


class Table:
    def __init__(self, name):
        self.name = name


factory = ModernFactory()
table = factory.create_table()
print(table.name)