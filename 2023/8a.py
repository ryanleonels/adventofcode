#!/usr/bin/python3
import math
steps = 0
nodes = {}
fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
instructions = fileLines[0]
n = len(instructions)
positions = []
nPos = 0
nSteps = []
for i in range(2, len(fileLines)):
	if len(fileLines[i]) == 0:
		continue
	nodePos = fileLines[i].split('=')[0].strip()
	nodeLeft = fileLines[i].split('(')[1].split(',')[0].strip()
	nodeRight = fileLines[i].split(',')[1].split(')')[0].strip()
	nodes[nodePos] = (nodeLeft, nodeRight)
	if nodePos[2] == 'A':
		positions.append(nodePos)
		nPos += 1
		nSteps.append(0)
nz = 0
while nz < nPos:
	instruction = instructions[steps % n]
	for i in range(0, nPos):
		if instruction == 'L':
			positions[i] = nodes[positions[i]][0]
		if instruction == 'R':
			positions[i] = nodes[positions[i]][1]
	steps += 1
	for i in range(0, nPos):
		if positions[i][2] == 'Z' and nSteps[i] == 0:
			nz += 1
			nSteps[i] = steps
steps = 1
for i in range(0, nPos):
	steps = math.lcm(steps, nSteps[i])
print(steps)
