#!/usr/bin/python3

seats = []
fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	seats.append(list(fileLine.strip()))

row = len(seats)
col = len(seats[0])
print(row, col)

seats1 = []
for i in range(0, row):
	seats1.append([])
	for j in range(0, col):
		seats1[i].append(seats[i][j])

changed = True
(rounds, n) = (0, 0)
while changed:
	changed = False
	for i in range(0, row):
		for j in range(0, col):
			seats1[i][j] = seats[i][j]
			if seats[i][j] != '.':
				adj = 0
				for i1 in range(-1, 2):
					for j1 in range(-1, 2):
						if (i1 != 0 or j1 != 0) and i+i1 >= 0 and i+i1 < row and j+j1 >= 0 and j+j1 < col and seats[i+i1][j+j1] == '#':
							adj += 1
				if seats[i][j] == 'L' and adj == 0:
					seats1[i][j] = '#'
					changed = True
				if seats[i][j] == '#' and adj >= 4:
					seats1[i][j] = 'L'
					changed = True
	rounds += 1
	n = 0
	for i in range(0, row):
		for j in range(0, col):
			if seats1[i][j] == '#':
				n += 1
			seats[i][j] = seats1[i][j]
	print("Round " + str(rounds) + ": " + str(n) + " seats occupied")
print(n)
