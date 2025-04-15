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

fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

units = {} # (row, col) -> (type, HP, processed_in_turn)
grid = []

row = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))
	for col in range(0, len(fileLine)):
		if fileLine[col] == 'E' or fileLine[col] == 'G':
			units[(row, col)] = (fileLine[col], 200, True)
	row += 1
col = len(grid[0])

"""for i in range(0, row):
	print(''.join(grid[i]))
for unit in units:
	print(unit, units[unit])"""

# each turn: do each unit according to reading order at start of turn, both movement part + attack part before moving on to next unit
combatEnd = False
rounds = 0
opponents = {'E': 'G', 'G': 'E'}
while not combatEnd:
	#enumerate targets
	(e, g) = (0, 0)
	units1 = []
	for i in range(0, row):
		for j in range(0, col):
			if (i, j) in units:
				units1.append((i, j))
				if units[(i, j)][0] == 'E':
					e += 1
				if units[(i, j)][0] == 'G':
					g += 1
				units[(i, j)] = (units[(i, j)][0], units[(i, j)][1], False)
	#if there are no targets in one side, end
	if e == 0 or g == 0:
		combatEnd = True
	else:
		for (i, j) in units1:
			if (i, j) in units and units[(i, j)][1] > 0 and units[(i, j)][2] == False:
				type = units[(i, j)][0]
				type1 = opponents[type]
				(i0, j0) = (i, j)
				# determine if there are no more targets = end
				targetExist = False
				for i1 in range(0, row):
					if type1 in grid[i1]:
						targetExist = True
				if not targetExist:
					combatEnd = True
					break
				# move if no adjacent targets
				if grid[i - 1][j] != type1 and grid[i][j - 1] != type1 and grid[i][j + 1] != type1 and grid[i + 1][j] != type1:
					#determine targets
					moveTargets = []
					for i1 in range(1, row - 1):
						for j1 in range(1, col - 1):
							if grid[i1][j1] == '.' and (grid[i1 - 1][j1] == type1 or grid[i1][j1 - 1] == type1 or grid[i1][j1 + 1] == type1 or grid[i1 + 1][j1] == type1):
								moveTargets.append((i1, j1))
					# calculate shortest paths
					adj = {}
					for i1 in range(0, row):
						for j1 in range(0, col):
							if grid[i1][j1] != '#':
								adj[(i1, j1)] = {}
								if i1 > 0 and grid[i1 - 1][j1] == '.':
									adj[(i1, j1)][(i1 - 1, j1)] = 1
								if i1 < row - 1 and grid[i1 + 1][j1] == '.':
									adj[(i1, j1)][(i1 + 1, j1)] = 1
								if j1 > 0 and grid[i1][j1 - 1] == '.':
									adj[(i1, j1)][(i1, j1 - 1)] = 1
								if j1 < col - 1 and grid[i1][j1 + 1] == '.':
									adj[(i1, j1)][(i1, j1 + 1)] = 1
					adjGraph = Graph(adj)
					distances = adjGraph.shortest_distances((i, j))
					# determine move target
					moveTarget = (i, j)
					minDist = 999
					for (i1, j1) in moveTargets:
						if distances[(i1, j1)] < minDist:
							moveTarget = (i1, j1)
							minDist = distances[moveTarget]
					# determine which way to move
					if minDist < 999:
						moveTo = (i, j)
						minDist1 = minDist
						if grid[i - 1][j] == '.':
							distances = adjGraph.shortest_distances((i - 1, j))
							if distances[moveTarget] < minDist1:
								moveTo = (i - 1, j)
								minDist1 = distances[moveTarget]
						if grid[i][j - 1] == '.':
							distances = adjGraph.shortest_distances((i, j - 1))
							if distances[moveTarget] < minDist1:
								moveTo = (i, j - 1)
								minDist1 = distances[moveTarget]
						if grid[i][j + 1] == '.':
							distances = adjGraph.shortest_distances((i, j + 1))
							if distances[moveTarget] < minDist1:
								moveTo = (i, j + 1)
								minDist1 = distances[moveTarget]
						if grid[i + 1][j] == '.':
							distances = adjGraph.shortest_distances((i + 1, j))
							if distances[moveTarget] < minDist1:
								moveTo = (i + 1, j)
								minDist1 = distances[moveTarget]
						# then do move
						if moveTo != (i, j):
							(i0, j0) = moveTo
							grid[i0][j0] = type
							grid[i][j] = '.'
							units[(i0, j0)] = units[(i, j)]
							del units[(i, j)]
				# attack
				(targetFound, minHP) = (False, 999)
				target = (i0, j0)
				if grid[i0 - 1][j0] == type1 and units[(i0 - 1, j0)][1] < minHP:
					targetFound = True
					target = (i0 - 1, j0)
					minHP = units[target][1]
				if grid[i0][j0 - 1] == type1 and units[(i0, j0 - 1)][1] < minHP:
					targetFound = True
					target = (i0, j0 - 1)
					minHP = units[target][1]
				if grid[i0][j0 + 1] == type1 and units[(i0, j0 + 1)][1] < minHP:
					targetFound = True
					target = (i0, j0 + 1)
					minHP = units[target][1]
				if grid[i0 + 1][j0] == type1 and units[(i0 + 1, j0)][1] < minHP:
					targetFound = True
					target = (i0 + 1, j0)
					minHP = units[target][1]
				if targetFound:
					units[target] = (units[target][0], units[target][1] - 3, units[target][2])
					if units[target][1] <= 0:
						del units[target]
						grid[target[0]][target[1]] = '.'
				units[(i0, j0)] = (units[(i0, j0)][0], units[(i0, j0)][1], True)
		if not combatEnd:
			rounds += 1
	"""if combatEnd:
		print("end")
	else:
		print(rounds)
	for i in range(0, row):
		print(''.join(grid[i]))
	for unit in units:
		print(unit, units[unit])"""
	if combatEnd:
		hp = 0
		for unit in units:
			if units[unit][1] > 0:
				hp += units[unit][1]
		print(rounds * hp)
