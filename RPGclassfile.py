import random
import sys
import math

class sword:
    __swordName = ""
    __swordDamageFactor = 1.2
    __swordRangeFactor = 0.5
    __swordDamageType = "physical"
    __bowDamageFinal = 0.0
    __bowRangeFinal = 0.0

    def __init__(self, name, damagefactor, rangefactor, damagetype):
        self.__swordName = name
        self.__swordDamageFactor = damagefactor
        self.__swordRangeFactor = rangefactor
        self.__swordDamageType = damagetype

    def generateSwordDamage(self, damagefactor):
        damage = math.floor(damagefactor * (roomCounter / (2 + roomCounter/2)))
        return damage

    def swordName(self, name):
        return name

class bow:
    __bowName = ""
    __bowDamageFactor = 0.8
    __bowRangeFactor = 1.5
    __bowDamageType = "piercing"
    __bowDamageFinal = 0.0
    __bowRangeFinal = 0.0

    def __init__(self, name, damagefactor, rangefactor, damagetype):
        self.__bowName = name
        self.__bowDamageFactor = damagefactor
        self.__bowRangeFactor = rangefactor
        self.__bowDamageType = damagetype

    def generateBowDamage(self, damagefactor):
        damage = math.floor(damagefactor * (roomCounter / (2 + roomCounter/2)))
        return damage

    def bowName(self, name):
        return name

class staff:
    __staffDamageFactor = 1.0
    __staffRangeFactor = 1.0
    __staffDamageType = "magic"

class dust:
    __dustName = ""

    def __init__(self, name):
        self.__dustName = name

class weapon:
    __weaponType = ""
    __weaponDamage = 0
    __weaponRange = 0
    __weaponElement = ""

    def __init__(self, typie, damage, rangef, element):
        self.__weaponType = typie
        self.__weaponDamage = damage
        self.__weaponRange = rangef
        self.__weaponElement = element
    
weaponTypes = ["sword", "bow", "staff"]

class slime:
    __slimeHealthBase = 3
    __slimeHealthFactor = 1
    __slimeDamageBase = 1
    __slimeDamageFactor = 1
    __slimeWeakness = "magic"

    def __init__(self):
        self.__slimeHealthBase = healthBase
        self.__slimeHealthFactor = healthFactor
        self.__slimeDamageBase = damageBase
        self.__slimeDamageFactor = damageFactor
        self.__slimeWeakness = weakness

    def generateSlime(self, healthBase, healthFactor, damageBase, damageFactor, roomCounter):
        healthFinal = healthBase + (roomCounter * healthFactor)
        damageFinal = damageBase + (roomCounter * damageFactor)

        return healthFinal, damageFinal


class skeleton:
    __skeletonHealthBase = 1
    __skeletonHealthFactor = 1
    __skeletonDamageBase = 1
    __skeletonDamageFactor = 1
    __skeletonWeakness = "piecing"

class troll:
    __trollHealthBase = 1
    __trollHealthFactor = 1
    __trollDamageBase = 1
    __trollDamageFactor = 1
    __trollWeakness = "physical"

class room:
    __roomIsBoss = False
    __roomPotAmount = 0
    __roomHasMonster = False
    __roomHasChest = False

    def __init__(self, potAmount, hasChest, hasMonster, isBoss):
        self.__roomPotAmount = potAmount
        self.__roomHasChest = hasChest
        self.__roomHasMonster = hasMonster
        self.__roomIsBoss = isBoss

    def generateEmptyRoom(self):
        potAmount = random.randint(0, 5)
        return potAmount

    def generateMonsterRoom(self):
        monsterGenned = random.randint(0, 2)
        if monsterGenned == 0:
            generateSlime(1, 1, 1, 1, roomCounter)
        elif monsterGenned == 1:
            generateSkeleton()
        elif monsterGenned == 2:
            generateTroll()
        else:
            print("An anthropomorphic battle toaster has appeared")

    def listRoomMonster(self, monster):
        return monster
    def listRoomChest(self, chest):
        return chest
    def listRoomBoss(self, boss):
        return boss

    #def createMonsterRoom(self, potAmount):


