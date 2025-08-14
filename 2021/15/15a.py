#!/usr/bin/python3

from heapq import heapify, heappop, heappush

adj = {}
fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid1 = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid1.append([int(x) for x in list(fileLine)])
row1 = len(grid1)
col1 = len(grid1[0])
row = row1 * 5
col = col1 * 5
grid = []
for i in range(0, row):
	(i0, i1) = (i // row1, i % row1)
	grid.append([])
	for j in range(0, col):
		(j0, j1) = (j // col1, j % col1)
		cur = grid1[i1][j1] + i0 + j0
		if cur > 9:
			cur -= 9
		grid[i].append(cur)

start = (0, 0)
end = (row - 1, col - 1)
for i in range(0, row):
	for j in range(0, col):
		adj[(i, j)] = {}
		if i > 0:
			adj[(i, j)][(i - 1, j)] = grid[i - 1][j]
		if i < row - 1:
			adj[(i, j)][(i + 1, j)] = grid[i + 1][j]
		if j > 0:
			adj[(i, j)][(i, j - 1)] = grid[i][j - 1]
		if j < col - 1:
			adj[(i, j)][(i, j + 1)] = grid[i][j + 1]

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
print(distances[end])
