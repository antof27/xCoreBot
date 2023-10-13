
def flags_mapping(string):
    string = string.split('-')[1]

    char_to_word = {
        'a': 'artist',
        'c': 'country',
        'g': 'genre',
        't': 'title'
    }

    words = [char_to_word[char] for char in string if char in char_to_word]

    return words


def remove_whitespace(string):
    string = string.strip()
    return string


def arguments_checker(input_string):
    command = input_string.split(" ")[0]
    flags = None
    values = None
    if command == "/all":
        return command, flags, values
    elif command == "/filter": 
        try:
            flags = input_string.split(" ")[1]
            flags = flags_mapping(flags)

            stringList = input_string.split(' ', 2)
            tags = stringList[2]            
            values = tags.split(',')
            values = [remove_whitespace(value) for value in values]

            # Check if flags and values have the same length
            if len(flags) != len(values):
                print("Error: flags and values have different length")
                return None, None, None 
        except:
            print("Error: incorrect syntax")
            return None, None, None
        

    return command, flags, values


    
# Example usage:
input_string = "/filter -g progressicve"
command, flags, values = arguments_checker(input_string)


