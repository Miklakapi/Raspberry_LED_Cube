#!/usr/bin/env python

"""This module is responsible for loading and managing sequences."""

from typing import TypeVar
import random

from file_reader import FileReader

SL = TypeVar('SL', bound='SequenceLoader')


class SequenceLoader:
    """
    This class is designed to read all the sequences from the file and recopy them, and then handle the requests.
    """

    __all_sequences_dict: dict = None
    """Stores all sequences"""

    __all_sequences_list: list = None
    """Stores all sequences"""

    __iter: int = 0
    """Stores number of sequence"""

    __number_of_sequences: int = None
    """Stores number of sequences"""

    def __init__(self) -> None:
        """
        This constructor loads the sequences and randomize them.

        :return: None
        """
        self.load_sequences()
        self.randomize_sequences()
        self.__number_of_sequences = len(self.__all_sequences_dict)
        if not self.__number_of_sequences:
            FileReader.append_error("Zero sequences in json file. SequenceLoader cannot display empty sequence.")
            raise Exception("Zero sequences to display.")

    def load_sequences(self, path_to_file: str = None) -> SL:
        """
        Load object from json file.

        :param path_to_file: str | Path to the file
        :return: self
        """
        fr = None
        if path_to_file:
            fr = FileReader(path_to_file)
        else:
            fr = FileReader()
        self.__all_sequences_dict = fr.read_sequences()
        self.__all_sequences_list = list(self.__all_sequences_dict.items())
        self.__iter = 0

        return self

    def randomize_sequences(self) -> SL:
        """
        This function randomizes the data from the json file.

        :return: self
        """
        temp_list = list(self.__all_sequences_dict.items())
        random.shuffle(temp_list)
        self.__all_sequences_dict = dict(temp_list)
        self.__all_sequences_list = list(self.__all_sequences_dict.items())
        self.__iter = 0

        return self

    def get_sequence_by_order(self) -> list:
        """
        This function returns a single sequence in order.

        :return: list | A single sequence to be displayed by the cube class
        """
        if self.__iter == self.__number_of_sequences:
            self.randomize_sequences()
        self.__iter += 1
        return self.__all_sequences_list[self.__iter - 1]

    def get_sequence_by_name(self, name: str) -> dict:
        """
        This function returns a single sequence by its name.

        :param name: str | Sequence name
        :return: dict | A single sequence to be displayed by the cube class
        """
        return self.__all_sequences_dict[name]
