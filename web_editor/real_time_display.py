#!/usr/bin/env python

"""This module is responsible for managing the LED cube in real time."""

import RPi.GPIO as GPIO
import requests
import threading

import import_from_root
from src.shift_register import ShiftRegister
from src.loop_rate import LoopRate


class OnlineDisplay(threading.Thread):
    """
    This class displays the given sequence until it receives a new one.
    """

    __shift_register: ShiftRegister = None
    """Stores ShiftRegister"""

    __loop_rate: LoopRate = None
    """Stores LoopRate to cube"""

    __loop_rate2: LoopRate = None
    """Stores LoopRate to thread"""

    __data: list = None
    """Data to display"""

    __working: bool = None
    """Stops the thread"""

    def __init__(self, number_of_shift_registers: int = 4, cube_loop_rate: int = 300, data_getter_rate: int = 10) -> None:
        """
        This constructor loads all private data.

        :param number_of_shift_registers: int | Number of shift registers
        :return: None
        """
        self.__shift_register = ShiftRegister(number_of_shift_registers)
        self.__loop_rate = LoopRate(cube_loop_rate)
        self.__loop_rate2 = LoopRate(data_getter_rate)
        self.__working = True
        threading.Thread.__init__(self)

    def run_cube(self) -> None:
        """
        This function takes one sequence and displays it until it gets a new one.

        :return: None
        """
        self.__data = self.__get_data_from_web()
        while True:
            for i in range(5):
                level = "00000"
                level = level[:-(i + 1)] + '1' + level[-(i + 1):-1]
                self.__shift_register.run(level + self.__data[i] + '00')
                self.__loop_rate.slow_loop()

    def run(self) -> None:
        """
        This function acts as a second thread and gets data from the web server and writes it to the variable data.

        :return: None
        """
        while self.__working:
            self.__data = self.__get_data_from_web()
            self.__loop_rate2.slow_loop()

    @staticmethod
    def __get_data_from_web() -> list:
        """
        This function gets data from web server.

        :return: list | Data to display
        """
        response = requests.get('http://192.168.1.184:5000/get/data/').json()['data']
        if not response:
            response = [
                '0000000000000000000000000',
                '0000000000000000000000000',
                '0000000000000000000000000',
                '0000000000000000000000000',
                '0000000000000000000000000',
            ]
        return response

    def stop(self):
        self.__working = False
