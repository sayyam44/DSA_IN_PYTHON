# https://leetcode.com/problems/binary-tree-paths/
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val= val
#         self.left=left
#         self.right=right
def binarytreepaths(self,root):
    ans=[]
    def dfs(root,s):
        nonlocal ans
        if root.left:
            dfs(root.left,s+"->"+str(root.left.val))
        if root.right:
            dfs(root.right,s,"->"+str(root.right.val))
        if not root.left and not root.right:
            ans.append(s)
        return 
    dfs(root,str(root.val))
    return ans 


