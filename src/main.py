#!/usr/bin/env python

"""This module is main file to manage all classes."""

from cube import Cube


if __name__ == '__main__':
    cube = Cube()

    data = [
        '1010101010101010101010101',
        '0101010101010101010101010',
        '1010101010101010101010101',
        '0101010101010101010101010',
        '1010101010101010101010101',
    ]

    try:
        """Main Loop"""
        while True:
            cube.run()

    except KeyboardInterrupt:
        pass
