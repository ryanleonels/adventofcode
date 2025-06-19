#!/usr/bin/python3

sum1 = 0
fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	stack = [(None, '')]
	depth = 0
	n = len(fileLine)
	for i in range(0, n):
		ch = fileLine[i]
		if ch == '(':
			depth += 1
			stack.append((None, ''))
		if ch == ')':
			depth -= 1
			(num, ch1) = stack.pop()
			if stack[depth][0] == None:
				stack[depth] = (num, stack[depth][1])
			else:
				res = stack[depth][0]
				if stack[depth][1] == '+':
					res += num
				if stack[depth][1] == '*':
					res *= num
				stack[depth] = (res, '')
		if ch == '+':
			stack[depth] = (stack[depth][0], '+')
		if ch == '*':
			stack[depth] = (stack[depth][0], '*')
		if ch >= '0' and ch <= '9':
			num = int(ch)
			if stack[depth][0] == None:
				stack[depth] = (num, stack[depth][1])
			else:
				res = stack[depth][0]
				if stack[depth][1] == '+':
					res += num
				if stack[depth][1] == '*':
					res *= num
				stack[depth] = (res, '')
	result = stack[0][0]
	sum1 += result

print(sum1)
