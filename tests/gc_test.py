import sys, os
import pytest

# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.genre_checker import is_genre_satisfied
from src.strings_operations import lower_case, remove_whitespace



@pytest.mark.parametrize("query_genre, release_genre, expected_result", [
    ("", ["progressive metalcore", "hardcore", "metalcore"], True),  # Empty query genre
    ("progressive", ["metalcore", "rapcore", "Progressive Metalcore"], True),  # Single query genre present
    ("deathcore", ["alternative metal", "nu metal", "metalcore"], False),  # Single query genre absent
    ("progressive+metalcore", ["progressive metalcore", "hardcore", "metalcore"], True),  # Multiple query genres all present
    ("progressive+deathcore", ["progressive metalcore", "hardcore", "metalcore"], False),  # Multiple query genres, one missing
    ("progressive+deathcore", ["progressive metalcore", "deathcore", "metalcore"], True),  # Multiple query genres all present
    ("progressive+deathcore", ["progressive", "deathcore", "metalcore"], True),  # One query genre missing
    ("progressive+metalcore+hardcore", ["progressive metalcore", "hardcore", "metalcore"], True),  # All query genres present
    ("progressive+metalcore+hardcore", ["progressive metalcore", "hardcore", "metalcore", "hardcore"], True),  # All query genres present with additional genres
    ("", [], True),  # Empty query genre with empty release genres
])
def test_is_genre_satisfied(query_genre, release_genre, expected_result):
    assert is_genre_satisfied(query_genre, release_genre) == expected_result
