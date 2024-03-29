"""
Module for extracting tokens from input strings.
"""
#Run Pylint with the following command: pylint --disable=E0401 </path/to/file.py>
#The import-error can be ignored as it is a false negative error
from typing import List, Optional, Tuple
import os
import sys
# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.strings_operations import remove_whitespace

DEFAULT_NUMBER_OF_SONGS = 20


def flags_mapping(string: str) -> Optional[List[str]]:
    """
    Map flags to their corresponding attributes.

    Args:
        string (str): A string containing flags.

    Returns:
        list or None: A list of attributes corresponding to the flags, or None in case of an error.
    """
    string = string.split('-')[1]

    char_to_word = {
        'a': 'artist',
        'c': 'country',
        'g': 'genre',
        't': 'title'
    }

    if not all(char in char_to_word for char in string):
        print("Error: flag not found")
        return None

    words = [char_to_word[char] for char in string if char in char_to_word]
    return words


def n_songs_checker(string: str) -> Tuple[str, int]:
    """
    Extract the number of songs if present and the remaining string.

    Args:
        string (str): The input string.
        songs (int): Default number of songs.

    Returns:
        tuple: A tuple containing the modified string and the number of songs.
    """
    if string.split(' ')[-1].isdigit():
        songs = int(string.split(' ')[-1])
        string = string.rsplit(' ', 1)[0]
        return string, songs
    return string, DEFAULT_NUMBER_OF_SONGS


def arguments_retriever(input_string: str) -> Tuple[Optional[str], \
                                                  Optional[List[str]], Optional[List[str]], Optional[int]]:
    """
    Parse the input string to extract the command, flags, values, and songs.

    Args:
        input_string (str): The input string to be parsed.

    Returns:
        tuple: A tuple containing the command, flags, values, and songs.
    """
    command = input_string.split(" ")[0]
    flags = None
    values = None
    input_string, n_songs = n_songs_checker(input_string)

    if command == "/all":
        if len(input_string.split(" ")) > 1 and not input_string.split(" ")[1].isdigit():
            print("Error: invalid command")
            return None, None, None, None
        if len(input_string.split(" ")) > 1:
            return None, None, None, None
        return command, flags, values, n_songs
    if command == "/filter":
        try:
            flags = input_string.split(" ")[1]
            flags = flags_mapping(flags)
            if flags is None:
                return None, None, None, None

            string_list = input_string.split(' ', 2)
            tags = string_list[2]
            values = tags.split(',')
            values = [remove_whitespace(value) for value in values]
            if len(flags) != len(values):
                print("Error: flags and values have different lengths")
                return None, None, None, None
        except Exception as exception:
            print("Error:", str(exception))
            return None, None, None, None
    else:
        print("Error: invalid command")
        return None, None, None, None
    return command, flags, values, n_songs

# Example usage:
# String = "/filter -gcat rock-metalcore-rapcore, usa, artist, song 50"
# String1 = "/all"
# Command, Flags, Values, songs = arguments_retriever(String1)
# print("Command: ", Command, "\nFlags: ", Flags, "\nValues: ", Values, "\nsongs: ", songs)
