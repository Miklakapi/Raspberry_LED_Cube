#!/usr/bin/env python

import unittest

import import_from_root
from time import sleep

from src.clock import Clock


class TestClock(unittest.TestCase):

    def test_value(self):
        cl = Clock()
        sleep(1.5)
        self.assertAlmostEqual(cl.restart().as_seconds(), 1.50, 1)
        sleep(0.25)
        self.assertAlmostEqual(cl.restart().as_seconds(), 0.25, 1)
        cl.restart()
        sleep(0.5)
        cl.stop()
        self.assertAlmostEqual(cl.get_elapsed_time().as_seconds(), 0.5, 1)
        sleep(0.2)
        self.assertAlmostEqual(cl.get_elapsed_time().as_seconds(), 0.5, 1)
        self.assertFalse(cl.is_running())
        cl.resume()
        sleep(0.2)
        self.assertAlmostEqual(cl.restart().as_seconds(), 0.7, 1)


if __name__ == '__main__':
    unittest.main()
