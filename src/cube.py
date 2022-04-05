#!/usr/bin/env python

"""This module managed the led cube."""

import RPi.GPIO as GPIO
import time

from sequence_loader import SequenceLoader
from shift_register import ShiftRegister
from loop_rate import LoopRate
from clock import Clock


class Cube:
    """
    This is the main class of the program. It manages the led cube using mainly ShiftRegister and SequenceLoader.
    """

    __sequence_loader: SequenceLoader = None
    """Stores SequenceLoader"""

    __shift_register: ShiftRegister = None
    """Stores ShiftRegister"""

    __loop_rate: LoopRate = None
    """Stores LoopRate"""

    __clock: Clock = None
    """Stores Clock"""

    def __init__(self, number_of_shift_registers: int = 4) -> None:
        """
        This constructor loads all private data.

        :param number_of_shift_registers: int | Number of shift registers
        :return: None
        """
        self.__sequence_loader = SequenceLoader()
        self.__shift_register = ShiftRegister(number_of_shift_registers)
        self.__loop_rate = LoopRate(300)
        self.__clock = Clock()

    def run(self) -> None:
        """
        This function gets one sequence from the SequenceLoader and runs led cube routed by the ShiftRegister.

        :return: None
        """
        sequence = self.__sequence_loader.get_sequence_by_order()
        data: list = sequence[1]['data']
        repeat: int = sequence[1]['repeat']

        for i in range(repeat):
            for j in range(len(data) - 1):
                self.display_actual_position(data[j], data[j][-1])

    def display_actual_position(self, data: list, delay: float):
        self.__clock.restart()
        while self.__clock.get_elapsed_time().as_seconds() < delay:
            for i in range(5):
                level = "00000"
                level = level[:i] + '1' + level[(i + 1):]
                self.__shift_register.run(level + data[i] + '00')
                self.__loop_rate.slow_loop()

    def __del__(self) -> None:
        """
        Cleans the pins of the raspberry.

        :return: None
        """
        GPIO.cleanup()
