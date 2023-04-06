
valid_terms = ['binary', 'text']


def determine_conversion(args) -> str:
    
    #guard clauses
    if(len(args) <= 3):
        return 'Error: Format <to> <from> <...terms>'
    if(args[1] not in valid_terms):
        return "Error: invalid <to> term"
    if(args[2] not in valid_terms):
        return "Error: invalid <from> term"

    if (args[1].lower() == 'binary' and args[2].lower() == 'text'):
        return convert_binary_to_text(args[3:])
    elif (args[1].lower() == 'text' and args[2].lower() == 'binary'):
        return convert_text_to_binary(args[3:])
        


def convert_text_to_binary(args):
    prompt = convert_args_to_prompt(args[0:len(args)])
    response = ' '.join(format(ord(char), '08b') for char in prompt)
    return response


def convert_binary_to_text(args):
    prompt = convert_args_to_prompt(args[0:len(args)])
    response = "".join([chr(int(binary, 2)) for binary in prompt.split(" ")])
    return response


# convert argument format to a string prompt
def convert_args_to_prompt(args) -> str:
    return ' '.join(args)
