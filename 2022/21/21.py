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
while not done:
	done = True
	for monkey in monkeys:
		if type(monkeys[monkey]) is not int:
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
print(monkeys['root'])
