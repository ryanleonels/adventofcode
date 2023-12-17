#!/usr/bin/python3

valueSum = 0
histories = []
fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	history = []
	for entry in fileLine.split(' '):
		history.append(int(entry))
	histories.append(history)
	n = len(history)
	historyDiffs = []
	historyDiffs.append(history)
	order = 0
	allZero = False
	while allZero == False:
		order += 1
		historyDiff = []
		for i in range(0, n - order):
			historyDiff.append(historyDiffs[order - 1][i + 1] - historyDiffs[order - 1][i])
		historyDiffs.append(historyDiff)
		allZero = True
		for i in range(0, n - order):
			if historyDiffs[order][i] != 0:
				allZero = False
				break
	prevVal = 0
	for i in range(order - 1, -1, -1):
		prevVal = historyDiffs[i][0] - prevVal
		if i == 0:
			value = prevVal
			valueSum += value
print(valueSum)
