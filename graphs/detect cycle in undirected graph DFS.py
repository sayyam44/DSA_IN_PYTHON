#^^^^^^^COPY^^^^^^
#tc=n,sc=n
#https://www.youtube.com/watch?v=Y9NFqI6Pzd4&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=10

from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def dfs_recur(self,v,visited,parent): #v=the current node , parent = the parent node of the current node
        visited[v]=True #making the current node's visited array val as true
        for i in self.graph[v]: #checking for all the adjacent nodes of the current node v
            if visited[i]==False:
                if (self.dfs_recur(i,visited,v)):#here the parent node= v, and the current node= i
                    #this is recursively checking if any neighbor is already been visited 
                    return True #yes, there is cycle
                elif parent != i:
                    return False  #no, there is not a cycle
        return False
    def dfs(self): #same as detect cycle in undirected graph using bfs
        visited=[False]*(max(self.graph)+1)
        for i in range(max(self.graph)+1):
            if visited[i]==False: #checking for the current node
                if (self.dfs_recur(i,visited,-1)):
                    return True #yes, there is cycle
        return False #no, there is not a cycle
g = graph(5)
g.addedge(1, 0)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(0, 3)
g.addedge(3, 4)
 
if g.dfs():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
g1 = graph(3)
g1.addedge(0, 1)
g1.addedge(1, 2)
 
 
if g1.dfs():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")