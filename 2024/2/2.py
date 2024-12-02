#!/usr/bin/python3

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
	safe = True
	if report[1] == report[0]:
		continue
	if report[1] > report[0]:
		dir1 = 1
	if report[1] < report[0]:
		dir1 = -1
	for i in range(0, n - 1):
		if dir1 == 1 and ((report[i+1] < report[i] + 1) or (report[i+1] > report[i] + 3)):
			safe = False
			break
		if dir1 == -1 and ((report[i+1] > report[i] - 1) or (report[i+1] < report[i] - 3)):
			safe = False
			break
	if safe == True:
		safeReports += 1
print(safeReports)
