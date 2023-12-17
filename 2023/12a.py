#!/usr/bin/python3

counts = {}

def cnt(row, group):
	key = row + "|" + str(group);
	if key in counts:
		return counts[key]
	counts[key] = doCount(row, group)
	return counts[key]

def doCount(row, group):
	if len(row) == 0: # string done
		if len(group) == 0: # if groups done = 1 else 0
			return 1
		return 0
	if row.count('#') > sum(group): # more #s than the ones in groups = not possible
		return 0
	if row[0] == '#': # check if next n characters can all contain #
		num = group[0]
		if len(row) < num: # not enough string length for group = not possible (0)
			return 0
		if row[:num].count('.') > 0: # group interrupted with non-broken spring
			return 0
		if len(row) > num and row[:num].count('.') == 0 and row[num] == '#': # group length > indicated
			return 0
		if len(row) == num: # truncate to end of group (+1 if there are still more characters)
			return cnt(row[num:], group[1:])
		return cnt(row[num+1:], group[1:])
	if row[0] == '.': # not broken, move forward
		return cnt(row[1:], group)
	if row[0] == '?': # count = count(broken) + count(not broken)
		return cnt('.'+row[1:], group) + cnt('#'+row[1:], group)
	return 0

sumCount = 0
fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
rows = []
groups = []
#fileLines = ["???.### 1,1,3",".??..??...?##. 1,1,3","?#?#?#?#?#?#?#? 1,3,1,6","????.#...#... 4,1,1","????.######..#####. 1,6,5","?###???????? 3,2,1"]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	row = fileLine.split(' ')[0]
	rows.append(row)
	group = []
	groupLine = fileLine.split(' ')[1].split(',')
	for groupEntry in groupLine:
		group.append(int(groupEntry))
	groups.append(group)
	# row = condition string (. = operational, # = damaged, ? = unknown)
	# group = contiguous groups of damaged springs
	# transformation for part 2
	row = row+"?"+row+"?"+row+"?"+row+"?"+row
	group = group+group+group+group+group
	#print(row + "|" + str(group))
	counts = {}
	count = cnt(row, group)
	#print(count)
	sumCount += count
print(sumCount)
