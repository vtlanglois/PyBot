from commands import openai_api, help

def handle_response(message) -> str:
    # Split message into arguments
    args = message.lower().split(" ")
    nargs = len(args)

    if args[0] == '!help':
        return help.generate_help_response(args)
    if args[0] == '!draw':
        return openai_api.draw_image(args)
    if args[0] == '!ask':
        return openai_api.generate_text_response(args)
    return args


# convert argument format to a string prompt
def convert_args_to_prompt(args) -> str:
    return ' '.join(args)
