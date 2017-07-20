import os
import random

CHAR_NAME = None
CHAR_RACE = None
CHAR_ROLE = None


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def name_input():
    global CHAR_NAME
    CHAR_NAME = input('Enter your name.')


def race_input():
    global CHAR_RACE
    CHAR_RACE = input('Choose your race.')


def role_input():
    global CHAR_ROLE
    CHAR_ROLE = input('Choose your role.')


class LivingCreature():
    hp = None
    name = None
