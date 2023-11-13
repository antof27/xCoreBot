"""
Module for scraping CoreRadio website.
"""

import time
import requests
from bs4 import BeautifulSoup
from token_extractor import arguments_checker, remove_whitespace


def song_cleaning(song):
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


def lower_case(string):
    """
    Convert a string to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The lowercase string.
    """
    return string.lower()


def requests_and_soup(url):
    """
    Send a request to a URL and return the BeautifulSoup object of the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        BeautifulSoup: The BeautifulSoup object of the response.
    """
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        time.sleep(5)
        response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def values_extractor(flags, values):
    """
    Extract query values based on flags.

    Args:
        flags (list): List of flags.
        values (list): List of corresponding values.

    Returns:
        tuple: The extracted query values (query_genre, query_country, query_artist, query_title).
    """
    flag_mapping = {
        "genre": None,
        "country": None,
        "artist": None,
        "title": None
    }

    for flag in flag_mapping:
        if flag in flags:
            index = flags.index(flag)
            flag_mapping[flag] = values[index]

    query_genre = flag_mapping["genre"]
    query_country = flag_mapping["country"]
    query_artist = flag_mapping["artist"]
    query_title = flag_mapping["title"]

    return query_genre, query_country, query_artist, query_title


def site_requests(command, flags, values, page_number):
    """
    Scrape the CoreRadio website for music information based on the given command, 
    flags, and page number.

    Args:
        command (str): The command (/all or /filter).
        flags (list): List of flags.
        values (list): List of corresponding values.
        page_number (int): The page number to scrape.

    Returns:
        list: A list of scraped music information.
    """
    
    if command == "/filter":
        
        query_genre, query_country, query_artist, query_title = values_extractor(flags, values)

    site_url = "https://coreradio.online/page/" + str(page_number)

    print("Page: ", page_number)
    page_list = []
    elements_list = []

    release_genre = []
    release_country = None
    release_artist = None
    release_title = None

    soup = requests_and_soup(site_url)

    # Find the content div
    content_div = soup.find("div", {"id": "dle-content"})
    information = content_div.text.strip()
    lines = information.splitlines()
    lines = [line for line in lines if line.strip() != ""]

    subtoken = 0
    for token in lines:
        if token in ["more", "MAIN", '«', '»', "Load more"] or \
            "Quality:" in token or len(token) < 2:
            continue

        if subtoken % 3 == 0:
            try:
                release_genre = token.split(":")[1].strip()
                release_genre = release_genre.split("/")
            except IndexError:
                continue
            subtoken += 1

        elif subtoken % 3 == 1:
            try:
                release_country = token.split(":")[1].strip()
            except IndexError:
                continue
            subtoken += 1

        elif subtoken % 3 == 2:
            try:
                release_artist = token.split("-")[0].strip()
                release_title = song_cleaning(token.split("-")[1].strip())
            except IndexError:
                continue
            subtoken += 1

        if subtoken % 3 == 0:
            elements_list = [release_genre, release_country, release_artist, release_title]
            if all(elements_list):
                if command == "/all":
                    page_list.append(elements_list)
                elif command == "/filter":
                    # Check if the release values are equal to the query values

                    # Initialize a flag to check if at least one condition is satisfied
                    genre_satisfied = False

                    if query_genre: 
                        #split the genre by - and put into a query_genre_list
                        query_genre_list = query_genre.split("-")
                        #check if any of the query_genre_list is in the release_genre
                        '''
                        for q_genre in query_genre_list:
                            genre_satisfied = any(lower_case(q_genre) in remove_whitespace(lower_case(genre)) for genre in release_genre)
                            if genre_satisfied:
                                break  # Stop checking further q_genres once a match is found

                        if genre_satisfied:
                            continue
                        '''
                        n_genre = len(query_genre_list)
                        releases_counter = 0

                        for q_genre in query_genre_list:
                            releases_counter += any(lower_case(q_genre) in remove_whitespace(lower_case(r_genre)) for r_genre in release_genre)
                            if releases_counter >= n_genre:
                                genre_satisfied = True
                                break   

                    if query_country and lower_case(query_country) != lower_case(release_country):
                        continue

                    if query_artist and lower_case(query_artist) != lower_case(release_artist):
                        continue

                    if query_title and lower_case(query_title) != lower_case(release_title):
                        continue

                    # Append to the list if at least one condition is satisfied
                    if genre_satisfied is True:
                        page_list.append(elements_list)

    return page_list


def calling(string):
    """
    Parse the input string and execute the corresponding command.

    Args:
        string (str): The input command string.

    Returns:
        None
    """
    command, flags, values, total_pages = arguments_checker(string)
    print("Command: ", command)
    print("Flags: ", flags)
    print("Values: ", values)
    print("Total pages: ", total_pages)

    if command is None:
        print("Error: Command not found")
        return
    if command == "/all":
        for i in range(1, total_pages + 1):
            elements = site_requests(command, flags, values, i)
            print(elements)
    elif command == "/filter":
        for i in range(1, total_pages + 1):
            elements = site_requests(command, flags, values, i)
            if len(elements) == 0:
                continue
            for element in elements:
                print(element)
    else:
        print("Error: command not found")
        return



if __name__ == "__main__":
    Command = "/filter -cg australia, technical-progressive 2"
    calling(Command)
