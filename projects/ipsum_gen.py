from random import randint

pokemon = [
    'Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Eevee', 'Meowth', 'Mew', 'Snorlax', 'Dratini', 'Geodude', 'Zubat', 'Scyther', 'Sandshrew', 'Machop'
]

def pokerize(word):
    random_pos = randint(0, len(pokemon) - 1)
    return f'{word}{pokemon[random_pos]}'    

paragraphs = int(input('How many poke paragraphs? -> '))

with open('ipsum.txt') as ipsum_original:
    items = ipsum_original.read().split()
    
    for n in range(paragraphs):
        poke_text = list(map(pokerize, items))
        with open('poke_ipsum.txt', 'a') as poke_ipsum:
            poke_ipsum.write(' '.join(poke_text) + '\n\n')