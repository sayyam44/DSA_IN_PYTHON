# https://www.youtube.com/watch?v=uzVUw90ZFIg&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=13

#we will make two visited arrays , first array will be normally become true when the element's dfs is called 
#and in 2nd array it will become true same way but again will become false when it moves recursively backwards
#for an element both the arrays have true value this means there is a cycle in graph.

from collections import defaultdict

class Graph():
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def isCyclicUtil(self, v, visited, recStack): #here we are not taking parent as it is a directed graph

		# Mark current node as visited and
		# adds to recursion stack
		visited[v] = True
		recStack[v] = True

		# Recur for all neighbours
		# if any neighbour is visited and in
		# recStack then graph is cyclic
		for i in self.graph[v]:
			if visited[i] == False:
				if self.isCyclicUtil(i, visited, recStack): #this is recursively checking if any neighbor is already been visited
					return True
			elif visited[i] == True and recStack[i] == True:
				return True

		# The node needs to be popped from
		# recursion stack before function ends
		recStack[v] = False #whenever dfs for an element is completed make the 2nd array value as False again 
		return False

	# Returns true if graph is cyclic else false
	def isCyclic(self):
		visited = [False] * (max(self.graph) + 1)
		recStack = [False] * (max(self.graph) + 1)
		for node in range(max(self.graph)+1):
			if visited[node] == False:
				if self.isCyclicUtil(node,visited,recStack):
					return True
		return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
	print "Graph has a cycle"
else:
	print "Graph has no cycle"

# Thanks to Divyanshu Mehta for contributing this code
