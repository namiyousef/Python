"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/zigzag-conversion/
Constraints:
    - input string length bounded by 1 and 1000
    - consists of lower and upper case chars, as well as '.' and ','
Date started: 21.10.2020
Date complete:
Results:
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
    
encrypt_zigzag()


def zigzag(s = 'PAYPALISHIRING', numRows = 4):
    string = ""
    const = -2
    delta = [2*numRows - 2, -2]
    index = 0
    activate_flipflop = False
    for i in range(numRows):
        j = i
        if i != numRows - 1 and i != 0:
            delta[index] -= 2
            if i != int(numRows/2):
                activate_flipflop = True

        else:
            delta[index] = 2*numRows -2
            activate_flipflop = False
        while j < len(s):
            string += s[j]
            j = j + delta[index]
            if activate_flipflop:
                #index = 1 - index
                #j += delta[index]
                delta[index] += const
                const = -const
                
            
    print(string)
zigzag()