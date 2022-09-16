# floor for a value in bst is the value that is just smaller or equal to that value
# https://www.youtube.com/watch?v=xm_W1ub-K-w&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=44
class TreeNode:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

    def floor_(root,key):
        floor=-1 #update floor whenever we find some value smaller than or equal to key
        while root:
            if root.val==key:
                floor=root.val
                return floor

            if key>root.val: #we will update the value of floor everytime we find some root value smaller than key value
                #and we need to find the val(max)<=key
                floor=root.val #update floor 
                root=root.right  #because we need to find max value that is just less than key so in bst we will find max value on right of root
            else:
                root=root.left
        return floor
            
