# https://www.youtube.com/watch?v=q_a6lpbKJdw
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231327/PYTHON-solution-with-explanation

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = collections.defaultdict(list) #defining a dict
        q = collections.deque([[root, 0, 0]]) #val,hd,level

        while q:
            for i in range (len(q)):
                node,x,y=q.popleft()
                dic[x].append((y,node.val)) # hd,l,val #eg. vertical={0:[0,3],-1:[1,9]....etc}

                if node.left:
                    q.append(node.left,x-1,y+1) # going down if node. left is present then hd by -1 and level by +1 
                if node.right:
                    q.append(node.left,x+1,y+1) # going down if node. left is present then hd by +1 and level by +1 
        
        output=[]
        for i in sorted(dic.keys()): #sorting dict on hd values
            level=[x[1] for x in sorted(dic[i],key=lambda x:(-x[0],x[1]))]   
            #here we are sorting level wise and returning the x[1] that is the node values.
			output.append(level)
        
        return output




