#!/usr/bin/python3

from itertools import permutations

ingredients = {}
ingredients1 = []
fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	name = fileLine.split(': ')[0]
	ingredients[name] = {}
	ingredients1.append(name)
	properties = fileLine.split(': ')[1].split(', ')
	for property1 in properties:
		propertyName = property1.split(' ')[0]
		propertyValue = int(property1.split(' ')[1])
		ingredients[name][propertyName] = propertyValue
n = len(ingredients)

def calcMaxScore(qtys):
	if len(qtys) == n:
		capacity = 0
		durability = 0
		flavor = 0
		texture = 0
		calories = 0
		for i in range(0, n):
			ingredient = ingredients1[i]
			capacity += (qtys[i] * ingredients[ingredient]['capacity'])
			durability += (qtys[i] * ingredients[ingredient]['durability'])
			flavor += (qtys[i] * ingredients[ingredient]['flavor'])
			texture += (qtys[i] * ingredients[ingredient]['texture'])
			calories += (qtys[i] * ingredients[ingredient]['calories'])
		score = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
		if calories != 500:
			score = 0
		return score
	if len(qtys) == n - 1:
		qtys1 = qtys.copy()
		n1 = 0
		for i in range(0, n - 1):
			n1 += qtys[i]
		n1 = 100 - n1
		qtys1.append(n1)
		return calcMaxScore(qtys1)
	n0 = len(qtys)
	qtys1 = qtys.copy()
	qtys1.append(0)
	n1 = 0
	for i in range(0, n0):
		n1 += qtys[i]
	n1 = 100 - n1
	scoreMax = 0
	for i in range(0, n1):
		qtys1[n0] = i
		score = calcMaxScore(qtys1)
		scoreMax = max(scoreMax, score)
	return scoreMax

maxScore = calcMaxScore([])
print(maxScore)