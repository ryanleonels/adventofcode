#!/usr/bin/python3

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
		#print(pattern)
		rows = []
		for i in range(0, row): #calculate hash of rows
			x = 0
			for j in range(0, col):
				x *= 2
				if pattern[i][j] == '#':
					x += 1
			rows.append(x)
		cols = []
		for i in range(0, col): #calculate hash of columns
			x = 0
			for j in range(0, row):
				x *= 2
				if pattern[j][i] == '#':
					x += 1
			cols.append(x)
		#print(rows)
		#print(cols)
		#calculate notes by checking if there's any reflection on each rows/cols
		reflect = True
		for i in range(1, row):
			reflect = True
			for j in range(i, row):
				row1 = j
				row2 = (2 * i - 1) - j
				if row1 >= 0 and row1 < row and row2 >= 0 and row2 < row:
					if rows[row1] != rows[row2]:
						reflect = False
			if reflect == True:
				#print("reflection on row "+str(i))
				sumNotes += (100 * i)
		for i in range(1, col):
			reflect = True
			for j in range(i, col):
				col1 = j
				col2 = (2 * i - 1) - j
				if col1 >= 0 and col1 < col and col2 >= 0 and col2 < col:
					if cols[col1] != cols[col2]:
						reflect = False
			if reflect == True:
				#print("reflection on col "+str(i))
				sumNotes += i
		n += 1
		row = 0
		pattern = []
		continue
	pattern.append(fileLine)
	row += 1
	if row == 1:
		col = len(fileLine)
print(sumNotes)
