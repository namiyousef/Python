"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/trapping-rain-water/
Date started: 06.11.2020
Date complete: 
Results: 
    - faster than 5.45%
    - less memory than 87.19%
"""

def find_water(height):
    i = 0
    water = 0
    while i<len(height) - 1:
        if height[i]:
            j = i+1
            while j < len(height) - 1 and height[j] < height[i]:
                #and height[i] <= max(height[i+1:])
                water += min(height[i],max(height[j:])) - height[j]
                j += 1
            i = j
        else:
            i += 1
    return water


print(find_water(height = [0,1,0,2,1,0,1,3,2,1,2,1])) # 6

print(find_water(height = [4,2,0,3,2,5])) # 9


print(find_water(height = [4,2,3])) # 1

print(find_water(height = [0,1,0,2,1,0,1,3,2,1,2,1])) # 6

print(find_water(height = [5,4,1,2])) # 1