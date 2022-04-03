#!/usr/bin/env python

"""This module controls the physical object 'shift register'"""

import RPi.GPIO as GPIO

from file_reader import FileReader


class ShiftRegister:
    """
    This class is used to handle shift registers.
    """

    __data: int = 0
    """Data pin number"""

    __clock: int = 0
    """Clock pin number"""

    __latch: int = 0
    """Latch pin number"""

    __modules: int = 0
    """Number of shift registers"""

    def __init__(self, modules: int = 1) -> None:
        """
        This constructor prepares the raspberry to run and writes the data needed to use the shift register.

        :param modules: int | Number of shift registers to control
        :return: None
        """
        if modules <= 0:
            FileReader.append_error('Number of modules in ShiftRegister class must be greater than 0.')
            raise ValueError('Number of modules must be greater than 0.')

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        file = FileReader()
        file_dict = file.read_pins()

        if 'data' and 'clock' and 'latch' not in file_dict:
            FileReader.append_error('Not enough data in the pins.json file.')
            raise Exception('Not enough data in the pins file.')

        self.__data = file_dict["data"]
        self.__clock = file_dict["clock"]
        self.__latch = file_dict["latch"]
        self.__modules = modules

        GPIO.setup(self.__data, GPIO.OUT)
        GPIO.setup(self.__clock, GPIO.OUT)
        GPIO.setup(self.__latch, GPIO.OUT)

    def clear(self) -> None:
        """
        This function clear all shift registers.

        :return: None
        """
        for x in range(self.__modules):
            self.run(0x00000000)

    def run(self, byte: bin) -> None:
        """
        Runs one complete cycle of data movements in a shift register.

        :param byte: bin | Binary data to display
        :return: None
        """
        for x in range(8 * self.__modules):
            GPIO.output(self.__data, (byte >> x) & 1)
            GPIO.output(self.__clock, 1)
            GPIO.output(self.__clock, 0)
        GPIO.output(self.__latch, 1)
        GPIO.output(self.__latch, 0)

    def __del__(self) -> None:
        """
        This destructor clears the shift registers and turns off the control pins.

        :return: None
        """
        self.clear()
        GPIO.output(self.__data, 0)
        GPIO.output(self.__clock, 0)
        GPIO.output(self.__latch, 0)
