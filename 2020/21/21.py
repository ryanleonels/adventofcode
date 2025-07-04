#!/usr/bin/python3

sum1 = 0
fileHandle = open("21.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

foods = [] # foods[n] = ingredients present in n-th food
allergens = [] # allergens[n] = known allergens in n-th food
foodsDict = {} # foodsDict[x] = food ids where ingredient x is present
allergensDict = {} # allergensDict[x] = food ids where allergen x is known to present
n = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	foods1 = set()
	allergens1 = set()
	for food in fileLine.split(' (')[0].split(' '):
		foods1.add(food)
		food1 = []
		if food in foodsDict:
			food1 = foodsDict[food]
		food1.append(n)
		foodsDict[food] = food1
	if " (contains" in fileLine:
		for allergen in fileLine.split(' (contains ')[1].split(')')[0].split(', '):
			allergens1.add(allergen)
			allergen1 = []
			if allergen in allergensDict:
				allergen1 = allergensDict[allergen]
			allergen1.append(n)
			allergensDict[allergen] = allergen1
	foods.append(foods1)
	allergens.append(allergens1)
	n += 1

#for food in foodsDict:
	#print(food, foodsDict[food])
#print("---")
allergenic = set()
for allergen in allergensDict:
	#print(allergen, allergensDict[allergen])
	allergenFoods = allergensDict[allergen]
	n1 = len(allergenFoods)
	foods1 = foods[allergenFoods[0]]
	#print(foods1)
	foods2 = set()
	for food in foods1:
		presentInAll = True
		for i in range(1, n1):
			if food not in foods[allergenFoods[i]]:
				presentInAll = False
				break
		if presentInAll:
			foods2.add(food)
			allergenic.add(food)
	#print(foods2)

cnt = 0
for i in range(0, n):
	for food in foods[i]:
		if food not in allergenic:
			cnt += 1
print(cnt)
