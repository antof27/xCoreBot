import os 
import sys 
import pytest
from unittest.mock import patch

# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.site_requests import requests_and_soup, site_requests_maker

# Mocking the requests library
class MockResponse:
    def __init__(self, text):
        self.text = text

def mocked_requests_get(*args, **kwargs) -> MockResponse:
    return MockResponse("<html><body><div id='dle-content'>Test Content</div></body></html>")

@patch('src.site_requests.requests.get', side_effect=mocked_requests_get)
def test_requests_and_soup(mock_get) -> None:
    url = "https://coreradio.online/page/1"
    soup = requests_and_soup(url)
    assert soup.find("div", {"id": "dle-content"}).text == "Test Content"

# Test site_requests_maker
# Test site_requests_maker
def test_site_requests_maker() -> None:
    command = "/all"
    flags = []
    values = []
    page_number = 1
    total_songs = 10
    songs_counter = 0

    page_list, songs_counter = site_requests_maker(command, flags, values, page_number, total_songs, songs_counter)
    print("Length of page_list:", len(page_list))
    print("page_list:", page_list)
    assert len(page_list) == total_songs  # Assuming the function returns 5 songs per page
