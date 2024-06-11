from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots','potatoes']
anagrams = []

# Option One, 'for' loop:
# -----------------------

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# ----------------------

# Option Two: 'map' function:
# -- Map funtion Syntax:
# -- map(function, data)
# ----------------------

# print(list(map(jumble,words)))

# ----------------------

# Option Three: comprehension method
# -----------------------

print( [ jumble(word) for word in words ] )
