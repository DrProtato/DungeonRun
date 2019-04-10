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
swordNames = open("swordnames.txt", "r")
bowNames = open("bownames.txt", "r")
staffNames = open("staffnames.txt", "r")
roomList = []
responseTrue = []
equippedWeapon = {}

def commandLoop(inventoryNames, roomContents, roomCounter, contents, rList, equippedWeapon):

    while True:
        response = str(input(""))
        response = response.lower()
        response = response.strip()
        responseTrue = response.rstrip()
        repsonseList = responseTrue.split(" ")
        if repsonseList[0] == "help":
            commands = open("commands.txt", "r")
            printLine()
            for line in commands:
                data = line.split(":")
                print(data[0] + " - " + data[1], end="")
            print("")
            printLine()
        elif repsonseList[0] == "exit":
            exit()
        elif repsonseList[0] == "break":
            printLine()
            print("You started breaking the pots\n")
            i = 0
            while i < contents[3]:
                gennedNum = random.randint(0, 100)
                print("You broke a pot.")
                if gennedNum <= 20:
                    itemAddedInventory("potion", "potion")
                else:
                    print("You got nothing.\n")
                contents[3] = contents[3] - 1
            printLine()
        elif repsonseList[0] == "open":
            if repsonseList[1] == "door":
                roomNum = int(repsonseList[2])
                if roomNum == roomCounter - 1 or roomNum == roomCounter + 1:
                    roomCounter = roomNum
                    enterRoom(roomCounter, roomList)
                else:
                    printLine()
                    print("Sorry that isn't possible.")
                    printLine()
                #returns room counter and puts player in the room equal to counter
            elif repsonseList[1] == "chest":
                if contents[2] == True:
                    createWeapon()
                    contents[2] = False
                else: 
                    print("There is no chest in this room.")
                #change chest present from true to false
        elif repsonseList[0] == "look":
            printLine()
            print("You are in room " + str(roomCounter) + ".")
            i = 0
            boolin = True
            while boolin == True:
                if i < 3:
                    while i < 3:
                        if i == 0 and contents[i] is True:
                            print("You look to see a hulking monster, larger than the average.  You realise that it is a boss.")
                            #print(boss monster type + " Boss")
                            printLine()
                            boolin = False
                            break
                        elif i == 1 and contents[i] is True:
                            #print("There is a " + monsterGennedType)
                            print("A monster is in this room")
                            if roomCounter - 1 == 0:
                                print("There is one door, labelled " + str(roomCounter + 1))
                            else:
                                print("There are two doors, labelled " + str(roomCounter - 1) + " and " + str(roomCounter + 1))
                            boolin = False
                            if contents[3] == 1:
                                print("There is also " + str(contents[3]) + " pot.")
                                printLine()
                                break
                            elif contents[3] != 0:
                                print("There are also " + str(contents[3]) + " pots.")
                                printLine()
                                break
                            else:
                                break
                            break
                        elif i == 2 and contents[i] is True:
                            print("There is a chest in the room.")
                            if roomCounter - 1 == 0:
                                print("There is one door, labelled " + str(roomCounter + 1))
                            else:
                                print("There are two doors, labelled " + str(roomCounter - 1) + " and " + str(
                                    roomCounter + 1))
                            boolin = False
                            if contents[3] == 1:
                                print("There is also " + str(contents[3]) + " pot.")
                                printLine()
                                break
                            elif contents[3] != 0:
                                print("There are also " + str(contents[3]) + " pots.")
                                printLine()
                                break
                            else:
                                break
                            break
                        else:
                            i = i + 1
                else:
                    print("You see nothing of interest in the room.")
                    if roomCounter - 1 == 0:
                        print("There is one door, labelled " + str(roomCounter + 1))
                    else:
                        print("There are two doors, labelled " + str(roomCounter - 1) + " and " + str(roomCounter + 1))
                    if contents[3] == 1:
                        print("There is also " + str(contents[3]) + " pot.")
                        printLine()
                        break
                    elif contents[3] != 0:
                        print("There are also " + str(contents[3]) + " pots.")
                        printLine()
                        break
                    else:
                        break
                    break

        elif repsonseList[0] == "inventory":
            printLine()
            for i in range(len(inventoryNames)):
                print(inventoryNames[i] + " | ", end="")
            print("")
            printLine()

        else:
            printLine()
            print("Sorry. I don't understand what you said.")
            printLine()

def printLine():
    print("------------------------------------------------------------------------------------------------")

def gameStart(roomList):
    printLine()
    print("Welcome to the dungeon! \n")
    print("Type 'start' to enter the dungeon, or 'help' for a list of basic commands.")
    printLine()
    while True:
        response = str(input(""))
        responseTrue = response.lower()
        if (responseTrue == "start"):
            enterDungeon(roomList)
            break
        elif responseTrue == "help":
            commands = open("commands.txt", "r")
            printLine()
            for line in commands:
                data = line.split(":")
                print(data[0] + " - " + data[1], end="")
            print("")
            printLine()
        elif responseTrue == "exit":
            exit()
        else:
            printLine()
            print("Sorry. I don't understand what you said.")
            printLine()

def enterDungeon(roomList):
    printLine()
    print("You start your descent into the dungeon. \n")
    print("Along your way you see some weapons on the wall, so you decide to take one. \n")
    print("There is a sword, a bow and a staff.  Which one do you take?")
    printLine()
    weaponChoiceTemp = str(input(""))
    weaponChoiceTemp2 = weaponChoiceTemp.lower()
    weaponChoice = weaponChoiceTemp2.split(" ")
    bool = True
    j = 0
    while bool == True:
        if j < len(weaponChoice):
            for i in weaponChoice:
                if i == "sword":
                    printLine()
                    print("You picked up the sword.")
                    generateWeapon(i)
                    bool = False
                elif i == "bow":
                    printLine()
                    print("You picked up the bow.")
                    generateWeapon(i)
                    bool = False
                elif i == "staff":
                    printLine()
                    print("You picked up the staff.")
                    generateWeapon(i)
                    bool = False
                j = j +1

        else:
            printLine()
            print("In your confusion, you picked up some dust off the ground.")
            generateWeapon(dust)
            bool = False

    print("You walk further down the steps until you see a door.")
    print("You open the door and are greeted with an empty room.")
    print("You take a couple of steps before you hear the door behind you close and lock.")
    print("You can only go forward from here.\n")
    print("You can see 3 doors that lead out of the room.  They are labeled 1, 2 and 3.\n")
    print("Which door do you go through?")
    printLine()
    while True:
        doorNumberTemp = input("")
        doorNumber = doorNumberTemp.split(" ")
        j = 0
        for i in doorNumber:
            if j < len(doorNumber):
                if i == "1":
                    enterRoom(1, roomList)
                    break
                elif i == "2":
                    enterRoom(2, roomList)
                    break
                elif i == "3":
                    enterRoom(3, roomList)
                    break
                j = j + 1
            else:
                print("You walked into a wall")
                print("You hear laughing in the distance")
                print("")

def itemAddedInventory(item, name):
    printLine()
    print("You got a " + name + "!")
    printLine()
    inventoryItems.append(item)
    inventoryNames.append(name)
    #append item to inventory

def generateWeapon(weaponchoice):
    j = 0
    if weaponchoice == "sword":
        indexNum = random.randint(0, 19)
        for i in swordNames:
            if j == indexNum:
                nameGenned = i.strip("\n")
                name = nameGenned + " Lv" + str(roomCounter)
                weapongenned = sword(name, 1.2, 0.5, "physcical")
                swordname = weapongenned.swordName(name)
                itemAddedInventory(weapongenned, swordname)
            j = j + 1

    elif weaponchoice == "bow":
        indexNum = random.randint(0, 19)
        for i in bowNames:
            if j == indexNum:
                nameGenned = i.strip("\n")
                name = nameGenned + " Lv" + str(roomCounter)
                weapongenned = bow(name, 0.8, 1.5, "piercing")
                bowname = weapongenned.bowName(name)
                itemAddedInventory(weapongenned, bowname)
            j = j + 1
    elif weaponchoice == "staff":
        indexNum = random.randint(0, 19)
        for i in staffNames:
            if j == indexNum:
                nameGenned = i.strip("\n")
                name = nameGenned + " Lv" + str(roomCounter)
                weapongenned = staff(name, 1, 1, "magic")
                staffname = weapongenned.staffName(name)
                itemAddedInventory(weapongenned, staffname)
            j = j + 1
    else:
        name = "pile of dust"
        weapongenned = dust(name)
        itemAddedInventory(weapongenned, name)

def createWeapon():
    weaponchoice = random.randint(0,4)
    j = 0
    if weaponchoice == 1:
        indexNum = random.randint(0, 19)
        for i in swordNames:
            if j == indexNum:
                nameGenned = i.strip("\n")
                name = nameGenned + " Lv" + str(roomCounter)
                weapongenned = sword(name, 1.2, 0.5, "physcical")
                swordname = weapongenned.swordName(name)
                itemAddedInventory(weapongenned, swordname)
            j = j + 1

    elif weaponchoice == 2:
        indexNum = random.randint(0, 19)
        for i in bowNames:
            if j == indexNum:
                nameGenned = i.strip("\n")
                name = nameGenned + " Lv" + str(roomCounter)
                weapongenned = bow(name, 0.8, 1.5, "piercing")
                bowname = weapongenned.bowName(name)
                itemAddedInventory(weapongenned, bowname)
            j = j + 1
    elif weaponchoice == 3:
        indexNum = random.randint(0, 19)
        for i in staffNames:
            if j == indexNum:
                nameGenned = i.strip("\n")
                name = nameGenned + " Lv" + str(roomCounter)
                weapongenned = staff(name, 1, 1, "magic")
                staffname = weapongenned.staffName(name)
                itemAddedInventory(weapongenned, staffname)
            j = j + 1
    else:
        name = "pile of dust"
        weapongenned = dust(name)
        itemAddedInventory(weapongenned, name)

def enterRoom(roomNum, roomList):
    printLine()
    print("You push the door open, hearing it creak as it echoes into the new room")
    printLine()
    roomCounter = roomNum
    if roomCounter == 1 or roomCounter == 4 or roomCounter == 6:
        contents, rList = createRoom(False, False, False, roomList)
    elif roomCounter == 2 or roomCounter == 5 or roomCounter == 7 or roomCounter == 8:
        contents, rList = createRoom(False, True, False, roomList)
    elif roomCounter == 3 or roomCounter == 9:
        contents, rList = createRoom(False,  False, True, roomList)
    elif roomCounter == 10:
        contents, rList = createRoom(True, False, False, roomList)
    else:
        print("it didnt work")

    commandLoop(inventoryNames, roomList, roomNum, contents, rList, equippedWeapon)
    return roomCounter

def createRoom(isBoss, hasMonster, hasChest, roomList):
    potAmount = random.randint(0, 5)
    roomGenned = room(isBoss, hasMonster, hasChest, potAmount)
    roomContents = [roomGenned.listRoomBoss(isBoss), roomGenned.listRoomMonster(hasMonster), roomGenned.listRoomChest(hasChest), potAmount]
    roomList.append(roomGenned)
    return roomContents, roomList

gameStart(roomList)
