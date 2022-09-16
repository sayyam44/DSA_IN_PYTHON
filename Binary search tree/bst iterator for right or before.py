#see bst iterator for left solution

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
            root=root.right

    def next(self) -> int: #since we are following inorder traversal
        node=self.stack.pop()
        x=node.left
        while x:
            self.stack.append(x)
            x=x.right
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack)>0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()