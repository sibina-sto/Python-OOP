from abc import ABC, abstractmethod


class PersonObserver(ABC):
    @abstractmethod
    def person_born(self, person):
        pass

    @abstractmethod
    def person_died(self, person):
        pass


class PersonRegistryObserver(PersonObserver):
    def __init__(self):
        self.people = []

    def person_born(self, person):
        self.people.append(person)

    def person_died(self, person):
        self.people.remove(person)

    def get_people_count(self):
        return len(self.people)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class PersonSubject:
    def __init__(self):
        self.observers = []

    def born(self, person):
        [observer.person_born(person) for observer in self.observers]

    def add_observer(self, observer):
        self.observers.append(observer)


subj1 = PersonSubject()
subj2 = PersonSubject()

obs1 = PersonRegistryObserver()
subj1.add_observer(obs1)

obs2 = PersonRegistryObserver()
subj2.add_observer(obs1)
subj2.add_observer(obs2)

subj1.born(Person('Elena', 'Borisova'))

# observers = [
#     PersonRegistryObserver(),
#     PersonRegistryObserver(),
# ]
#
#
# def notify(observers, event, person):
#     if event == 'born':
#         [observer.person_born(person) for observer in observers]
#     else:
#         [observer.person_died(person) for observer in observers]
#
#
# notify(observers, 'born', Person('Elena', 'Borisova'))
# print(observers[0].get_people_count())