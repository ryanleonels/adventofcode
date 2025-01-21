#!/usr/bin/python3

def playerWin(playerStats, bossStats):
	(playerHP, playerDamage, playerArmor) = (playerStats[0], playerStats[1], playerStats[2])
	(bossHP, bossDamage, bossArmor) = (bossStats[0], bossStats[1], bossStats[2])
	playerToBoss = max(playerDamage - bossArmor, 1)
	bossToPlayer = max(bossDamage - playerArmor, 1)
	while True:
		# player attack
		bossHP -= playerToBoss
		if bossHP <= 0:
			return True
		# boss attack
		playerHP -= bossToPlayer
		if playerHP <= 0:
			return False

minCost = 999999999
weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)];
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)];
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)];
(nWeapon, nArmor, nRing) = (len(weapons), len(armors), len(rings))
(bossHP, bossDamage, bossArmor) = (0, 0, 0)
fileHandle = open("21.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine.split(': ')[0] == "Hit Points":
		bossHP = int(fileLine.split(': ')[1])
	if fileLine.split(': ')[0] == "Damage":
		bossDamage = int(fileLine.split(': ')[1])
	if fileLine.split(': ')[0] == "Armor":
		bossArmor = int(fileLine.split(': ')[1])
for weapon in range(0, nWeapon):
	for armor in range(-1, nArmor):
		for ring1 in range(-1, nRing):
			for ring2 in range(-1, nRing):
				if ring1 != ring2 or ring1 == -1:
					cost = 0
					(playerHP, playerDamage, playerArmor) = (100, 0, 0)
					if weapon != -1:
						cost += weapons[weapon][0]
						playerDamage += weapons[weapon][1]
						playerArmor += weapons[weapon][2]
					if armor != -1:
						cost += armors[armor][0]
						playerDamage += armors[armor][1]
						playerArmor += armors[armor][2]
					if ring1 != -1:
						cost += rings[ring1][0]
						playerDamage += rings[ring1][1]
						playerArmor += rings[ring1][2]
					if ring2 != -1:
						cost += rings[ring2][0]
						playerDamage += rings[ring2][1]
						playerArmor += rings[ring2][2]
					if playerWin((playerHP, playerDamage, playerArmor), (bossHP, bossDamage, bossArmor)):
						minCost = min(cost, minCost)
print(minCost)