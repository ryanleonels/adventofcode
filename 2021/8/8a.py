#!/usr/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	patterns = fileLine.split(' | ')[0].split(' ')
	values = fileLine.split(' | ')[1].split(' ')
	pattern2s = ""
	pattern3s = ""
	pattern4s = ""
	pattern5s = []
	pattern6s = []
	pattern7s = ""
	for pattern in patterns:
		if len(pattern) == 2:
			pattern2s = pattern
		if len(pattern) == 3:
			pattern3s = pattern
		if len(pattern) == 4:
			pattern4s = pattern
		if len(pattern) == 5:
			pattern5s.append(pattern)
		if len(pattern) == 6:
			pattern6s.append(pattern)
		if len(pattern) == 7:
			pattern7s = pattern
	(a, b, c, d, e, f, g) = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
	for ch in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
		if ch in pattern3s and ch not in pattern2s:
			a = ch
		if ch in pattern4s and ch not in pattern2s and ch in pattern6s[0] and ch in pattern6s[1] and ch in pattern6s[2]:
			b = ch
		if ch in pattern2s and (ch not in pattern6s[0] or ch not in pattern6s[1] or ch not in pattern6s[2]):
			c = ch
		if ch in pattern4s and ch not in pattern2s and (ch not in pattern6s[0] or ch not in pattern6s[1] or ch not in pattern6s[2]):
			d = ch
		if ch not in pattern4s and (ch not in pattern6s[0] or ch not in pattern6s[1] or ch not in pattern6s[2]):
			e = ch
		if ch in pattern2s and ch in pattern6s[0] and ch in pattern6s[1] and ch in pattern6s[2]:
			f = ch
		if ch not in pattern3s and ch not in pattern4s and ch in pattern5s[0] and ch in pattern5s[1] and ch in pattern5s[2]:
			g = ch
	nval = len(values)
	curval = ""
	for i in range(0, nval):
		if len(values[i]) == 2:
			curval += '1'
		if len(values[i]) == 3:
			curval += '7'
		if len(values[i]) == 4:
			curval += '4'
		if len(values[i]) == 5 and f not in values[i]:
			curval += '2'
		if len(values[i]) == 5 and b not in values[i] and e not in values[i]:
			curval += '3'
		if len(values[i]) == 5 and c not in values[i]:
			curval += '5'
		if len(values[i]) == 6 and d not in values[i]:
			curval += '0'
		if len(values[i]) == 6 and c not in values[i]:
			curval += '6'
		if len(values[i]) == 6 and e not in values[i]:
			curval += '9'
		if len(values[i]) == 7:
			curval += '8'
	#print(curval)
	n += int(curval)
print(n)

"""
1 = 2 segments = cf
7 = 3 segments = acf
4 = 4 segments = bcdf
8 = 7 segments = abcdefg

5 segments: 2, 3, 5
2 = acdeg (missing b, f)
3 = acdfg (missing b, e)
5 = abdfg (missing c, e)

6 segments: 0, 6, 9
0 = abcefg (missing d)
6 = abdefg (missing c)
9 = abcdfg (missing e)

given all 10 patterns:
a = on the 3-segment pattern but not on the 2-segment pattern
b = on the 4-segment pattern but not on the 2-segment pattern + present on all 6-segment patterns
c = on the 2-segment pattern, missing from one of the 6-segment patterns
d = on the 4-segment pattern but not on the 2-segment pattern + missing from one of the 6-segment patterns
e = not on the 4-segment pattern and missing from one of the 6-segment patterns
f = on the 2-segment pattern and all of the 6-segment patterns
g = on all of the 5-segment patterns but not on the 3-segment pattern or 4-segment pattern
"""
