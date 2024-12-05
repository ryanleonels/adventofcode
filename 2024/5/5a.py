#!/usr/bin/python3

result = 0
fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
part = 0
nRule = 0
rules = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		part += 1
		continue
	if part == 0:
		rules.append([int(x) for x in fileLine.split('|')])
		nRule += 1
	if part == 1:
		pages = [int(x) for x in fileLine.split(',')]
		nPage = len(pages)
		first = {}
		for i in range(0, nPage):
			first[pages[i]] = i
		brokenRule = False
		for i in range(0, nRule):
			if (rules[i][0] in first) and (rules[i][1] in first) and (first[rules[i][0]] > first[rules[i][1]]):
				brokenRule = True
				break
		if brokenRule == True:
			while True:
				n = 0
				for i in range(0, nRule):
					if (rules[i][0] in first) and (rules[i][1] in first) and (first[rules[i][0]] > first[rules[i][1]]):
						a = first[rules[i][0]]
						b = first[rules[i][1]]
						temp = pages[a]
						pages[a] = pages[b]
						pages[b] = temp
						n += 1
					first = {}
					for i in range(0, nPage):
						first[pages[i]] = i
				if n == 0:
					break
			result += pages[nPage // 2]
print(result)
