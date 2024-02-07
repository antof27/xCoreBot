import pytest
from coreradio_scraper import (
    song_cleaning,
    lower_case,
    values_extractor,
    site_requests,
    calling,
)

# Test the song_cleaning function
def test_song_cleaning():
    """
    Test cases for the song_cleaning function.
    """
    # Test removing parentheses and year
    assert song_cleaning("Cellar Door (2023)") == "Cellar Door"
    # Test removing square brackets
    assert song_cleaning("Glass [Single]") == "Glass"
    # Test a string with no parentheses or square brackets
    assert song_cleaning("An Offering  ") == "An Offering"
    # Test an empty string
    assert song_cleaning("") == ""

# Test the lower_case function
def test_lower_case():
    """
    Test cases for the lower_case function.
    """
    # Test converting to lowercase
    assert lower_case("Vintas") == "vintas"
    # Test lowercase input
    assert lower_case("HAZE") == "haze"
    # Test an empty string
    assert lower_case("") == ""
    # Test mixed case
    assert lower_case("cUrReNtS") == "currents"

# Test the values_extractor function
def test_values_extractor():
    """
    Test cases for the values_extractor function.
    """
    # Test extracting genre and country
    flags = ["genre", "country"]
    values = ["metalcore", "USA"]
    result = values_extractor(flags, values)
    assert result == ("metalcore", "USA", None, None)

    # Test extracting genre, artist, and title
    flags = ["genre", "artist", "title"]
    values = ["progressive", "ice sealed eyes", "deadweight"]
    result = values_extractor(flags, values)
    assert result == ("progressive", None, "ice sealed eyes", "deadweight")

    # Test extracting title
    flags = ["title"]
    values = ["on the verge"]
    result = values_extractor(flags, values)
    assert result == (None, None, None, "on the verge")


# Test the calling function
# You can use pytest's capsys to capture printed output and then assert against it.

# Mock the arguments_checker function or provide sample input to the calling function to test it.

# Run the tests by executing pytest in your terminal.

# Example values for testing
command = "/filter"
flags = ["artist", "genre"]
values = ["Ice Seales Eyes", "progressive"]
page_number = 5

def test_site_requests_all():
    # Test the /all command
    result = site_requests("/all", [], [], 1)
    assert isinstance(result, list)
    assert len(result) > 0  # There should be some results

def test_site_requests_filter():
    # Test the /filter command with specific flags and values
    result = site_requests(command, flags, values, page_number)
    assert isinstance(result, list)
    for item in result:
        # Ensure that the results match the filter criteria
        assert flags[0] in item[0]
        assert flags[1] == item[1]

def test_site_requests_invalid_command():
    # Test an invalid command
    result = site_requests("/invalid", [], [], 1)
    assert result == []

