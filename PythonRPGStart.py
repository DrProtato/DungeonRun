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
inventory = []
commands = open("commands.txt", "r")

def commandLoop():
    while True:
        response = str(input(""))
        responseTrue = response.lower()
        if responseTrue == "restart":
            inventory = []
            gameStart()
            return inventory
        elif responseTrue == "help":
            for line in commands:
                data = line.split(":")
                print(data[0] + " - " + data[1], end="")
            print("\n")
        elif responseTrue == "exit":
            exit()
        elif responseTrue == "break":
            print("break needs to be added")
        elif responseTrue == "open":
            print("open needs to be added.  with chests, there is a variable that is for when a chest is present, and if there is then the user opens chest & sets the variable of chest present to false and runs the weapon gen function")
        else:
            print("Sorry. I don't understand what you said.\n")

def gameStart():
    print("Welcome to the dungeon! \n")
    print("Type 'help' for a list of basic commands. \n")
    while True:
        response = str(input(""))
        responseTrue = response.lower()
        if (responseTrue == "start"):
            enterDungeon()
            break
        elif responseTrue == "help":
            for line in commands:
                data = line.split(":")
                print(data[0] + " - " + data[1], end="")
            print("\n")
        elif responseTrue == "exit":
            exit()
        else:
            print("Sorry. I don't understand what you said.\n")

    
def enterDungeon():
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
    doorNumber = int(input("Which door do you go through?\n\n"))
    enterRoom(roomCounter)

def enterRoom(roomNum):
    roomNum = roomNum + 1

    roomGeneration(roomNum)

    commandLoop()


def roomGeneration(roomNum):
    potAmount = 0
    if (roomNum % 10 == 0):
        generateBoss()
    else:
        numGen = random.randint(1, 100)
        if (numGen <= 10):
            generateChest()
        elif (numGen <= 70):
            print("generateMonster()")
        else:
            print("generateEmptyRoom()")

def itemAddedInventory(item, name):
    print("\nYou got a " + name + "!")
    inventory.append(item)
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

    #weaponGenned is the value returned from each function

gameStart()
