import requests
import json

def generate_word_definition(args) -> str:
    if len(args) != 2:
        return "Please enter a word to define\nFORMAT: !define <word>"
    
    word = args[1]
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    info = json.loads(response.text)
    info = info[0]
    header = "{word}\n".format(word=info.get('word'))
    body = ''
    for meaning in info.get('meanings'):
#        body += 'Part of Speech: {partOfSpeech}\n'.format(meaning.get("partOfSpeech"))
        definitions = meaning.get('definitions')
        for definition in definitions:
            body += '> {definition}\n'.format(definition=definition.get("definition"))

    message = "{header}{body}".format(header=header, body=body)
    return message
