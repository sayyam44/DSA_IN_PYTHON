# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #the deepest/lowest common node.val among all the ancestors of the given 2 elements
        if not root:
            return None
        if root.val==p or root.val==q:
            return root
        
        # Look for keys in left and right subtrees
        left_lca=self.lowestCommonAncestor(root.left,p,q)
        right_lca=self.lowestCommonAncestor(root.right,p,q)

        #if for a node one element occurs in node.left and another occurs in node.right 
        #then that node will be the lca node
        if left_lca and right_lca:
            return root
        
        #if above conditions doesnt satisfy then check seperately in the left and right subtree
        return left_lca if left_lca else right_lca
