"""
Module for parallelized web scraping of CoreRadio website.
"""
#Run Pylint with the following command: pylint --disable=E0401 parallel_requests.py 
#The import-error can be ignored as it is a false negative error
from math import ceil
from typing import List, Tuple, Union
from concurrent.futures import ThreadPoolExecutor
from src.token_extractor import arguments_checker
from src.site_requests import site_requests_maker


def site_requests_wrapper(args: Tuple[str, str, str, int, int, int]) -> Tuple[List[Union[str, List[str]]], int]:
    """
    Wrapper function for site_requests to use with ThreadPoolExecutor.

    Args:
        args (tuple): A tuple of arguments for site_requests.

    Returns:
        tuple: The result of site_requests.
    """
    return site_requests_maker(*args)


def calling_parallel(string: str, max_workers: int = 16) -> List[Union[str, List[str]]]:
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

    songs_counter = 0

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
