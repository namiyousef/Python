"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/zigzag-conversion/
Constraints:
    - input string length bounded by 1 and 1000
    - consists of lower and upper case chars, as well as '.' and ','
Date started: 21.10.2020
Date complete: 22.10.2020
Results: time limit exceeded, not sure why, code seems fairly efficient?
"""

def encrypt_zigzag(s='PAYPALISHIRING', numRows = 3):
    const = -2
    string = ""
    row1 = 2*numRows - 2
    for i in range(numRows):
        j = i
        const = -const
        if i != numRows -1 and i != 0:
            row1 -= 2
        else:
            row1 = 2*numRows - 2
        counter = 0
        while j < len(s) and j>=0:
            print(j,row1,i)
            string+= s[j]
            # need to add alternating += 2, depending on whether text is odd / even? 
            # write this on paper to visualise it better
            j = j+ row1 
            #if counter >0:
            #    j = j - const
            #    const = -const
            #counter += 1
                
    rows = [[] for _ in range(numRows)]
    for row in rows:
        row.append(1)
    print(string)
    
#encrypt_zigzag()


def zigzag(s = 'A', numRows = 5):
    string = ""
    delta = [2*numRows - 2, -2]
    if len(s) == 1:
        return s
    for i in range(numRows):
        j = i
        if i != numRows - 1 and i != 0:
            delta[0] -= 2
            delta[1] = 2*i

        else:
            delta[0] = 2*numRows -2
            delta[1] = 2*numRows -2
        index = 0
        while j < len(s):
            print(j,s[j],delta[index],index)
            string += s[j]
            j = j + delta[index]
            index = 1 - index

                
    return string
zigzag()

def zigzag_final(s='PAYPALISHIRING', numRows = 5):
    string = ""
    delta = 2*numRows - 2
    for i in range(numRows):
        j = i
        while j < len(s):
            string+=s[j]
            j += delta
            if i != numRows -1 and i != 0 and j - 2*i < len(s):
                string+=s[j - 2*i]
    return string
zigzag_final()    