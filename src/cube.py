#!/usr/bin/env python

"""Temporary file"""

import RPi.GPIO as GPIO
import time

from sequence_loader import SequenceLoader
from shift_register import ShiftRegister
from clock import Clock

sr = ShiftRegister(4)
sl = SequenceLoader()

sequence = sl.get_sequence_by_name("hourGlass")
cl = Clock()
for i in range(sequence['repeat']):
    for j in range(len(sequence['data'])):
        cl.restart()
        while cl.get_elapsed_time().as_seconds() < sequence['delay']:
            for k in range(5):
                level = "00000"
                level = level[:k] + '1' + level[(k + 1):]
                sr.run(level + sequence['data'][j][k] + '00')
                time.sleep(0.003)


class Cube:
    """
    123
    """

    __sequence_loader: SequenceLoader = None

    __shift_register: ShiftRegister = None
    """123"""

    __clock: Clock = None
    """123"""

    def __init__(self, number_of_shift_registers: int = 4) -> None:
        """


        :param number_of_shift_registers:
        :return: None
        """
        self.__shift_register = ShiftRegister(number_of_shift_registers)
        self.__clock = Clock()

    def run(self) -> None:
        """

        :return: None
        """
        pass

    def __del__(self) -> None:
        """
        Cleans the pins of the raspberry.

        :return: None
        """
        GPIO.cleanup()
