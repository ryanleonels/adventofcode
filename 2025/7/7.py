#!/usr/bin/python3

splits = 0
fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
row = len(fileLines) - 1
col = len(fileLines[0])
s = fileLines[0].find('S')
if s != -1:
	beams = set()
	beams.add(s)
	for i in range(1, row):
		beams1 = set()
		for beam in beams:
			if fileLines[i][beam] == '^':
				splits += 1
				beams1.add(beam - 1)
				beams1.add(beam + 1)
			else:
				beams1.add(beam)
		beams = beams1
print(splits)
