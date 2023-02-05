import random
import openai
import secrets

openai.api_key = secrets.OPEN_AI_KEY


def handle_response(message) -> str:
    # Split message into arguments
    args = message.lower().split(" ")
    nargs = len(args)

    if args[0] == '!image':
        prompt = ' '.join(args[1:nargs])
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    return args
