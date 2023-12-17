#!/usr/bin/python3

def checkRow(row, group):
	curGroup = 0
	curStreak = 0
	n = len(row)
	n1 = len(group)
	for i in range(0, n):
		if row[i] == 0: # end previous streak if prev=1 (curStreak>0) / otherwise go forward (no-op)
			if curStreak > 0:
				if curStreak != group[curGroup]:
					return False
				curGroup += 1
				curStreak = 0
		if row[i] == 1: # continue previous streak if prev=1 (curStreak>0) / otherwise start new streak
			curStreak += 1
			if curGroup >= n1:
				return False
		if i == (n - 1) and curStreak > 0:
			if curStreak != group[curGroup]:
				return False
			curGroup += 1
	if curGroup != n1:
		return False
	return True

sumCount = 0
fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
rows = []
groups = []
unknowns = []
#fileLines = ["???.### 1,1,3",".??..??...?##. 1,1,3","?#?#?#?#?#?#?#? 1,3,1,6","????.#...#... 4,1,1","????.######..#####. 1,6,5","?###???????? 3,2,1"]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	row = []
	group = []
	rowLine = fileLine.split(' ')[0]
	n = len(rowLine)
	n1 = 0
	unknown = []
	for i in range(0, len(rowLine)):
		if rowLine[i] == '.':
			row.append(0)
		if rowLine[i] == '#':
			row.append(1)
		if rowLine[i] == '?':
			row.append(-1)
			n1 += 1
			unknown.append(i)
	rows.append(row)
	unknowns.append(unknown)
	groupLine = fileLine.split(' ')[1].split(',')
	for groupEntry in groupLine:
		group.append(int(groupEntry))
	groups.append(group)
	#row = condition (0 = operational, 1 = damaged, -1 = unknown)
	#group = contiguous groups of damaged springs
	#unknown = locations of unknowns
	#row1 = row after substitution
	count = 0
	n2 = 1
	for i in range(0, n1):
		n2 *= 2
	for i in range(0, n2):
		i1 = i
		row1 = row
		for i2 in range(0, n1):
			row1[unknown[i2]] = (i1 % 2)
			i1 = int(i1 / 2)
		if checkRow(row1, group) == True:
			count += 1
	#print(count)
	sumCount += count
print(sumCount)
