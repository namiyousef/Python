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
        my_target = nums[i]
        
        for j in range(i+1,len(nums)):
            my_target += nums[j]
            if my_target == target:
                number_found = True
                indices = [i, j]
                break
            my_target = nums[i]
            
        i+=1
    return indices
    

# test
    
print(return_indices(nums = [2,7,11,15], target = 9))
            
            
print(return_indices(nums = [3,2,4], target = 6))

print(return_indices(nums = [3,3], target = 6))

print(return_indices(nums = [3,2,3], target = 6))

# feedback:

# runtime: 7 ms, faster than 5.01% of submissions
# memory: 15.1 MB, less than 15.82% of submissions
# significant improvements needed


# things I can learn:    
        
def kinetic_energy(m:'in KG', v:'in M/S' = 4)->'Joules': 
    ke = 1/2*m*v**2
    return ke

"""
From what you can see above, when declaring functions you can add some annotations to the functions for the
purposes of documentation. 

This is better than the way you used to it. So in a sense, you can document some stuff like units 
or the ideal datatype, for example int, float.
"""