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

partSum = 0
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
lines = []
lineNums = []
#num,start,end,isPart
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
				isPart = False
				if isSymbol(i,numStart-1) == True or isSymbol(i,numEnd+1) == True:
					isPart = True
				for k in range(numStart-1,numEnd+2):
					if isSymbol(i-1,k) == True or isSymbol(i+1,k) == True:
						isPart = True
				lineNums[i][lines[i]-1]['isPart'] = isPart
				if isPart == True:
					partSum += lineNums[i][lines[i]-1]['num']
		else:
			if isNum(i,j) == True: # start num
				inNum = True
				lines[i] += 1
				lineNums[i].append({'num':-1,'start':j,'end':-1,'isPart':None})
print(partSum)
