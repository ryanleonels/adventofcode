#!/usr/bin/python3

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
outputs = {}
paths = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	device = fileLine.split(': ')[0]
	outputs[device] = fileLine.split(': ')[1].split(' ')

def getPaths(device):
	if device == "out":
		return 1
	if device in paths:
		return paths[device]
	total = 0
	for output in outputs[device]:
		total += getPaths(output)
	paths[device] = total
	return total

print(getPaths("you"))
