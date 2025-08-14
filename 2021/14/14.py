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

polymer = template
for step in range(1, 11):
	n = len(polymer)
	polymer1 = polymer[0]
	for i in range(1, n):
		if polymer[i-1:i+1] in rules:
			polymer1 += rules[polymer[i-1:i+1]]
		polymer1 += polymer[i]
	polymer = polymer1

n = len(polymer)
most = ('', 0)
least = ('', n)
occur = {}
for i in range(0, n):
	if polymer[i] in occur:
		occur[polymer[i]] += 1
	else:
		occur[polymer[i]] = 1
for ch in occur:
	if occur[ch] > most[1]:
		most = (ch, occur[ch])
	if occur[ch] < least[1]:
		least = (ch, occur[ch])
#print(occur)
#print(most, least)
print(most[1] - least[1])
