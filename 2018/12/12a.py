#!/usr/bin/python3

fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

(initialState, rules) = ("", {})
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine[:7] == "initial":
		initialState = fileLine[15:]
	else:
		(curState, nextState) = fileLine.split(" => ")
		rules[curState] = nextState

n = len(initialState)
gens = 1000 #by 1000th generation all plant-containing pots has been degenerated to pairs of '##' moving right one pot per second (or '#.#' in the example / any other patterns that will move right one pot per second)
pots = {}
for i in range(0, n):
	pots[i] = initialState[i]
for i in range(1, ((gens + 1) * 2) + 1):
	pots[-i] = '.'
	pots[n + i - 1] = '.' 

pots1 = {}
sum1 = 0
for i in range(1, gens + 1):
	for j in range(-(gens + 1) * 2, n + ((gens + 1) * 2)):
		pots1[j] = '.'
	for j in range(-(i * 2), n + (i * 2)):
		curState = pots[j-2] + pots[j-1] + pots[j] + pots[j+1] + pots[j+2]
		nextState = '.'
		if curState in rules:
			nextState = rules[curState]
		pots1[j] = nextState
	sum1 = 0
	#res = ''
	for j in range(-(gens + 1) * 2, n + ((gens + 1) * 2)):
		pots[j] = pots1[j]
		if pots[j] == '#':
			sum1 += j
			if i == gens:
				sum1 += (50000000000 - gens)
	#print(res)
print(sum1)