#!/usr/bin/python3

import collections

fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	name = ' '.join(fileLine.split('[')[0][:-4].split('-'))
	sectorId = int(fileLine.split('[')[0][-3:])
	n = len(name)
	realName = ""
	for ch in name:
		if ch == ' ':
			realName += ' '
		else:
			ord1 = ((ord(ch) - 97) + sectorId) % 26
			realName += chr(ord1 + 97)
	if realName == "northpole object storage":
		print(sectorId)
