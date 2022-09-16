# ceil for a value in bst is the value that is just greater than or equal to that value
# https://www.youtube.com/watch?v=KSsk8AhdOZA&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=43

class TreeNode:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

    def ceil_(root,key):
        ceil=-1
        while root:
            if root.val==key:
                ceil=root.val
                return ceil
            if root.val<key: #every condition is same just update ceil while moving on left
                root=root.right
            else:
                ceil=root.val
                root=root.left
        return ceil