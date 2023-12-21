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
steps = 26501365
n = row
n2 = steps % row #happens to be = int(n / 2) in the test case
diff0 = []
diff1 = []
diff2 = []
plots = set()
plots.add((rowStart,colStart))
i = 0
diffsComplete = False
while diffsComplete == False:
	plots1 = set()
	for plot in plots:
		if fileLines[(plot[0]-1)%n][plot[1]%n] != '#' and (plot[0]-1,plot[1]) not in plots1:
			plots1.add((plot[0]-1,plot[1]))
		if fileLines[(plot[0]+1)%n][plot[1]%n] != '#' and (plot[0]+1,plot[1]) not in plots1:
			plots1.add((plot[0]+1,plot[1]))
		if fileLines[plot[0]%n][(plot[1]-1)%n] != '#' and (plot[0],plot[1]-1) not in plots1:
			plots1.add((plot[0],plot[1]-1))
		if fileLines[plot[0]%n][(plot[1]+1)%n] != '#' and (plot[0],plot[1]+1) not in plots1:
			plots1.add((plot[0],plot[1]+1))
	i += 1
	plots = plots1
	print("steps="+str(i)+", plots="+str(len(plots)))
	if i == steps:
		diffsComplete = True
		print(len(plots))
		exit(0)
	if i % n == n2:
		diff0.append(len(plots))
		if len(diff0) > 1:
			diff1.append(diff0[-1]-diff0[-2])
		if len(diff1) > 1:
			diff2.append(diff1[-1]-diff1[-2])
		print(diff0)
		print(diff1)
		print(diff2)
		if len(diff2) > 1:
			if diff2[-1] == diff2[-2]:
				diffsComplete = True
nPlots = diff0[-1]
nPlots1 = diff1[-1]
nPlots2 = diff2[-1]
while i < steps:
	nPlots1 += nPlots2
	nPlots += nPlots1
	i += n
print(nPlots)
