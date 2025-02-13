#!/usr/bin/python3

from heapq import heapify, heappop, heappush

fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
seed = int(fileData.strip())
#print(seed)

start = (1, 1)
goal = (31, 39)
(xsize, ysize) = (100, 100)

"""seed = 10
start = (1, 1)
goal = (7, 4)
(xsize, ysize) = (10, 7)"""

grid = []
for y in range(0, ysize):
	grid.append([])
	for x in range(0, xsize):
		seedsum = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + seed
		bitcount = 0
		while seedsum > 0:
			curbit = seedsum % 2
			if curbit == 1:
				bitcount += 1
			seedsum //= 2
		grid[y].append('.#'[bitcount % 2])
	#print(''.join(grid[y]))

adj = {}
for i in range(0, ysize):
	for j in range(0, xsize):
		if grid[i][j] != '#':
			adj[(j, i)] = {}
			if j > 0 and grid[i][j-1] != '#':
				adj[(j, i)][(j-1, i)] = 1
			if j < xsize - 1 and grid[i][j+1] != '#':
				adj[(j, i)][(j+1, i)] = 1
			if i > 0 and grid[i-1][j] != '#':
				adj[(j, i)][(j, i-1)] = 1
			if i < ysize - 1 and grid[i+1][j] != '#':
				adj[(j, i)][(j, i+1)] = 1

class Graph:
	def __init__(self, graph: dict = {}):
		self.graph = graph  # A dictionary for the adjacency list

	def add_edge(self, node1, node2, weight):
		if node1 not in self.graph:  # Check if the node is already added
			self.graph[node1] = {}  # If not, create the node
		self.graph[node1][node2] = weight  # Else, add a connection to its neighbor

	def shortest_distances(self, source: str):
		global end, minScore

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

adjGraph = Graph(adj)
distances = adjGraph.shortest_distances(start)
print(distances[goal])
