# https://www.youtube.com/watch?v=SZ3zpzQk2jg

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result=[]
        path=[]
        n=len(graph)
        
        def dfs(curr):
            path.append(curr)
            if curr==n-1: #if the current element is the last element
                result.append(path[:])
                path.pop() # we will empty the path list as we need to store another path if possible
                return #recursively call the prev element
            else:
                for i in graph[curr]:
                    dfs(i)
                #done searching the current node 
                path.pop()
            
        dfs(0) #as we need to start from 0
        return result
