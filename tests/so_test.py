from src.strings_operations import song_cleaning, lower_case, remove_whitespace, values_extractor

def test_song_cleaning():
    # Test with parentheses and square brackets
    assert song_cleaning("Song (feat. Artist)") == "Song"
    assert song_cleaning("Song [Official Music Video]") == "Song"
    # Test without parentheses and square brackets
    assert song_cleaning("Song Title") == "Song Title"

def test_lower_case():
    # Test with uppercase string
    assert lower_case("RAIN") == "rain"
    # Test with mixed case string
    assert lower_case("DiE fOr yOU") == "die for you"
    # Test with already lowercase string
    assert lower_case("the devil exists") == "the devil exists"

def test_remove_whitespace():
    # Test with leading and trailing whitespace
    assert remove_whitespace("  hello  ") == "hello"
    # Test with leading whitespace
    assert remove_whitespace("  hello") == "hello"
    # Test with trailing whitespace
    assert remove_whitespace("hello  ") == "hello"
    # Test with no leading or trailing whitespace
    assert remove_whitespace("hello") == "hello"

def test_values_extractor():
    # Test with all flags and values provided
    flags = ["genre", "country", "artist", "title"]
    values = ["progressive", "usa", "currents", "remember me"]
    assert values_extractor(flags, values) == ("progressive", "usa", "currents", "remember me")
    # Test with only genre flag provided
    flags = ["genre"]
    values = ["metalcore"]
    assert values_extractor(flags, values) == ("metalcore", None, None, None)
    # Test with no flags provided
    flags = []
    values = []
    assert values_extractor(flags, values) == (None, None, None, None)
