#!/usr/bin/python3

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
fs = {}
cmd = ""
curDir = ""
fsDir = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if cmd == "" and fileLine[0] == "$" and curDir != "": # ls done, write fsDir to fs
		fs[curDir] = fsDir
	cmd = ""
	if fileLine[:5] == "$ cd ":
		cmd = "cd"
		dir1 = fileLine[5:]
		if dir1 == "/":
			curDir = "/"
		if dir1 == "..":
			curDir = '/'.join(curDir.split('/')[:-1])
			if curDir == "":
				curDir = "/"
		if dir1 != "/" and dir1 != "..":
			if curDir != "/":
				curDir += "/"
			curDir += dir1
		#print(curDir)
	if fileLine[:4] == "$ ls":
		cmd = "ls"
		fsDir = {}
	if cmd == "":
		(size, name) = fileLine.split(' ')
		if size == "dir":
			size = 0
		else:
			size = int(size)
		fsDir[name] = size
if len(fsDir) > 0:
	fs[curDir] = fsDir
#for dir1 in fs:
	#print(dir1, fs[dir1])

def getSize(dir1):
	if dir1 not in fs:
		return 0
	fsDir = fs[dir1]
	size = 0
	for file in fsDir:
		if fsDir[file] == 0:
			dir2 = dir1
			if dir1 != "/":
				dir2 += "/"
			dir2 += file
			size += getSize(dir2)
		else:
			size += fsDir[file]
	return size

totalSize = 0
for dir1 in fs:
	curSize = getSize(dir1)
	#print(dir1, curSize)
	if curSize <= 100000:
		totalSize += curSize
print(totalSize)
