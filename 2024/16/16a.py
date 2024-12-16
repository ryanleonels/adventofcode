#!/usr/bin/python3

from heapq import heapify, heappop, heappush

maze = []
adj = {}
start = (-1, -1, '>')
end = (-1, -1, '>')
minScore = 999999999
fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		roomDone = True
		continue
	maze.append(fileLine)
row = len(maze)
col = len(maze[0])
for i in range(0, row):
	for j in range(0, col):
		if maze[i][j] != '#':
			adj[(i, j, '>')] = {}
			adj[(i, j, 'v')] = {}
			adj[(i, j, '<')] = {}
			adj[(i, j, '^')] = {}
			if maze[i][j] == 'S':
				start = (i, j, '>')
			if maze[i][j] != 'E':
				adj[(i, j, '>')][(i, j, 'v')] = 1000
				adj[(i, j, '>')][(i, j, '^')] = 1000
				adj[(i, j, 'v')][(i, j, '<')] = 1000
				adj[(i, j, 'v')][(i, j, '>')] = 1000
				adj[(i, j, '<')][(i, j, '^')] = 1000
				adj[(i, j, '<')][(i, j, 'v')] = 1000
				adj[(i, j, '^')][(i, j, '>')] = 1000
				adj[(i, j, '^')][(i, j, '<')] = 1000
				if i > 0 and maze[i-1][j] != '#':
					adj[(i, j, '^')][(i-1, j, '^')] = 1
				if i < row - 1 and maze[i+1][j] != '#':
					adj[(i, j, 'v')][(i+1, j, 'v')] = 1
				if j > 0 and maze[i][j-1] != '#':
					adj[(i, j, '<')][(i, j-1, '<')] = 1
				if j < col-1 and maze[i][j+1] != '#':
					adj[(i, j, '>')][(i, j+1, '>')] = 1

class Graph:
	def __init__(self, graph: dict = {}):
		self.graph = graph  # A dictionary for the adjacency list

	def add_edge(self, node1, node2, weight):
		if node1 not in self.graph:  # Check if the node is already added
			self.graph[node1] = {}  # If not, create the node
		self.graph[node1][node2] = weight  # Else, add a connection to its neighbor

	def shortest_distances(self, source: str, firstRun = False):
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
					if maze[neighbor[0]][neighbor[1]] == 'E' and firstRun == True:
						if tentative_distance < minScore:
							minScore = tentative_distance
							end = neighbor

		return distances

adjGraph = Graph(adj)
distances = adjGraph.shortest_distances(start, True)
nodeCount = len(distances)
tiles = set()
i = 0
for node in distances:
	print(str(i)+"/"+str(nodeCount)+" nodes processed")
	i += 1
	distances1 = adjGraph.shortest_distances(node)
	if distances[node] + distances1[end] == distances[end]:
		tile = (node[0], node[1])
		tiles.add(tile)
print(len(tiles))
