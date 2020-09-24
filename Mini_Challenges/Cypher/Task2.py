# continuation from Task 1

# can you script solve the following puzzle? 

text = ('KCXCHUHCRIB KCGO RIKA CI RDW XCITB. QDH CP YO DBO RDW CXUZCIUHCRIB, RDW JRBBCQCKCHCOB'
        ' QOVRXO KCXCHKOBB. -FUXCO JURKCIOHHC')

# we need to a) unearth this message
# b) find out the key that was used in the encryption process
import re
from Task1 import find_possible_cypher
from Task1 import df
from Task1 import encrypt

text_list = re.split(',| |\.|-',text)
text_list = list(filter(None, text_list))

                     
text_decrypted = text
print(text_list)

matches = []
for word in text_list:
    print(word)
    code, _ = encrypt(word)
    matches.append(find_possible_cypher(code,df))
    text_decrypted = text_decrypted.replace(word,'{}',1)
    # need to now, after having found the 'possible' matches, you need to make sure that you find the indices
    # of the letters that appear together, i.e. 
    # KCXCHUHCRIB and CXUZCIUHCRIB have the same last 6 letters. So you need to run a script that goes
    # through words from 'text' that have the same length, matches their 'like indices' and then finds 
    # works from matches that match the same indices ! 
    
    # maybe don't even use previous stuff?
#print(matches)
    



