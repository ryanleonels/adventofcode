#!/usr/bin/python3

from itertools import permutations

maxHappiness = -999999999
changes = {}
people = []
fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	words = fileLine.split(' ')
	person1 = words[0]
	person2 = words[-1][:-1]
	change = int(words[3])
	if words[2] == 'lose':
		change = -change
	if person1 not in people:
		people.append(person1)
		changes[person1] = {}
		changes[person1][person1] = 0
	if person2 not in people:
		people.append(person2)
		changes[person2] = {}
		changes[person2][person2] = 0
	changes[person1][person2] = change
people.append("You")
changes["You"] = {}
for person in people:
	changes[person]["You"] = 0
	changes["You"][person] = 0
n = len(people)
orders = list(permutations(people))
for order in orders:
	curHappiness = 0
	for i in range(0, n):
		p1 = order[i]
		p2 = order[(i+1)%n]
		curHappiness += changes[p1][p2]
		curHappiness += changes[p2][p1]
	if curHappiness > maxHappiness:
		maxHappiness = curHappiness
print(maxHappiness)