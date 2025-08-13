#!/usr/bin/python3

fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

adj = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(a, b) = fileLine.split('-')
	if a not in adj:
		adj[a] = []
	adj[a].append(b)
	if b not in adj:
		adj[b] = []
	adj[b].append(a)
#for x in adj:
	#print(x, adj[x])

n = 0

def traverse(path):
	global n
	if path[-1] == 'end':
		n += 1
		#print(','.join(path))
		return
	for adj1 in adj[path[-1]]:
		if ord(adj1[0]) <= 90 or adj1 not in path:
			path1 = path.copy()
			path1.append(adj1)
			traverse(path1)

traverse(['start'])
print(n)
