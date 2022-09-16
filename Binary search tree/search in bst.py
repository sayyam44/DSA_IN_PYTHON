# https://leetcode.com/problems/search-in-a-binary-search-tree/
# tc= height of the tree
# class TreeNode:
#     def __init__(self,key):
#         self.val=key
#         self.left=None
#         self.right=None

class solution:
    def searchBST(self,root,val):
        if not root:
            return 
        if root.val=val:
            return root
        if root.val>val:
            return self.searchBST(root.left,val)
        if root.val<val:
            return self.searchBST(root.right,val)