#!/usr/bin/python3

sum1 = 0
fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	stack = [(1, 0)] # current *s term, current +s term
	depth = 0
	n = len(fileLine)
	for i in range(0, n):
		ch = fileLine[i]
		if ch == '(':
			depth += 1
			stack.append((1, 0))
		if ch == ')':
			stack[depth] = (stack[depth][0] * stack[depth][1], 0)
			depth -= 1
			(num, temp) = stack.pop()
			stack[depth] = (stack[depth][0], stack[depth][1] + num)
		if ch == '+':
			pass
		if ch == '*':
			stack[depth] = (stack[depth][0] * stack[depth][1], 0)
		if ch >= '0' and ch <= '9':
			num = int(ch)
			stack[depth] = (stack[depth][0], stack[depth][1] + num)
	stack[depth] = (stack[depth][0] * stack[depth][1], 0)
	result = stack[0][0]
	#print(result)
	sum1 += result

print(sum1)
