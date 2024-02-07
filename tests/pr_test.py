import pytest
from unittest.mock import patch

from src.token_extractor import arguments_checker
from src.site_requests import site_requests_maker
from src.parallel_requests import calling_parallel

# Mocking arguments_checker to avoid actual parsing of string
def mocked_arguments_checker(string):
    return "/all", [], [], 20

@patch('src.token_extractor.arguments_checker', side_effect=mocked_arguments_checker)
def test_calling_parallel(mock_arguments_checker):
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
    

    