#!/usr/bin/python3

totalCards = 0
fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
cards = []
wins = []
for i in range(0,188):
	cards.append(1)
	wins.append(0)
for i in range(0,188):
	winningNums = set()
	numWins = 0
	points = 0
	totalCards += cards[i]
	for j in range(0,10):
		winningNums.add(int(fileLines[i][(3*j)+10:(3*j)+12]))
	for j in range(0,25):
		x = int(fileLines[i][(3*j)+42:(3*j)+44])
		if x in winningNums:
			numWins += 1
	wins[i] = numWins
	for j in range(i+1, i+numWins+1):
		if j < 188:
			cards[j] += cards[i]
print(totalCards)
