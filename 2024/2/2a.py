#!/usr/bin/python3

def isSafe(report):
	n = len(report)
	safe = True
	if report[1] == report[0]:
		return False
	if report[1] > report[0]:
		dir1 = 1
	if report[1] < report[0]:
		dir1 = -1
	for i in range(0, n - 1):
		if dir1 == 1 and ((report[i+1] < report[i] + 1) or (report[i+1] > report[i] + 3)):
			return False
		if dir1 == -1 and ((report[i+1] > report[i] - 1) or (report[i+1] < report[i] - 3)):
			return False
	return True

report = []
safeReports = 0
fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	report = [int(x) for x in fileLine.split()]
	n = len(report)
	safe = isSafe(report)
	if safe == True:
		safeReports += 1
	else:
		for i in range(0, n):
			report1 = []
			for j in range(0, n):
				if j != i:
					report1.append(report[j])
			safe1 = isSafe(report1)
			if safe1 == True:
				safe = True
				break
		if safe == True:
			safeReports += 1
print(safeReports)
