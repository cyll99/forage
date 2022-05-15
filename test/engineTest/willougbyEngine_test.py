import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestPalindrome(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willou = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willou.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        willou = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willou.needs_service())