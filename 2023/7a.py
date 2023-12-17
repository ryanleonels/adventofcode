#!/usr/bin/python3

def getStrength(hand):
	cards = []
	jokers = 0
	for i in range(0,5):
		cardsIn = False
		for j in range(0,len(cards)):
			if hand[i] == cards[j][0]:
				cards[j] = (cards[j][0], cards[j][1] + 1)
				cardsIn = True
		if cardsIn == False:
			if hand[i] == 'J':
				jokers += 1
			else:
				cards.append((hand[i],1))
	nn = {}
	for i in range(1,6):
		nn[i] = 0
	for i in range(0, len(cards)):
		nn[cards[i][1]] += 1
	maxnn = 0
	for i in range(1, 6):
		if nn[i] > 0:
			maxnn = i
	if jokers > 0:
		if maxnn > 0:
			nn[maxnn] -= 1
		nn[maxnn+jokers] += 1
	strength = 0
	#detect hands
	if nn[5] == 1:
		strength = 6000000
	if nn[4] == 1:
		strength = 5000000
	if nn[3] == 1 and nn[2] == 1:
		strength = 4000000
	if nn[3] == 1 and nn[2] == 0:
		strength = 3000000
	if nn[2] == 2:
		strength = 2000000
	if nn[2] == 1 and nn[1] == 3:
		strength = 1000000
	#sort current hand by strength
	values = {'A':12, 'K':11, 'Q':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, 'J':0}
	strength += ((values[hand[0]] * (13**4)) + (values[hand[1]] * (13**3)) + (values[hand[2]] * (13**2)) + (values[hand[3]] * (13**1)) + (values[hand[4]] * (13**0)))
	return strength

totalWinnings = 0
hands = []
bids = []
strengths = []
fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	hands.append(fileLine.split(' ')[0])
	bids.append(int(fileLine.split(' ')[1]))
	strengths.append(getStrength(hands[n]))
	n += 1
for i in range(0, n):
	rank = 0
	for j in range(0, n):
		if strengths[i] >= strengths[j]:
			rank += 1
	winnings = rank * bids[i]
	totalWinnings += winnings
print(totalWinnings)
