#!/usr/bin/env python

"""This module reads all the necessary files and creates an error log."""

import json
from datetime import datetime
import os


class FileReader:
    """
    This class reads all the necessary files for the program to run and writes the errors to a file.
    """

    __file_directory: str = None
    """Stores directory to all files."""

    def __init__(self, file_directory: str = '..\\data\\') -> None:
        """
        This constructor check that the folder exists and stores it to variable.

        :param file_directory: str | Path to the file.
        :return: None
        """
        if not os.path.isdir(file_directory):
            e = Exception('"' + file_directory + '" folder not found.')
            self.append_error(str(e))
            raise e
        self.__file_directory = file_directory

    def read_pins(self) -> dict:
        """
        Reads all data from the json pins file.

        :return: dict | All data from the file.
        """
        try:
            file = open(self.__file_directory + 'pins.json', 'r')
            data = json.load(file)
            file.close()
            return data
        except FileNotFoundError as e:
            self.append_error(str(e))
            raise e

    def read_sequences(self) -> dict:
        """
        Reads all data from the json sequences file.

        :return: dict | All data from the file.
        """
        try:
            file = open(self.__file_directory + 'sequences.json', 'r')
            data = json.load(file)
            file.close()
            return data
        except FileNotFoundError as e:
            self.append_error(str(e))
            raise e

    @staticmethod
    def append_error(error_data: str, current_folder: bool = False, file_directory: str = '..\\data\\',) -> None:
        """
        Writes errors to the file.

        :param error_data: str | Data to display int the file.
        :param current_folder: bool | Search file in current folder.
        :param file_directory: str | Path to the error file.
        :return: None
        """
        if not current_folder:
            if not os.path.isdir(file_directory):
                current_folder = True
        now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        if current_folder:
            file = open("error.log", "a")
            file.write(now + ': ' + error_data + '\n')
            file.close()
        else:
            file = open(file_directory + 'error.log', 'a')
            file.write(now + ': ' + error_data + '\n')
            file.close()
