import os
import random
import sys

platform = sys.platform

clear = lambda:os.system('cls' if os.name == 'nt' else 'clear')

name = input("Enter your name\n")
print("Welcome,", name + ", it is time to start.")
print("Beware! This game is hard. Once you are dead, you will be dead for good.")

choice = 0
loop = 0
chance = 1
enemySelected = 0

potionCount = 2
playerHP = 30
playerMaxHP = 30
playerATK = 5
playerDEF = 2
playerEXP = 0
expForLevel = 100
level = 1

enemyType = 1
enemyHP = 1
enemyATK = 1
enemyCount = 0
expForKill = 1

while playerHP > 0:
    clear()

    if enemyHP <= 0:
        enemyHP = enemyHP + 20
        enemySelected = 0
        playerEXP = playerEXP + expForKill
        enemyCount = enemyCount + 1
        chance = random.randint(1, 100)
        if chance <= 10:
            potionCount = potionCount + 1
            print("You found a potion!")
        else:
            potionCount = potionCount

    while enemySelected != 1:
        chance = random.randint(1, 100)
        if 0 <= chance <= 25:
            enemyType = "Rat"
            enemyHP = 15
            enemyATK = 3
            expForKill = 5
            enemySelected = 1
        elif 26 <= chance <= 50:
            enemyType = "Goblin"
            enemyHP = 25
            enemyATK = 5
            expForKill = 10
            enemySelected = 1
        elif 51 <= chance <= 60 and level > 5:
            enemyType = "Troll"
            enemyHP = 100
            enemyATK = 15
            expForKill = 30
            enemySelected = 1
        elif 61 <= chance <= 80:
            enemyType = "Kobold"
            enemyHP = 30
            enemyATK = 7
            expForKill = 15
            enemySelected = 1
        else:
            enemyType = "Hound"
            enemyHP = 15
            enemyATK = 10
            expForKill = 10
            enemySelected = 1

    if playerEXP >= expForLevel:
            print("Level Up! Max HP increased!")
            level = level + 1
            expForLevel = expForLevel * 2
            playerMaxHP = playerMaxHP + 10

    loop = 0
    print(name+", level", level, "Fighter.")
    print("You have", str(playerHP)+"/"+str(playerMaxHP), "HP.")
    print("Experience:", str(playerEXP)+"/"+str(expForLevel))
    print("You have", potionCount, "potions")
    print("You killed", enemyCount, "enemies")
    print("You have encountered an enemy. It's a", enemyType+".")
    print("It has", enemyHP, "HP.")
    while loop != 1:
        choice = input("Actions: 1. Attack, 2. Defend, 3. Drink a potion.\n")
        if choice == "1":
            playerHP = playerHP - (enemyATK - playerDEF) / 2
            enemyHP = enemyHP - playerATK
            loop = 1
            os.system('cls')
        elif choice == "2":
            playerHP = playerHP - (enemyATK - playerDEF) / 2
            loop = 1
        elif choice == "3":
            if potionCount > 0:
                print("You drink a potion of healing. You have recovered 15 HP.")
                if playerHP + 15 > playerMaxHP:
                    playerHP = playerMaxHP
                else:
                    playerHP = playerHP + 15
                potionCount = potionCount - 1
            else:
                print("You are out of potions.")
            loop = 1
        else:
            print("Wrong. Try again")
            loop = 1
print("You lost. You have slain", enemyCount, "enemies.")
