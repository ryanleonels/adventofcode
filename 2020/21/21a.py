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
allergensList = {}
allergensListFinal = {}
nAllergen = 0
for allergen in sorted(allergensDict):
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
	#print(foods2)
	allergensList[allergen] = foods2
	nAllergen += 1
	#print(allergen, foods2)

n2 = 0
while n2 < nAllergen:
	deleteList = []
	finalizeList = []
	for allergen in allergensList:
		if len(allergensList[allergen]) == 0:
			deleteList.append(allergen)
		if len(allergensList[allergen]) == 1:
			finalizeList.append(allergen)
	for allergen in deleteList:
		del allergensList[allergen]
	for allergen in finalizeList:
		ingredient = ""
		for ingredient1 in allergensList[allergen]:
			ingredient = ingredient1
		#print(allergen, ingredient)
		allergensListFinal[allergen] = ingredient
		n2 += 1
		for allergen1 in allergensList:
			if ingredient in allergensList[allergen1]:
				allergenList = allergensList[allergen1]
				allergenList.remove(ingredient)
				allergensList[allergen1] = allergenList

#print(allergensListFinal)
ingredientList = ""
for allergen in sorted(allergensListFinal):
	if ingredientList != "":
		ingredientList += ","
	ingredientList += allergensListFinal[allergen]
print(ingredientList)
