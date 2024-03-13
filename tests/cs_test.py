import os, sys
import pytest
from unittest.mock import patch, MagicMock
from typing import List

# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.coreradio_scraper import calling_parallel, print_outcomes

# Mocking arguments_checker to avoid actual parsing of string
def mocked_arguments_checker(string: str) ->  List[str]:
    return "/all", [], [], 100


def test_print_outcomes(capsys) -> None:
    final_list = ["Sleepless Deathbed", "Endless Hollow", "Continuum"]
    print_outcomes(final_list)
    captured = capsys.readouterr()
    assert captured.out == "Sleepless Deathbed\nEndless Hollow\nContinuum\n"
