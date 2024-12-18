#!/usr/bin/python3

from heapq import heapify, heappop, heappush

size = 71
maze = []
bytePos = []
adj = {}
start = (0, 0)
end = (size - 1, size - 1)
for i in range(0, size):
	maze.append([])
	for j in range(0, size):
		maze[i].append('.')

fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	byte1 = (int(fileLine.split(',')[0]), int(fileLine.split(',')[1]))
	bytePos.append(byte1)
maxBytes = len(bytePos)

def prepareGraph(n):
	global adj
	for i in range(0, size):
		for j in range(0, size):
			maze[i][j] = '.'
	for i in range(0, n):
		maze[bytePos[i][0]][bytePos[i][1]] = '#'
	adj = {}
	for i in range(0, size):
		for j in range(0, size):
			if maze[i][j] != '#':
				adj[(i, j)] = {}
				if i > 0 and maze[i-1][j] != '#':
					adj[(i, j)][(i-1, j)] = 1
				if i < size - 1 and maze[i+1][j] != '#':
					adj[(i, j)][(i+1, j)] = 1
				if j > 0 and maze[i][j-1] != '#':
					adj[(i, j)][(i, j-1)] = 1
				if j < size - 1 and maze[i][j+1] != '#':
					adj[(i, j)][(i, j+1)] = 1

class Graph:
	def __init__(self, graph: dict = {}):
		self.graph = graph  # A dictionary for the adjacency list

	def add_edge(self, node1, node2, weight):
		if node1 not in self.graph:  # Check if the node is already added
			self.graph[node1] = {}  # If not, create the node
		self.graph[node1][node2] = weight  # Else, add a connection to its neighbor

	def shortest_distances(self, source: str):
		# Initialize the values of all nodes with infinity
		distances = {node: float("inf") for node in self.graph}
		distances[source] = 0  # Set the source value to 0

		# Initialize a priority queue
		pq = [(0, source)]
		heapify(pq)

		# Create a set to hold visited nodes
		visited = set()

		while pq:  # While the priority queue isn't empty
			current_distance, current_node = heappop(pq) # Get the node with the min distance

			if current_node in visited:
			   continue  # Skip already visited nodes
			visited.add(current_node)  # Else, add the node to visited set

			for neighbor, weight in self.graph[current_node].items():
				# Calculate the distance from current_node to the neighbor
				tentative_distance = current_distance + weight
				if tentative_distance < distances[neighbor]:
					distances[neighbor] = tentative_distance
					heappush(pq, (tentative_distance, neighbor))

		return distances

def getMinSteps(n):
	prepareGraph(n)
	adjGraph = Graph(adj)
	distances = adjGraph.shortest_distances(start)
	return distances[end]

nmin = 1
nmax = maxBytes
while nmax - nmin > 1:
	nmid = (nmin + nmax) // 2
	minSteps = getMinSteps(nmid)
	if minSteps > 999999999:
		nmax = nmid
	else:
		nmin = nmid

print(str(bytePos[nmax-1][0])+','+str(bytePos[nmax-1][1]))