from project import Animal
from project import Dog


class Teacher(Animal, Dog):
    @staticmethod
    def teach():
        return "teaching..."
