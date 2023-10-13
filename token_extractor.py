
def flags_mapping(string):
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

    else:
        words = [char_to_word[char] for char in string if char in char_to_word]
        return words


def remove_whitespace(string):
    string = string.strip()
    return string

def pages_checker(string, pages=20):
    if string.split(' ')[-1].isdigit():
        pages = int(string.split(' ')[-1])
        string = string.rsplit(' ', 1)[0]
    return string, pages


def arguments_checker(input_string):
    command = input_string.split(" ")[0]
    flags = None
    values = None
    pages = 20
    if command == "/all":
        try:
            string, pages = pages_checker(input_string, pages)
            input_string = string
        except:
            return command, flags, values, pages
        
    elif command == "/filter": 
        try:
            
            flags = input_string.split(" ")[1]
            flags = flags_mapping(flags)
            if flags == None:
                return None, None, None, None

            #check if the last element is a number, if so, store it and remove it from the list
            input_string, pages = pages_checker(input_string, pages)
            
            stringList = input_string.split(' ', 2)
            tags = stringList[2]    
            
            values = tags.split(',')
            values = [remove_whitespace(value) for value in values]

            # Check if flags and values have the same length
            if len(flags) != len(values):
                print("Error: flags and values have different length")
                return None, None, None, None
        except:
            print("Error: incorrect syntax")
            return None, None, None, None
        

    return command, flags, values, pages


'''
# Example usage:
input_string = "/all 50"
command, flags, values, pages = arguments_checker(input_string)
print("Command: ", command, "\nFlags: ", flags, "\nValues: ", values, "\nPages: ", pages)
'''

