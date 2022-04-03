#!/usr/bin/env python

import unittest
from unittest import TestCase

import import_from_root
from src.shift_register import ShiftRegister


class TestShiftRegister(unittest.TestCase):

    def test_data(self):
        self.assertRaises(ValueError, ShiftRegister, -1)
        sr = ShiftRegister()
        li = [1, 0, 1, 0, 0, 1, 0, 1]
        self.assertListEqual(sr.virtual_run(0b10100101).get_virtual_data(), li)


if __name__ == '__main__':
    unittest.main()
