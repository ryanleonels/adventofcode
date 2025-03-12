#!/usr/bin/python3

from heapq import heapify, heappop, heappush

fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

adjs = {}
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	a = int(fileLine.split(' <-> ')[0])
	b = [int(x) for x in fileLine.split(' <-> ')[1].split(', ')]
	adjs[a] = b

adj = {}
for a in adjs:
	adj[a] = {}
	for b in adjs[a]:
		if a != b:
			adj[a][b] = 1

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
n = len(adjs)
groups = []
for i in range(0, n):
	groups.append(0)
prog = 0
group = 0
while prog < n:
	if groups[prog] == 0:
		group += 1
		distances = adjGraph.shortest_distances(prog)
		#group1 = []
		for a in distances:
			if distances[a] <= n:
				groups[a] = group
				#group1.append(a)
		#print(group,group1)
	prog += 1
print(group)