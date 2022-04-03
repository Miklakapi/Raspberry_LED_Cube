#!/usr/bin/env python

import unittest

import import_from_root
from src.time_converter import TimeConverter, Unit
from src.clock import Clock


class TestTimeConverter(unittest.TestCase):

    def test_value(self):
        self.assertRaises(ValueError, TimeConverter, -1)
        tc = TimeConverter(90)
        self.assertAlmostEqual(tc.as_seconds(), 90)
        self.assertAlmostEqual(tc.as_minutes(), 1.5)
        self.assertAlmostEqual(tc.as_milliseconds(), 90000)
        self.assertAlmostEqual(tc.as_microseconds(), 90000000)
        tc.set_time(2.5, Unit.MIN)
        self.assertAlmostEqual(tc.as_seconds(), 150)
        self.assertAlmostEqual(tc.as_minutes(), 2.5)
        self.assertAlmostEqual(tc.as_milliseconds(), 150000)
        self.assertAlmostEqual(tc.as_microseconds(), 150000000)
        tc.set_time(20, Unit.MS)
        self.assertAlmostEqual(tc.as_seconds(), 0.02)
        self.assertAlmostEqual(tc.as_minutes(), 0.000333, 5)
        self.assertAlmostEqual(tc.as_milliseconds(), 20)
        self.assertAlmostEqual(tc.as_microseconds(), 20000)


if __name__ == '__main__':
    unittest.main()
