#^^^^^^^^^^^^^^^^^ COPY ^^^^^^^^^^^^^^^^^^
# https://www.youtube.com/watch?v=bkxqA8Rfv04
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS, tc=n
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[] #it will have all the diameters
        
        def dfs(root): #we are using another function and not the given function for recursion because the given function gives only one output i.e. int but we want height and depth 2 outputs.
            if not root :
                return -1 #for null tree height = -1
            left=dfs(root.left)
            right=dfs(root.right)
            res.append(max(res[0],left+right+2)) #calculating diameter here
            
            return 1 + max(left,right) #calculating height here
            #we are returning height because for calculating diameter also we need height left+height right+2
        dfs(root)
        return res[0]

