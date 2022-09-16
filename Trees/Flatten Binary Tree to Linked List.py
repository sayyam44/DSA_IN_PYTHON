# https://www.youtube.com/watch?v=sWf7k1x9XR4
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#we are converting a tree into another tree basically with all the right edges  
from sympy import preview
class Solution:
    def __init__(self):
        self.prev= None
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        self.flatten(root.right)
        self.flatten(root.left)
        root.right=self.prev
        root.left= None
        self.prev= root #updating the prev value

