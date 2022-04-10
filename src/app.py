#!/usr/bin/env python

"""This module is main file to manage all classes."""

from cube import Cube


if __name__ == '__main__':
    cube = Cube()

    try:
        """Main Loop"""
        while True:
            cube.run()

    except KeyboardInterrupt:
        pass
