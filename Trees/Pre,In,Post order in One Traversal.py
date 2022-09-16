# ^^^^^^^^^^COPY^^^^^^^^^^^^^
# https://www.geeksforgeeks.org/preorder-postorder-and-inorder-traversal-of-a-binary-tree-using-a-single-stack/
# https://www.youtube.com/watch?v=ySp2epYvgTE

class None:
    def __init__(self,key):
        self.val=key
        self.right=right
        self.left=left

def allTraversal(root):
    pre=[]
    post=[]
    inn=[]
    s=[]
    s.append([root,1]) #node,num
    #keep one thing in mind that we will only pop in inorder traversal because we need all the nodes in all the 3 traversals
    while (len(s)):
        p=s[-1] # Stores the top element of the stack bot node and num
        if p[1]==1:
            pre.append(p[0].val) #appending only the node.val part
            s[-1][1]+=1 # Update the status of top node
            if p[0].left:
                s.append(p[0].left,1)
        
        elif p[1]==2:
            inn.append(p[0].val)
            s[-1][1]+=1
            if p[0].rght:
                s.append(p[0].right,1)
            
        elif p[1]==3:
            post.append(p[0].val)
            stack.pop()





    print("Preorder Traversal: ",end=" ")
    for i in pre:
        print(i,end=" ")
    print()
 
    # Printing Inorder
    print("Inorder Traversal: ",end=" ")
 
    for i in inn:
        print(i,end=" ")
    print()
 
    # Printing Postorder
    print("Postorder Traversal: ",end=" ")
 
    for i in post:
        print(i,end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
 
    # Creating the root
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    # Function call
    allTraversal(root)





