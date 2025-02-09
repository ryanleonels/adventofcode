#!/usr/local/bin/python3

fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
data = fileData.strip()

def decompress(dataStr):
	result = ""
	n = len(dataStr)
	pos = 0
	markerState = 0
	(seqLength, seqTimes, seqStart) = (0, 0, 0)
	curNum = ""
	sequence = ""
	while pos < n:
		ch = dataStr[pos]
		match markerState:
			case 0: # not in sequence
				if ch == '(':
					markerState = 1
					curNum = ""
				else:
					result += ch
			case 1: # sequence length
				if ch == 'x':
					markerState = 2
					seqLength = int(curNum)
					curNum = ""
				else:
					curNum += ch
			case 2: # sequence times
				if ch == ')':
					markerState = 0
					seqTimes = int(curNum)
					seqStart = pos + 1
					sequence = dataStr[seqStart:seqStart+seqLength]
					for i in range(0, seqTimes):
						result += sequence
					pos += seqLength
				else:
					curNum += ch
		pos += 1
	return result

output = decompress(data)
print(len(output))