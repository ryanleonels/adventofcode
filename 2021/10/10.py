#!/usr/bin/python3

fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
score = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	stk = []
	for i in range(0, n):
		ch = fileLine[i]
		if ch in ['(', '[', '{', '<']:
			stk.append(ch)
		if ch == ')' and (len(stk) == 0 or stk[-1] != '('):
			score += 3
			break
		if ch == ']' and (len(stk) == 0 or stk[-1] != '['):
			score += 57
			break
		if ch == '}' and (len(stk) == 0 or stk[-1] != '{'):
			score += 1197
			break
		if ch == '>' and (len(stk) == 0 or stk[-1] != '<'):
			score += 25137
			break
		if ch in [')', ']', '}', '>']:
			stk.pop()
print(score)
