class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price:
            return "Not enough budget"

        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount_to_pay = sum([worker.salary for worker in self.workers])
        if self.__budget >= amount_to_pay:
            self.__budget -= amount_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount_to_pay = sum([animal.get_needs() for animal in self.animals])
        if self.__budget >= amount_to_pay:
            self.__budget -= amount_to_pay
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([l.__repr__() for l in lions]) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join([t.__repr__() for t in tigers]) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join([c.__repr__() for c in cheetahs])
        return result

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([k.__repr__() for k in keepers]) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([c.__repr__() for c in caretakers]) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join([v.__repr__() for v in vets])
        return result
