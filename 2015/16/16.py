#!/usr/bin/python3

gift = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	sue = int(fileLine.split(': ')[0][4:])
	items = {}
	itemsList = ': '.join(fileLine.split(': ')[1:]).split(', ')
	for item in itemsList:
		itemName = item.split(': ')[0]
		itemValue = int(item.split(': ')[1])
		items[itemName] = itemValue
	match = True
	for item in gift:
		if item in items and items[item] != gift[item]:
			match = False
			break
	if match == True:
		print(sue)
