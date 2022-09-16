# https://www.youtube.com/watch?v=fmflMqVOC7k&t=506s
#tc=n in worst case ,where n is the number of nodes in the binary tree

class TreeNode:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

class solution:
    def check(root,k,arr):
        if not root:
            return False
        
        arr.append(root.val)

        if root.val==k:
            return true
        
        if self.check(root.left,k,arr) or self.check(root.right,k,arr):
            return True
        
        arr.pop(-1)
        return False

    def printpath(root,k):
        arr=[]
        if check(root,k,arr):
            for i in (len(arr)-1):
                print(arr[i],"-->")
            print(arr[len(arr)-1])
        else:
            print('x is not present')


def checkpath(root,k,arr):
    if not root:
        return False
    arr.append(root.val)
    if root.val==k:
        return True

    if self.checkpath(root.left,k,arr) or self.checkpath(root.right,k,arr):
        return True
    
    else:
        arr.pop(-1)
        return False

def path(root,k):
    arr=[]
    if checkpath(root,k,arr):
        for i in range(len(arr)-1):
            print(arr[i],'-->')
        print(len(arr)-1)
    else:
        print(not present)
