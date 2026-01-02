#!/usr/bin/python3

(curLine, n, joltages) = ("", 0, {})

def maxJoltage(len1, pos):
	if len1 == 0:
		return ""
	if pos == n - len1:
		return curLine[pos:]
	if (len1, pos) in joltages:
		return joltages[(len1, pos)]
	joltage = max(curLine[pos] + maxJoltage(len1 - 1, pos + 1), maxJoltage(len1, pos + 1))
	joltages[(len1, pos)] = joltage
	return joltage

total = 0
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(curLine, n, joltages) = (fileLine, len(fileLine), {})
	joltage = maxJoltage(12, 0)
	total += int(joltage)
print(total)
