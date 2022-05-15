from engine.engine import Engine
from battery.battery import Battery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = Engine()
        self.battery = Battery()

    def needs_service(self):
        pass
