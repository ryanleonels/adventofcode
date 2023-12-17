#!/usr/bin/python3

steps = 0
nodes = {}
fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
instructions = fileLines[0]
n = len(instructions)
for i in range(2, len(fileLines)):
	if len(fileLines[i]) == 0:
		continue
	nodePos = fileLines[i].split('=')[0].strip()
	nodeLeft = fileLines[i].split('(')[1].split(',')[0].strip()
	nodeRight = fileLines[i].split(',')[1].split(')')[0].strip()
	nodes[nodePos] = (nodeLeft, nodeRight)
curPos = 'AAA'
while curPos != 'ZZZ':
	instruction = instructions[steps % n]
	if instruction == 'L':
		curPos = nodes[curPos][0]
	if instruction == 'R':
		curPos = nodes[curPos][1]
	steps += 1
print(steps)
