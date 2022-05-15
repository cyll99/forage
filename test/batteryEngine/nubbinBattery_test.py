import unittest
from datetime import datetime

from battery.nubbinBattery import NubbinBattery


class NubbinBattery_test(unittest.TestCase):
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