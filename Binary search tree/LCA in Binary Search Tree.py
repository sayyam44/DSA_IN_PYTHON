#if both p and q value are on left or both of them are on right of root then we move, 
#to the root at which one element is on its left and other is on right that root is the LCA. 

# https://www.youtube.com/watch?v=cX_kPV_foZc
#the moment we cannot say both p and q are on left or both p and q are on right that node is the lca
#tc=h(height of tree),sc=1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small=min(p.val,q.val)
        large=max(p.val,q.val)
        while root:
            if root.val > large:  # p, q belong to the left subtree
                root = root.left
            elif root.val < small:  # p, q belong to the right subtree
                root = root.right
            else:# Now, small <= root.val <= large -> This is the LCA between p and q
                #this means one value among p and q lies left side and another on the right side of root
                return root
        return None
