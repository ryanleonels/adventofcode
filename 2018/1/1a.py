#!/usr/bin/python3

freq = 0
freqs = set()
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
freqs.add(0)
done = False
while not done:
	for fileLine in fileLines:
		if fileLine.strip() == '':
			continue
		f = int(fileLine)
		freq += f
		if freq in freqs:
			done = True
			print(freq)
			break
		freqs.add(freq)
