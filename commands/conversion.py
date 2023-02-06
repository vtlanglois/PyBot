

def determine_conversion(args) -> str:
    return convert_text_to_binary(args)

def convert_text_to_binary(args):
    prompt = convert_args_to_prompt(args[1:len(args)])
    response = ' '.join(format(ord(char), '08b') for char in prompt)
    return response


# convert argument format to a string prompt
def convert_args_to_prompt(args) -> str:
    return ' '.join(args)