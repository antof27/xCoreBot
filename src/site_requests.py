"""
Module for making requests and scraping music information from the CoreRadio website.
"""

import time
import requests
from bs4 import BeautifulSoup
from src.strings_operations import song_cleaning, values_extractor
from src.element_processing import process_elements_list


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

def site_requests_maker(command, flags, values, page_number, total_songs, songs_counter):
    """
    Scrape the CoreRadio website for music information based on the given command,
    flags, and page number.

    Args:
        command (str): The command (/all or /filter).
        flags (list): List of flags.
        values (list): List of corresponding values.
        total_songs (int): The total number of songs to scrape.

    Returns:
        list: A list of scraped music information.
    """
    if command == "/filter":
        query_genre, query_country,\
              query_artist, query_title = values_extractor(flags, values)
    else:
        query_genre, query_country, \
            query_artist, query_title = None, None, None, None

    site_url = "https://coreradio.online/page/" + str(page_number)

    page_list = []
    elements_list = []
    release_genre = []
    release_country, release_artist, release_title = None, None, None
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
            if songs_counter < total_songs:
                #print("Elements list: ", elements_list, "songs counter: ",\
                # songs_counter, "total songs: ", total_songs)
                songs_counter = process_elements_list(command, elements_list, query_genre,
                                    release_genre, query_country, release_country, query_artist,
                                    release_artist, query_title, release_title, songs_counter,
                                    total_songs, page_list)
            else:
                break
    return page_list, songs_counter
