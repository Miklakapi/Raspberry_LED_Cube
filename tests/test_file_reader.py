#!/usr/bin/env python

import unittest

import import_from_root
from src.file_reader import FileReader


class TestFileReader(unittest.TestCase):

    def test(self):
        self.assertRaises(Exception, FileReader, 'abc')
        fr = FileReader()
        self.assertIsInstance(fr.read_pins(), dict)


if __name__ == '__main__':
    unittest.main()
