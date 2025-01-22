#!/usr/bin/python3

globalmin = 999999999

def leastMana(playerStats, spellTimers, bossStats, playerTurn, spentMana, skillsSoFar):
	global globalmin
	(playerHP, playerArmor, playerMana) = (playerStats[0], playerStats[1], playerStats[2])
	(shieldTimer, poisonTimer, rechargeTimer) = (spellTimers[0], spellTimers[1], spellTimers[2])
	(bossHP, bossDamage) = (bossStats[0], bossStats[1])
	if spentMana > globalmin: #not optimal
		return 999999999
	# hard difficulty (poisoned)
	if playerTurn == True:
		playerHP -= 1
		if playerHP <= 0: #player dead = lose
			return 999999999
	# current shield
	if shieldTimer > 0:
		shieldTimer -= 1
		if shieldTimer == 0:
			playerArmor -= 7
	#current poison
	if poisonTimer > 0:
		bossHP -= 3
		poisonTimer -= 1
		if bossHP <= 0: #boss dead = win
			globalmin = min(globalmin, spentMana)
			print(spentMana, globalmin, "poison", skillsSoFar)
			return spentMana
	#current recharge
	if rechargeTimer > 0:
		playerMana += 101
		rechargeTimer -= 1
	if playerTurn == True: #player turn
		canCastSpell = False
		minMana = 999999999
		skills = []
		for skill in skillsSoFar:
			skills.append(skill)
		skills.append("")
		#Magic Missile
		if playerMana >= 53:
			canCastSpell = True
			skills[-1] = "Magic Missile"
			if bossHP <= 4: #boss dead on spell = win
				curMana = spentMana + 53
				globalmin = min(globalmin, curMana)
				print(curMana, globalmin, "missile", skills)
			else:
				curMana = leastMana((playerHP, playerArmor, playerMana - 53), (shieldTimer, poisonTimer, rechargeTimer), (bossHP - 4, bossDamage), False, spentMana + 53, skills)
			minMana = min(curMana, minMana)
		#Drain
		if playerMana >= 73:
			canCastSpell = True
			skills[-1] = "Drain"
			if bossHP <= 2: #boss dead on spell = win
				curMana = spentMana + 73
				globalmin = min(globalmin, curMana)
				print(curMana, globalmin, "drain", skills)
			else:
				curMana = leastMana((playerHP + 2, playerArmor, playerMana - 73), (shieldTimer, poisonTimer, rechargeTimer), (bossHP - 2, bossDamage), False, spentMana + 73, skills)
			minMana = min(curMana, minMana)
		#Shield
		if playerMana >= 113 and shieldTimer == 0:
			canCastSpell = True
			skills[-1] = "Shield"
			#next turn if cast shield
			curMana = leastMana((playerHP, playerArmor + 7, playerMana - 113), (6, poisonTimer, rechargeTimer), (bossHP, bossDamage), False, spentMana + 113, skills)
			minMana = min(curMana, minMana)
		#Poison
		if playerMana >= 173 and poisonTimer == 0:
			canCastSpell = True
			skills[-1] = "Poison"
			#next turn if cast poison
			curMana = leastMana((playerHP, playerArmor, playerMana - 173), (shieldTimer, 6, rechargeTimer), (bossHP, bossDamage), False, spentMana + 173, skills)
			minMana = min(curMana, minMana)
		#Recharge
		if playerMana >= 229 and rechargeTimer == 0:
			canCastSpell = True
			skills[-1] = "Recharge"
			#next turn if cast recharge
			curMana = leastMana((playerHP, playerArmor, playerMana - 229), (shieldTimer, poisonTimer, 5), (bossHP, bossDamage), False, spentMana + 229, skills)
			minMana = min(curMana, minMana)
		#if cannot cast spell, you lose
		if canCastSpell == False:
			return 999999999
		return minMana
	if playerTurn == False: #boss turn
		bossToPlayer = max(bossDamage - playerArmor, 1)
		playerHP -= bossToPlayer
		if playerHP <= 0: #player dead = lose
			return 999999999
		#else player next turn
		return leastMana((playerHP, playerArmor, playerMana), (shieldTimer, poisonTimer, rechargeTimer), (bossHP, bossDamage), True, spentMana, skillsSoFar)

(playerHP, playerArmor, playerMana) = (50, 0, 500)
(shieldTimer, poisonTimer, rechargeTimer) = (0, 0, 0)
(bossHP, bossDamage) = (0, 0)
fileHandle = open("22.in", "r")
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
print(leastMana((playerHP, playerArmor, playerMana), (shieldTimer, poisonTimer, rechargeTimer), (bossHP, bossDamage), True, 0, []))