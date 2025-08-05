#!/usr/bin/python3

fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nStacks = 0
stacks = {}
stackData = []
stackNames = []
onStack = True
for fileLine in fileLines:
	if fileLine.strip() == '':
		if onStack == True:
			onStack = False
			n1 = len(stackData)
			len1 = len(stackData[-1])
			for i in range(1, len1, 4):
				ch = stackData[-1][i]
				stackNames.append(ch)
				stacks[ch] = []
			for i in range(n1 - 2, -1, -1):
				for j in range(1, len1, 4):
					if stackData[i][j] != ' ':
						ch = stackNames[j // 4]
						stacks[ch].append(stackData[i][j])
		continue
	if onStack == True:
		stackData.append(fileLine)
	if onStack == False:
		n1 = int(fileLine.split("move ")[1].split(" from ")[0])
		from1 = fileLine.split(" from ")[1].split(" to ")[0]
		to1 = fileLine.split(" to ")[1]
		for i in range(0, n1):
			temp = stacks[from1].pop()
			stacks[to1].append(temp)
tops = ""
for i in range(0, len(stackNames)):
	ch = stackNames[i]
	#print(ch, stacks[ch])
	tops += stacks[ch][-1]
print(tops)
