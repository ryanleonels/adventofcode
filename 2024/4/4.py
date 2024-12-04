#!/usr/bin/python3

n = 0
word = "XMAS"
fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
grid = fileData.split('\n')
row = len(grid) - 1
col = len(grid[0])
len1 = len(word)
for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] == word[0]:
			if i >= len1 - 1 and j >= len1 - 1:
				isWord = True
				for k in range(1, len1):
					if grid[i - k][j - k] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
			if i >= len1 - 1:
				isWord = True
				for k in range(1, len1):
					if grid[i - k][j] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
			if i >= len1 - 1 and j <= col - len1:
				isWord = True
				for k in range(1, len1):
					if grid[i - k][j + k] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
			if j >= len1 - 1:
				isWord = True
				for k in range(1, len1):
					if grid[i][j - k] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
			if j <= col - len1:
				isWord = True
				for k in range(1, len1):
					if grid[i][j + k] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
			if i <= row - len1 and j >= len1 - 1:
				isWord = True
				for k in range(1, len1):
					if grid[i + k][j - k] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
			if i <= row - len1:
				isWord = True
				for k in range(1, len1):
					if grid[i + k][j] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
			if i <= row - len1 and j <= col - len1:
				isWord = True
				for k in range(1, len1):
					if grid[i + k][j + k] != word[k]:
						isWord = False
						break
				if isWord == True:
					n += 1
print(n)