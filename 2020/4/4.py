#!/usr/bin/python3

valid = 0
fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

fields = {}
for fileLine in fileLines:
	if fileLine.strip() == '': # check validity
		if 'byr' in fields and 'iyr' in fields and 'eyr' in fields and 'hgt' in fields and 'hcl' in fields and 'ecl' in fields and 'pid' in fields:
			valid += 1
		fields = {}
		continue
	fields1 = fileLine.split(' ')
	for field1 in fields1:
		(k, v) = field1.split(':')
		fields[k] = v

print(valid)
