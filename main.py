import os
import player


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


player.name_input()