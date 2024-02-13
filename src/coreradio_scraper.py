"""
Module for scraping CoreRadio website.
"""
#Run Pylint with the following command: pylint --disable=E0401 </path/to/file.py>
#The import-error can be ignored as it is a false negative error
import os
import sys

# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.parallel_requests import calling_parallel

def print_outcomes(final_list):
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

# if __name__ == "__main__":
#     print("Insert a valid command!")
#     user_input = input()
#     print("Searching...")
#     print_outcomes(calling_parallel(user_input))
#     #calling_parallel(user_input)

def query_results(command_query):
    results = calling_parallel(command_query)
    return results
