##VERY IMPORTANT---- INORDER TRAVERSAL OF BST ALWAYS GIVES YOU THE NODES IN SORTED FORMAT increasing order 
# https://www.youtube.com/watch?v=9TJYWh0adfk
#BUT IF WE DIRECTLY DO INORDER TRAVERSAL AND FIND THE Kth SMALLEST/Largert ELEMENT IT WILL TAKE N EXTRA SPACE FOR STORING 

#INSTEAD WE WILL USE A COUNTER AND START DOING INORER TRAVERSAL DO COUNTER++ AND WHEN WE REACH COUNTER==K THAT NODE WILL BE THE REQ Kth SMALLEST NODE

#FOR FINDING Kth LARGEST ELEMENT WE NEED TO FIND (len(root)-K)th smallest element


#Kth smallest element in bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.helper(root,res)
        return res[k-1]
    def helper(self,node,res):
        if not node:
            return 
        self.helper(node.left,res)
        res.append(node.val)
        self.helper(node.right,res)

#Kth largest element in bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.helper(root,res)
        return res[len(res)-(k-1)]
    def helper(self,node,res):
        if not node:
            return 
        self.helper(node.left,res)
        res.append(node.val)
        self.helper(node.right,res)
        
        
