from random import randint


class Die_8:
    def __init__(self, num_sides=8):
        self.num_sides = num_sides

    def result(self):
        return randint(1, self.num_sides)

