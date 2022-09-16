# https://www.youtube.com/watch?v=QfJsau0ItOY&t=367s
# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#brute force approach i.e. DFS  from the root node then it will take n2 time , because we are iterating
# through each node 2 times , one for checking if balanced and other for finding the height difference.
#tc for brute force=n2

#optimized approach , i.e. start DFS recursively from LEAF(bottom) nodes instead of the root node 
# and return balanced or not(tru/false) and height in each iteration so that while iterating its parent
# node we will only check the diff between heights of its left subtree and right subtree must differ by 
# atmax 1 , reaching upto root node so 
# tc=n 

#optimized approach
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        #we are not using the above function directly because the above func is only returning bool value
        #but we want bool value as well as the height of this tree
        
        ##we are using another function and not the given function for recursion because the given function gives only one output i.e. bool but we want bool(if its balanced or not) and height of each subtree visited at each step.   
        def dfs(root):
            if not root: return [True,0]
            
            left,right=dfs(root.left),dfs(root.right)
            balanced=(left[0] and right[0] and abs(left[1]-right[1])<=1)
            #balanced will return the boolean value for the root of the above left and right calculated starting 
            # from the LEAF nodes left[0] and right[0] means both left and right subtrees must be true 
            # i.e. must be balanced)
                                          
            return (balanced,1+max(left[1],right[1])) #returning balanced true/false and height of the node
        return dfs(root)[0] #returning only thr boolean value for balanced or not.

