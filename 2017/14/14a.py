#!/usr/bin/python3

from heapq import heapify, heappop, heappush

fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
key = fileData.strip()

def knotHash(data):
	lengths = [ord(x) for x in data.strip()] + [17, 31, 73, 47, 23]
	n = len(lengths)

	size = 256
	list1 = list(range(0, size))
	(pos, skip) = (0, 0)

	for rnd in range(0, 64):
		for i in range(0, n):
			length = lengths[i]
			(start, end) = (pos, pos + length)
			if end > size:
				(len1, len2) = (size - start, end - size)
				list2 = (list1[start:size] + list1[0:len2])[::-1]
				(list1[start:size], list1[0:len2]) = (list2[0:len1], list2[len1:length])
			else:
				list1[start:end] = list1[start:end][::-1]
			pos = (pos + length + skip) % size
			skip += 1

	hash1 = []
	for i in range(0, 16):
		num = list1[16 * i]
		for j in range(1, 16):
			num ^= list1[(16 * i) + j]
		hash1.append(num)

	result = ""
	for i in range(0, 16):
		result += ("0123456789abcdef"[hash1[i] // 16] + "0123456789abcdef"[hash1[i] % 16])
	return result

grid = []
for i in range(0, 128):
	grid.append([])
	hashInput = key + "-" + str(i)
	hashOutput = knotHash(hashInput)
	#print(hashOutput)
	for j in range(0, 32):
		digit = "0123456789abcdef".index(hashOutput[j])
		grid[i].append(digit // 8)
		grid[i].append((digit // 4) % 2)
		grid[i].append((digit // 2) % 2)
		grid[i].append(digit % 2)
	#print(''.join([str(x) for x in grid[i]]))

adj = {}
region = []
for i in range(0, 128):
	region.append([])
	for j in range(0, 128):
		if grid[i][j] == 1:
			adj[(i, j)] = {}
			if i > 0 and grid[i - 1][j] == 1:
				adj[(i, j)][(i - 1, j)] = 1
			if i < 127 and grid[i + 1][j] == 1:
				adj[(i, j)][(i + 1, j)] = 1
			if j > 0 and grid[i][j - 1] == 1:
				adj[(i, j)][(i, j - 1)] = 1
			if j < 127 and grid[i][j + 1] == 1:
				adj[(i, j)][(i, j + 1)] = 1
			region[i].append(0)
		else:
			region[i].append(-1)

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
regions = 0
for i in range(0, 128):
	for j in range(0, 128):
		if region[i][j] == 0:
			regions += 1
			#print(regions, (i, j))
			distances = adjGraph.shortest_distances((i, j))
			for (i1, j1) in distances:
				if distances[(i1, j1)] <= 9999:
					region[i1][j1] = regions
#for i in range(0, 128):
	#print(region[i])
print(regions)