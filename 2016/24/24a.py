#!/usr/bin/python3

from heapq import heapify, heappop, heappush
from itertools import permutations

fileHandle = open("24.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)

(xsize, ysize) = (len(grid[0]), len(grid))

adj = {}
pois = {}
maxnum = 0
for i in range(0, ysize):
	for j in range(0, xsize):
		if grid[i][j] >= '0' and grid[i][j] <= '9':
			num = ord(grid[i][j]) - ord('0')
			pois[num] = (j, i)
			maxnum = max(num, maxnum)
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

#print(pois)
#print(maxnum)

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
dist = []
for i in range(0, maxnum + 1):
	dist.append([])
	distances = adjGraph.shortest_distances(pois[i])
	for j in range(0, maxnum + 1):
		dist[i].append(distances[pois[j]])
	#print(dist[i])

seq = []
for i in range(1, maxnum + 1):
	seq.append(i)
orders = list(permutations(seq))
minStep = 999999999
for order in orders:
	curStep = 0
	prev = 0
	for i in range(0, maxnum):
		cur = order[i]
		curStep += dist[prev][cur]
		prev = cur
	curStep += dist[cur][0]
	minStep = min(curStep, minStep)
print(minStep)