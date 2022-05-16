import random

from tire import Tire

class Carrigan(Tire):
    def __init__(self, tires):
        self.tires = tires
        self.tires[0] = random.random()
        self.tires[1] = random.random()
        self.tires[2] = random.random()
        self.tires[3] = random.random()


    def needs_service(self):
        for i in self.tires:
            if i > 0.9:
                return True
            return False
