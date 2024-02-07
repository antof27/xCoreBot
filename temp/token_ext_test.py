from token_extractor import arguments_checker, pages_checker, remove_whitespace, flags_mapping

def test_arguments_checker_all_command_single_page():
    # Test the "/all" command with a single page
    input_string = "/all 1"
    command, flags, values, pages = arguments_checker(input_string)
    assert command == "/all"
    assert flags is None
    assert values is None
    assert pages == 1

def test_arguments_checker_all_command_multiple_pages():
    # Test the "/all" command with multiple pages
    input_string = "/all 10"
    command, flags, values, pages = arguments_checker(input_string)
    assert command == "/all"
    assert flags is None
    assert values is None
    assert pages == 10

def test_arguments_checker_filter_command_valid_input():
    # Test the "/filter" command with valid input
    input_string = "/filter -gcat Rock, USA, Artist, Song 5"
    command, flags, values, pages = arguments_checker(input_string)
    assert command == "/filter"
    assert flags == ["genre", "country", "artist", "title"]
    assert values == ["Rock", "USA", "Artist", "Song"]
    assert pages == 5

def test_arguments_checker_filter_command_no_pages():
    # Test the "/filter" command with valid input but no pages specified
    input_string = "/filter -gcat Rock, USA, Artist, Song"
    command, flags, values, pages = arguments_checker(input_string)
    assert command == "/filter"
    assert flags == ["genre", "country", "artist", "title"]
    assert values == ["Rock", "USA", "Artist", "Song"]
    assert pages == 20  # Default to 20 pages if not specified

def test_arguments_checker_invalid_command():
    # Test an invalid command
    input_string = "/invalid -gc Rock, USA"
    command, flags, values, pages = arguments_checker(input_string)
    assert command is None
    assert flags is None
    assert values is None
    assert pages is None

def test_arguments_checker_invalid_flags():
    # Test input with invalid flags
    input_string = "/filter -xc Rock, USA"
    command, flags, values, pages = arguments_checker(input_string)
    assert command is None
    assert flags is None
    assert values is None
    assert pages is None

def test_arguments_checker_flags_values_mismatch():
    # Test input with mismatched number of flags and values
    input_string = "/filter -gc Rock USA Artist"
    command, flags, values, pages = arguments_checker(input_string)
    assert command is None
    assert flags is None
    assert values is None
    assert pages is None

def test_flags_mapping():
    # Test valid flags mapping
    string = "-acgt"
    attributes = flags_mapping(string)
    assert attributes == ["artist", "country", "genre", "title"]

def test_flags_mapping_invalid_flags():
    # Test input with invalid flags
    string = "-xyz"
    attributes = flags_mapping(string)
    assert attributes is None

def test_flags_mapping_mixed_valid_invalid_flags():
    # Test input with a mix of valid and invalid flags
    string = "-agxbct"
    attributes = flags_mapping(string)
    assert attributes is None

def test_remove_whitespace():
    # Test removing leading and trailing whitespace
    string = "  This is a test string.  "
    result = remove_whitespace(string)
    assert result == "This is a test string."

def test_pages_checker_with_pages():
    # Test input with specified number of pages
    input_string = "Some text 5"
    modified_string, pages = pages_checker(input_string)
    assert modified_string == "Some text"
    assert pages == 5

def test_pages_checker_without_pages():
    # Test input without specifying pages
    input_string = "Some text"
    modified_string, pages = pages_checker(input_string)
    assert modified_string == "Some text"
    assert pages == 20  # Default to 20 pages if not specified

def test_pages_checker_with_invalid_pages():
    # Test input with invalid pages
    input_string = "Some text not_a_number"
    modified_string, pages = pages_checker(input_string)
    assert modified_string == "Some text not_a_number"
    assert pages == 20  # Default to 20 pages if not a valid number