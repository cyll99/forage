from datetime import datetime
import unittest

from battery.spindlerBattery import SpindlerBattery


class SpindlerBattery_test(unittest.TestCase):
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