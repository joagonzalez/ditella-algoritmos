import sys

VOWELS = ['a', 'e', 'i', 'o', 'u']
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
RULE_TYPES = ['VOWEL', 'SIMPLE', 'DOUBLE_SIMPLE']
RULES = {
    'a': 'VOWEL',
    'b': 'SIMPLE',
    'c': 'SIMPLE',
    'd': 'SIMPLE',
    'e': 'VOWEL',
    'f': 'DOUBLE_SIMPLE',
    'g': 'SIMPLE',
    'h': 'hache',
    'i': 'VOWEL',
    'j': 'jota',
    'k': 'ka',
    'l': 'DOUBLE_SIMPLE',
    'm': 'DOUBLE_SIMPLE',
    'n': 'DOUBLE_SIMPLE',
    'o': 'VOWEL',
    'p': 'SIMPLE',
    'q': 'qu',
    'r': 'DOUBLE_SIMPLE',
    's': 'DOUBLE_SIMPLE',
    't': 'SIMPLE',
    'u': 'VOWEL',
    'v': 'SIMPLE',
    'w': 'doble ve',
    'x': 'equis',
    'y': 'i',
    'z': 'zeta'
}

RESULT =  []

for letter in LETTERS:
    l = {}
    if letter in RULES:
        if RULES[letter] == 'VOWEL':
            l[letter] = letter
            RESULT.append(l)
        elif RULES[letter] == 'SIMPLE':
            l[letter] = letter + 'e'
            RESULT.append(l)
        elif RULES[letter] == 'DOUBLE_SIMPLE':
            l[letter] = 'e' + letter + 'e'
            RESULT.append(l) 
        else:
            l[letter] = RULES[letter]
            RESULT.append(l) 

print(RESULT)     

def pronunciacion(letra):
    for letter in RESULT:
        if letra in letter:
            return letter[letra]