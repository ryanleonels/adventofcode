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

def containShinyGold(bag):
	for (bag1, qty) in bags[bag]:
		if bag1 == "shiny gold":
			return True
		if containShinyGold(bag1):
			return True
	return False

n = 0
for bag in bags:
	#print(bag, bags[bag])
	if containShinyGold(bag):
		n += 1
print(n)
