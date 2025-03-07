#!/usr/bin/python3

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
programs = {}
below = {}
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	name = fileLine.split(' (')[0]
	weight = int(fileLine.split('(')[1].split(')')[0])
	above = []
	if ' -> ' in fileLine:
		above = fileLine.split(' -> ')[1].split(', ')
		for program1 in above:
			below[program1] = name
	programs[name] = (weight, above)
for program in programs:
	if program not in below:
		print(program)