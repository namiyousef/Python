path = '/Users/yousefnami/Desktop/Yousef/PrivateTings/My Stuff/Coding/Python/Python_Learning/Python/Mini_Challenges/Cypher/Files/words.txt'

f = open(path,'r')

text = f.read()

text_list = text.split('\n')

# Part 1: for any string of chars, return a pattern, i.e. apple = 01123
def encrypt(string):
    letters = {}
    encrypted_string = ''
    counter = 0
    for letter in string:
        if letter not in letters:
            letters[letter] = counter
            encrypted_string += str(counter)

            counter += 1
        else:        
            encrypted_string += str(letters[letter])
    return encrypted_string,letters

print(encrypt('apple'))

# Part 2: for a given string of characters representing a word pattern , return possible candidate words

import pandas as pd

df = pd.DataFrame(data = {
    'string': text_list,
    'length': [len(string) for string in text_list]
    })
    
def find_possible_cypher(code, df):
    df = df[df.length == len(code)]
    matches = []
    for string in df.string.values:
        encrypted_string, _ = encrypt(string)
        if encrypted_string == code:
            matches.append(string)
    
    return matches
        
print(find_possible_cypher('01223',df))

