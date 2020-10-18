"""
Author: Yousef Nami
Problem difficulty: medium
Problem description: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Problem constraints:
    - length of string <= 5*10^4
    - string can have letters, digits symbols and spaces
Assumptions:
    - unclear from the problem whether upper or lower case lettering matters. Will assume that upper case
    letters are distinct from their lower case counterparts
Date started: 18.10.2020
Date complete: 18.10.2020
Results:
    - faster than 11.33% of online submissions
    - less memory than 100% of online submissions

"""

def find_longest_substring(string = 'Yousef'):
    length = len(string)
    substrings = []
    for i in range(length):
        substring_found = 0
        substring = ""
        j = 0
        while not substring_found and i+j < length:
            if string[i+j] not in substring:
                substring += string[i+j]
            else:
                substring_found = 1
            j+=1
            
        substrings.append(substring)

#        if substrings and len(substrings[-1]) > length/2:
 #           return len(substrings[-1])

    if substrings:
        #print()
        return len(max(substrings, key = len))
    else:
        return 0

print(find_longest_substring("anviaj"))
