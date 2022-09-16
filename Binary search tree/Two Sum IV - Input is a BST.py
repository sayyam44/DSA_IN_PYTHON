# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# DO BST ITERATOR CODE - make a next stack same as bst iterator and another before named stack 
# Now check if st1.pop()+st2.pop()== k if yes then return true 

#this is the failed method but it follows the same procedure as BST ITERATOR just for understanding, THE 2ND solution is success

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, root: Optional[TreeNode]):
        self.s1=[]
        self.s2=[]
        while root:
            self.s1.append(root)
            root=root.left
        while root:
            self.s2.append(root)
            root=root.right
    def next_(self):
        node=self.s1.pop()
        x=node.right
        while x:
            self.s1.append(x)
            x=x.left
        i=node.val
        return i
    def before_(self):
        node_=self.s2.pop()
        y=node_.left
        while y:
            self.s2.append(y)
            y=y.right
        j=node_.val
        return j
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        i=self.next_() #i will be pointing towards the smallest elementof bst
        j=self.before_() #j will be pointing towards the largest element of bst
        while i<j:
            if i+j<k: #this means we will need to increase the min value that is i
                i=self.s1.pop()
            if i+j>k: #this means we would need to decrease the max value
                i=self.s2.pop()
            return (i+j)==k
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False

