# https://www.youtube.com/watch?v=D2jMcmxU4bs
#bst iterator means to implement next() and hasnext() function for bst .
#start the root from BSTiterator value and push all the values to its left into the stack one by one, 
# for NEXT pop the element from stack and push all the elements to the nodes right's left  if it have
# for HASnext if there are any elements in the stack then return true else return false

#sc=h , as we are just storing left left left elements that is equaivalent to height 
#tc=1, pushing n elements on n calls i.e. = n/n=1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left

    def next(self) -> int: #since we are following inorder traversal
        node=self.stack.pop()
        x=node.right
        while x:
            self.stack.append(x)
            x=x.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack)>0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()