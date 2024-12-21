#!/usr/bin/python3

total = 0

movesKeypad = {}
movesKeypad['0'] = {}
movesKeypad['0']['0'] = ['A']
movesKeypad['0']['1'] = ['^<A']
movesKeypad['0']['2'] = ['^A']
movesKeypad['0']['3'] = ['^>A', '>^A']
movesKeypad['0']['4'] = ['^^<A', '^<^A']
movesKeypad['0']['5'] = ['^^A']
movesKeypad['0']['6'] = ['^^>A', '^>^A', '>^^A']
movesKeypad['0']['7'] = ['^^^<A', '^^<^A', '^<^^A']
movesKeypad['0']['8'] = ['^^^A']
movesKeypad['0']['9'] = ['^^^>A', '^^>^A', '^>^^A']
movesKeypad['0']['A'] = ['>A']
movesKeypad['1'] = {}
movesKeypad['1']['0'] = ['>vA']
movesKeypad['1']['1'] = ['A']
movesKeypad['1']['2'] = ['>A']
movesKeypad['1']['3'] = ['>>A']
movesKeypad['1']['4'] = ['^A']
movesKeypad['1']['5'] = ['^>A', '>^A']
movesKeypad['1']['6'] = ['^>>A', '>^>A', '>>^A']
movesKeypad['1']['7'] = ['^^A']
movesKeypad['1']['8'] = ['^^>A', '^>^A', '>^^A']
movesKeypad['1']['9'] = ['^^>>A', '^>>^A', '^>^>A', '>>^^A', '>^>^A', '>^^>A']
movesKeypad['1']['A'] = ['>>vA', '>v>A']
movesKeypad['2'] = {}
movesKeypad['2']['0'] = ['vA']
movesKeypad['2']['1'] = ['<A']
movesKeypad['2']['2'] = ['A']
movesKeypad['2']['3'] = ['>A']
movesKeypad['2']['4'] = ['^<A', '<^A']
movesKeypad['2']['5'] = ['^A']
movesKeypad['2']['6'] = ['^>A', '>^A']
movesKeypad['2']['7'] = ['^^<A', '^<^A', '<^^A']
movesKeypad['2']['8'] = ['^^A']
movesKeypad['2']['9'] = ['^^>A', '^>^A', '>^^A']
movesKeypad['2']['A'] = ['v>A', '>vA']
movesKeypad['3'] = {}
movesKeypad['3']['0'] = ['v<A', '<vA']
movesKeypad['3']['1'] = ['<<A']
movesKeypad['3']['2'] = ['<A']
movesKeypad['3']['3'] = ['A']
movesKeypad['3']['4'] = ['^<<A', '<^<A', '<<^A']
movesKeypad['3']['5'] = ['^<A', '<^A']
movesKeypad['3']['6'] = ['^A']
movesKeypad['3']['7'] = ['^^<<A', '^<<^A', '^<^<A', '<^^<A', '<^<^A', '<<^^A']
movesKeypad['3']['8'] = ['^^<A', '^<^A', '<^^A']
movesKeypad['3']['9'] = ['^^A']
movesKeypad['3']['A'] = ['vA']
movesKeypad['4'] = {}
movesKeypad['4']['0'] = ['>vvA', 'v>vA']
movesKeypad['4']['1'] = ['vA']
movesKeypad['4']['2'] = ['v>A', '>vA']
movesKeypad['4']['3'] = ['v>>A', '>v>A', '>>vA']
movesKeypad['4']['4'] = ['A']
movesKeypad['4']['5'] = ['>A']
movesKeypad['4']['6'] = ['>>A']
movesKeypad['4']['7'] = ['^A']
movesKeypad['4']['8'] = ['^>A', '>^A']
movesKeypad['4']['9'] = ['^>>A', '>^>A', '>>^A']
movesKeypad['4']['A'] = ['>>vvA', '>v>vA', '>vv>A', 'v>>vA', 'v>v>A']
movesKeypad['5'] = {}
movesKeypad['5']['0'] = ['vvA']
movesKeypad['5']['1'] = ['v<A', '<vA']
movesKeypad['5']['2'] = ['vA']
movesKeypad['5']['3'] = ['v>A', '>vA']
movesKeypad['5']['4'] = ['<A']
movesKeypad['5']['5'] = ['A']
movesKeypad['5']['6'] = ['>A']
movesKeypad['5']['7'] = ['^<A', '<^A']
movesKeypad['5']['8'] = ['^A']
movesKeypad['5']['9'] = ['^>A', '>^A']
movesKeypad['5']['A'] = ['vv>A', 'v>vA', '>vvA']
movesKeypad['6'] = {}
movesKeypad['6']['0'] = ['vv<A', 'v<vA', '<vvA']
movesKeypad['6']['1'] = ['v<<A', '<v<A', '<<vA']
movesKeypad['6']['2'] = ['v<A', '<vA']
movesKeypad['6']['3'] = ['vA']
movesKeypad['6']['4'] = ['<<A']
movesKeypad['6']['5'] = ['<A']
movesKeypad['6']['6'] = ['A']
movesKeypad['6']['7'] = ['^<<A', '<^<A', '<<^A']
movesKeypad['6']['8'] = ['^<A', '<^A']
movesKeypad['6']['9'] = ['^A']
movesKeypad['6']['A'] = ['vvA']
movesKeypad['7'] = {}
movesKeypad['7']['0'] = ['>vvvA', 'v>vvA', 'vv>vA']
movesKeypad['7']['1'] = ['vvA']
movesKeypad['7']['2'] = ['vv>A', 'v>vA', '>vvA']
movesKeypad['7']['3'] = ['vv>>A', 'v>v>A', 'v>>vA', '>vv>A', '>v>vA', '>>vvA']
movesKeypad['7']['4'] = ['vA']
movesKeypad['7']['5'] = ['v>A', '>vA']
movesKeypad['7']['6'] = ['v>>A', '>v>A', '>>vA']
movesKeypad['7']['7'] = ['A']
movesKeypad['7']['8'] = ['>A']
movesKeypad['7']['9'] = ['>>A']
movesKeypad['7']['A'] = ['>>vvvA', '>v>vvA', '>vv>vA', '>vvv>A', 'v>>vvA', 'v>v>vA', 'v>vv>A', 'vv>>vA', 'vv>v>A']
movesKeypad['8'] = {}
movesKeypad['8']['0'] = ['vvvA']
movesKeypad['8']['1'] = ['vv<A', 'v<vA', '<vvA']
movesKeypad['8']['2'] = ['vvA']
movesKeypad['8']['3'] = ['vv>A', 'v>vA', '>vvA']
movesKeypad['8']['4'] = ['v<A', '<vA']
movesKeypad['8']['5'] = ['vA']
movesKeypad['8']['6'] = ['v>A', '>vA']
movesKeypad['8']['7'] = ['<A']
movesKeypad['8']['8'] = ['A']
movesKeypad['8']['9'] = ['>A']
movesKeypad['8']['A'] = ['vvv>A', 'vv>vA', 'v>vvA', '>vvvA']
movesKeypad['9'] = {}
movesKeypad['9']['0'] = ['vvv<A', 'vv<vA', 'v<vvA', '<vvvA']
movesKeypad['9']['1'] = ['vv<<A', 'v<v<A', 'v<<vA', '<vv<A', '<v<vA', '<<vvA']
movesKeypad['9']['2'] = ['vv<A', 'v<vA', '<vvA']
movesKeypad['9']['3'] = ['vvA']
movesKeypad['9']['4'] = ['v<<A', '<v<A', '<<vA']
movesKeypad['9']['5'] = ['v<A', '<vA']
movesKeypad['9']['6'] = ['vA']
movesKeypad['9']['7'] = ['<<A']
movesKeypad['9']['8'] = ['<A']
movesKeypad['9']['9'] = ['A']
movesKeypad['9']['A'] = ['vvvA']
movesKeypad['A'] = {}
movesKeypad['A']['0'] = ['<A']
movesKeypad['A']['1'] = ['^<<A', '<^<A']
movesKeypad['A']['2'] = ['^<A', '<^A']
movesKeypad['A']['3'] = ['^A']
movesKeypad['A']['4'] = ['^^<<A', '^<^<A', '^<<^A', '<^^<A', '<^<^A']
movesKeypad['A']['5'] = ['^^<A', '^<^A', '<^^A']
movesKeypad['A']['6'] = ['^^A']
movesKeypad['A']['7'] = ['^^^<<A', '^^<^<A', '^^<<^A', '^<^^<A', '^<^<^A', '^<<^^A', '<^^^<A', '<^^<^A', '<^<^^A']
movesKeypad['A']['8'] = ['^^^<A', '^^<^A', '^<^^A', '<^^^A']
movesKeypad['A']['9'] = ['^^^A']
movesKeypad['A']['A'] = ['A']

movesDirpad = {} # sequence(s) when moving from button 1 to button 2 + activate (locally optimal = always pick the first one)
movesDirpad['^'] = {}
movesDirpad['^']['^'] = ['A']
movesDirpad['^']['<'] = ['v<A']
movesDirpad['^']['v'] = ['vA']
movesDirpad['^']['>'] = ['v>A', '>vA'] #conf
movesDirpad['^']['A'] = ['>A']
movesDirpad['<'] = {}
movesDirpad['<']['^'] = ['>^A']
movesDirpad['<']['<'] = ['A']
movesDirpad['<']['v'] = ['>A']
movesDirpad['<']['>'] = ['>>A']
movesDirpad['<']['A'] = ['>>^A', '>^>A'] #conf
movesDirpad['v'] = {}
movesDirpad['v']['^'] = ['^A']
movesDirpad['v']['<'] = ['<A']
movesDirpad['v']['v'] = ['A']
movesDirpad['v']['>'] = ['>A']
movesDirpad['v']['A'] = ['^>A', '>^A'] #conf
movesDirpad['>'] = {}
movesDirpad['>']['^'] = ['<^A', '^<A'] #conf
movesDirpad['>']['<'] = ['<<A']
movesDirpad['>']['v'] = ['<A']
movesDirpad['>']['>'] = ['A']
movesDirpad['>']['A'] = ['^A']
movesDirpad['A'] = {}
movesDirpad['A']['^'] = ['<A']
movesDirpad['A']['<'] = ['v<<A', '<v<A'] #conf
movesDirpad['A']['v'] = ['<vA', 'v<A'] #conf
movesDirpad['A']['>'] = ['vA']
movesDirpad['A']['A'] = ['A']

def getShortestSequenceNum(code, depth):
	shortestLen = 999999999999999999
	shortestSeq = ""
	moves1 = movesKeypad['A'][code[0]]
	moves2 = movesKeypad[code[0]][code[1]]
	moves3 = movesKeypad[code[1]][code[2]]
	moves4 = movesKeypad[code[2]][code[3]]
	for move1 in moves1:
		for move2 in moves2:
			for move3 in moves3:
				for move4 in moves4:
					seq1 = 'A'+move1+move2+move3+move4
					seq2 = {}
					n = len(seq1)
					for i in range(1, n):
						if (seq1[i-1], seq1[i]) in seq2:
							seq2[(seq1[i-1], seq1[i])] += 1
						else:
							seq2[(seq1[i-1], seq1[i])] = 1
					seq = getShortestSequenceDir(seq2, depth - 1)
					lenSeq = 0
					for pair in seq:
						lenSeq += seq[pair]
					if lenSeq < shortestLen:
						shortestSeq = seq
						shortestLen = lenSeq
	return shortestSeq

def getShortestSequenceDir(seq, depth):
	#seq = {(1,2): 3, (4,5): 6, etc.}
	seq1 = {}
	for pair in seq:
		ch1 = pair[0]
		ch2 = pair[1]
		n = seq[pair]
		seqString = 'A' + movesDirpad[ch1][ch2][0] # we only need to use the optimal one
		lenString = len(seqString)
		for i in range(1, lenString):
			if (seqString[i-1], seqString[i]) in seq1:
				seq1[(seqString[i-1], seqString[i])] += n
			else:
				seq1[(seqString[i-1], seqString[i])] = n
	if depth == 0:
		return seq1
	return getShortestSequenceDir(seq1, depth - 1)

#fileHandle = open("temp.in", "r")
fileHandle = open("21.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	seq = getShortestSequenceNum(fileLine, 25)
	length = 0
	for pair in seq:
		length += seq[pair]
	#print([fileLine, '->', length])
	num = int(fileLine[:3])
	complexity = length * num
	#print([length, '*', num, '=', complexity])
	total += complexity

print(total)
