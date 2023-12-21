#!/usr/bin/python3

nPlots = 0
modules = {}
pulses = {}
pulses1 = {}
fileHandle = open("21.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["...........",".....###.#.",".###.##..#.","..#.#...#..","....#.#....",".##..S####.",".##..#...#.",".......##..",".##.#.####.",".##..##.##.","..........."]
row = len(fileLines)
col = len(fileLines[0])
for fileLine in fileLines:
	if len(fileLine) == 0:
		row -= 1
print((row,col))
rowStart = -1
colStart = -1
for i in range(0, row):
	if fileLines[i].find('S') != -1:
		rowStart = i
		colStart = fileLines[i].find('S')
print((rowStart,colStart))
steps = 64
plots = set()
plots.add((rowStart,colStart))
for i in range(0, steps):
	plots1 = set()
	for plot in plots:
		if plot[0] > 0 and fileLines[plot[0]-1][plot[1]] != '#' and (plot[0]-1,plot[1]) not in plots1:
			plots1.add((plot[0]-1,plot[1]))
		if plot[0] < row-1 and fileLines[plot[0]+1][plot[1]] != '#' and (plot[0]+1,plot[1]) not in plots1:
			plots1.add((plot[0]+1,plot[1]))
		if plot[1] > 0 and fileLines[plot[0]][plot[1]-1] != '#' and (plot[0],plot[1]-1) not in plots1:
			plots1.add((plot[0],plot[1]-1))
		if plot[1] < col-1 and fileLines[plot[0]][plot[1]+1] != '#' and (plot[0],plot[1]+1) not in plots1:
			plots1.add((plot[0],plot[1]+1))
	plots = plots1
	print("steps="+str(i+1)+", plots="+str(len(plots)))
nPlots = len(plots)
print(nPlots)
