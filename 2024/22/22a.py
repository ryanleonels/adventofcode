#!/usr/bin/python3

def mix(x, y):
	return x ^ y

def prune(x):
	return x % 16777216

def encrypt(x):
	x1 = prune(mix(x, x * 64))
	x2 = prune(mix(x1, x1 // 32))
	x3 = prune(mix(x2, x2 * 2048))
	return x3

def genSeq(x):
	prices = []
	changes = []
	prev = x
	for i in range(0, 2000):
		cur = encrypt(prev)
		mod = (cur % 10) - (prev % 10)
		prices.append(cur % 10)
		changes.append(mod)
		prev = cur
	return (prices, changes)

maxBananas = 0
allPrices = []
allChanges = []
#fileHandle = open("temp2.in", "r")
fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

n = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n += 1
	secret = int(fileLine)
	(prices, changes) = genSeq(secret)
	allPrices.append(prices)
	allChanges.append(changes)

bananas = {}
for i in range(0, n):
	bananas1 = {}
	for j in range(0, 1997):
		seq = (allChanges[i][j], allChanges[i][j+1], allChanges[i][j+2], allChanges[i][j+3])
		if seq not in bananas1:
			bananas1[seq] = allPrices[i][j+3]
	for seq in bananas1:
		if seq in bananas:
			bananas[seq] += bananas1[seq]
		else:
			bananas[seq] = bananas1[seq]

for seq in bananas:
	if bananas[seq] > maxBananas:
		maxBananas = bananas[seq]
		#print([seq, bananas[seq]])

print(maxBananas)
