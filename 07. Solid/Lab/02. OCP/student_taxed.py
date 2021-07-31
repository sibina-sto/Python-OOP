# Ines

from abc import ABC, abstractmethod

class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    @abstractmethod
    def get_discount(self):
        pass


class FortyPercentDiscount(StudentTaxes):
    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4


class TwentyPercentDiscount(StudentTaxes):
    def get_discount(self):
        if 4 > self.average_grade <= 5:
            return self.semester_tax * 0.2


discounter = TwentyPercentDiscount("test", 360, 5.50)
discounter.get_discount()
