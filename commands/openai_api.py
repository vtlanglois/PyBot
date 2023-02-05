import openai
import secrets

openai.api_key = secrets.OPEN_AI_KEY

"""
This file contains all the necessary functions and helper functions for OpenAI image and text generation API calls.
"""
def draw_image(args) -> str:
    prompt = convert_args_to_prompt(args[1:len(args)])
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url


def generate_text_response(args) -> str:
    instructions = "Answer the following prompt with sufficient information in a kind and friendly manner. If your response has code, please use Markdown formatting for your code. The prompt is: "
    prompt = instructions + convert_args_to_prompt(args[1:len(args)])
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    answer = response['choices'][0]['text']
    return answer



# convert argument format to a string prompt
def convert_args_to_prompt(args) -> str:
    return ' '.join(args)
