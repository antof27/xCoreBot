"""
Module for scraping CoreRadio website.
"""
#Run Pylint with the following command: pylint --disable=E0401 </path/to/file.py>
#The import-error can be ignored as it is a false negative error
import os
import sys
from typing import List
# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)
from src.parallel_requests import calling_parallel


def print_outcomes(final_list: List[str]) -> None:
    """
    Print elements from a list, handling TypeError.

    Args:
        final_list (list): The list to print elements from.

    Returns:
        None: Returns None if a TypeError occurs during printing.
    """
    try:
        for item in final_list:
            print(item)
    except TypeError:
        pass

def query_results(command_query: str) -> List[str]:
    """
    Retrieve query results based on the provided command query.

    This function fetches results by calling a parallel execution mechanism
    to process the command query efficiently. The results are returned for further
    processing or display.

    Args:
        command_query (str): The command query to be processed.

    Returns:
        list: A list containing the query results retrieved based on the provided command query.
    """
    results: List[str] = calling_parallel(command_query)
    return results
