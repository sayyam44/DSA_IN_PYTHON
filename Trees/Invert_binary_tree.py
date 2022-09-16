# https://leetcode.com/problems/invert-binary-tree/
#DFS method
#tc=n(only traversing the tree)
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #use recursive methode 
        #step1- swap left with right subtree
        #step2- run the same on the left subtree and then on right sub tree
        
        if root is None:
            return None
        
        temp=root.left
        root.left=root.right
        root.right=temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

            