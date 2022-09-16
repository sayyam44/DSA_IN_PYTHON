#https://www.youtube.com/watch?v=Yh6EFazXipA&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=14
#there can be many combinations of topological sort

#we are traversing DFS in such a way that when we move from one edge to the other edge the ending adjacentvertex
#of that edge should be the 1st one to go into the stack after that the 1st vertex will go into the stack
#eg if we traverse through 1->2 , then 2 will go into stack before 1.
#whenever the dfs call for some vertex is over we add that to the stack

#tc=n+e
#sc=n for the visited array
#asc=n for recursion call of dfs

#step1- for loop for i 
#step2- dfs for i 
#step3-if i doesnt have any adjacent node or all the adjacent nodes of i are visited then only make visited of i =TRUE and then only add it to stack
#step4- check if any adjacent of i is left unvisited, then firstly do dfs(repeat process) of that adjacent element n
#step5- if no adjacent values of n or all adjacent elements of n are visited then add n to stack


from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    
    def dfs_recur(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False: #means he have some unexplored adjacent nodes
                self.dfs_recur(i,visited,stack)
        stack.append(v) #append the last element of all the adjacent values of some element before and after that we need to add the actual element
        return stack    
    def dfs(self):
        visited=[False]*(max(self.graph)+1)
        stack=[]
        for i in range(max(self.graph)+1):
            if visited[i]==False:
                self.dfs_recur(i,visited,stack)

