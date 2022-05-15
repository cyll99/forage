import unittest
from datetime import datetime

from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery
from carFactory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCalliope(unittest.TestCase):
    def test_spindlerBattery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_spindlerBattery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)


        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)


        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willou = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willou.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        willou = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willou.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        spindler = SpindlerBattery(today,last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        spindler = SpindlerBattery(today,last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)


        nubin = NubbinBattery(today,last_service_date)
        self.assertTrue(nubin.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)


        nubin = NubbinBattery(today,last_service_date)
        self.assertTrue(nubin.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = NubbinBattery(today, last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)


        car = NubbinBattery(today, last_service_date)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
