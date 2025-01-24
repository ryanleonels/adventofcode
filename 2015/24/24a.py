#!/usr/local/bin/python3

total = 0
packages = []
fileHandle = open("24.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	package = int(fileLine.strip())
	total += package
	packages.append(package)
n = len(packages)
total4 = total // 4
packages.reverse()

minPackage = 999999999
minEntanglement = 999999999999999999

def getMin(curTotal, packages1):
	global minPackage, minEntanglement
	minN = 999999999
	n2 = 0
	if len(packages1) > 0:
		n2 = packages1[-1] + 1
	for i in range(n2, n):
		if curTotal + packages[i] < total4:
			curN = getMin(curTotal + packages[i], packages1 + [i])
			minN = min(curN, minN)
		if curTotal + packages[i] == total4:
			curN = len(packages1) + 1
			minN = min(curN, minN)
			if curN == minN:
				curEntanglement = packages[i]
				np = len(packages1)
				for j in range(0, np):
					curEntanglement *= packages[packages1[j]]
				if curN == minPackage:
					minEntanglement = min(curEntanglement, minEntanglement)
				if curN < minPackage:
					minPackage = curN
					minEntanglement = curEntanglement
				if curN == minPackage and curEntanglement == minEntanglement:
					print(minPackage, minEntanglement, packages1 + [i])
	return minN

n1 = getMin(0, [])
print(minEntanglement)