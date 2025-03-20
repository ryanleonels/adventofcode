#!/usr/local/bin/python3

fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))

(nrow, ncol) = (len(grid), len(grid[0]))
#print(nrow, ncol)
#for i in range(0, nrow):
	#print(''.join(grid[i]))

startcol = 0
while grid[0][startcol] != '|':
	startcol += 1
start = (0, startcol)
pos = start
dir1 = (1, 0)
done = False
letters = ''
steps = 1
while not done:
	if grid[pos[0]][pos[1]] >= 'A' and grid[pos[0]][pos[1]] <= 'Z':
		letters += grid[pos[0]][pos[1]]
	turn = False
	pos1 = (pos[0] + dir1[0], pos[1] + dir1[1])
	if pos1[0] < 0 or pos1[0] >= nrow or pos1[1] < 0 or pos1[1] >= ncol or grid[pos1[0]][pos1[1]] == ' ':
		turn = True
		#print(pos)
	if turn and dir1 == (1, 0) and pos[1] > 0 and grid[pos[0]][pos[1] - 1] == '-':
		turn = False
		dir1 = (0, -1)
	if turn and dir1 == (1, 0) and pos[1] < ncol - 1 and grid[pos[0]][pos[1] + 1] == '-':
		turn = False
		dir1 = (0, 1)
	if turn and dir1 == (-1, 0) and pos[1] > 0 and grid[pos[0]][pos[1] - 1] == '-':
		turn = False
		dir1 = (0, -1)
	if turn and dir1 == (-1, 0) and pos[1] < ncol - 1 and grid[pos[0]][pos[1] + 1] == '-':
		turn = False
		dir1 = (0, 1)
	if turn and dir1 == (0, 1) and pos[0] > 0 and grid[pos[0] - 1][pos[1]] == '|':
		turn = False
		dir1 = (-1, 0)
	if turn and dir1 == (0, 1) and pos[0] < nrow - 1 and grid[pos[0] + 1][pos[1]] == '|':
		turn = False
		dir1 = (1, 0)
	if turn and dir1 == (0, -1) and pos[0] > 0 and grid[pos[0] - 1][pos[1]] == '|':
		turn = False
		dir1 = (-1, 0)
	if turn and dir1 == (0, -1) and pos[0] < nrow - 1 and grid[pos[0] + 1][pos[1]] == '|':
		turn = False
		dir1 = (1, 0)
	if turn:
		done = True
		continue
	pos = (pos[0] + dir1[0], pos[1] + dir1[1])
	steps += 1
print(steps)