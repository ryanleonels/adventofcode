#!/usr/bin/python3

from heapq import heapify, heappop, heappush

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

fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

(depth, targetX, targetY) = (0, 0, 0)

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine[:5] == "depth":
		depth = int(fileLine.split(': ')[1])
	if fileLine[:6] == "target":
		targetX = int(fileLine.split(': ')[1].split(',')[0])
		targetY = int(fileLine.split(': ')[1].split(',')[1])

#(depth, targetX, targetY) = (510, 10, 10)
(maxX, maxY) = (targetX * 2, targetY * 2)

geo1 = {}
geo1[(0, 0)] = 0
geo1[(targetX, targetY)] = 0

def ero(x):
	return (x + depth) % 20183

def geo(x, y):
	if (x, y) in geo1:
		return geo1[(x, y)]
	if y == 0:
		geoi = x * 16807
	if x == 0:
		geoi = y * 48271
	if x != 0 and y != 0:
		geoi = ero(geo(x - 1, y)) * ero(geo(x, y - 1))
	geo1[(x, y)] = geoi
	return geoi

regions = {}
for i in range(0, maxX + 1):
	for j in range(0, maxY + 1):
		regions[(i, j)] = (ero(geo(i, j)) % 3)

start = (0, 0, 'T')
finish = (targetX, targetY, 'T')
adj = {}
for i in range(0, maxX + 1):
	for j in range(0, maxY + 1):
		reg = regions[(i, j)]
		if reg != 0:
			adj[(i, j, 'N')] = {}
			if i > 0 and regions[(i - 1, j)] != 0:
				adj[(i, j, 'N')][(i - 1, j, 'N')] = 1
			if i < maxX and regions[(i + 1, j)] != 0:
				adj[(i, j, 'N')][(i + 1, j, 'N')] = 1
			if j > 0 and regions[(i, j - 1)] != 0:
				adj[(i, j, 'N')][(i, j - 1, 'N')] = 1
			if j < maxY and regions[(i, j + 1)] != 0:
				adj[(i, j, 'N')][(i, j + 1, 'N')] = 1
			if reg != 1:
				adj[(i, j, 'N')][(i, j, 'T')] = 7
			if reg != 2:
				adj[(i, j, 'N')][(i, j, 'C')] = 7
		if reg != 1:
			adj[(i, j, 'T')] = {}
			if i > 0 and regions[(i - 1, j)] != 1:
				adj[(i, j, 'T')][(i - 1, j, 'T')] = 1
			if i < maxX and regions[(i + 1, j)] != 1:
				adj[(i, j, 'T')][(i + 1, j, 'T')] = 1
			if j > 0 and regions[(i, j - 1)] != 1:
				adj[(i, j, 'T')][(i, j - 1, 'T')] = 1
			if j < maxY and regions[(i, j + 1)] != 1:
				adj[(i, j, 'T')][(i, j + 1, 'T')] = 1
			if reg != 0:
				adj[(i, j, 'T')][(i, j, 'N')] = 7
			if reg != 2:
				adj[(i, j, 'T')][(i, j, 'C')] = 7
		if reg != 2:
			adj[(i, j, 'C')] = {}
			if i > 0 and regions[(i - 1, j)] != 2:
				adj[(i, j, 'C')][(i - 1, j, 'C')] = 1
			if i < maxX and regions[(i + 1, j)] != 2:
				adj[(i, j, 'C')][(i + 1, j, 'C')] = 1
			if j > 0 and regions[(i, j - 1)] != 2:
				adj[(i, j, 'C')][(i, j - 1, 'C')] = 1
			if j < maxY and regions[(i, j + 1)] != 2:
				adj[(i, j, 'C')][(i, j + 1, 'C')] = 1
			if reg != 0:
				adj[(i, j, 'C')][(i, j, 'N')] = 7
			if reg != 1:
				adj[(i, j, 'C')][(i, j, 'T')] = 7

adjGraph = Graph(adj)
distances = adjGraph.shortest_distances(start)
print(distances[finish])