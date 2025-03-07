#!/usr/bin/python3

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

programs = {}
below = {}
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	name = fileLine.split(' (')[0]
	weight = int(fileLine.split('(')[1].split(')')[0])
	above = []
	if ' -> ' in fileLine:
		above = fileLine.split(' -> ')[1].split(', ')
		for program1 in above:
			below[program1] = name
	programs[name] = (weight, above)

root = ""
for program in programs:
	if program not in below:
		root = program

totalWeights = {}

def calcTotalWeight(node):
	totalWeight = programs[node][0]
	for node1 in programs[node][1]:
		totalWeight += calcTotalWeight(node1)
	totalWeights[node] = totalWeight
	return totalWeight

calcTotalWeight(root)

"""nodes = [root]
while len(nodes) > 0:
	nodes1 = []
	for node in nodes:
		print(node, totalWeights[node], programs[node])
		for node1 in programs[node][1]:
			nodes1.append(node1)
	print('')
	nodes = nodes1"""

balanced = False
node = root
balanceDiff = 0
while not balanced:
	totalWeights1 = []
	for node1 in programs[node][1]:
		totalWeights1.append(totalWeights[node1])
	weightCounts = {}
	n = len(totalWeights1)
	for i in range(0, n):
		if totalWeights1[i] in weightCounts:
			weightCounts[totalWeights1[i]] += 1
		else:
			weightCounts[totalWeights1[i]] = 1
	#print(node, totalWeights[node], programs[node], totalWeights1)
	if len(weightCounts) == 1:
		balanced = True
		#print("subnodes balanced, current node weight should be:")
		print(programs[node][0] - balanceDiff)
	else:
		balanced = False
		for weight in weightCounts:
			if weightCounts[weight] > 1: #assuming only one weight will be different
				expected = weight
			else:
				balanceDiff = weight
		balanceDiff -= expected
		nextNode = node
		for node1 in programs[node][1]:
			if totalWeights[node1] == expected + balanceDiff:
				nextNode = node1
		#print(expected, balanceDiff, nextNode)
		node = nextNode