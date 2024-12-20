#!/usr/bin/python3

from heapq import heapify, heappop, heappush

row = 0
col = 0
maze = []
adj = {}
start = (0, 0)
end = (0, 0)

fileHandle = open("20.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	maze.append(list(fileLine))
row = len(maze)
col = len(maze[0])

for i in range(0, row):
	for j in range(0, col):
		if maze[i][j] != '#':
			if maze[i][j] == 'S':
				start = (i, j)
			if maze[i][j] == 'E':
				end = (i, j)
			adj[(i, j)] = {}
			if i > 0 and maze[i-1][j] != '#':
				adj[(i, j)][(i-1, j)] = 1
			if i < row - 1 and maze[i+1][j] != '#':
				adj[(i, j)][(i+1, j)] = 1
			if j > 0 and maze[i][j-1] != '#':
				adj[(i, j)][(i, j-1)] = 1
			if j < col - 1 and maze[i][j+1] != '#':
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

adjGraph = Graph(adj)
distances = adjGraph.shortest_distances(start)
minDist = distances[end]
print(minDist)

allDist = {}
cheats = {}

for i in range(0, row):
	print("Computing horizontal cheats for row "+str(i)+"...")
	for j in range(1, col - 1):
		if maze[i][j] == '#' and maze[i][j-1] != '#' and maze[i][j+1] != '#':
			cheat1 = (i, j - 1)
			cheat2 = (i, j + 1)
			if cheat1 not in allDist:
				allDist[cheat1] = adjGraph.shortest_distances(cheat1)
			if cheat2 not in allDist:
				allDist[cheat2] = adjGraph.shortest_distances(cheat2)
			dist1 = distances[cheat1] + 2 + allDist[cheat2][end]
			saved1 = minDist - dist1
			if saved1 > 0:
				if saved1 in cheats:
					cheats[saved1] += 1
				else:
					cheats[saved1] = 1
			dist2 = distances[cheat2] + 2 + allDist[cheat1][end]
			saved2 = minDist - dist2
			if saved2 > 0:
				if saved2 in cheats:
					cheats[saved2] += 1
				else:
					cheats[saved2] = 1

for i in range(1, row - 1):
	print("Computing vertical cheats for row "+str(i)+"...")
	for j in range(0, col):
		if maze[i][j] == '#' and maze[i-1][j] != '#' and maze[i+1][j] != '#':
			cheat1 = (i - 1, j)
			cheat2 = (i + 1, j)
			if cheat1 not in allDist:
				allDist[cheat1] = adjGraph.shortest_distances(cheat1)
			if cheat2 not in allDist:
				allDist[cheat2] = adjGraph.shortest_distances(cheat2)
			dist1 = distances[cheat1] + 2 + allDist[cheat2][end]
			saved1 = minDist - dist1
			if saved1 > 0:
				if saved1 in cheats:
					cheats[saved1] += 1
				else:
					cheats[saved1] = 1
			dist2 = distances[cheat2] + 2 + allDist[cheat1][end]
			saved2 = minDist - dist2
			if saved2 > 0:
				if saved2 in cheats:
					cheats[saved2] += 1
				else:
					cheats[saved2] = 1

total = 0
for cheat in sorted(cheats):
	print("There are " + str(cheats[cheat]) + " cheat(s) that save " + str(cheat) + " picosecond(s).")
	if cheat >= 100:
		total += cheats[cheat]
print(total)