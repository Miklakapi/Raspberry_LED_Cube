#!/usr/bin/env python

"""This module measures the elapsed time."""

from time import time
from typing import TypeVar

from time_converter import TimeConverter

C = TypeVar('C', bound='Clock')


class Clock:
    """
    This class measures the elapsed time.
    """

    __time_start_point: time = None
    """Stores the time from which the class measures the elapsed time."""

    __time_count: TimeConverter = None
    """Stores the elapsed time."""

    __run: bool = True
    """Keeps information whether the clock is running."""

    def __init__(self) -> None:
        """
        This constructor sets the time from which the class measures the elapsed time.

        :return: None
        """
        self.__time_count = TimeConverter(0)
        self.__time_start_point = time()

    def resume(self) -> C:
        """
        This function resumes the clock.

        :return: self
        """
        if not self.__run:
            self.__run = True
            self.__time_start_point = time()
        return self

    def stop(self) -> C:
        """
        This function stops the clock

        :return: self
        """
        if self.__run:
            self.__time_count = TimeConverter(time() - self.__time_start_point + self.__time_count.as_seconds())
            self.__run = False
        return self

    def is_running(self):
        return self.__run

    def get_elapsed_time(self) -> TimeConverter:
        """
        This method returns the elapsed time.

        :return: TimeConverter | Elapsed time
        """
        if self.__run:
            return TimeConverter(time() - self.__time_start_point + self.__time_count.as_seconds())
        else:
            return self.__time_count

    def restart(self) -> TimeConverter:
        """
        This method returns the elapsed time and restarts the clock.

        :return: TimeConverter | Elapsed time
        """
        elapsed = 0
        if self.__run:
            elapsed = TimeConverter(time() - self.__time_start_point + self.__time_count.as_seconds())
        else:
            elapsed = self.__time_count

        self.__time_count = TimeConverter(0)
        self.__run = True
        self.__time_start_point = time()
        return elapsed
