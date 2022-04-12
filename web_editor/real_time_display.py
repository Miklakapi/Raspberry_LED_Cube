#!/usr/bin/env python

"""This module is responsible for managing the LED cube in real time."""

import RPi.GPIO as GPIO

import import_from_root
import time
from src.shift_register import ShiftRegister
from src.loop_rate import LoopRate


class OnlineDisplay:
    """
    This class displays the given sequence until it receives a new one.
    """

    __shift_register: ShiftRegister = None
    """Stores ShiftRegister"""

    __loop_rate: LoopRate = None
    """Stores LoopRate"""

    def __init__(self, number_of_shift_registers: int = 4) -> None:
        """
        This constructor loads all private data.

        :param number_of_shift_registers: int | Number of shift registers
        :return: None
        """
        self.__shift_register = ShiftRegister(number_of_shift_registers)
        self.__loop_rate = LoopRate(300)

    def run(self) -> None:
        """
        This function takes one sequence and displays it until it gets a new one.

        :return: None
        """
        for i in range(5):
            # self.__loop_rate.slow_loop()
            level = "00000"
            level = level[:-(i + 1)] + '1' + level[-(i + 1):-1]
            self.__shift_register.run(level + '0000000000000000000000000' + '00')
            time.sleep(0.004)

    def __del__(self) -> None:
        """
        Cleans the pins of the raspberry.

        :return: None
        """
        GPIO.cleanup()
