def song_cleaning(song):
    """
    Clean song title by removing parentheses and square brackets.

    Args:
        song (str): The song title.

    Returns:
        str: The cleaned song title.
    """
    song = song.split("(")[0].strip()
    song = song.split("[")[0].strip()
    return song


def lower_case(string):
    """
    Convert a string to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The lowercase string.
    """
    return string.lower()

def remove_whitespace(string):
    """
    Remove leading and trailing whitespace from a string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with leading and trailing whitespace removed.
    """
    string = string.strip()
    return string

def values_extractor(flags, values):
    """
    Extract query values based on flags.

    Args:
        flags (list): List of flags.
        values (list): List of corresponding values.

    Returns:
        tuple: The extracted query values (query_genre, query_country, query_artist, query_title).
    """
    flag_mapping = {
        "genre": None,
        "country": None,
        "artist": None,
        "title": None
    }

    for flag in flag_mapping:
        if flag in flags:
            index = flags.index(flag)
            flag_mapping[flag] = values[index]

    query_genre = flag_mapping["genre"]
    query_country = flag_mapping["country"]
    query_artist = flag_mapping["artist"]
    query_title = flag_mapping["title"]

    return query_genre, query_country, query_artist, query_title