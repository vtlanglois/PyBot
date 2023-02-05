import random
import openai
import secrets

openai.api_key = secrets.OPEN_AI_KEY

def handle_response(message) -> str:
    # Split message into arguments
    args = message.lower().split(" ")
    nargs = len(args)

    if args[0] == '!image':
        # assume the args after the !image command is the image generation prompt
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url

    if args[0] == '!ask':
        prompt = convert_args_to_prompt(args[1:nargs])
        prompt = "Answer the following prompt as simple as possible, with sufficient information. If your response has code, please use Markdown formatting for your code. The prompt is: " + prompt
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=255,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )

        answer = response['choices'][0]['text']
        return answer
    return args


#convert argument format to a string prompt
def convert_args_to_prompt(args) -> str:
    return ' '.join(args)
