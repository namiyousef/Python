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

def encrypt_zigzag(s='PAYPALISHIRING', numRows=3):
    string = ""
    row1 = 2*numRows - 2
    for i in range(numRows):
        j = i
        if i != numRows -1 and i != 0:
            row1 -= 2
        else:
            row1 = 2*numRows - 2
        while j < len(s) and j>=0:
            print(j,row1)
            string+= s[j]
            # need to add alternating += 2, depending on whether text is odd / even? 
            # write this on paper to visualise it better
            j = j+ row1 
        
    rows = [[] for _ in range(numRows)]
    for row in rows:
        row.append(1)
    print(string)
    
encrypt_zigzag()