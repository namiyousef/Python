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
         
     def findTrees(root, init_tree = [[]]):
         
        trees = init_tree
        #if len(trees) == 1 and not len(trees[-1]):
        #    trees[-1].append(root.val)
        try:
            left = root.left
            #trees[-1].append(trees[-1][:TreeNode.counter])
            trees[-1].append(left.val)
            trees = TreeNode.findTrees(left, trees)
        except:

            pass
        
        try:
            right = root.right
            trees[-1].append(right.val)
            trees = TreeNode.findTrees(right, trees)
        except:
            trees.append([])

        return trees 
    
     def findMax(trees, i = 0, first_node = 8, diff = 0):
        print(i)
        if not len(trees[i]):
            return diff # ensures that we return the first node if no other nodes
        
        try:
            len(trees[i]) #checks whether tree has ended or not
                # if the length hasn't ended, i.e. we still have a tree
               # then
            max_val = first_node if first_node > max(trees[i]) else first_node
            diff = diff if max_val - min(trees[i]) < diff else max_val - min(trees[i])
            diff = TreeNode.findMax(trees, i = i + 1, first_node = trees[i][0], diff = diff)
        except:
            diff = TreeNode.findMax(trees, i = i + 1, first_node = 8, diff = diff)
        
        return diff

                
                
     
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

root2 = TreeNode(
    1,
    None,
    TreeNode(
        2,
        None,
        TreeNode(
            0,
            TreeNode(
                3,
                None,
                None
                ),
            None
            )
        )
    )


root3 = 0
        
"""    try:
        left = root.left
        trees[-1].append(left.val)
        trees = findMax(left, trees)
        
        
        right = root.right
        trees[-1].append(root.val)
        trees[-1].append(right.val)
        right = findMax(right, trees)
    except:
        try:
            
            right = root.right
            trees[-1].append(right.val)
            right = findMax(right, trees)
            
            left = root.left
            trees[-1].append(left.val)
            trees = findMax(left, trees)
        except:
            trees.append([])
       
    return trees
"""
a = TreeNode.findTrees(root)
print(a)

b = TreeNode.findMax(a)
print(b)
