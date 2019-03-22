import random
import math
import time
from RPGclassfile import bow
from RPGclassfile import sword
from RPGclassfile import staff
from RPGclassfile import weapon
from RPGclassfile import slime
from RPGclassfile import skeleton
from RPGclassfile import troll
from RPGclassfile import dust
from RPGclassfile import room

roomCounter = 0
inventoryItems = []
inventoryNames = []
commands = open("commands.txt", "r")
roomList = []
responseTrue = []


def commandLoop(inventoryNames, roomContents, roomCounter, contents, rList):

    while True:
        response = str(input(""))
        response = response.lower()
        response = response.strip()
        responseTrue = response.rstrip()

        '''        responseTrue.append(response.split(" "))
        for i in responseTrue:
            word = responseTrue[i]
            print(word)'''
        if responseTrue == "restart":
            inventoryItems = []
            inventoryNames = []
            gameStart(roomList)
            return inventoryItems, inventoryNames
        elif responseTrue == "help":
            for line in commands:
                data = line.split(":")
                print(data[0] + " - " + data[1], end="")
            print("")
            print("----------------")
        elif responseTrue == "exit":
            exit()
        elif responseTrue == "break":
            print("break needs to be added")
        elif responseTrue == "open":
            print("open needs to be added.  with chests, there is a variable that is for when a chest is present, and if there is then the user opens chest & sets the variable of chest present to false and runs the weapon gen function")
        elif responseTrue == "look":
            for i in range(len(contents)):
                print(str(contents[i]) + ", ", end="")
        elif responseTrue == "inventory":
            for i in range(len(inventoryNames)):
                print(inventoryNames[i] + ", ", end="")
            print("")
            print("----------------")

        else:
            print("Sorry. I don't understand what you said.\n")


def gameStart(roomList):
    print("\nWelcome to the dungeon! \n")
    print("Type 'help' for a list of basic commands.")
    print("")
    while True:
        response = str(input(""))
        responseTrue = response.lower()
        if (responseTrue == "start"):
            enterDungeon(roomList)
            break
        elif responseTrue == "help":
            for line in commands:
                data = line.split(":")
                print(data[0] + " - " + data[1], end="")
            print("")
            print("----------------")
        elif responseTrue == "exit":
            exit()
        else:
            print("Sorry. I don't understand what you said.\n")


def enterDungeon(roomList):
    print("\nYou start your descent into the dungeon. \n")
    print("Along your way you see some weapons on the wall, so you decide to take one. \n")
    weaponChoiceTemp = str(input("There is a sword, a bow and a staff.  Which one do you take? \n"))
    weaponChoice = weaponChoiceTemp.lower()
    print("\nYou picked up the " + weaponChoice + ".")
    generateWeapon(weaponChoice)
    print("\nYou walk further down the steps until you see a door.")
    print("You open the door and are greeted with an empty room.")
    print("You take a couple of steps before you hear the door behind you close and lock.")
    print("You can only go forward from here.\n")
    print("You can see 3 doors that lead out of the room.  They are labeled 1, 2 and 3.\n")
    while True:
        doorNumber = int(input("Which door do you go through?\n\n"))
        if (doorNumber >= 1 and doorNumber <= 3):
            enterRoom(doorNumber, roomList)
            break
        else:
            print("You walked into a wall")
            print("You hear laughing in the distance")
            print("")


def itemAddedInventory(item, name):
    print("\nYou got a " + name + "!")
    inventoryItems.append(item)
    inventoryNames.append(name)
    #append item to inventory

def generateWeapon(weaponchoice):
    if weaponchoice == "sword":
        name = "Sword Lv" + str(roomCounter)
        weapongenned = sword(name, 1.2, 0.5, "piercing")
        swordname = weapongenned.swordName(name)
        itemAddedInventory(weapongenned, swordname)
    elif weaponchoice == "bow":
        name = "Bow Lv" + str(roomCounter)
        weapongenned = bow(name, 0.8, 1.5, "piercing")
        bowname = weapongenned.bowName(name)
        itemAddedInventory(weapongenned, bowname)
        #needs to append weapon to inventory and also give name to say that its been added
    elif weaponchoice == "staff":
        generateStaff()
    else:
        name = "dust"
        weapongenned = dust(name)
        itemAddedInventory(weapongenned, name)

def enterRoom(roomNum, roomList):
    print("You push the door open, hearing it creak as it echoes into the new room")
    roomCounter = roomNum + 1
    if roomCounter == 1 or roomCounter == 4 or roomCounter == 6:
        contents, rList = createRoom(False, False, False, roomList)
    elif roomCounter == 2 or roomCounter == 5 or roomCounter == 7 or roomCounter == 8:
        contents, rList = createRoom(False, True, False, roomList)
    elif roomCounter == 3 or roomCounter == 9:
        contents, rList = createRoom(True,  False, False, roomList)
    else:
        contents, rList = createRoom(False, False, True, roomList)

    commandLoop(inventoryNames, roomList, roomNum, contents, rList)
    return roomCounter

def createRoom(hasChest, hasMonster, isBoss, roomList):
    potAmount = random.randint(0, 5)
    roomGenned = room(potAmount, hasChest, hasMonster, isBoss)
    roomContents = [roomGenned.listRoomBoss(isBoss), roomGenned.listRoomMonster(hasMonster), roomGenned.listRoomChest(hasChest), potAmount]
    roomList.append(roomGenned)
    return roomContents, roomList

gameStart(roomList)
