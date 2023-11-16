"""
Module for scraping CoreRadio website.
"""

import time
from parallel_requests import calling_parallel


def print_outcomes(final_list):
    """
    Print elements from a list, handling TypeError.

    Args:
        final_list (list): The list to print elements from.

    Returns:
        None: Returns None if a TypeError occurs during printing.
    """
    try:
        for i in final_list:
            print(i)
    except TypeError:
        return None    


if __name__ == "__main__":
    print("Insert a valid command!")
    Command = input()
    print("Searching...")
    start_time = time.time()
    print_outcomes(calling_parallel(Command))
    
    end_time = time.time()
    print("Time elapsed: ", end_time - start_time)