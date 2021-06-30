class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, value):
        if (self.size - self.quantity) >= value:
            self.quantity += value

    def status(self):
        return self.size - self.quantity

# Test code
# cup = Cup(100, 50)
# cup.fill(50)
# cup.fill(10)
# print(cup.status())
