import random

from tire import Tire


class Octoprime(Tire):
    def __init__(self, tires):
        self.tires = tires
        self.tires[0] = random.random()
        self.tires[1] = random.random()
        self.tires[2] = random.random()
        self.tires[3] = random.random()

    def needs_service(self):
        if sum(self.tires) >= 3:
            return False
        return True
