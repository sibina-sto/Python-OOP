# Ines

# Liner approach implementation of hashing
class HashTable:
    """
    Hashable represents a custom dictionary implementation
    where we use two private lists to achieve storing and hashing of
    key-value pairs functionality
    """
    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __getitem__(self, key):
        index = self.__keys.index(key)
        return self.__values[index]

    def __resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity = self.max_capacity * 2

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if self.actual_length == self.max_capacity:
            self.__resize()
        index = self.__hash(key)
        self.__keys[index] = key
        self.__values[index] = value

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def add(self, key, value):
        self[key] = value

    @property
    def keys(self):
        return self.__keys

    @property
    def values(self):
        return self.__values

    def __check_available_index_(self, index):
        """
        Checks if there is empty slot on this index,
        if not implements the liner approach when there is a
        collision between two hash indexes and returns the next
        AVAILABLE index
        :param index: int
        :return: int -> next/current available index
        """
        if index == len(self.__keys):
            return self.__check_available_index_(0)
        if self.__keys[index] is None:
            return index
        return self.__check_available_index_(index + 1)

    def __hash(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        available_index = self.__check_available_index_(index)
        return available_index

    def __len__(self):
        return self.max_capacity

    @property
    def actual_length(self):
        return len([el for el in self.__keys if el is not None])

    def __repr__(self):
        result = [
            f"{self.__keys[index]}: {self.__values[index]}"
                  for index in range(len(self.__keys))
                  if self.__keys[index] is not None
        ]
        return "{" + "{}".format(", ".join(result)) + "}"


# table = HashTable()
#
# table["name"] = "Peter"
# table["age"] = 25
# table["age"] = 26
# table.add("work", "Some title")
# # table["eyes color"] = "blue"
# # table["hair color"] = "black"
# # table["name"] = "Peter"
# # table["age"] = 25
# # table["work"] = "Some title"
# # table["eyes color"] = "blue"
# # table["hair color"] = "black"
#
# print(table["name"])
# print(table.get("5"))
# print(table["age"])
# print(len(table))
# print(table.actual_length)
# print(table)



#
class HashTable:
    """
    This class is used to implement the logic of hash tables and dictionaries
    The moving index of simplicity is O1
    """

    def __init__(self):
        self.max_capacity = 4
        self.keys = [None] * self.max_capacity
        self.values = [None] * self.max_capacity

    def __getitem__(self, item):
        if item in self.keys:
            index = self.keys.index(item)
            return self.values[index]

    def __len__(self):
        return len(self.keys)

    def __setitem__(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            index = self.hash(key)
            self.__validate_collisions(index)
            self.keys[index] = key
            self.values[index] = value

    def __str__(self):
        return f'{[(self.keys[index] ,self.values[index]) for index in range(len(self.keys)) if self.keys[index]]}'

    def hash(self, key):
        index = sum([ord(char) for char in key]) % len(self.keys)
        validated_index = self.__validate_collisions(index)
        return validated_index

    def add(self, key, value):
        self[key] = value

    def get(self, key):
        index = self.keys.index(key)
        return self.values[index]

    def __resize_lists(self):
        if all(self.keys):
            self.keys = self.keys + [None] * self.max_capacity
            self.values = self.values + [None] * self.max_capacity
            self.max_capacity *= 2

    def __validate_collisions(self, index):
        if index == len(self.keys):
            self.__resize_lists()
            return self.__validate_collisions(0)
        if self.keys[index] is None:
            return index
        return self.__validate_collisions(index + 1)


table = HashTable()
table['name'] = 12
table['age'] = 12
table['value'] = 12
table['mmama'] = 12
table['tate'] = 12
table['tate'] = 33
print(table)