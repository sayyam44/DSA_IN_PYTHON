#^^^^^^^^^^^COPY^^^^^^^^^
# https://www.youtube.com/watch?v=oNI0rf2P9gE
# Number of vertices in the graph
#tc=n3
V = 4

INF = 99999
def floydWarshall(graph):
    #initializing dist as same as the given matrix
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

	for k in range(V):#k loop will be used to perform i,j iteration for allthe vertices that is from 1 to 4

		for i in range(V):
			for j in range(V): #i,j loop will be used for a single matrix

				dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j]
								)
	printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
	print ("Following matrix shows the shortest distances\
between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print ("%7s" % ("INF"),end=" ")
			else:
				print ("%7d\t" % (dist[i][j]),end=' ')
			if j == V-1:
				print ()


# Driver program to test the above program
# Let us create the following weighted graph
"""
			10
	(0)------->(3)
		|		 /|\
	5 |		 |
		|		 | 1
	\|/		 |
	(1)------->(2)
			3		 """
#inf means no edge between 2 nodes
#0 means no self loop is present
graph = [[0, 5, INF, 10],
		[INF, 0, 3, INF],
		[INF, INF, 0, 1],
		[INF, INF, INF, 0]
		]
# Print the solution
floydWarshall(graph)
# This code is contributed by Mythri J L
