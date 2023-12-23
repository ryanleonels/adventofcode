#!/usr/bin/python3

import sys

def step(x,y,dir1,step1,path):
	global maxSteps
	if x == (row - 1):
		print("goal reached in " + str(step1) + " steps")
		if step1 > maxSteps:
			maxSteps = step1
			print("new longest hike: " + str(maxSteps) + " steps")
		return
	if x > 0 and dir1 != 'D' and fileLines[x-1][y] != '#' and (x-1,y) not in path:
		path1 = path.copy()
		path1.add((x-1,y))
		step(x-1,y,'U',step1+1,path1)
	if x < (row - 1) and dir1 != 'U' and fileLines[x+1][y] != '#' and (x+1,y) not in path:
		path1 = path.copy()
		path1.add((x+1,y))
		step(x+1,y,'D',step1+1,path1)
	if y > 0 and dir1 != 'R' and fileLines[x][y-1] != '#' and (x,y-1) not in path:
		path1 = path.copy()
		path1.add((x,y-1))
		step(x,y-1,'L',step1+1,path1)
	if y < (col - 1) and dir1 != 'L' and fileLines[x][y+1] != '#' and (x,y+1) not in path:
		path1 = path.copy()
		path1.add((x,y+1))
		step(x,y+1,'R',step1+1,path1)

maxSteps = 0
trail = []
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
path0 = set()
path0.add((0,1))
step(0,1,'D',0,path0)
print(maxSteps)
