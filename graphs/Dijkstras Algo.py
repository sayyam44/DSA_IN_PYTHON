# https://www.youtube.com/watch?v=jbhuqIASjoM&t=497s
#DIKSTRA'S ALGORITHM- it helps us to find the shortest path between a source and every other node 
#^^^^^^^^^COPY^^^^^^^^^^^

#We will create adjacency list in pair format having (node,weight),we will create a visited array which initially
#have infinite value for each element , and create a priority queue/set in which it will store 
#values in pairs(dist from root node,node),we will iterate through each element and will find out 
#the total distance from root node(SOURCE) to all the adjacent nodes of current node , the value(basically its
# the distance from parent node to current node) for an element will be updated in visited array 
# only if the prev value was infinity or greater than the current value ,and similarly store elements in priority queue

#tc=(n+e)logn 
#sc=n+n=n


# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet): #this function is to reach to index that is currently at min dist

		# Initialize minimum distance for next node
		min = sys.maxsize

		# Search not nearest vertex not in the
		# shortest path tree
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False: #till this time dist[u]=0 is only for one case i.e. for index 1
				min = dist[u] #min =0 for 1st case in copy 
				min_index = u #min_index=1 for 1st case in copy

		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V 
		dist[src] = 0 #beacaue 1st dist will always be 0
		sptSet = [False] * self.V #we are creating set because there may occur some duplicate values 
                                  #that we dont want

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# x is always equal to src in first iteration
			x = self.minDistance(dist, sptSet) #it will return 1 in the example in copy

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[x] = True #make index 1 == True for 1st time.

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current(already existing)
			# distance(dist[y]) is greater than new distance(dist[x] + self.graph[x][y]) and
			# the vertex in not in the shortest path tree
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
						dist[y] = dist[x] + self.graph[x][y]
						#dist[y]=inf in 1st case
						#dist[x]=0 in 1st case that we just calculated above
						#self.graph[x][y]=prev val.
		self.printSolution(dist)

# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		];

g.dijkstra(0);


