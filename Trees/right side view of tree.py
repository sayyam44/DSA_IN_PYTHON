# youtube.com/watch?v=KV4mRzTjlAk&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=26
# https://leetcode.com/problems/binary-tree-right-side-view/
#tc=n,sc=H(height of tree)
# Input: root = [1,null,3]
# Output: [1,3]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #root,right,left traversal
        
        self.res=[]
        self.newfunc(root,0)
        return self.res
        
    def newfunc(self,root,level):
        if not root:
            return
        if level == len(self.res):
            self.res.append(root.val)
        self.newfunc(root.right,level+1) #jonsa view dekhna hai usko pehle iterate karna hai so that level = res size par right side vale elements print honge
        self.newfunc(root.left,level+1)

