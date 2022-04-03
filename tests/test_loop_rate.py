#!/usr/bin/env python

import unittest

import import_from_root
from src.loop_rate import LoopRate
from src.clock import Clock


class TestLoopRate(unittest.TestCase):

    def test_value(self):
        self.assertRaises(ValueError, LoopRate, -1)
        self.assertRaises(ValueError, LoopRate, 0)

    def test_time(self):
        lp = LoopRate(1)
        cl = Clock()
        while True:
            lp.slow_loop()
            et = cl.restart()
            break
        self.assertAlmostEqual(et.as_seconds(), 1.00, 1)
        lp = LoopRate(2)
        cl = Clock()
        while True:
            lp.slow_loop()
            et = cl.restart()
            break
        self.assertAlmostEqual(et.as_seconds(), 0.50, 1)


if __name__ == '__main__':
    unittest.main()
