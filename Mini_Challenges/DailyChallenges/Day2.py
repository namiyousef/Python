"""
Author: Yousef Nami
Problem description: https://leetcode.com/problems/add-two-numbers/
Date started: 14.10.2020
Date completed: 14.10.2020
"""

def add_numbers(list1, list2):
    output = []
    num1 = convert_to_str(list1)
    num2 = convert_to_str(list2)
    total = str(int(num1) + int(num2))
    for i in range(len(total), 0, -1):
        output.append(int(total[i-1]))
    return output


def convert_to_str(list_num):
    mystring = ''
    for num in list_num:
        mystring += str(num)
    return mystring


print(add_numbers([9,9,9,9,9,9,9],[9,9,9,9]))

# verification seems to work here; was not able to get it on LeetCode


print(add_numbers([2,4,3],[5,6,4]))

# figured out why this does not work...
# seems like the LeetCode will require the outcome to be in a 'ListNode' format...
# major modifications had to be made to the LeetCode submission...
