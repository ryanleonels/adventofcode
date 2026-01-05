#!/usr/bin/python3

from heapq import heapify, heappop, heappush

result = 0
boxes = []
distances = {}
allDist = []
connections = {}
group = {}
groups = {}
sizes = []
adj = {}
fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y, z) = [int(w) for w in fileLine.strip().split(',')]
	boxes.append((x, y, z))
n = len(boxes)
for i in range(0, n):
	distances[i] = {}
	distances[i][i] = 0
	connections[i] = []
	for j in range(0, i):
		dist = ((boxes[i][0] - boxes[j][0]) ** 2) + ((boxes[i][1] - boxes[j][1]) ** 2) + ((boxes[i][2] - boxes[j][2]) ** 2)
		distances[i][j] = dist
		distances[j][i] = dist
		allDist.append((dist, i, j))
allDist.sort()
for i in range(0, n):
	adj[i] = {}
for i in range(0, 1000):
	adj[allDist[i][1]][allDist[i][2]] = allDist[i][0]
	adj[allDist[i][2]][allDist[i][1]] = allDist[i][0]

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

adjGraph = Graph(adj)
for i in range(0, n):
	if i not in group:
		group[i] = i
		groups[i] = []
		distances = adjGraph.shortest_distances(i)
		for j in distances:
			if distances[j] != float("inf"):
				group[j] = i
				groups[i].append(j)
		sizes.append(len(groups[i]))
sizes.sort()
result = sizes[-1] * sizes[-2] * sizes[-3]
print(result)
