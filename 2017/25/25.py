#!/usr/local/bin/python3

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

begin = '.'
steps = 0
(curState, curValue) = ('.', -1)
(write, move, nextState) = (-1, 0, '.')
logic = {}
tape = {}
tape[0] = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	words = fileLine.strip().split(' ')
	if words[0] == 'Begin':
		begin = words[-1][0]
	if words[0] == 'Perform':
		steps = int(words[-2])
	if words[0] == 'In':
		curState = words[-1][0]
	if words[0] == 'If':
		curValue = int(words[-1][0])
	if words[1] == 'Write':
		write = int(words[-1][0])
	if words[1] == 'Move':
		if words[-1] == 'right.':
			move = 1
		else:
			move = -1
	if words[1] == 'Continue':
		nextState = words[-1][0]
		logic[(curState, curValue)] = (write, move, nextState)

"""for state in logic:
	print(state, logic[state])"""

step = 0
(curState, pos) = (begin, 0)
while step < steps:
	curValue = tape[pos]
	(write, move, nextState) = logic[(curState, curValue)]
	tape[pos] = write
	pos += move
	if pos not in tape:
		tape[pos] = 0
	curState = nextState
	step += 1

checksum = 0
for pos in tape:
	if tape[pos] == 1:
		checksum += 1
print(checksum)