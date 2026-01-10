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

paths[False] = {}
paths[False][False] = {}
paths[False][True] = {}

paths[True] = {}
paths[True][False] = {}
paths[True][True] = {}

def getPaths(device, hasDac = False, hasFft = False):
	if device == "out":
		if hasDac and hasFft:
			return 1
		else:
			return 0
	if device in paths[hasDac][hasFft]:
		return paths[hasDac][hasFft][device]
	total = 0
	for output in outputs[device]:
		(hasDac1, hasFft1) = (hasDac, hasFft)
		if output == "dac":
			hasDac1 = True
		if output == "fft":
			hasFft1 = True
		total += getPaths(output, hasDac1, hasFft1)
	paths[hasDac][hasFft][device] = total
	return total

print(getPaths("svr"))
