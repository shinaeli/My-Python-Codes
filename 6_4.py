glossary = {
    'loop': 'It is used to automate repetitive tasks.',
    'input': 'It is used to request for inputs from a user.',
    'string': 'It is a sequence of characters which are mainly letters, numbers and symbols.',
    'number': 'It is a data-type which can be an integer or a float.',
    'formatted string': 'It is a special type of string formulation that allows incorporation of expressions within it.'
}

for word, meaning in glossary.items():
    print(f'{word.title()}: \n{meaning}')