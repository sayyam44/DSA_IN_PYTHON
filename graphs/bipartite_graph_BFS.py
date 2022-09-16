#^^^^^^^^^^^^^^^COPY^^^^^^^^^^^^^^^
#A graph that can be colored using 2 different colors such that no 2 adjacent nodes have same color is called bipartite graph.
# https://www.youtube.com/watch?v=nbgaEu-pvkU
import collections

class Solution:
    def isBipartite(self, graph):
        seen = {}  # dictionay with key as node and value as it's colour
        
        for node in range(len(graph)):          # graph may have different disjoint components
            if node not in seen:
                q = collections.deque([(node, 1)])
                while q:
                    node, color = q.popleft()
                    
                    if node in seen:            # graph is cyclic
                        if seen[node] == color: # previour color is same as current color
                            continue            # cyclic graph with EVEN length
                        else:                   # previour color diffrent with current color
                            return False        # cyclic graph with ODD length
                    
                    seen[node] = color #putting the node along with its color in seen 
                    # store neighbors nodes with opposit color
                    for nei in graph[node]:
                        q.append((nei, color * (-1))) #we are making a queue witl alternate values as 1,-1

        return True  
    

# Time = number of nodes + number of edges
# Time: O(n) + O(n)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)


