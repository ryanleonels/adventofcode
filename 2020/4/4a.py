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
			validFields = 0
			if len(fields['byr']) == 4 and fields['byr'].isnumeric() and int(fields['byr']) >= 1920 and int(fields['byr']) <= 2002:
				validFields += 1
			if len(fields['iyr']) == 4 and fields['iyr'].isnumeric() and int(fields['iyr']) >= 2010 and int(fields['iyr']) <= 2020:
				validFields += 1
			if len(fields['eyr']) == 4 and fields['eyr'].isnumeric() and int(fields['eyr']) >= 2020 and int(fields['eyr']) <= 2030:
				validFields += 1
			if len(fields['hgt']) == 5 and fields['hgt'][-2:] == 'cm' and fields['hgt'][:-2].isnumeric() and int(fields['hgt'][:-2]) >= 150 and int(fields['hgt'][:-2]) <= 193:
				validFields += 1
			if len(fields['hgt']) == 4 and fields['hgt'][-2:] == 'in' and fields['hgt'][:-2].isnumeric() and int(fields['hgt'][:-2]) >= 59 and int(fields['hgt'][:-2]) <= 76:
				validFields += 1
			if len(fields['hcl']) == 7 and fields['hcl'][0] == '#' and fields['hcl'][1] in '0123456789abcdef' and fields['hcl'][2] in '0123456789abcdef' and fields['hcl'][3] in '0123456789abcdef' and fields['hcl'][4] in '0123456789abcdef' and fields['hcl'][5] in '0123456789abcdef' and fields['hcl'][6] in '0123456789abcdef':
				validFields += 1
			if fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				validFields += 1
			if len(fields['pid']) == 9 and fields['pid'].isnumeric():
				validFields += 1
			if validFields == 7:
				valid += 1
		fields = {}
		continue
	fields1 = fileLine.split(' ')
	for field1 in fields1:
		(k, v) = field1.split(':')
		fields[k] = v

print(valid)
