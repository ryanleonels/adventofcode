#!/usr/bin/python3

fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
template = ""
rules = {}

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if template == '':
		template = fileLine.strip()
	if ' -> ' in fileLine:
		(pair, el) = fileLine.split(' -> ')
		rules[pair] = el

# 40 steps = 2^40 expansion rate, need to count pairs (cur, prev) instead of storing full polymer
n1 = len(template)
polymer = {}
polymer[(template[0], ' ')] = 1
for i in range(1, n1):
	(cur, prev) = (template[i], template[i-1])
	if (cur, prev) in polymer:
		polymer[(cur, prev)] += 1
	else:
		polymer[(cur, prev)] = 1

# [prev][cur] -> [new] means (cur, prev) becomes (new, prev) + (cur, new)
for step in range(1, 41):
	polymer1 = {}
	for (cur, prev) in polymer:
		pair = prev + cur
		if pair in rules:
			new1 = rules[pair]
			if (new1, prev) in polymer1:
				polymer1[(new1, prev)] += polymer[(cur, prev)]
			else:
				polymer1[(new1, prev)] = polymer[(cur, prev)]
			if (cur, new1) in polymer1:
				polymer1[(cur, new1)] += polymer[(cur, prev)]
			else:
				polymer1[(cur, new1)] = polymer[(cur, prev)]
		else:
			polymer1[(cur, prev)] = polymer[(cur, prev)]
	polymer = polymer1

n = 0
for (cur, prev) in polymer:
	n += polymer[(cur, prev)]
most = ('', 0)
least = ('', n)
occur = {}
for (cur, prev) in polymer:
	if cur in occur:
		occur[cur] += polymer[(cur, prev)]
	else:
		occur[cur] = polymer[(cur, prev)]
for ch in occur:
	if occur[ch] > most[1]:
		most = (ch, occur[ch])
	if occur[ch] < least[1]:
		least = (ch, occur[ch])
#print(occur)
#print(most, least)
print(most[1] - least[1])
