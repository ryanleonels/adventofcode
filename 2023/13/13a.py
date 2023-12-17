#!/usr/bin/python3

rowx = 0
colx = 0

def countReflection(pattern1):
	count = 0
	nrow = len(pattern1)
	ncol = len(pattern1[0])
	rows1 = []
	for i in range(0, nrow): #calculate hash of rows
		x = 0
		for j in range(0, ncol):
			x *= 2
			if pattern1[i][j] == '#':
				x += 1
		rows1.append(x)
	cols1 = []
	for i in range(0, ncol): #calculate hash of columns
		x = 0
		for j in range(0, nrow):
			x *= 2
			if pattern1[j][i] == '#':
				x += 1
		cols1.append(x)
	reflect = True
	for i in range(1, nrow):
		reflect = True
		for j in range(i, nrow):
			row1 = j
			row2 = (2 * i - 1) - j
			if row1 >= 0 and row1 < nrow and row2 >= 0 and row2 < nrow:
				if rows1[row1] != rows1[row2]:
					reflect = False
		if reflect == True and i != rowx:
			#print("new reflection on row "+str(i))
			count += (100 * i)
	for i in range(1, ncol):
		reflect = True
		for j in range(i, ncol):
			col1 = j
			col2 = (2 * i - 1) - j
			if col1 >= 0 and col1 < ncol and col2 >= 0 and col2 < ncol:
				if cols1[col1] != cols1[col2]:
					reflect = False
		if reflect == True and i != colx:
			#print("new reflection on col "+str(i))
			count += i
	return count

sumNotes = 0
fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
pattern = []
n = 0
row = 0
col = 0
rows = []
cols = []
#fileLines = ["#.##..##.","..#.##.#.","##......#","##......#","..#.##.#.","..##..##.","#.#.##.#.","","#...##..#","#....#..#","..##..###","#####.##.","#####.##.","..##..###","#....#..#",""]
for fileLine in fileLines:
	if len(fileLine) == 0:
		#print("Pattern "+str(n+1)+": "+str(row)+"x"+str(col))
		#for k in range(0, row):
			#print(pattern[k])
		rowx = 0
		colx = 0
		notes = countReflection(pattern)
		#print(notes)
		rowx = int(notes / 100)
		colx = notes % 100
		newNotes = []
		for i in range(0, row):
			for j in range(0, col):
				pattern2 = []
				for k in range(0, row):
					pattern2.append(pattern[k])
				if pattern[i][j] == '.':
					patternRow = list(pattern2[i])
					patternRow[j] = '#'
					pattern2[i] = "".join(patternRow)
				if pattern[i][j] == '#':
					patternRow = list(pattern2[i])
					patternRow[j] = '.'
					pattern2[i] = "".join(patternRow)
				temp = countReflection(pattern2)
				if temp != 0 and temp != notes:
					#print("smudge on " + str((i,j))+": " + str(temp))
					if temp not in newNotes:
						newNotes.append(temp)
					#for k in range(0, row):
						#print(pattern2[k])
		#print(newNotes)
		sumNotes += sum(newNotes)
		n += 1
		row = 0
		pattern = []
		continue
	pattern.append(fileLine)
	row += 1
	if row == 1:
		col = len(fileLine)
print(sumNotes)
