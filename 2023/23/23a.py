#!/usr/bin/python3

import sys

def setPaths(x,y,dir0):
	n = 1
	dir1 = dir0
	if dir0 == 'U':
		x1 = x - 1
		y1 = y
	if dir0 == 'D':
		x1 = x + 1
		y1 = y
	if dir0 == 'L':
		x1 = x
		y1 = y - 1
	if dir0 == 'R':
		x1 = x
		y1 = y + 1
	nBranch = 1
	while nBranch == 1:
		#print(x1,y1)
		nBranch = 0
		u = False
		d = False
		l = False
		r = False
		if dir1 != 'D' and x1 > 0 and fileLines[x1-1][y1] != '#':
			u = True
			nBranch += 1
		if dir1 != 'U' and x1 < (row - 1) and fileLines[x1+1][y1] != '#':
			d = True
			nBranch += 1
		if dir1 != 'R' and y1 > 0 and fileLines[x1][y1-1] != '#':
			l = True
			nBranch += 1
		if dir1 != 'L' and y1 < (col - 1) and fileLines[x1][y1+1] != '#':
			r = True
			nBranch += 1
		if nBranch == 1 and u == True:
			x1 -= 1
			dir1 = 'U'
			n += 1
		if nBranch == 1 and d == True:
			x1 += 1
			dir1 = 'D'
			n += 1
		if nBranch == 1 and l == True:
			y1 -= 1
			dir1 = 'L'
			n += 1
		if nBranch == 1 and r == True:
			y1 += 1
			dir1 = 'R'
			n += 1
		#print(str(nBranch)+str(dir1))
	if (x,y) not in paths:
		paths[(x,y)] = {}
	if dir0 not in paths[(x,y)]:
		if dir1 == 'U':
			dir2 = 'D'
		if dir1 == 'D':
			dir2 = 'U'
		if dir1 == 'L':
			dir2 = 'R'
		if dir1 == 'R':
			dir2 = 'L'
		paths[(x,y)][dir0] = [(x1,y1),dir1,n]
		if (x1,y1) not in paths:
			paths[(x1,y1)] = {}
		if dir0 == 'U':
			dir3 = 'D'
		if dir0 == 'D':
			dir3 = 'U'
		if dir0 == 'L':
			dir3 = 'R'
		if dir0 == 'R':
			dir3 = 'L'
		if dir2 not in paths[(x1,y1)]:
			paths[(x1,y1)][dir2] = [(x,y),dir3,n]
	if u == True and 'U' not in paths[(x1,y1)]:
		setPaths(x1,y1,'U')
	if d == True and 'D' not in paths[(x1,y1)]:
		setPaths(x1,y1,'D')
	if l == True and 'L' not in paths[(x1,y1)]:
		setPaths(x1,y1,'L')
	if r == True and 'R' not in paths[(x1,y1)]:
		setPaths(x1,y1,'R')

def step(x,y,dir1,step1,path):
	global maxSteps
	global pathsChecked
	if x == (row - 1):
		pathsChecked += 1
		if pathsChecked % 10000 == 0 or step1 > maxSteps:
			print(str(pathsChecked) + " paths checked")
		#print("goal reached in " + str(step1) + " steps")
		if step1 > maxSteps:
			maxSteps = step1
			print("new longest hike: " + str(maxSteps) + " steps")
		return
	if x > 0 and dir1 != 'D' and 'U' in paths[(x,y)] and paths[(x,y)]['U'][0] not in path:
		nextNode = paths[(x,y)]['U']
		path1 = path.copy()
		path1.add(nextNode[0])
		step(nextNode[0][0],nextNode[0][1],nextNode[1],step1+nextNode[2],path1)
	if x < (row - 1) and dir1 != 'U' and 'D' in paths[(x,y)] and paths[(x,y)]['D'][0] not in path:
		nextNode = paths[(x,y)]['D']
		path1 = path.copy()
		path1.add(nextNode[0])
		step(nextNode[0][0],nextNode[0][1],nextNode[1],step1+nextNode[2],path1)
	if y > 0 and dir1 != 'R' and 'L' in paths[(x,y)] and paths[(x,y)]['L'][0] not in path:
		nextNode = paths[(x,y)]['L']
		path1 = path.copy()
		path1.add(nextNode[0])
		step(nextNode[0][0],nextNode[0][1],nextNode[1],step1+nextNode[2],path1)
	if y < (col - 1) and dir1 != 'L' and 'R' in paths[(x,y)] and paths[(x,y)]['R'][0] not in path:
		nextNode = paths[(x,y)]['R']
		path1 = path.copy()
		path1.add(nextNode[0])
		step(nextNode[0][0],nextNode[0][1],nextNode[1],step1+nextNode[2],path1)

maxSteps = 0
trail = []
paths = {}
pathsChecked = 0
fileHandle = open("23.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["#.#####################","#.......#########...###","#######.#########.#.###","###.....#.>.>.###.#.###","###v#####.#v#.###.#.###","###.>...#.#.#.....#...#","###v###.#.#.#########.#","###...#.#.#.......#...#","#####.#.#.#######.#.###","#.....#.#.#.......#...#","#.#####.#.#.#########v#","#.#...#...#...###...>.#","#.#.#v#######v###.###v#","#...#.>.#...>.>.#.###.#","#####v#.#.###v#.#.###.#","#.....#...#...#.#.#...#","#.#########.###.#.#.###","#...###...#...#...#.###","###.###.#.###v#####v###","#...#...#.#.>.>.#.>.###","#.###.###.#.###.#.#v###","#.....###...###...#...#","#####################.#"]
row = len(fileLines)
col = len(fileLines[0])
for fileLine in fileLines:
	if len(fileLine) == 0:
		row -= 1
#print(str(row)+"x"+str(col))
sys.setrecursionlimit(row*col)
setPaths(0,1,'D')
for path in paths:
	print(str(path)+": "+str(paths[path]))
path0 = set()
path0.add((0,1))
step(0,1,'D',0,path0)
print(str(pathsChecked) + " paths checked")
print(maxSteps)
