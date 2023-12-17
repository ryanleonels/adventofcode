#!/usr/bin/python3

def isNum(x,y):
	if x < 0 or x >= 140 or y < 0 or y >= 140:
		return False
	if fileLines[x][y] >= '0' and fileLines[x][y] <= '9':
		return True
	return False

def isSymbol(x,y):
	if x < 0 or x >= 140 or y < 0 or y >= 140:
		return False
	if (fileLines[x][y] < '0' or fileLines[x][y] > '9') and fileLines[x][y] != '.':
		return True
	return False

def whichNum(x,y):
	if isNum(x,y) == False:
		return False
	for i in range(0,lines[x]):
		if y >= lineNums[x][i]['start'] and y <= lineNums[x][i]['end']:
			return (x,i)
	return False

gearSum = 0
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
lines = []
lineNums = []
#num,start,end
for i in range(0,140):
	lines.append(0)
	lineNums.append([])
	inNum = False
	for j in range(0,140):
		if inNum == True:
			if isNum(i,j) == False or j == 139: # end num
				inNum = False
				if isNum(i,j) == False:
					lineNums[i][lines[i]-1]['end'] = j-1
				else:
					lineNums[i][lines[i]-1]['end'] = j
				numStart = lineNums[i][lines[i]-1]['start']
				numEnd = lineNums[i][lines[i]-1]['end']
				lineNums[i][lines[i]-1]['num'] = int(fileLines[i][numStart:numEnd+1])
		else:
			if isNum(i,j) == True: # start num
				inNum = True
				lines[i] += 1
				lineNums[i].append({'num':-1,'start':j,'end':-1})
for i in range(0,140):
	for j in range(0,140):
		if fileLines[i][j] == '*':
			nums = set(())
			for i1 in range(i-1,i+2):
				for j1 in range(j-1,j+2):
					if isNum(i1,j1) == True:
						nums.add(whichNum(i1,j1))
			if len(nums) == 2:
				gear = 1
				for (x,y) in nums:
					gear *= lineNums[x][y]['num']
				gearSum += gear
print(gearSum)
