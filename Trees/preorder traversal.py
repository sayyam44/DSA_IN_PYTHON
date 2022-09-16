# https://leetcode.com/problems/binary-tree-preorder-traversal/
##METHOD 1- RECURSIVE PREORDER
#TC=N,SC=N(auxiliary stack space)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:       
        if root== None:
            return[]
        res=[]
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        
        return res



#METHOD 2-ITERATIVE PREORDER
#TC=N,SC=N(auxiliary stack space)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:      
         
        stack=[]
        res=[]
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            root=stack.pop()
            root=root.right
        return res


