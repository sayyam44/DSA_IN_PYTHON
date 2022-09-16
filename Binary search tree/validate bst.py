# https://www.youtube.com/watch?v=f-sj7I5oXEI&t=449s

# class TreeNode:
#     def __init__(self,key):
#         self.val=key
#         self.left=None
#         self.right=None
#for each node we will define a range and the node must lie within that range 
class solution:
    def isValisBST(self,root):
        def isValid(root,minVal,maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val>=maxVal:
                #if root.val is out of its range then return false
                return False
            else:
                return isValid(root.left,minVal,root.val) and isValid(root.right,root.val,maxVal)
        return isValid(root,-float("inf"),float("inf")) #as we dnt know the initial range so take it as - inf and +inf
        