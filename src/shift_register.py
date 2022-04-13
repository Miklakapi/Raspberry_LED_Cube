#!/usr/bin/env python

"""This module controls the physical object 'shift register'"""

from typing import TypeVar
import RPi.GPIO as GPIO

from file_reader import FileReader

S = TypeVar('S', bound="ShiftRegister")


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

    __virtual_data: list = None
    """Data to virtual shift register"""

    def __init__(self, modules: int = 1, directory_name: str = '../data/') -> None:
        """
        This constructor prepares the raspberry to run and writes the data needed to use the shift register.

        :param modules: int | Number of shift registers to control
        :return: None
        """
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        file = FileReader(directory_name)
        file_dict = file.read_pins()

        if 'data' and 'clock' and 'latch' not in file_dict:
            FileReader.append_error('Not enough data in the pins.json file.')
            raise Exception('Not enough data in the pins file.')

        self.__data = file_dict["data"]
        self.__clock = file_dict["clock"]
        self.__latch = file_dict["latch"]
        self.set_modules(modules)
        self.__virtual_data = [0, 0, 0, 0, 0, 0, 0, 0]

        GPIO.setup(self.__data, GPIO.OUT)
        GPIO.setup(self.__clock, GPIO.OUT)
        GPIO.setup(self.__latch, GPIO.OUT)

    def clear(self) -> None:
        """
        This function clear all shift registers.

        :return: None
        """
        self.run('00000000' * self.__modules)

    def run(self, data: str) -> None:
        """
        Runs one complete cycle of data movements in the shift register.

        :param data: str | String data to display
        :return: None
        """
        for x in range(8 * self.__modules):
            GPIO.output(self.__data, data[- x - 1] == '1')
            GPIO.output(self.__clock, 1)
            GPIO.output(self.__clock, 0)
        GPIO.output(self.__latch, 1)
        GPIO.output(self.__latch, 0)

    def virtual_clear(self) -> S:
        """
        This function clear virtual shift registers.

        :return: self
        """
        self.virtual_run('00000000')
        return self

    def virtual_run(self, data: str) -> S:
        """
        Runs one complete cycle of data movements in the virtual shift register.

        :param data: str | String data to display
        :return: self
        """
        temp_data = [0, 0, 0, 0, 0, 0, 0, 0]
        for x in range(8):
            temp_data.pop()
            temp_data.insert(0, int(data[- x - 1] == '1'))
        self.__virtual_data = temp_data

        return self

    def virtual_display(self) -> None:
        """
        This function shows status of virtual shift register.

        :return: None
        """
        temp_data = list(self.__virtual_data)
        temp_data.pop(0)
        print(self.__virtual_data)
        print(' Vcc     {}     SER    GND   LATCH  SRCLK  SRCLR    Q '.format(self.__virtual_data[0]))
        print('  |      |      |      |      |      |      |      | ')
        print('-----------------------------------------------------')
        print('|                                                   |')
        print('|>                     74HC595                      |')
        print('|  o                                                |')
        print('-----------------------------------------------------')
        print('  |      |      |      |      |      |      |      | ')
        print('  {}      {}      {}      {}      {}      {}      {}    GND'.format(*temp_data))

    def get_modules(self) -> int:
        """
        self.__modules getter.

        :return: int | Number of shift registers
        """
        return self.__modules

    def set_modules(self, modules: int) -> None:
        """
        self.__modules setter.

        :param modules: int | Number of shift registers to control
        :return: None
        """
        if modules <= 0:
            FileReader.append_error('Number of modules in ShiftRegister class must be greater than 0.')
            raise ValueError('Number of modules must be greater than 0.')

        self.__modules = modules

    def get_virtual_data(self) -> list:
        """
        self.__virtual_data getter.

        :return: list[int] | List of all virtual data
        """
        return self.__virtual_data

    def __del__(self) -> None:
        """
        This destructor clears the shift registers and turns off the control pins.

        :return: None
        """
        self.clear()
        GPIO.cleanup()
