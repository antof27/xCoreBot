import sys, os

# Get the current script's file path
# Get the current script's file path
script_path: str = os.path.abspath(__file__)

# Get the directory containing the script
script_directory: str = os.path.dirname(script_path)
parent_directory: str = os.path.dirname(script_directory)

sys.path.insert(1, parent_directory)

from src.strings_operations import remove_whitespace
from src.token_extractor import flags_mapping, n_songs_checker, arguments_retriever



def test_remove_whitespace() -> None:
    assert remove_whitespace("  test  ") == "test"
    assert remove_whitespace("  leading  and trailing  ") == "leading  and trailing"

def test_flags_mapping() -> None:
    assert flags_mapping("-acgt") == ['artist', 'country', 'genre', 'title']
    assert flags_mapping("-acxt") is None  # Non-existent flag

def test_n_songs_checker() -> None:
    assert n_songs_checker("/all") == ("/all", 20)
    assert n_songs_checker("/all 10") == ("/all", 10)

def test_arguments_checker() -> None:
    # Test valid /all command
    command, flags, values, songs = arguments_retriever("/all")
    assert command == "/all"
    assert flags is None
    assert values is None
    assert songs == 20

    # Test valid /filter command
    command, flags, values, songs = arguments_retriever("/filter -gcat rock-metalcore-rapcore, usa, artist, song 50")
    assert command == "/filter"
    assert flags == ['genre', 'country', 'artist', 'title']
    assert values == ['rock-metalcore-rapcore', 'usa', 'artist', 'song']
    assert songs == 50

    # Test invalid command
    command, flags, values, songs = arguments_retriever("/invalid")
    assert command is None
    assert flags is None
    assert values is None
    assert songs is None

    # Test invalid /filter command (different lengths of flags and values)
    command, flags, values, songs = arguments_retriever("/filter -gcat rock-metalcore-rapcore, usa, artist")
    assert command is None
    assert flags is None
    assert values is None
    assert songs is None
