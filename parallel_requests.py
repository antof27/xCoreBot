"""
Module for parallelized web scraping of CoreRadio website.
"""

from math import ceil
from concurrent.futures import ThreadPoolExecutor
from token_extractor import arguments_checker
from site_requests import site_requests_maker


def site_requests_wrapper(args):
    """
    Wrapper function for site_requests to use with ThreadPoolExecutor.

    Args:
        args (tuple): A tuple of arguments for site_requests.

    Returns:
        tuple: The result of site_requests.
    """
    return site_requests_maker(*args)


def calling_parallel(string, max_workers=16):
    """
    Perform parallelized web scraping of CoreRadio website.

    Args:
        string (str): The input command string.
        max_workers (int): The maximum number of workers for ThreadPoolExecutor.

    Returns:
        list: A list of scraped music information.
    """
    command, flags, values, total_songs = arguments_checker(string)
    final_list = []

    try:
        page_number = ceil(total_songs / 32)
    except TypeError:
        print("Error: invalid command")
        return None

    songs_counter = 1

    if command is None:
        print("Error: Command not found")
        return None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        args_list = [(command, flags, values, i, total_songs, songs_counter) \
                     for i in range(1, page_number + 1)]
        results = list(executor.map(site_requests_wrapper, args_list))

    for elements, _ in results:
        final_list.extend(elements)

    final_list.reverse()
    return final_list




# def calling(string):
#     """
#     Parse the input string and execute the corresponding command.

#     Args:
#         string (str): The input command string.

#     Returns:
#         None
#     """
#     command, flags, values, total_songs = arguments_checker(string)
#     # print("Command: ", command)
#     # print("Flags: ", flags)
#     # print("Values: ", values)
#     # print("Total songs: ", total_songs)
#     #calculate page_number as the ceiling of the total_songs
#     final_list = []
#     try:
#         page_number = ceil(total_songs/32)
#     except TypeError:
#         print("Error: invalid command")
#         return None
#     songs_counter = 1
#     if command is None:
#         print("Error: Command not found")
#         return None
#     if command == "/all":
#         for i in range(1, page_number + 1):
#             elements, songs_counter = \
#                  site_requests(command, flags, values, i, total_songs, songs_counter)
#             final_list.extend(elements)

#     elif command == "/filter":
#         for i in range(1, page_number + 1):
#             elements, songs_counter = \
#                   site_requests(command, flags, values, i, total_songs, songs_counter)
#             if len(elements) == 0:
#                 continue
#             final_list.extend(elements)
#     else:
#         print("Error: command not found")
#         return None
#     final_list.reverse()
#     return final_list
