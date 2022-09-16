# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# class TreeNode:
#     def __init__(self,key):
#         self.val=key
#         self.left=None
#         self.right=None
class solution :
    def sortedarraytobst(self,nums):
        def dfs(r,l): #r gives the index of root in the tree and l gives hte index of last node of tree i.e. len(nums)-1
            if r>l or r<0 or l<0 or l>=len(nums) or r>=len(nums):
                return None
            
            mid= (r+l)//2 #floor division
            root=TreeNode(nums[mid])
            root.left=nums[r,mid-1]
            root.right=nums[mid+1,l]
            return root
        return dfs(0,len(nums)-1)


