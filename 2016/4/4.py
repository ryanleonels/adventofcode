#!/usr/bin/python3

import collections

fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
total = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	name = ''.join(fileLine.split('[')[0][:-4].split('-'))
	sectorId = int(fileLine.split('[')[0][-3:])
	checksum = fileLine.split('[')[1].split(']')[0]
	letters = {}
	maxLetters = 0
	for ch in name:
		if ch in letters:
			letters[ch] += 1
		else:
			letters[ch] = 1
		if letters[ch] > maxLetters:
			maxLetters = letters[ch]
	n = 0
	letters = collections.OrderedDict(sorted(letters.items()))
	realChecksum = ""
	for i in range(maxLetters, 0, -1):
		for ch in letters:
			if letters[ch] == i:
				realChecksum += ch
				n += 1
				if n == 5:
					break
		if n == 5:
			break
	if checksum == realChecksum:
		total += sectorId
print(total)