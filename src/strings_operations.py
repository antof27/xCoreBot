"""
Module for providing string manipulation functions.

This module includes functions for cleaning song titles, converting strings to lowercase,
removing leading and trailing whitespace, and extracting query values based on flags.
"""
from typing import List, Tuple

def song_cleaning(song:str) -> str:
    """
    Clean song title by removing parentheses and square brackets.

    Args:
        song (str): The song title.

    Returns:
        str: The cleaned song title.
    """
    song = song.split("(")[0].strip()
    song = song.split("[")[0].strip()
    return song


def lower_case(string:str) -> str:
    """
    Convert a string to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The lowercase string.
    """
    return string.lower()


def remove_whitespace(string:str) -> str:
    """
    Remove leading and trailing whitespace from a string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with leading and trailing whitespace removed.
    """
    return string.strip()


def values_extractor(flags: List[str], values: List[str]) -> Tuple[str, str, str, str]:
    """
    Extract query values based on flags.

    Args:
        flags (list): List of flags.
        values (list): List of corresponding values.

    Returns:
        tuple: The extracted query values (query_genre, query_country, query_artist, query_title).
    """
    flag_mapping = {"genre": None, "country": None, "artist": None, "title": None}

    for flag in flag_mapping:
        if flag in flags:
            index = flags.index(flag)
            flag_mapping[flag] = values[index]
    return flag_mapping["genre"], flag_mapping["country"], \
        flag_mapping["artist"], flag_mapping["title"]
