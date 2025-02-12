#!/usr/local/bin/python3

nElements = 0
elements = []
generators = []
microchips = []

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

floor = 0
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	floor += 1
	components = fileLine.split(' a ')[1:]
	for component in components:
		element = component.split(' ')[0].split('-')[0]
		componentType = component.split(' ')[1][:9]
		if element in elements:
			curElement = elements.index(element)
		else:
			elements.append(element)
			nElements += 1
			curElement = nElements - 1
			generators.append(0)
			microchips.append(0)
		if componentType == "generator":
			generators[curElement] = floor
		if componentType == "microchip":
			microchips[curElement] = floor

nElements += 2
generators.append(1)
microchips.append(1)
generators.append(1)
microchips.append(1)

"""print(floor)
print(elements)
print(generators)
print(microchips)"""

"""5 elements, 5 generators each can be in 4 floors: 4^10 states * elevator in floors 1-4
1, generators, microchips is start state
4, [4,4,4,4,4], [4,4,4,4,4] is end state"""

def hashState(elevator, generators, microchips):
	result = elevator - 1
	for i in range(0, nElements):
		result *= floor
		result += (generators[i] - 1)
	for i in range(0, nElements):
		result *= floor
		result += (microchips[i] - 1)
	return result

def unhashState(state):
	state1 = state
	microchips = []
	for i in range(0, nElements):
		microchips.append((state1 % floor) + 1)
		state1 //= floor
	microchips.reverse()
	generators = []
	for i in range(0, nElements):
		generators.append((state1 % floor) + 1)
		state1 //= floor
	generators.reverse()
	elevator = state1 + 1
	return (elevator, generators, microchips)

startState = hashState(1, generators, microchips)
goalState = hashState(4, [4] * len(generators), [4] * len(microchips))
print(startState)
print(goalState)
print(unhashState(startState))
print(unhashState(goalState))

def stateValid(generators, microchips):
	#each element microchip must not be in the same floor as generator of any other element, unless its own generator is also on the same floor
	for i in range(0, nElements):
		if generators[i] != microchips[i]:
			for j in range(0, nElements):
				if i != j and generators[j] == microchips[i]:
					return False
	return True

states = {}
states[startState] = 0
step = 0
curStep = [startState]
nextStep = []
while goalState not in states:
	step += 1
	# try all new valid states from each state in curStep and put them in nextStep
	for state in curStep:
		(elevator, generators, microchips) = unhashState(state)
		#print((elevator, generators, microchips))
		curFloor = []
		for i in range(0, nElements):
			if generators[i] == elevator:
				curFloor.append(i)
			if microchips[i] == elevator:
				curFloor.append(nElements + i)
		#print(curFloor)
		nItems = len(curFloor)
		# one can move up or down (if not on top/bottom floor) with 1 or 2 items from curFloor
		if elevator < floor:
			#move up
			elevator1 = elevator + 1
			for i in range(0, nItems): # try with 1 item
				item1 = curFloor[i]
				generators1 = generators.copy()
				microchips1 = microchips.copy()
				if item1 >= nElements:
					microchips1[item1 - nElements] = elevator1
				else:
					generators1[item1] = elevator1
				#check if valid and state not already visited
				if stateValid(generators1, microchips1):
					nextState = hashState(elevator1, generators1, microchips1)
					if nextState not in states:
						states[nextState] = step
						nextStep.append(nextState)
			for i in range(0, nItems - 1): # try with 2 items
				item1 = curFloor[i]
				for j in range(i + 1, nItems):
					item2 = curFloor[j]
					generators1 = generators.copy()
					microchips1 = microchips.copy()
					if item1 >= nElements:
						microchips1[item1 - nElements] = elevator1
					else:
						generators1[item1] = elevator1
					if item2 >= nElements:
						microchips1[item2 - nElements] = elevator1
					else:
						generators1[item2] = elevator1
					#check if valid and state not already visited
					if stateValid(generators1, microchips1):
						nextState = hashState(elevator1, generators1, microchips1)
						if nextState not in states:
							states[nextState] = step
							nextStep.append(nextState)
		if elevator > 1:
			#move down
			elevator1 = elevator - 1
			for i in range(0, nItems): # try with 1 item
				item1 = curFloor[i]
				generators1 = generators.copy()
				microchips1 = microchips.copy()
				if item1 >= nElements:
					microchips1[item1 - nElements] = elevator1
				else:
					generators1[item1] = elevator1
				#check if valid and state not already visited
				if stateValid(generators1, microchips1):
					nextState = hashState(elevator1, generators1, microchips1)
					if nextState not in states:
						states[nextState] = step
						nextStep.append(nextState)
			for i in range(0, nItems - 1): # try with 2 items
				item1 = curFloor[i]
				for j in range(i + 1, nItems):
					item2 = curFloor[j]
					generators1 = generators.copy()
					microchips1 = microchips.copy()
					if item1 >= nElements:
						microchips1[item1 - nElements] = elevator1
					else:
						generators1[item1] = elevator1
					if item2 >= nElements:
						microchips1[item2 - nElements] = elevator1
					else:
						generators1[item2] = elevator1
					#check if valid and state not already visited
					if stateValid(generators1, microchips1):
						nextState = hashState(elevator1, generators1, microchips1)
						if nextState not in states:
							states[nextState] = step
							nextStep.append(nextState)
	print(step, len(nextStep))
	if goalState in states:
		print(step)
	curStep = nextStep
	nextStep = []
