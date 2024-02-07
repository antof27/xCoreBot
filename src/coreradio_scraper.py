"""
Module for scraping CoreRadio website.
"""

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

if __name__ == "__main__":
    print("Insert a valid command!")
    user_input = input()
    print("Searching...")
    print_outcomes(calling_parallel(user_input))
