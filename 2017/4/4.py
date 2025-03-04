#!/usr/bin/python3

fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nValid = 0
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	words = fileLine.strip().split(' ')
	nWords = len(words)
	wordsSoFar = set()
	valid = True
	for i in range(0, nWords):
		if words[i] in wordsSoFar:
			valid = False
			break
		wordsSoFar.add(words[i])
	if valid == True:
		nValid += 1
print(nValid)