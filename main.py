import os
import random

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

name = input("Enter your name\n")
print("Welcome,", name + ", it is time to start.")
print("Beware! This game is hard. Once you are dead, you will be dead for good.")

choice = 0
loop = 0
chance = 1
enemy_selected = False

potion_count = 2
player_hp = 30
player_max_hp = 30
player_atk = 5
player_def = 2
player_exp = 0
exp__for_level = 100
level = 1

enemy_type = 1
enemy_hp = 1
enemy_atk = 1
enemy_count = 0
exp_for_kill = 1

while player_hp > 0:
    clear()

    if enemy_hp <= 0:
        enemy_hp = enemy_hp + 20
        enemy_selected = False
        player_exp = player_exp + exp_for_kill
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
            enemy_hp = 15
            enemy_atk = 3
            exp_for_kill = 5
            enemy_selected = True
        elif 26 <= chance <= 50:
            enemy_type = "Goblin"
            enemy_hp = 25
            enemy_atk = 5
            exp_for_kill = 10
            enemy_selected = True
        elif 51 <= chance <= 60 and level > 5:
            enemy_type = "Troll"
            enemy_hp = 100
            enemy_atk = 15
            exp_for_kill = 30
            enemy_selected = True
        elif 61 <= chance <= 80:
            enemy_type = "Kobold"
            enemy_hp = 30
            enemy_atk = 7
            exp_for_kill = 15
            enemy_selected = True
        else:
            enemy_type = "Hound"
            enemy_hp = 15
            enemy_atk = 10
            exp_for_kill = 10
            enemy_selected = True

    if player_exp >= exp__for_level:
            print("Level Up! Max HP increased!")
            level = level + 1
            exp__for_level = exp__for_level * 2
            player_max_hp = player_max_hp + 10

    loop = 0
    print(name+", level", level, "Fighter.")
    print("You have", str(player_hp) + "/" + str(player_max_hp), "HP.")
    print("Experience:", str(player_exp) + "/" + str(exp__for_level))
    print("You have", potion_count, "potions")
    print("You killed", enemy_count, "enemies")
    print("You have encountered an enemy. It's a", enemy_type + ".")
    print("It has", enemy_hp, "HP.")
    while loop != 1:
        choice = input("Actions: 1. Attack, 2. Defend, 3. Drink a potion.\n")
        if choice == "1":
            player_hp = player_hp - (enemy_atk - player_def) / 2
            enemy_hp = enemy_hp - player_atk
            loop = 1
            clear()
        elif choice == "2":
            player_hp = player_hp - (enemy_atk - player_def) / 2
            loop = 1
        elif choice == "3":
            if potion_count > 0:
                print("You drink a potion of healing. You have recovered 15 HP.")
                if player_hp + 15 > player_max_hp:
                    player_hp = player_max_hp
                else:
                    player_hp = player_hp + 15
                potion_count = potion_count - 1
            else:
                print("You are out of potions.")
            loop = 1
        else:
            print("Wrong. Try again")
            loop = 1
print("You lost. You have slain", enemy_count, "enemies.")
