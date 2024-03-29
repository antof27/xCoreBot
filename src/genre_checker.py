"""
Module for checking genre conditions.
"""
#Run Pylint with the following command: pylint --disable=E0401 </path/to/file.py>
#The import-error can be ignored as it is a false negative error
from typing import List
import os
import sys
# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.strings_operations import lower_case, remove_whitespace

def is_genre_satisfied(query_genre: str, release_genre: List[str]) -> bool:
    """
    Check if the query genre conditions are satisfied based on the release genres.

    Args:
        query_genre (str): The query genre.
        release_genre (list): List of release genres.

    Returns:
        bool: True if the query genre conditions are satisfied, False otherwise.
    """
    if not query_genre:
        return True

    query_genre_list = query_genre.split("+")
    n_genre = len(query_genre_list)
    releases_counter = 0

    for q_genre in query_genre_list:
        releases_counter += any(
            lower_case(q_genre) in remove_whitespace(lower_case(r_genre))
            for r_genre in release_genre
        )

        if releases_counter >= n_genre:
            return True

    return False
