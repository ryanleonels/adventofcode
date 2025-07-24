#!/usr/bin/python3

fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
scores = []
scores1 = {'(': 1, '[': 2, '{': 3, '<': 4}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	stk = []
	valid = True
	for i in range(0, n):
		ch = fileLine[i]
		if ch in ['(', '[', '{', '<']:
			stk.append(ch)
		if ch == ')' and (len(stk) == 0 or stk[-1] != '('):
			valid = False
			break
		if ch == ']' and (len(stk) == 0 or stk[-1] != '['):
			valid = False
			break
		if ch == '}' and (len(stk) == 0 or stk[-1] != '{'):
			valid = False
			break
		if ch == '>' and (len(stk) == 0 or stk[-1] != '<'):
			valid = False
			break
		if ch in [')', ']', '}', '>']:
			stk.pop()
	if valid:
		n1 = len(stk)
		score = 0
		for i in range(n1 - 1, -1, -1):
			score *= 5
			score += scores1[stk[i]]
		scores.append(score)
scores = sorted(scores)
n2 = len(scores)
print(scores[n2 // 2])
