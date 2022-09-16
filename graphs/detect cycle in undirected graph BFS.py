#for this we will append the values,parent values into the queue as we iterate through them by bfs rule
#https://www.youtube.com/watch?v=A8ko93TyOns&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=9
from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    
    def bfs_recur(self,v,visited,parent): #parent node is the previous node of current node , significance
        #  of parent node is that parent node is already True in visited just before  so we need not
        #  to return if we get True for parent node in visited we just need to return False that there is no cycle
        visited[v]=True
        q=[[v,parent]]
        while q:
            a,b=q.pop()
            for i in self.graph[a]:
                if visited[i]==False:
                    q.append([i,v])
                    visited[i]==True
                    if (self.bfs_recur(self,i,visited,v)):
                        return True
                    elif parent !=i: #other than the 1st case if parent==i then return False
                        return False
            return False

                    

    def bfs(self):
        visited=[False]*(max(self.graph)+1)
        for i in (max(self.graph)+1): #this for loop is to iterate through all the nodes of graph whether or not it is connected or not connected graph
            if visited[i]==False:
                if (self.bfs_recur(i,visited,-1)):
                    return True
                else:
                    return False
        return 
        



























            