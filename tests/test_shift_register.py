#!/usr/bin/env python

import unittest

import import_from_root
from src.shift_register import ShiftRegister


class TestShiftRegister(unittest.TestCase):

    def test_data(self):
        sr = ShiftRegister()
        self.assertRaises(ValueError, sr.set_modules, -1)
        li = [1, 0, 1, 0, 0, 1, 0, 1]
        self.assertListEqual(sr.virtual_run('10100101').get_virtual_data(), li)


if __name__ == '__main__':
    unittest.main()
