"""
Module: element_processing

This module provides functions for processing elements.
"""
#Run Pylint with the following command: pylint --disable=E0401 element_processing.py 
#The import-error can be ignored as it is a false negative error
from typing import List, Union
import os 
import sys

# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.strings_operations import lower_case
from src.genre_checker import is_genre_satisfied

def process_elements_list(command: str,
                          elements_list: List[Union[str, List[str]]],
                          query_genre: str,
                          release_genre: List[str],
                          query_country: str,
                          release_country: str,
                          query_artist: str,
                          release_artist: str,
                          query_title: str,
                          release_title: str,
                          songs_counter: int,
                          total_songs: int,
                          page_list: List[List[Union[str, List[str]]]]) -> int:
    """
    Process a list of elements based on the given
    command and conditions, and append to the page list.

    Args:
        command (str): The command (/all or /filter).
        elements_list (list): List of music information elements.
        query_genre (str): The query genre.
        release_genre (list): List of release genres.
        query_country (str): The query country.
        release_country (str): The release country.
        query_artist (str): The query artist.
        release_artist (str): The release artist.
        query_title (str): The query title.
        release_title (str): The release title.
        songs_counter (int): Counter for the songs.
        total_songs (int): Total number of songs to scrape.
        page_list (list): The list to append the processed elements.

    Returns:
        int: Updated songs counter.
    """
    # Avoid unnecessary nesting
    if not all(elements_list):
        return songs_counter

    if command == "/all":
        if songs_counter < total_songs:
            songs_counter += 1
        page_list.append(elements_list)
    elif command == "/filter":
        # Initialize a flag to check if at least one condition is satisfied
        genre_satisfied = is_genre_satisfied(query_genre, release_genre)

        country_condition = query_country and \
            lower_case(query_country) != lower_case(release_country)
        artist_condition = query_artist and \
            lower_case(query_artist) != lower_case(release_artist)
        title_condition = query_title \
            and lower_case(query_title) != lower_case(release_title)

        if country_condition or artist_condition or title_condition:
            songs_counter += 1
            return songs_counter
        # Append to the list if at least one condition is satisfied
        # and songs_counter is within limit
        songs_counter += 1
        if genre_satisfied and songs_counter < total_songs:
            page_list.append(elements_list)
    return songs_counter
