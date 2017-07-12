import os
import random
import sys

clear = lambda:os.system('cls' if os.name == 'nt' else 'clear')

name = input("Enter your name\n")
print("Welcome,", name + ", it is time to start.")
print("Beware! This game is hard. Once you are dead, you will be dead for good.")

choice = 0
loop = 0
chance = 1
enemy_selected = False

potion_count = 2
player_HP = 30
player_Max_HP = 30
player_ATK = 5
player_DEF = 2
player_EXP = 0
exp__for_level = 100
level = 1

enemy_type = 1
enemy_HP = 1
enemy_ATK = 1
enemy_count = 0
exp_for_kill = 1

while player_HP > 0:
    clear()

    if enemy_HP <= 0:
        enemy_HP = enemy_HP + 20
        enemy_selected = False
        player_EXP = player_EXP + exp_for_kill
        enemy_count = enemy_count + 1
        chance = random.randint(1, 100)
        if chance <= 10:
            potion_count = potion_count + 1
            print("You found a potion!")
        else:
            potion_count = potion_count

    while enemy_selected != 1:
        chance = random.randint(1, 100)
        if 0 <= chance <= 25:
            enemy_type = "Rat"
            enemy_HP = 15
            enemy_ATK = 3
            exp_for_kill = 5
            enemy_selected = True
        elif 26 <= chance <= 50:
            enemy_type = "Goblin"
            enemy_HP = 25
            enemy_ATK = 5
            exp_for_kill = 10
            enemy_selected = True
        elif 51 <= chance <= 60 and level > 5:
            enemy_type = "Troll"
            enemy_HP = 100
            enemy_ATK = 15
            exp_for_kill = 30
            enemy_selected = True
        elif 61 <= chance <= 80:
            enemy_type = "Kobold"
            enemy_HP = 30
            enemy_ATK = 7
            exp_for_kill = 15
            enemy_selected = True
        else:
            enemy_type = "Hound"
            enemy_HP = 15
            enemy_ATK = 10
            exp_for_kill = 10
            enemy_selected = True

    if player_EXP >= exp__for_level:
            print("Level Up! Max HP increased!")
            level = level + 1
            exp__for_level = exp__for_level * 2
            player_Max_HP = player_Max_HP + 10

    loop = 0
    print(name+", level", level, "Fighter.")
    print("You have", str(player_HP) + "/" + str(player_Max_HP), "HP.")
    print("Experience:", str(player_EXP) + "/" + str(exp__for_level))
    print("You have", potion_count, "potions")
    print("You killed", enemy_count, "enemies")
    print("You have encountered an enemy. It's a", enemy_type + ".")
    print("It has", enemy_HP, "HP.")
    while loop != 1:
        choice = input("Actions: 1. Attack, 2. Defend, 3. Drink a potion.\n")
        if choice == "1":
            player_HP = player_HP - (enemy_ATK - player_DEF) / 2
            enemy_HP = enemy_HP - player_ATK
            loop = 1
            clear()
        elif choice == "2":
            player_HP = player_HP - (enemy_ATK - player_DEF) / 2
            loop = 1
        elif choice == "3":
            if potion_count > 0:
                print("You drink a potion of healing. You have recovered 15 HP.")
                if player_HP + 15 > player_Max_HP:
                    player_HP = player_Max_HP
                else:
                    player_HP = player_HP + 15
                potion_count = potion_count - 1
            else:
                print("You are out of potions.")
            loop = 1
        else:
            print("Wrong. Try again")
            loop = 1
print("You lost. You have slain", enemy_count, "enemies.")
