#!/usr/bin/python3

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
monkeys = {}
curMonkey = -1
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine.strip().split(' ')[0] == "Monkey":
		curMonkey = int(fileLine.strip().split(' ')[1].split(':')[0])
		monkeys[curMonkey] = {}
	if fileLine.strip().split(': ')[0] == "Starting items":
		startingItems = [int(x) for x in fileLine.strip().split(': ')[1].split(', ')]
		monkeys[curMonkey]['startingItems'] = startingItems
	if fileLine.strip().split(': ')[0] == "Operation":
		(op, qty) = fileLine.strip().split("new = old ")[1].split(' ')
		if qty == "old":
			if op == '*':
				(op, qty) = ('**', 2)
			if op == '+':
				(op, qty) = ('*', 2)
		qty = int(qty)
		monkeys[curMonkey]['operation'] = (op, qty)
	if fileLine.strip().split(': ')[0] == "Test":
		mod = int(fileLine.strip().split("divisible by ")[1])
		monkeys[curMonkey]['test'] = mod
	if fileLine.strip().split(': ')[0] == "If true":
		nxt = int(fileLine.strip().split("throw to monkey ")[1])
		monkeys[curMonkey]['ifTrue'] = nxt
	if fileLine.strip().split(': ')[0] == "If false":
		nxt = int(fileLine.strip().split("throw to monkey ")[1])
		monkeys[curMonkey]['ifFalse'] = nxt
monkeyItems = {}
nInspect = {}
#print("Round 0")
for monkey in monkeys:
	#print(monkey, monkeys[monkey])
	monkeyItems[monkey] = monkeys[monkey]['startingItems']
	nInspect[monkey] = 0
	#print("Monkey " + str(monkey) + ": " + str(monkeyItems[monkey]))
for t in range(1, 21):
	for monkey in monkeys:
		for item in monkeyItems[monkey]:
			item1 = item
			(op, qty) = monkeys[monkey]['operation']
			if op == '+':
				item1 += qty
			if op == '*':
				item1 *= qty
			if op == '**':
				item1 **= qty
			item1 //= 3
			mod = item1 % monkeys[monkey]['test']
			if mod == 0:
				monkeyItems[monkeys[monkey]['ifTrue']].append(item1)
			else:
				monkeyItems[monkeys[monkey]['ifFalse']].append(item1)
			nInspect[monkey] += 1
		monkeyItems[monkey] = []
	#print("Round " + str(t))
	#for monkey in monkeys:
		#print("Monkey " + str(monkey) + ": " + str(monkeyItems[monkey]))
nInspect1 = []
for monkey in monkeys:
	nInspect1.append(nInspect[monkey])
nInspect1 = sorted(nInspect1)
print(nInspect1[-1] * nInspect1[-2])
