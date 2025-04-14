#!/usr/bin/python3

fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

carts = {} # (row, col) -> (dir, turns, processed_in_turn)
grid = []

row = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	line = list(fileLine)
	for col in range(0, len(fileLine)):
		if fileLine[col] == '^':
			line[col] = '|'
			carts[(row, col)] = ('^', 0, True)
		if fileLine[col] == 'v':
			line[col] = '|'
			carts[(row, col)] = ('v', 0, True)
		if fileLine[col] == '<':
			line[col] = '-'
			carts[(row, col)] = ('<', 0, True)
		if fileLine[col] == '>':
			line[col] = '-'
			carts[(row, col)] = ('>', 0, True)
	grid.append(''.join(line))
	row += 1
col = len(grid[0])

"""print("t = " + str(t))
for i in range(0, row):
	for j in range(0, col):
		if (i, j) in carts:
			print(str((i, j)) + ": " + str(carts[(i, j)]))"""

t = 0
while len(carts) > 1:
	t += 1
	#print("t = " + str(t))
	for i in range(0, row):
		for j in range(0, col):
			if (i, j) in carts:
				cart = carts[(i, j)]
				carts[(i, j)] = (cart[0], cart[1], False) 
	for i in range(0, row):
		for j in range(0, col):
			if (i, j) in carts and not carts[(i, j)][2]:
				cart = carts[(i, j)]
				pos = (i, j)
				del carts[pos]
				if cart[0] == '^':
					pos = (i - 1, j)
				if cart[0] == 'v':
					pos = (i + 1, j)
				if cart[0] == '<':
					pos = (i, j - 1)
				if cart[0] == '>':
					pos = (i, j + 1)
				if grid[pos[0]][pos[1]] == '/':
					nextdir = {'^': '>', 'v': '<', '<': 'v', '>': '^'}
					cart = (nextdir[cart[0]], cart[1], True)
				if grid[pos[0]][pos[1]] == '\\':
					nextdir = {'^': '<', 'v': '>', '<': '^', '>': 'v'}
					cart = (nextdir[cart[0]], cart[1], True)
				if grid[pos[0]][pos[1]] == '+':
					nextdirs = [{}, {}, {}]
					nextdirs[0] = {'^': '<', 'v': '>', '<': 'v', '>': '^'}
					nextdirs[1] = {'^': '^', 'v': 'v', '<': '<', '>': '>'}
					nextdirs[2] = {'^': '>', 'v': '<', '<': '^', '>': 'v'}
					cart = (nextdirs[cart[1] % 3][cart[0]], cart[1] + 1, True)
				cart = (cart[0], cart[1], True)
				#print(str(pos) + ": " + str(cart))
				if pos in carts:
					print("t = " + str(t) + ": Crash at " + str((pos[1], pos[0])))
					del carts[pos]
				else:
					carts[pos] = cart
for i in range(0, row):
	for j in range(0, col):
		if (i, j) in carts:
			print((j, i))