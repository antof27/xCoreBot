import pytest
from unittest.mock import patch
import os 
import sys
from typing import List
# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.token_extractor import arguments_checker
from src.site_requests import site_requests_maker
from src.parallel_requests import calling_parallel

DEFAULT_NUMBER_OF_SONGS = 20

# Mocking arguments_retriever to avoid actual parsing of string
def mocked_arguments_retriever(string: str) ->  List[str]:
    return "/all", [], [], DEFAULT_NUMBER_OF_SONGS

@patch('src.token_extractor.arguments_retriever', side_effect=mocked_arguments_retriever)
def test_calling_parallel(mock_arguments_retriever: List[str]) -> None:
    # Test with 100 songs and default max_workers
    string = "/all 20"
    result = calling_parallel(string)
    assert len(result) == 20  # Assuming the function returns 100 songs
    # Test with 0 songs
    string = "/all 0"
    result = calling_parallel(string)
    assert result == []  # Expect an empty list if there are no songs
    # Test with invalid command
    string = "invalid_command"
    result = calling_parallel(string)
    assert result is None  # Expecting None if the command is invalid
    

    