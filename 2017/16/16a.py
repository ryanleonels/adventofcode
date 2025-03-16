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
allpos = {}
allpos[programs] = 0

def dance(prog):
	programs = prog
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
	return programs

#print(0, programs)
(t, t1, cycle) = (0, 0, 0)
duplicate = False
while duplicate == False:
	programs = dance(programs)
	t += 1
	#print(t, programs)
	if programs in allpos:
		duplicate = True
		#print("duplicate of " + str(allpos[programs]))
		t1 = allpos[programs]
		cycle = t - t1
	else:
		allpos[programs] = t

allpos1 = {}
for pos in allpos:
	allpos1[allpos[pos]] = pos

print(allpos1[((1000000000 - t1) % cycle) + t1])