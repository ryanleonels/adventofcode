#!/usr/bin/python3

fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
numbers = []
boards = []
curBoard = []
nBoard = -1
for fileLine in fileLines:
	if fileLine.strip() == '':
		nBoard += 1
		if nBoard > 0:
			boards.append(curBoard)
			curBoard = []
		continue
	if nBoard < 0:
		numbers = [int(x) for x in fileLine.split(',')]
	else:
		row = [int(x) for x in fileLine.strip().replace('  ', ' ').split(' ')]
		curBoard.append(row)

#print(numbers)
#for board1 in boards:
	#print(board1)

n = len(numbers)
state = []
for board in range(0, nBoard):
	state.append([[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]])

won = False
for i in range(0, n): # bingo each number
	for board in range(0, nBoard): # bingo each board
		for x in range(0, 5):
			for y in range(0, 5):
				if boards[board][x][y] == numbers[i]:
					state[board][x][y] = True
		# check if the board won
		for x in range(0, 5):
			if state[board][x][0] and state[board][x][1] and state[board][x][2] and state[board][x][3] and state[board][x][4]:
				won = True
				break
			if state[board][0][x] and state[board][1][x] and state[board][2][x] and state[board][3][x] and state[board][4][x]:
				won = True
				break
		if won:
			#print(i, board)
			score = 0
			for x in range(0, 5):
				for y in range(0, 5):
					if state[board][x][y] == False:
						score += boards[board][x][y]
			score *= numbers[i]
			print(score)
			break
	if won:
		break
