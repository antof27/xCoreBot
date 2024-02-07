import os, sys
import pytest
from unittest.mock import patch, MagicMock

# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.coreradio_scraper import calling_parallel, print_outcomes

# Mocking arguments_checker to avoid actual parsing of string
def mocked_arguments_checker(string):
    return "/all", [], [], 100


def test_print_outcomes(capsys):
    final_list = ["Sleepless Deathbed", "Endless Hollow", "Continuum"]
    print_outcomes(final_list)
    captured = capsys.readouterr()
    assert captured.out == "Sleepless Deathbed\nEndless Hollow\nContinuum\n"
