#!/usr/bin/python3

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

bags = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(bag, content) = fileLine.split(" bags contain ")
	if content == "no other bags.":
		bags[bag] = []
	else:
		contents = []
		contents1 = content.split(", ")
		for content1 in contents1:
			contents2 = content1.split(" ")
			qty = int(contents2[0])
			bag1 = " ".join(contents2[1:-1])
			contents.append((bag1, qty))
		bags[bag] = contents

def nContent(bag):
	n = 0
	for (bag1, qty) in bags[bag]:
		n += (qty * (nContent(bag1) + 1))
	return n

#for bag in bags:
	#print(bag, bags[bag])
	#print(bag, nContent(bag))
print(nContent("shiny gold"))
