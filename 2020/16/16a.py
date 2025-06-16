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

# determine which tickets are valid
validTickets = []
validTickets.append(tickets[0])
nTickets = len(tickets)
nFields = len(tickets[0])
for i in range(1, nTickets):
	validTicket = True
	for j in range(0, nFields):
		if not valid(tickets[i][j]):
			validTicket = False
	if validTicket:
		validTickets.append(tickets[i])

# determine valid options for each field
nValid = len(validTickets)
fields2 = []
for i in range(0, nFields):
	fields1 = set()
	#print("Field " + str(i) + ":")
	for field in fields:
		validOption = True
		(min1, max1, min2, max2) = fields[field]
		for j in range(0, nValid):
			if validTickets[j][i] < min1 or validTickets[j][i] > max2 or (validTickets[j][i] > max1 and validTickets[j][i] < min2):
				validOption = False
				break
		if validOption:
			fields1.add(field)
	#print(fields1)
	fields2.append(fields1)

# pinpoint fields
fieldNames = [''] * nFields
n = 0
while n < nFields:
	fieldsToProcess = []
	for i in range(0, nFields):
		if len(fields2[i]) == 1:
			fieldName = ''
			for field in fields2[i]:
				fieldName = field
			fieldNames[i] = fieldName
			fieldsToProcess.append(i)
			n += 1
			#print(i, fieldName)
	for i in fieldsToProcess:
		fieldName = fieldNames[i]
		for j in range(0, nFields):
			if fieldName in fields2[j]:
				fields2[j].remove(fieldName)

result = 1
for i in range(0, nFields):
	if fieldNames[i][:9] == "departure":
		result *= validTickets[0][i]
print(result)
