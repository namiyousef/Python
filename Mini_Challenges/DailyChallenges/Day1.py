"""
Author: Yousef Nami
Problem description: see https://leetcode.com/problems/two-sum/
Date started: 13.10.2020
Date completed: 13.10.2020
"""

def return_indices(nums, target):
    """
    A function that returns the indices of the digits in `nums` that add up to create `target`
    """
    indices = []
    i = 0
    number_found = False
    while not number_found:
        my_target = 0
        
        for j in range(i,len(nums)):
            my_target += nums[j]
            if my_target == target:
                number_found = True
                indices = [j-1, j]
                break
            
        i+=1
    return indices
    

# test
    
print(return_indices(nums = [2,7,11,15], target = 9))
            
            
print(return_indices(nums = [3,2,4], target = 6))

print(return_indices(nums = [3,3], target = 6))
