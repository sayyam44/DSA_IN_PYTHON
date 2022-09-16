#^^^^^^^^^^^^^COPY^^^^^^^^^^^^^^
#tc=E*V
# https://www.youtube.com/watch?v=f2EfGComRKM&t=621s
# https://www.youtube.com/watch?v=mQeF6bN8hMk
# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldtonew={} #creating a hashmap which stores old nodes and new nodes as it is visited 

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]#if the node is already present in the hashmap then return that prev node

            #old value is node and new value for that node is copy
            copy=Node(node.val) #creating a new node 'copy' of the graph as copy if the node is already not present in hashmap
            oldtonew[node]=copy #in order to add all the nodes into hashmap

            for n in node.neighbors: #iterating through all the neighbors
                copy.neighbors.append(dfs(n)) #creating all the neighbors of new cloned node 'Copy'
            return copy
        return dfs(node) if node else None #inotrder to get a connected graphs





