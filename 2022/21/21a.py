#!/usr/bin/python3

fileHandle = open("21.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
monkeys = {}
done = False
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(name, job) = fileLine.split(': ')
	if job.isdigit():
		monkeys[name] = int(job)
	else:
		monkeys[name] = tuple(job.split(' '))
monkeys['humn'] = 1j # j = human number
while not done:
	done = True
	for monkey in monkeys:
		if type(monkeys[monkey]) is not int and type(monkeys[monkey]) is not complex and monkey != 'root':
			(left, op, right) = monkeys[monkey]
			if type(monkeys[left]) is int and type(monkeys[right]) is int:
				done = False
				if op == '+':
					monkeys[monkey] = monkeys[left] + monkeys[right]
				if op == '-':
					monkeys[monkey] = monkeys[left] - monkeys[right]
				if op == '*':
					monkeys[monkey] = monkeys[left] * monkeys[right]
				if op == '/':
					monkeys[monkey] = monkeys[left] // monkeys[right]
			if type(monkeys[left]) is int and type(monkeys[right]) is complex:
				done = False
				if op == '+':
					monkeys[monkey] = monkeys[left] + monkeys[right]
				if op == '-':
					monkeys[monkey] = monkeys[left] - monkeys[right]
				if op == '*':
					monkeys[monkey] = monkeys[left] * monkeys[right]
				if op == '/':
					monkeys[monkey] = monkeys[left] / monkeys[right]
					exit(1)
			if type(monkeys[left]) is complex and type(monkeys[right]) is int:
				done = False
				if op == '+':
					monkeys[monkey] = monkeys[left] + monkeys[right]
				if op == '-':
					monkeys[monkey] = monkeys[left] - monkeys[right]
				if op == '*':
					monkeys[monkey] = monkeys[left] * monkeys[right]
				if op == '/':
					monkeys[monkey] = monkeys[left] / monkeys[right]
(left, op, right) = monkeys['root']
#print(monkeys[left], monkeys[right])
# a+bj = c -> j = (c - a) / b
(a, b, c) = (0, 0, 0)
if type(monkeys[left]) is int and type(monkeys[right]) is complex:
	(a, b, c) = (monkeys[right].real, monkeys[right].imag, monkeys[left])
if type(monkeys[left]) is complex and type(monkeys[right]) is int:
	(a, b, c) = (monkeys[left].real, monkeys[left].imag, monkeys[right])
print(int(((c - a) / b) + 0.1)) # +0.1 to offset rounding errors
