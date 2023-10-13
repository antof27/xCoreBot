

def flags_mapping(string):
    string =  string.split('-')[1]

    for char in string:
        char = {
            'a' : 'artist',
            'c' : 'country',
            'g' : 'genre',
            't' : 'title'
            }
        print("char", char)

    return char    
    

def arguments_checker(input_string):
    command = input_string.split(" ")[0]
    flags = None
    values = None
    if command == "/all":
        return command, flags, values
    elif command == "/filter": 
        
        flags = input_string.split(" ")[1]

        stringList = input_string.split(' ', 2)
        tags = stringList[2]            
        values = tags.split(',')
            
        

    return command, flags, values


    



# Example usage:
input_string = "/filter -a bring"

command, flags, values = arguments_checker(input_string)
print("Command: ", command)
print("Flags: ", flags)
print("Values: ", values)

'''
command, flags, values = arguments_checker(input_string)
print("Command", command)
print("Flags", flags)
print("Values", values)
'''