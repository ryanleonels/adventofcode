#!/usr/bin/python3

fields = {}
tickets = []
fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if ': ' in fileLine:
		field = fileLine.split(': ')[0]
		(min1, max1) = [int(x) for x in fileLine.split(': ')[1].split(' or ')[0].split('-')]
		(min2, max2) = [int(x) for x in fileLine.split(' or ')[1].split('-')]
		fields[field] = (min1, max1, min2, max2)
	if ',' in fileLine:
		ticket = [int(x) for x in fileLine.strip().split(',')]
		tickets.append(ticket)

def valid(n):
	for field in fields:
		(min1, max1, min2, max2) = fields[field]
		if (n >= min1 and n <= max1) or (n >= min2 and n <= max2):
			return True
	return False

errorRate = 0
n = len(tickets)
for i in range(1, n):
	n1 = len(tickets[i])
	for j in range(0, n1):
		if not valid(tickets[i][j]):
			errorRate += tickets[i][j]
print(errorRate)
