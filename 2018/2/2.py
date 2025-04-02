#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(n2, n3) = (0, 0)
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	letters = {}
	n = len(fileLine)
	for i in range(0, n):
		if fileLine[i] in letters:
			letters[fileLine[i]] += 1
		else:
			letters[fileLine[i]] = 1
	(has2, has3) = (False, False)
	for letter in letters:
		if letters[letter] == 2:
			has2 = True
		if letters[letter] == 3:
			has3 = True
	if has2:
		n2 += 1
	if has3:
		n3 += 1
checksum = n2 * n3
print(checksum)
