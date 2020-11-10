"""
Author: Yousef Nami
Problem definition: LeetCode November Challenge "Maximum Difference Between Node and Ancestor"
https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3525/
Date started: 10.11.2020
Date complete: 
Comments:
    
"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

root = TreeNode(
    8,
    TreeNode(3,
             TreeNode(1,
                      None,
                      None),
             TreeNode(6,
                      TreeNode(
                          4,
                          None,
                          None),
                      TreeNode(
                          7,
                          None,
                          None)
                      )
             ),
    TreeNode(10,
             None,
             TreeNode(14,
                      TreeNode(13,
                               None,
                               None),
                      None)
             )
    )

def findMax(root, init_tree = [[]]):
    trees = init_tree
    
    try:
        print(root.val)
    except:
        pass
    
    try:
        left = root.left
        trees[-1].append(left.val)
        trees = findMax(left, trees)
    except:
        try:
            right = root.right.val
            right = findMax(right, trees)
        except:
            trees.append([])
            return trees
        
    return trees

    
        
    #val, left, right = root.val, root.left, root.right
    #if left or right: # if the node has a subtree
    #    trees = findMax(left, trees)
    #    trees = findMax(right, trees)
    #else:
    #    trees.append([])
    #    return trees
    
a = findMax(root)
print(a)
    
        