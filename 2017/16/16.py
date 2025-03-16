#!/usr/bin/python3

fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
moves = fileData.strip().split(',')
nMoves = len(moves)

n = 16
programs = ""
for i in range(0, n):
	programs += chr(i + 97)

for i in range(0, nMoves):
	move = moves[i]
	if move[0] == 's':
		x = int(move[1:])
		programs = programs[n-x:] + programs[0:n-x]
	if move[0] == 'x':
		(a, b) = [int(x) for x in move[1:].split('/')]
		p = list(programs)
		ch = p[a]
		p[a] = p[b]
		p[b] = ch
		programs = ''.join(p)
	if move[0] == 'p':
		(a1, b1) = move[1:].split('/')
		(a, b) = (programs.index(a1), programs.index(b1))
		p = list(programs)
		ch = p[a]
		p[a] = p[b]
		p[b] = ch
		programs = ''.join(p)

print(programs)