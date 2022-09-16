# ^^^^^^^^^^COPY ^^^^^^^^^^
# https://www.youtube.com/watch?v=ZbybYvcVLks
# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        res=0
        
        Q=[(root, 0)] #root,index
        
        while(Q):
            res=max(res, 1 if len(Q)==1 else Q[-1][1]-Q[0][1]+1)
            # 1 if len(Q)==1 is only if there is one single node in the level
            # Q[-1][1]-Q[0][1]+1 means ek level ka last vala index - ussi level ka 1st vala index on the basis
            #of their hd value
            new=[] 
            for q in Q: #here we are doing indexing
                if q[0].left: #for 1st case q is the min value of Q. and q[0] is the node
                    new.append((q[0].left, 2*q[1])) #here q[1] is the index of that node.
                if q[0].right:
                    new.append((q[0].right, 2*q[1]+1))
            Q=new #in every case we are creating a new queue which contains only the elements , its indexes 
            #of that only level
        
        return res
    
