#!/usr/bin/python3

totalPoints = 0
fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for i in range(0,188):
	winningNums = set()
	numWins = 0
	points = 0
	for j in range(0,10):
		winningNums.add(int(fileLines[i][(3*j)+10:(3*j)+12]))
	for j in range(0,25):
		x = int(fileLines[i][(3*j)+42:(3*j)+44])
		if x in winningNums:
			numWins += 1
	print(numWins)
	if numWins > 0:
		points = 2 ** (numWins - 1)
	totalPoints += points
print(totalPoints)
