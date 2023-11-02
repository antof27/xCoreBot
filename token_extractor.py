"""
Module for extracting tokens from input strings.
"""

def flags_mapping(string):
    """
    Map flags to their corresponding attributes.

    Args:
        string (str): A string containing flags.

    Returns:
        list or None: A list of attributes corresponding to the flags, or None in case of an error.
    """
    string = string.split('-')[1]

    char_to_word = {
        'a': 'artist',
        'c': 'country',
        'g': 'genre',
        't': 'title'
    }

    if not all(char in char_to_word for char in string):
        print("Error: flag not found")
        return None

    words = [char_to_word[char] for char in string if char in char_to_word]
    return words


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


def pages_checker(string, pages=20):
    """
    Extract the number of pages if present and the remaining string.

    Args:
        string (str): The input string.
        pages (int): Default number of pages.

    Returns:
        tuple: A tuple containing the modified string and the number of pages.
    """
    if string.split(' ')[-1].isdigit():
        pages = int(string.split(' ')[-1])
        string = string.rsplit(' ', 1)[0]
    return string, pages


def arguments_checker(input_string):
    """
    Parse the input string to extract the command, flags, values, and pages.

    Args:
        input_string (str): The input string to be parsed.

    Returns:
        tuple: A tuple containing the command, flags, values, and pages.
    """
    command = input_string.split(" ")[0]
    flags = None
    values = None
    pages = 20

    if command == "/all":
        try:
            string, pages = pages_checker(input_string, pages)
            input_string = string
        except ValueError:
            return command, flags, values, pages
    elif command == "/filter":
        try:
            flags = input_string.split(" ")[1]
            flags = flags_mapping(flags)
            if flags is None:
                return None, None, None, None

            input_string, pages = pages_checker(input_string, pages)
            string_list = input_string.split(' ', 2)
            
            tags = string_list[2]
            
            values = tags.split(',')
            values = [remove_whitespace(value) for value in values]
            
            if len(flags) != len(values):
                print("Error: flags and values have different lengths")
                return None, None, None, None
        except Exception as e:
            print("Error:", str(e))
            return None, None, None, None
    else:
        print("Error: invalid command")
        return None, None, None, None
    return command, flags, values, pages

# Example usage:
String = "/filter -gcat rock, usa, artist, song 50"
Command, Flags, Values, Pages = arguments_checker(String)
print("Command: ", Command, "\nFlags: ", Flags, "\nValues: ", Values, "\nPages: ", Pages)
