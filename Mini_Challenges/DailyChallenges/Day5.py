"""
Author: Yousef Nami
Problem difficulty: hard
Problem description: https://leetcode.com/problems/median-of-two-sorted-arrays/
Problem constraints:
    - list length <= 1000
    - at least one of the lists must have at least 1 item
    - numbers in list -10^6 <= and <= 10^6 
Assumptions:
    - you can have arrays that include repetitive numbers
Date started: 19.10.2020
Date complete:
Results:
    - faster than 20.98% of users
    - less memory than 8.02% of submissions
"""
import statistics as stat
def find_median(list1, list2):
    n = len(list1)
    m = len(list2)
    if list1 and list2:
        if n >= m:
            lower = 0
            for num in list1:
                lower, list2 = find_index(list2, num, lower)
            return stat.median(list2)
        else:
            lower = 0
            for num in list2:    
                lower, list1 = find_index(list1, num, lower)
            return stat.median(list1)
        
    elif len(list1+list2)%2 == 0:
        return ((list1+list2)[int((n+m)/2)]+(list1+list2)[int((n+m)/2)-1])/2
    else:
        return (list1+list2)[int((n+m-1)/2)]
    
    
def find_index(input_list,num, lower):
    lower = lower
    upper = len(input_list) -1
    if num >= input_list[upper]:
        input_list.insert(upper+1, num)
    elif num <= input_list[lower]:
        input_list.insert(lower, num)
    else:  
        while upper-lower != 1:
            mid = int((lower+upper)/2)
            if num > input_list[mid]:
                lower = mid
            else:
                upper = mid
        input_list.insert(lower+1,num)
    return lower, input_list


print(find_index([1,2,3],2,0))

print(find_median([],[1]))