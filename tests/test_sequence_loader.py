#!/usr/bin/env python

import unittest

import import_from_root
from src.sequence_loader import SequenceLoader


class TestSequenceLoader(unittest.TestCase):

    def test_data(self):
        sl = SequenceLoader()
        self.assertEqual(sl.get_sequence_by_name('hourGlass')['delay'], 0.06)


if __name__ == '__main__':
    unittest.main()
