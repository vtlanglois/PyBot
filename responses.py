from commands import dictionary, openai_api, help, conversion


def handle_response(message) -> str:
    # Split message into arguments
    args = message.lower().split(" ")
    nargs = len(args)

    match args[0]:
        case '!help':
            return help.generate_help_response(args)
        case '!draw':
            return openai_api.draw_image(args)
        case '!ask':
            return openai_api.generate_text_response(args)
        case '!convert':
            return conversion.determine_conversion(args)
        case '!define':
            return dictionary.generate_word_definition(args)
    return args


# convert argument format to a string prompt
def convert_args_to_prompt(args) -> str:
    return ' '.join(args)
