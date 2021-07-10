from creational.utils.print_props import IPrintAttributes


class Animal(IPrintAttributes):
    def __init__(self, name, age, species, weight):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight


class AnimalsBuilder:
    mandatory_attributes = {
        'name': str,
        'age': int,
        'species': str,
    }

    optional_attributes = {
        'weight': int,
    }

    def __init__(self):
        self.__attributes_dict = {}
        self.__reset()

    def set_name(self, name):
        self.__attributes_dict['name'] = name

    def set_age(self, age):
        self.__attributes_dict['age'] = age

    def set_species(self, species):
        self.__attributes_dict['species'] = species

    def set_weight(self, weight):
        self.__attributes_dict['weight'] = weight

    def __reset(self):
        for key, value in self.mandatory_attributes.items():
            self.__attributes_dict[key] = None

        for key, value in self.optional_attributes.items():
            self.__attributes_dict[key] = None

    def __validate(self):
        missing_attributes = [key for key, value in self.mandatory_attributes.items() if self.__attributes_dict[key] is None]
        if missing_attributes:
            raise ValueError(f'The following attributes are missing: '
                             f'{", ".join(missing_attributes)}')

    def build(self):
        self.__validate()
        result = Animal(**self.__attributes_dict)
        self.__reset()
        return result


print(Animal('Gosho', 3, 'dog', 40))

builder = AnimalsBuilder()
builder.set_name('Gosho')
builder.set_age(3)
builder.set_species('dog')
# builder.set_weight(40)
print(builder.build())

print(builder.build())